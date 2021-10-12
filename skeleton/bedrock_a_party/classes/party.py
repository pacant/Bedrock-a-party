"""File that contains all classes."""


class Food:

    def __init__(self, food, user):
        """
        :param food food that the guest will bring
        :param user username of the guest
        """
        self.food = food
        self.user = user

    def __eq__(self, other):
        if isinstance(other, Food):
            return self.food == other.food and self.user == other.user
        return False

    def serialize(self):
        return {'food': self.food,
                'user': self.user}


class FoodList():
    def __init__(self):
        self.foodlist = []

    def add(self, food, user):
        to_add = Food(food, user)
        if to_add in self.foodlist:
            raise ItemAlreadyInsertedByUser(user + " already committed to bring " + food)
        self.foodlist.append(to_add)
        return to_add

    def remove(self, food, user):
        to_remove = Food(food, user)
        try:
            self.foodlist.remove(to_remove)
        except ValueError:
            raise NotExistingFoodError("user " + user + " has not added " + food + " to this party foodlist")

    def serialize(self):
        return [f.serialize() for f in self.foodlist]


class Party:
    """
    params:
    :param _id id of the party
    :guests: array of users that will be able to add and remove food
    """

    def __init__(self, _id, guests):
        if len(guests) == 0:
            raise CannotPartyAloneError("You cannot create a party without guests")

        self.id = _id
        self.guests = guests
        self.food_list = FoodList()

    def get_food_list(self):
        return self.food_list

    def add_to_food_list(self, item, user):
        if user in self.guests:
            return self.food_list.add(item, user)
        else:
            raise NotInvitedGuestError(user + " is not invited to this party")

    def remove_from_food_list(self, item, user):
        self.food_list.remove(item, user)

    def serialize(self):
        return {
            'id': self.id,
            'guests': self.guests,
            'foodlist': self.food_list.serialize()
        }


class CannotPartyAloneError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NotInvitedGuestError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ItemAlreadyInsertedByUser(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NotExistingFoodError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

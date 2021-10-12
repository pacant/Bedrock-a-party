import json
import unittest

from bedrock_a_party.app import app as tested_app


class TestApp(unittest.TestCase):

    def test1_party(self):  # all parties
        app = tested_app.test_client()

        # no loaded parties
        reply = app.get('/parties')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(len(body['loaded_parties']), 0)

        # create 3 parties
        reply = app.post('/parties',
                         data=json.dumps({
                             "guests": [
                                 "Giacomo",
                                 "Francesco",
                                 "Federico"
                             ]
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['party_number'], 0)

        reply = app.post('/parties',
                         data=json.dumps({
                             "guests": [
                                 "Giacomo",
                                 "Francesco",
                                 "Federico"
                             ]
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['party_number'], 1)

        reply = app.post('/parties',
                         data=json.dumps({
                             "guests": [
                                 "Giacomo",
                                 "Francesco",
                                 "Federico"
                             ]
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['party_number'], 2)

        # get the three parties
        reply = app.get('/parties/loaded')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['loaded_parties'], 3)

        # get the three parties
        reply = app.get('/parties')
        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body, {
            "loaded_parties": [
                {
                    "id": 0,
                    "guests": [
                        "Giacomo",
                        "Francesco",
                        "Federico"
                    ],
                    "foodlist": []
                },

                {
                    "id": 1,
                    "guests": [
                        "Giacomo",
                        "Francesco",
                        "Federico"
                    ],
                    "foodlist": []
                },

                {
                    "id": 2,
                    "guests": [
                        "Giacomo",
                        "Francesco",
                        "Federico"
                    ],
                    "foodlist": []
                },

            ]
        })

        # create a party alone
        reply = app.post('/parties',
                         data=json.dumps({
                             "guests": []
                         }),
                         content_type='application/json')

        self.assertEqual(reply.status_code, 400)

    def test2_foodlist(self):
        app = tested_app.test_client()

        # retrieve existing party GET
        reply = app.get('/party/2')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body, {
            "foodlist": [],
            "guests": [
                "Giacomo",
                "Francesco",
                "Federico"
            ],
            "id": 2
        })

        # retrieve non-existing party GET
        reply = app.get('/party/100')
        self.assertEqual(reply.status_code, 404)

        # insert food from guest
        reply = app.post('/party/2/foodlist/Francesco/pizza',
                         content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body, {
            "food": "pizza",
            "user": "Francesco"
        })

        # insert food from non-guest
        reply = app.post('/party/2/foodlist/Stefano/pizza',
                         content_type='application/json')
        self.assertEqual(reply.status_code, 401)

        # get foodlist
        reply = app.get('/party/2/foodlist', content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body, {
            "foodlist": [
                {
                    "food": "pizza",
                    "user": "Francesco"
                }
            ]
        })

        # remove food
        reply = app.delete('/party/2/foodlist/Francesco/pizza', content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["msg"], "Food deleted!")

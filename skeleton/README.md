# Bedrock-a-Party

**Hi!** 

If you read this file it means that you are developing your (first?) *microservice* using [Flask](https://flask.palletsprojects.com/en/2.0.x/)
and [Flakon](https://pypi.org/project/flakon/)!

Now, let's start with a quick explanation of this skeleton:

### Directory structure

This is the structure of your first microservice:

```
bedrock_a_party
├── app.py
├── __init__.py
├── tests
│   ├── __init__.py
│   └── test_home.py
└── views
    ├── home.py
    ├── __init__.py
```

As you can see, we have `bedrock_a_party`, that is the service you are going to develop.
If you want, you can change the name of it (it does not generate problems).


### Setup the environment

To setup the environment, you should follow these steps:

1. Open the project in your IDE.
2. From IDE terminal, or normal Ubuntu/MacOS terminal execute the command `virtualenv venv` inside project root.
3. Now, you have to activate it, by executing the command `source venv/bin/activate`.
4. You have to install all requirements, let's do that with `pip install -r requirements.txt`.

**Perfect!** now you can run flask application!

<span style="color:orange">WARNING:</span> each time that you open a new terminal session you have
to execute the step 3.


### Run the application

If you want to run the application, you can use the script `run.sh` by typing `bash run.sh`,
or you can set these environment variables:

```
FLASK_DEBUG=1
FLASK_ENV=development
FLASK_APP=bedrock_a_party
```


That's all! :)
---

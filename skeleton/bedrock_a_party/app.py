import os

from flakon import create_app

from bedrock_a_party.views import blueprints

app = create_app(blueprints=blueprints)

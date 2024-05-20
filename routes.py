# Defining Routes: We define two routes - one for the home page and another for handling chat messages.
from flask import jsonify
from googleapiclient import discovery
from service import *
import markdown
from flask_restx import Resource, Namespace

api = Namespace('Exercise', description='Main operations for creating blogs')


@api.route('/check')
class Hello(Resource):
    def get(self):
        """
        A simple endpoint to return a greeting. Useful for verifying that the API is operational.

        Returns:
        str: A greeting message indicating the API is up and running.
        """
        return "Hello From EXERETO Back-End"


# Defining a route for handling HTTP POST requests to the '/generate_blog' endpoint
@api.route('/exercise')
class Exercise(Resource):
    def post(self):
        # try:
            # Generating a blog post using the 'generate_blog' function
            return generate_exercise()
            # Returning the generated blog post as a response to the client

        # except Exception as e:
        #     # Handling any exceptions that occur during the generation process
        #     # Returning a custom error message with an appropriate status code
        #     return "Error generating exercise: {}".format(str(e)), 500


def configure_routes(api_instance):
    """
    Configures routes for the Flask application by adding the defined Namespace to the Flask instance.

    Parameters:
    api_instance (Flask): The Flask application or API instance where the Namespace is to be added.

    This function ensures that all defined routes and resources under the 'Assessment_creator' Namespace
    are registered with the Flask application, enabling their accessibility via HTTP requests.
    """
    api_instance.add_namespace(api)

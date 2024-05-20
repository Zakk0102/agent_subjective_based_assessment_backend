from flask import Flask  # Import the Flask class to create a Flask application
from flask_cors import CORS  # Import CORS to enable Cross-Origin Resource Sharing
from flask_restx import Api  # Import Api from Flask-RESTx to structure the RESTful API
from routes import configure_routes

app = Flask(__name__)

CORS(app)
api = Api(app, prefix='/api/v1', version='1.0', title='Exercise Generator', description='Content Crafter Back-end')

configure_routes(api)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5003)

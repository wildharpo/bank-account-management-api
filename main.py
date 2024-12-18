# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask_cors import CORS

# Import our controller "Blueprints" from the controller classes we've created
from controllers.customer_controller import customer_bp
from controllers.account_controller import account_bp

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# Enable CORS for the entire application
CORS(app)

# Register our Blueprints
app.register_blueprint(customer_bp, url_previx='/customer')
app.register_blueprint(account_bp, url_previx='/account')

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Welcome to the bank-account-management-api!'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
from flask import Flask

app = Flask(__name__)

# Import the routes module
from app import routes

# Register the blueprint
app.register_blueprint(routes.bp)

# Run the application
if __name__ == "__main__":
    app.run()
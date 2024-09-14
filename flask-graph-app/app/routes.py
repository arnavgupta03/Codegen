from flask import render_template
from flask import Blueprint
import json
from graph_visualizer import generate_import_graph  # Assuming this function generates the graph

# Create a blueprint for the routes
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Generate the import graph
    graph = generate_import_graph('./Loop-Labyrinth-Analysis/')
    print(graph)
    
    # Convert the graph to a JSON serializable format
    graph_data = json.dumps(graph)

    return render_template('index.html', graph_data=graph_data)

# Add more routes as needed
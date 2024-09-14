# Flask Graph App

This is a Flask web application that visualizes the import graph of a Python codebase using the Python AST module and NetworkX.

## Project Structure

The project has the following files and directories:

- `app/__init__.py`: Initializes the Flask application and sets up the necessary configurations.
- `app/routes.py`: Defines the routes for the Flask application.
- `app/static/css/styles.css`: Contains the CSS styles for the web application.
- `app/static/js/graph.js`: Contains the JavaScript code for rendering the interactive 3D graph on the main page.
- `app/templates/index.html`: HTML template that defines the structure of the main page.
- `graph_visualizer.py`: Contains the graph visualizer function that parses and represents the import graph using the Python AST module and NetworkX.
- `requirements.txt`: Lists the required Python packages and their versions for the project.
- `README.md`: Documentation for the project.

## Usage

1. Install the required packages listed in `requirements.txt` using the following command:

   ```shell
   pip install -r requirements.txt
   ```

2. Run the Flask application using the following command:

   ```shell
   flask run
   ```

3. Open your web browser and navigate to `http://localhost:5000` to view the interactive 3D graph.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Please note that the `LICENSE` file is not mentioned in the project tree structure provided, so you may need to add it if required.
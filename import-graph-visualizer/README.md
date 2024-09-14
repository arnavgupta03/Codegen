# Import Graph Visualizer

This project is a Python application that visualizes the import graph of a given codebase. It uses the Python AST module to parse imports and the NetworkX library to represent the graph.

## Project Structure

The project has the following files:

- `src/main.py`: This file is the entry point of the application. It contains the main logic to run the import graph visualization. It imports the `graph_visualizer` module.

- `src/graph_visualizer.py`: This file contains the implementation of the import graph visualization. It uses the `import_parser` module to parse the imports and `NetworkX` library to represent the graph.

- `src/import_parser.py`: This file contains the implementation of the import parser. It uses the Python AST module to parse the imports in the provided codebase.

- `src/utils/__init__.py`: This file is an empty file that marks the `utils` directory as a Python package.

- `requirements.txt`: This file lists the dependencies required for the project. Make sure to install these dependencies using `pip` before running the project.

## Getting Started

To set up and run the import graph visualization, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/import-graph-visualizer.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the application:

   ```shell
   python src/main.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Please make sure to replace `your-username` in the repository URL with your actual GitHub username.
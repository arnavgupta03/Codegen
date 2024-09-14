import ast
import os
import networkx as nx
from networkx.readwrite import json_graph

def parse_imports(codebase_path):
    # Initialize an empty dictionary to store imports
    imports = {}

    # Parse the Python files in the codebase
    for file_path in get_python_files(codebase_path):
        with open(file_path, 'r') as file:
            # Parse the AST of the Python file
            tree = ast.parse(file.read(), filename=file_path)

            # Extract the imports from the AST
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        module_name = alias.name
                        imports[file_path] = imports.get(file_path, []) + [module_name]
                elif isinstance(node, ast.ImportFrom):
                    module_name = node.module
                    imports[file_path] = imports.get(file_path, []) + [module_name]

    return imports

def get_python_files(codebase_path):
    # Initialize an empty list to store file paths
    python_files = []

    # Recursively traverse the directory structure
    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    return python_files



def generate_import_graph(codebase_path):
    graph = nx.DiGraph()

    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")  # Debugging line
                with open(file_path, 'r') as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    graph.add_edge(file_path, alias.name)
                            elif isinstance(node, ast.ImportFrom):
                                module = node.module if node.module else ''
                                for alias in node.names:
                                    graph.add_edge(file_path, f"{module}.{alias.name}")
                    except SyntaxError as e:
                        print(f"Syntax error in file {file_path}: {e}")

    return json_graph.node_link_data(graph)  # Convert to node-link format for JSON serialization

def visualize_graph(graph_data):
    graph = json_graph.node_link_graph(graph_data)
    pos = nx.spring_layout(graph, dim=3)
    nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')

def visualize_import_graph(codebase_path):
    # Parse the Python codebase using the AST module
    tree = ast.parse(codebase_path)

    # Create a directed graph using NetworkX
    graph = nx.DiGraph()

    # Traverse the AST and extract import statements
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                graph.add_edge('main', alias.name)
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if node.module:
                    graph.add_edge(node.module, alias.name)
                else:
                    graph.add_edge('main', alias.name)

    # Visualize the import graph
    pos = nx.spring_layout(graph, dim=3)
    nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
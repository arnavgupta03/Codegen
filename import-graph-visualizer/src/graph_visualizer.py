import ast
import networkx as nx
import matplotlib.pyplot as plt
import os

def visualize_import_graph(codebase_path):
    # Parse the imports in the codebase
    imports = parse_imports(codebase_path)

    # Create a directed graph
    graph = nx.DiGraph()

    # Add nodes for each import
    for module in imports:
        graph.add_node(module)

    # Add edges between imported modules
    for module, imported_modules in imports.items():
        for imported_module in imported_modules:
            graph.add_edge(module, imported_module)

    # Visualize the import graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', linewidths=0.5)
    plt.title('Import Graph Visualization')
    plt.axis('off')
    plt.show()

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
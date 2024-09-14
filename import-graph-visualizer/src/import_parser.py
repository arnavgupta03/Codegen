import ast
import networkx as nx

def parse_imports(code):
    """
    Parse the imports in the provided codebase using the Python AST module.
    Returns a list of imported modules.
    """
    tree = ast.parse(code)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ""
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")
    return imports

def build_import_graph(codebase):
    """
    Build the import graph of the codebase using NetworkX.
    Returns a NetworkX DiGraph object representing the import graph.
    """
    graph = nx.DiGraph()
    for file_path, code in codebase.items():
        imports = parse_imports(code)
        for imported_module in imports:
            graph.add_edge(file_path, imported_module)
    return graph
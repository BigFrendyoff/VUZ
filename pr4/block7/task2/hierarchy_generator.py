import os
import graphviz


def create_module_hierarchy(root_path):
    graph = graphviz.Digraph()

    for dirpath, dirnames, filenames in os.walk(root_path):
        module_paths = [os.path.join(dirpath, f) for f in filenames if f.endswith('.py')]
        module_names = []
        for path in module_paths:
            module_name = os.path.splitext(os.path.basename(path))[0]
            module_names.append(module_name)
            graph.node(module_name)

        for path in module_paths:
            module_name = os.path.splitext(os.path.basename(path))[0]
            with open(path, 'r') as f:
                for line in f.readlines():
                    if line.startswith('import') or line.startswith('from'):
                        dependency = line.split()[1].split('.')[0]
                        if dependency in module_names:
                            graph.edge(module_name, dependency)

    return graph


graph = create_module_hierarchy('to_generate')
graph.render('module_hierarchy', format='png')

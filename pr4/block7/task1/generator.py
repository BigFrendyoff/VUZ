import inspect
import importlib
from pathlib import Path


def generate_markdown_doc(filename: str) -> str:
    with open(filename, 'r') as f:
        code = f.read()
    module = importlib.import_module(filename[:-3])
    module_name = inspect.getmodulename(filename)
    doc = f"# Модуль {module_name}\n\n"
    doc += inspect.getdoc(module) + "\n\n"

    classes = inspect.getmembers(module, inspect.isclass)
    functions = inspect.getmembers(module, inspect.isfunction)

    for cls_name, cls in classes:
        doc += f"## Класс {cls_name}\n\n"
        doc += inspect.getdoc(cls) + "\n\n"

        methods = inspect.getmembers(cls, inspect.isfunction)
        for method_name, method in methods:
            signature = str(inspect.signature(method))
            doc += f"* **Метод** `{method_name}{signature}`\n\n"
            doc += inspect.getdoc(method) + "\n\n"

    for func_name, func in functions:
        signature = str(inspect.signature(func))
        doc += f"## Функция {func_name}\n\n"
        doc += f"Сигнатура: `{func_name}{signature}`\n\n"
        doc += inspect.getdoc(func) + "\n\n"

    return doc


input_file = "example_module.py"
output_file = "generated_doc.md"
markdown_doc = generate_markdown_doc(input_file)
with open(output_file, 'w') as f:
    f.write(markdown_doc)

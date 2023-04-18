import contextlib

def context(name):
    print("<" + name + ">")
    yield name  # наш блок
    print("</" + name + ">")


class HTML:
    def __init__(self):
        s = ""

    @contextlib.contextmanager
    def body(self):
        print("<body>")
        yield
        print("</body>")

    @contextlib.contextmanager
    def div(self):
        print("<div>")
        yield
        print("</div>")

    @contextlib.contextmanager
    def p(self, s):
        print("<p>" + s + "</p>")


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

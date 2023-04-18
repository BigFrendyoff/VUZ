class SVG:
    def __init__(self):
        self.body = ""
        self.header = ""
    def line(self, x1, y1, x2, y2, color):
        self.body += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" />' + "\n"

    def circle(self, cx, cy, r, color):
        self.body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />' + "\n"

    def save(self, filename, width, height):
        self.header += f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">' + "\n"
        self.body += "</svg>"
        with open(filename, 'w') as f:
            f.write(self.header + self.body)

svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)

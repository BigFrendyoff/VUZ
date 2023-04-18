from svg_basic import *


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0
        self.scale_x = 25
        self.scale_y = 50

def draw_tree(node, x, y, dwg):
    if node is None:
        return x

    left_x = draw_tree(node.left, x, y + node.scale_y, dwg)
    right_x = draw_tree(node.right, left_x + node.scale_x, y + node.scale_y, dwg)

    node.x = left_x
    node.y = y

    dwg.circle(left_x, y, r=3, color='black')
    if node.left is not None:
        dwg.line(left_x, y, node.left.x, node.left.y, color="black")
    if node.right is not None:
        dwg.line(left_x, y, node.right.x, node.right.y, color="black")
    return right_x


def draw_binary_tree(root):
    dwg = SVG()
    draw_tree(root, 0, 20, dwg)
    dwg.save('tree.svg', 500, 500)


tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)
draw_binary_tree(tree)

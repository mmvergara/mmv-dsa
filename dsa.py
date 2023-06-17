from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{{val:{self.val} , next:{self.next}}}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{{val:{self.val} , left:{self.left} , right:{self.right} }}"


def print_binary_tree(root):
    lines, *_ = _print_tree_recursively(root)
    for line in lines:
        print(line)


def _print_tree_recursively(node):
    if node is None:
        line = "", ""
        return line

    left_lines, left_pos, left_width = _print_tree_recursively(node.left)
    right_lines, right_pos, right_width = _print_tree_recursively(node.right)

    value_width = len(str(node.value))
    pos = left_pos + value_width // 2
    width = left_pos + value_width + right_width - pos

    while len(left_lines) < len(right_lines):
        left_lines.append(" " * left_width)

    while len(right_lines) < len(left_lines):
        right_lines.append(" " * right_width)

    line = [
        f"{left_lines[i]}{' ' * (pos - len(left_lines[i]))}{str(node.value)}{' ' * (right_pos - pos - value_width)}{right_lines[i]}"
        for i in range(len(left_lines))
    ]
    middle_line = " " * left_width + "-" * value_width + " " * (right_width - right_pos)
    line.insert(len(left_lines) // 2, middle_line)

    return line, pos, width

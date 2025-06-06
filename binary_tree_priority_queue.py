class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.value}, p={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.root = self._insert(self.root, new_node)

    def _insert(self, root, node):
        if root is None:
            return node
        if node.priority > root.priority:
            node.left = root
            return node
        else:
            root.right = self._insert(root.right, node)
            return root

    def pop(self):
        if self.root is None:
            return None
        max_node = self.root
        self.root = self.root.left
        return max_node.value

    def peek(self):
        return self.root.value if self.root else None

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [(node.value, node.priority)] + self._inorder(node.right)

    def view(self):
        return self._inorder(self.root)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("task1", 3)
    pq.insert("task2", 5)
    pq.insert("task3", 1)
    pq.insert("task4", 4)

    print("Черга (inorder):", pq.view())
    print("Найвищий пріоритет:", pq.peek())
    print("Видалено:", pq.pop())
    print("Черга після видалення:", pq.view())
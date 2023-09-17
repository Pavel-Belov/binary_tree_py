class Node:
    """
    Класс реалзации ноды бинарного дерева
    """

    def __init__(self, value):
        """
        Конструктор класса Node
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Строковое представление экземпляра класса Node
        """
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:
    """
    Класс реализации бинарного дерева
    """

    def __init__(self, root_value):
        """
        Конструктор класса BinaryTree
        """
        self.root = Node(root_value)

    def add(self, value):
        """
        Метод, который добавляет новую ноду в бинарное дерево.
        """
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        """
        Метод, который ищет заданный узел
        """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count_nodes(self) -> int:
        """
        Метод, который считает количество элементов бинарного деревав
        """
        counter = 0
        node = self.root

        def inner_counter(node):
            nonlocal counter
            if node:
                counter += 1
                inner_counter(node.left)
                inner_counter(node.right)

        inner_counter(node)
        return counter

    def print_binary_tree(self) -> str:
        """
        Метод, который выводит всё дерево на экран
        """
        res = ""
        node = self.root

        def inner_print(node):
            nonlocal res
            if node:
                res += node.__str__()
                res += '\n'
                inner_print(node.left)
                inner_print(node.right)

        inner_print(node)
        return "\n".join(res.split('\n')[:-1])

    def delete_node(self, value):
        """
        Метод, который удаляет узел у бинарного дерева
        """
        node, parent = self.search(self.root, value)
        if node:
            if not node.left and not node.right:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
            elif (not node.left and node.right) or (node.left and not node.right):
                child = node.left if node.left else node.right
                if parent:
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    self.root = child
            else:
                min_node_parent = node
                min_node = node.right
                while min_node.left:
                    min_node_parent = min_node
                    min_node = min_node.left
                node.value = min_node.value
                if min_node_parent.left == min_node:
                    min_node_parent.left = min_node.right
                else:
                    min_node_parent.right = min_node.right


bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)

print('')
print(bt.print_binary_tree())
print(f'Количество элементов бинарного дерева: {bt.count_nodes()}')

print('')
print('Удаляем узел девера')
bt.delete_node(10)
print(bt.print_binary_tree())
print(f'Количество элементов бинарного дерева: {bt.count_nodes()}')

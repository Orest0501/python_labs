class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Resistor:
    def __init__(self, name: str, resistance: int, power: int, accuracy: float):
        self.name = name
        self.resistance = resistance
        self.power = power
        self.accuracy = accuracy

    def __str__(self):
        return f"Name: {self.name}. Resistance: {self.resistance}. Power: {self.power}. Accuracy: {self.accuracy}."


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_to_the_left(self, item):
        # add to the beginning of the list
        node = Node(item)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def add_to_the_right(self, item):
        # add to  end of the list
        node = Node(item)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
            node.prev = last
        else:
            self.head = node

    def insert_after_current_node(self, current_node, item):
        if current_node is None:
            return
        node = Node(item)
        node.next = current_node.next
        current_node.next = node
        node.prev = current_node
        if node.next:
            node.next.prev = node

    def append_by_resistance(self, item):
        current = self.head
        while current and current.data.resistance <= item.resistance:
            current = current.next
        if current is None:
            # add to the end
            self.add_to_the_right(item)
        elif current.prev:
            self.insert_after_current_node(current.prev, item)
        else:
            # add to the very beginning
            self.add_to_the_left(item)

    def print(self):
        current = self.head
        if current:
            while current:
                print(current.data)
                current = current.next
        else:
            print("LinkedList is empty")

    def print_by_accuracy(self, accuracy_boundary):
        current = self.head
        if current:
            while current:
                if current.data.accuracy < accuracy_boundary:
                    print(current.data)
                current = current.next
        else:
            print("LinkedList is empty")


if __name__ == "__main__":
    print("Sorted by resistance:")
    linked_list = DoubleLinkedList()
    for i in (5, 7, 8, 1, 6, 2, 3, 9, 4):
        resistor = Resistor(name=f"resistor{i}", resistance=i, power=i, accuracy=i)
        linked_list.append_by_resistance(resistor)
    linked_list.print()
    print("-" * 80)

    print("All resistors with accuracy less than 6")
    linked_list.print_by_accuracy(6)
    print("-" * 80)

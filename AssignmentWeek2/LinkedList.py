class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Added {data} as the head of the list.")
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print(f"Added {data} to the end of the list.")

    def print_list(self):
        """Print the contents of the list."""
        current = self.head
        if not current:
            print("List is empty.")
            return
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if self.head is None:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer (1-based).")

        if n == 1:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position {n} with value {deleted_value}.")
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError(f"Index {n} is out of range.")

        deleted_value = current.data
        prev.next = current.next
        print(f"Deleted node at position {n} with value {deleted_value}.")


# Test the implementation
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()
    # Add elements to the list
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    # Print the list
    ll.print_list()

    # Delete 2nd node
    ll.delete_nth_node(2)
    ll.print_list()

    # Try deleting 10th node (out of range)
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"Error: {e}")

    # Try deleting from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except Exception as e:
        print(f"Error: {e}")

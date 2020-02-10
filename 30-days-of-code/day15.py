def insert(self, head, data):
    if head is None:
        head = Node(data)  # noqa
    elif head.next is None:
        head.next = Node(data)  # noqa
    else:
        self.insert(head.next, data)

    return head

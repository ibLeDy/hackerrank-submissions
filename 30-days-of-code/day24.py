def removeDuplicates(self, head):
    if head is None:
        return head

    fptr = head.next
    sptr = head
    ha = {}

    while fptr is not None:
        if sptr.data not in ha:
            ha[sptr.data] = True

        if fptr.data in ha:
            sptr.next = fptr.next
            fptr = fptr.next
            continue

        sptr = fptr
        fptr = fptr.next

    return head

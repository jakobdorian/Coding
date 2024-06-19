def mergeLists(head1, head2):
    # create a dummy node to act as the head of the merged linked list
    dummy = SinglyLinkedList()
    # initialize a current pointer to the dummy node
    curr = dummy
    
    # loop until we reach the end of either list
    while head1 and head2:
        # compare the data of the current nodes in both lists
        if head1.data < head2.data:
            # if head1's data is smaller, add it to the merged list
            curr.next = head1
            # move to the next node in head1
            head1 = head1.next
        else:
            # if head2's data is smaller or equal, add it to the merged list
            curr.next = head2
            # move to the next node in head2
            head2 = head2.next
        # move the current pointer to the next node in the merged list
        curr = curr.next
    
    # if we've reached the end of head2 but head1 still has nodes,
    # append the remaining nodes of head1 to the merged list
    if head1:
        curr.next = head1
    
    # if we've reached the end of head1 but head2 still has nodes,
    # append the remaining nodes of head2 to the merged list
    if head2:
        curr.next = head2
    
    # return the merged list, starting from the node after the dummy node
    return dummy.next

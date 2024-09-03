import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    # Remove empty lists
    lists = [lst for lst in lists if lst]
    if not lists:
        return None

    # Initialize the heap with (value, list_index) pairs
    min_heap = [(lst.val, i) for i, lst in enumerate(lists)]
    heapq.heapify(min_heap)

    # Keep track of the head of the merged list
    head = None
    current = None

    while min_heap:
        val, list_index = heapq.heappop(min_heap)

        # Create or update the merged list
        if not head:
            head = lists[list_index]
            current = head
        else:
            current.next = lists[list_index]
            current = current.next

        # Move to the next node in the selected list
        lists[list_index] = lists[list_index].next

        # If there are more nodes in the list, add to the heap
        if lists[list_index]:
            heapq.heappush(min_heap, (lists[list_index].val, list_index))

    return head

# Example usage
lists = [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]

merged_list = merge_k_lists(lists)
# Output the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
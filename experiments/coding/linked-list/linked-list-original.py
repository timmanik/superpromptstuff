import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    # Initialize a min-heap
    min_heap = []
    
    # Push the first node of each list onto the heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
    
    # Dummy node to form the merged linked list
    dummy = ListNode(0)
    current = dummy
    
    # Merge the nodes
    while min_heap:
        # Get the smallest node from the heap
        _, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
        # Push the next node of the same list onto the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
    return dummy.next

# Example usage
# Define linked lists here
# Example: [[1,4,5],[1,3,4],[2,6]]
lists = [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]

merged_list = merge_k_lists(lists)
# Output the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next

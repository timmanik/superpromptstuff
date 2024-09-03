class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists_optimized(lists):
    # Remove empty lists
    lists = [lst for lst in lists if lst]
    
    if not lists:
        return None
    
    dummy = ListNode(0)
    current = dummy
    
    while lists:
        # Find the list with the smallest current node
        min_index = min(range(len(lists)), key=lambda i: lists[i].val)
        
        # Add the smallest node to the result
        current.next = lists[min_index]
        current = current.next
        
        # Move to the next node in the chosen list
        lists[min_index] = lists[min_index].next
        
        # Remove the list if it's empty
        if not lists[min_index]:
            lists.pop(min_index)
    
    return dummy.next

# Example usage
lists = [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]

merged_list = merge_k_lists_optimized(lists)

# Output the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
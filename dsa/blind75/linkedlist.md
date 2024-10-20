Here are solutions for various Linked List problems along with sample inputs and outputs.

---

### 1. **Reverse a Linked List**

Given a singly linked list, reverse the list.

#### Solution

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

#### Input/Output

**Input:**
```
1 -> 2 -> 3 -> 4 -> 5 -> None
```

**Output:**
```
5 -> 4 -> 3 -> 2 -> 1 -> None
```

---

### 2. **Detect Cycle in a Linked List**

Detect if a cycle exists in a linked list.

#### Solution

```python
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

#### Input/Output

**Input:**
```
1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)
```

**Output:**
```
True
```

---

### 3. **Merge Two Sorted Lists**

Merge two sorted linked lists into one sorted list.

#### Solution

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next
```

#### Input/Output

**Input:**
```
List1: 1 -> 3 -> 5 -> None
List2: 2 -> 4 -> 6 -> None
```

**Output:**
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

---

### 4. **Merge K Sorted Lists**

Merge `k` sorted linked lists into one sorted list.

#### Solution

```python
import heapq

def merge_k_lists(lists):
    heap = []
    dummy = ListNode()
    curr = dummy
    
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, l))
    
    while heap:
        val, node = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
    
    return dummy.next
```

#### Input/Output

**Input:**
```
Lists: 
[1 -> 4 -> 7 -> None, 
 2 -> 5 -> 8 -> None, 
 3 -> 6 -> 9 -> None]
```

**Output:**
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

---

### 5. **Remove Nth Node From End Of List**

Given a linked list, remove the n-th node from the end.

#### Solution

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    return dummy.next
```

#### Input/Output

**Input:**
```
List: 1 -> 2 -> 3 -> 4 -> 5 -> None, n = 2
```

**Output:**
```
1 -> 2 -> 3 -> 5 -> None
```

---

### 6. **Reorder List**

Reorder a linked list in such a way that you alter between the front and back nodes (1st with last, 2nd with second-last, etc.).

#### Solution

```python
def reorder_list(head):
    if not head or not head.next:
        return
    
    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        first_next = first.next
        second_next = second.next
        
        first.next = second
        second.next = first_next
        
        first = first_next
        second = second_next
```

#### Input/Output

**Input:**
```
List: 1 -> 2 -> 3 -> 4 -> 5 -> None
```

**Output:**
```
1 -> 5 -> 2 -> 4 -> 3 -> None
```

---

These solutions implement different linked list problems. The input lists can be constructed using the `ListNode` class, and the functions manipulate the nodes according to the respective problem requirements. Let me know if you need further details on any of these!
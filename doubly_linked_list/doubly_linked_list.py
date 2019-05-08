"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def __str__(self):
    return f'length: {self.length}'

  def add_to_head(self, value):
    if self.head == None:
      new_head = ListNode(value)
      self.head = new_head
      self.tail = new_head
      self.length += 1

    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    if self.head == None:
      return None
    
    elif self.head == self.tail:
      head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return head.value

    else: 
      self.head.delete()
      self.head = self.head.next
      self.length -= 1

  def add_to_tail(self, value):
    self.length += 1
    if self.head == None and self.tail == None:
      new_tail = ListNode(value)
      self.head = new_tail
      self.tail = new_tail
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

  def remove_from_tail(self):
    if self.head == None or self.tail == None:
      return None
    tail = self.tail
    self.delete(self.tail)
    return tail.value

  def move_to_front(self, node):
    if self.head == None and self.tail == None:
      return None
    elif self.head == self.tail:
      return None
    else: 
      self.delete(node)
      self.add_to_head(node.value)

  def move_to_end(self, node):
    if self.head == None and self.tail == None:
      return None
    elif self.head == self.tail:
      return None
    else:
      self.delete(node)
      self.add_to_tail(node.value)


  def delete(self, node):
    if self.head == None:
      return None
    self.length -= 1
    temp_prev = node.prev
    temp_next = node.next
    node.prev = None
    node.next = None
    if temp_prev:
      temp_prev.next = temp_next
    if temp_next:
      temp_next.prev = temp_prev
    if node == self.head:
      self.head = temp_next
    if node == self.tail:
      self.tail = temp_prev
    
  def get_max(self):
    if self.head == None and self.tail == None:
      return None
    max = 0
    current = self.head
    while current:
      if current.value > max:
        max = current.value
      current = current.next
    return max 



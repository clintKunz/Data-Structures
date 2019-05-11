class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return f'value: {self.value}'

  def insert(self, value):
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # check if no left child
      if not self.left:
        # park the new node here
        self.left = BinarySearchTree(value)
      # otherwise keep traversing further down
      else: 
        self.left.insert(value)
    #check the right side
    else:
      # check if no right child
      if not self.right:
        self.right = BinarySearchTree(value)
      else: 
        # keep recursing down to the right since there is a right child
        self.right.insert(value)


  def contains(self, target):
    if self.value == None:
      return False
    elif target == self.value:
      return True
    elif target < self.value and self.left:
      return self.left.contains(target)
    elif target > self.value and self.right:
      return self.right.contains(target)
    else: 
      return False

  def get_max(self):
    max = 0
    current = self
    while current:
      if current.value > max:
        max = current.value
      current = current.right
    return max

  def for_each(self, cb):
    self.value = cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

a = BinarySearchTree(11)
a.insert(5)
a.insert(15)
a.insert(3)
a.insert(6)
a.insert(20)

print(a.value)
print(a.get_max())
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

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
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass
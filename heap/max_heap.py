class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # loop until either the element reaches the top of the array
    # or we'll break the loop when we realize the element's priority
    # is not larger than its parent's value
    while index > 0:
      parent = (index - 1) // 2
      # check if the element at index has higher priority
      if self.storage[index] > self.storage[parent]:
        # then we need to swap the elements
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # update the index
        index = parent
      else: 
        # otherwise, our element has reached a spot in the heap where its parent is higher
        break

  def _sift_down(self, index):
    pass

from node import Node

class Stack:
  '''
  Linked list implementation of a stack.
  '''
  def __init__(self, limit=1000):
    # Initialize empty stack with a default limit of 1000 items.
    self.top_item = None
    self.size = 0
    self.limit = limit

  def push(self, value):
    # Check if stack has space, then pushes to head node of the linked list.
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      # Increment stack size by 1 here:
      self.size += 1
    else:
      print("Stack is full!")

  def pop(self):
    # Check if stack has items, then remove the head node from the list and return its value.
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")

  def peek(self):
    # Check if stack has items, then return the value of the head node.
    if not self.is_empty():
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")

  def has_space(self):
    # Check if stack has remaining space to prevent stack overflow.
    return self.limit > self.size

  def is_empty(self):
    # Check if stack is empty, to prevent stack underflow.
    return self.size == 0

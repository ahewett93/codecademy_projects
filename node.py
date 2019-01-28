class Node:
  '''
  Node implementation to be used for linked lists, stacks, etc.
  '''
  def __init__(self, value, next_node=None):
    # Initialize a node with a value and next node.
    self.value = value
    self.next_node = next_node

  def set_next_node(self, next_node):
    # Set a pointer to the next node in the list.
    self.next_node = next_node

  def get_next_node(self):
    # Return the object of the next node in the list.
    return self.next_node

  def get_value(self):
    # Return the value of this node.
    return self.value

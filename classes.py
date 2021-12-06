
class Node:
  def __init__(self, previous_node, next_node):
    self.previous_node = previous_node
    self.next_node = next_node

  def get_next(self):
    return self.next_node

  def set_next(self, new_node):
    self.next_node = new_node

  def get_previous(self):
    return self.previous_node

  def set_previous(self, new_node):
    self.previous_node = new_node

class linked_list:
  def __init__(self, head, tail):
    self.head = head

  def pop_front(self):
    first_node = self.head
    self.head = self.head.get_next()
    return first_node

  def get_front(self):
    return self.head

  def push_front(self, new_node):
    self.head.set_previous(new_node)
    new_node.set_next(self.head)
    self.head = new_node
  
  def pop_back(self):
    last_node = self.tail
    self.tail = self.head.get_previous()
    return last_node

  def get_back(self):
    return self.tail

  def push_back(self, new_node):
    self.tail.set_next(new_node)
    new_node.set_previous(self.tail)
    self.tail = new_node

  def clear(self):
    self.head = None
    self.tail = None
    
class Board:
  selected = []
  highlighted = linked_list(None, None)
  arrows = linked_list(None, None)

  #en passant, castling

  def __init__(self, user_colour, fen):
    self.user_colour = user_colour
    self.fen = fen

  def get_fen(self, fen):
    return self.fen
  
  def get_user_colour(self):
    return self.user_colour

  def set_highlighted(self, highlighted):
    self.highlighted = highlighted

  def get_highlighted(self):
    return self.highlighted

  def set_arrows(self, arrows):
    self.arrows = arrows

  def get_arrows(self):
    return self.arrows

  #def set_point_value(self, colour):
  """
  get point value to reflect current board
  """

  #def get_moves(self, colour):
  """
  return list of possible moves
  """

  #def is_valid(self, piece, location):
  """
  check if move is valid
  """

  #def set_move(self, piece, location):
  """
  check if move is valid
  update fen to reflect move
  """

  #def set_move_minimax(self, piece, location)
  """ 
  update fen to reflect move
  """ 

  #def minimax(self, depth, colour):
  """
  minimax through all possible moves
  """

  #print_fen(self)
  """
  helper function for now to make sure board is ok
  """
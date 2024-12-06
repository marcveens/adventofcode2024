from get_file import get_file_contents

def path_walker(file_contents):
  walker = Walker()
  
  walker.set_map(file_contents)
  
  walker.go_walk()
    
  positions_visited = len(walker.get_positions_visited())
  
  return positions_visited
  
class Walker:
  map = []
  walking_direction = "UP"
  positions_visited = []
  
  def set_map(self, file_contents):
    self.map = self.create_map(get_file_contents(file_contents))
  
  def go_walk(self):
    current_position = self.get_guard_position()
    
    while self.get_next_position(current_position):
      current_position = self.get_next_position(current_position)
      print(f"next {current_position}")
      
      if self.is_unique_position(current_position):
        self.positions_visited.append({
          "row": current_position.get("row"),
          "col": current_position.get("col")
        })
  
  def get_next_position(self, current_position):
    if self.walking_direction == "UP":
      next_position = next((x for x in self.map if 
                            x.get("row") == current_position.get("row") - 1 and
                            x.get("col") == current_position.get("col")), None)
    elif self.walking_direction == "RIGHT":
      next_position = next((x for x in self.map if 
                            x.get("row") == current_position.get("row") and
                            x.get("col") == current_position.get("col") + 1), None)
    elif self.walking_direction == "DOWN":
      next_position = next((x for x in self.map if 
                            x.get("row") == current_position.get("row") + 1 and
                            x.get("col") == current_position.get("col")), None)
    elif self.walking_direction == "LEFT":
      next_position = next((x for x in self.map if 
                            x.get("row") == current_position.get("row") and
                            x.get("col") == current_position.get("col") - 1), None)
    
    # If no next_position, it's complete
    if not next_position:
      return None   
    
    # If next_position is wall: rotate
    if next_position and next_position.get("is_wall"):
      if self.walking_direction == "UP":
        self.walking_direction = "RIGHT"
      elif self.walking_direction == "RIGHT":
        self.walking_direction = "DOWN"
      elif self.walking_direction == "DOWN":
        self.walking_direction = "LEFT"
      elif self.walking_direction == "LEFT":
        self.walking_direction = "UP"

      return self.get_next_position(current_position)    
    
    else:
      return next_position    
    
  def is_unique_position(self, position):
    return not next((x for x in self.positions_visited if 
                     x.get("row") == position.get("row") and
                     x.get("col") == position.get("col")), None)

  def get_guard_position(self):
    return next((x for x in self.map if x.get("is_guard") == True), None)
  
  def get_positions_visited(self):
    return self.positions_visited
  
  def create_map(self, file_contents):
    matrix = []
    
    split_rows = file_contents.split("\n")
    
    for row_idx, row in enumerate(split_rows):
      points = list(row)
      
      for col_idx, point in enumerate(points):
        matrix.append({
          "row": row_idx,
          "col": col_idx,
          "is_wall": point == "#",
          "is_floor": point != "#",
          "is_guard": point == "^"
        })
        
        if point == "^":
          self.positions_visited.append({
            "row": row_idx,
            "col": col_idx
          })
        
    return matrix
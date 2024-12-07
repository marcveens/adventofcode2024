from get_file import get_file_contents

def path_walker(file_contents):
  infinites = 0
  
  walker = Walker()
  
  walker.set_map(file_contents)
  
  try:
    walker.go_walk()
  except Exception as e:
    print(e)
  
  print(f"Total: {len(walker.positions_visited)}")
  
  for idx, point in enumerate(walker.positions_visited):
    walker.walking_direction = "UP"
    walker.positions_visited = []
    walker.set_map(file_contents)
    
    if not point.get("is_guard"):
      walker.set_extra_obstruction(point)
  
      try:
        walker.go_walk()
        print(f"id {idx}: succeeded")
      except Exception as e:
        print(f"id {idx}: {e}")
        infinites += 1
        
  # positions_visited = len(walker.get_positions_visited())
  
  # return positions_visited
  
  return infinites
  
class Walker:
  map = {}
  walking_direction = "UP"
  positions_visited = []
  
  def set_map(self, file_contents):
    self.map = self.create_map(get_file_contents(file_contents))
  
  def go_walk(self):
    current_position = self.get_guard_position()
    
    while self.get_next_position(current_position):
      current_position = self.get_next_position(current_position)
      # print(f"next {current_position}")
      
      if self.is_unique_position(current_position):
        self.positions_visited.append({
          "row": current_position["row"],
          "col": current_position["col"],
          "is_guard": current_position["is_guard"],
          "direction": self.walking_direction
        })
      elif self.is_starting_position_and_direction(current_position):
        raise Exception("infinite!")
  
  def get_next_position(self, current_position):
    if self.walking_direction == "UP":
      next_position = self.map.get(f"{current_position["row"] - 1}-{current_position["col"]}", None)
    elif self.walking_direction == "RIGHT":
      next_position = self.map.get(f"{current_position["row"]}-{current_position["col"] + 1}", None)
    elif self.walking_direction == "DOWN":
      next_position = self.map.get(f"{current_position["row"] + 1}-{current_position["col"]}", None)
    elif self.walking_direction == "LEFT":
      next_position = self.map.get(f"{current_position["row"]}-{current_position["col"] - 1}", None)
    
    # If no next_position, it's complete
    if not next_position:
      return None   
    
    # If next_position is wall: rotate
    if next_position and next_position["is_wall"]:
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
    
  def is_starting_position_and_direction(self, position):
    return next((x for x in self.positions_visited if 
                x.get("row") == position.get("row") and
                x.get("col") == position.get("col") and
                x.get("direction") == self.walking_direction), None)
  
  def get_guard_position(self):
    for key in self.map:
      if self.map[key]["is_guard"]:
        return self.map[key]    
    
    return None
        
  def set_extra_obstruction(self, position):
    self.map[f"{position["row"]}-{position["col"]}"]["is_wall"] = True
    
  def create_map(self, file_contents):
    matrix = {}
    
    split_rows = file_contents.split("\n")
    
    for row_idx, row in enumerate(split_rows):
      points = list(row)
      
      for col_idx, point in enumerate(points):
        matrix[f"{row_idx}-{col_idx}"] = {
          "row": row_idx,
          "col": col_idx,
          "is_wall": point == "#",
          "is_floor": point != "#",
          "is_guard": point == "^"
        }
        
        if point == "^":
          self.positions_visited.append({
            "row": row_idx,
            "col": col_idx,
            "is_guard": True,
            "direction": self.walking_direction
          })
          
    return matrix
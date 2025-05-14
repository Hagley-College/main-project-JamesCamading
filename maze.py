""" Title:  
Author:  James Allen A. Camading
Date: 
Version:  
Purpose:    
""" 
avatar = (1,2,'A') #row colum Representation
goal = (1,3,'G') #row colum Representation
MAZE = [[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1]]
def print_maze(maze,avitar,goal):
  """ prints out maze to standard io
      -----
      - AG-
      -----
  """    
  #add code to print out maze
  pass
  
def move(avi,maze):
  """ change possition of avitar
  """   
  #add code to move  avitar
  pass

def play_game(avatar,goal,MAZE):
  """ main game loop
  """ 
  while not(avatar[0] == goal[0] and avatar[0] == goal[0]):
    pass
  print("congratulations")
  
if __name__ == "__main__":
  play_game(avatar,goal,MAZE)

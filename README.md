# TrickyTrianglePlanning 
Group 3 Planning Project

To run the Prolog file:
Compile the file in SWI-Prolog.
Query the below actions.

Actions:
  in(Peg,Hole) :- Shows relationships between a peg and it's corresponding hole. Uses atom empty when no peg is present.
  
  adjacent(Hole1, Hole2) :- Shows relationships between adjacent holes. Can be used to create full adjacency matrix.
  
  can_jump(Peg1, Peg2, Hole) :- Show whether a jump from Peg1 over Peg2 into Hole is possible. A jump is legal if Peg2 is adjacent to Peg1 and an empty Hole.
      TODO: can_jump needs to check for linear jumps. 
  
  jump(Peg1, Peg2, Hole) :- Changes the state of the game by jumping (if possible) Peg1 over Peg2 into Hole. Jump calls can_jump.  
  
  out(Peg1, Peg2, Hole) :- Prints message. Jump Peg1 over Peg2 into Hole.

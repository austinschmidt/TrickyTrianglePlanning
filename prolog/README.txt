TrickyTrianglePlanning

Group 3 Planning Project
____________________________________________________


To play the Triangle Game with a 5 row triangle lattice: 

Compile the file in SWI-Prolog. Query the below actions. 

refresh_game(5). %number of rows 

play(14). %number of pegs


____________________________________________________
Actions:

refresh_game(N) - Will retract all known assumptions about the work. Recreates peg-in-hole relationships putting empty in the top hole. Similarly, this generates all facts needed for a valid adjacency matrix. N is the max number of rows to include.

in(Peg,Hole) - Shows relationships between a peg and it's corresponding hole. Uses atom empty when no peg is present.

adjacent(Hole1, Hole2) - Shows relationships between adjacent holes. Can be used to create full adjacency matrix.

set_in(Peg,Hole) - Asserts peg-in-hole.

set_adjacent(Hole1, Hole2) - Asserts horizontal adjacency.

set_l_adjacent(Hole1, Hole2) - Asserts upward left adjacency. 
set_r_adjacent(Hole1, Hole2) - Asserts upward right adjacency. 
set_ld_adjacent(Hole1, Hole2) - Asserts downward left adjacency. 
set_rd_adjacent(Hole1, Hole2) - Asserts downward right adjacency.

can_jump(Peg1, Peg2, Hole) - Show whether a jump from Peg1 over Peg2 into Hole is possible. A jump is legal if Peg2 is adjacent to Peg1 and an empty Hole. Checks for horizontal and vertical jumps.

can_jump_vl(Peg1, Peg2, Hole) - Specific rule checking for jumping upward and to the left OR downward and to the left. 
can_jump_vr(Peg1, Peg2, Hole) - Specific rule checking for jumping upward and to the right OR downward and to the right. 
can_jump_h(Peg1, Peg2, Hole) - Specific rule checking hor horizontal jumps.

jump(Peg1, Peg2, Hole) - Changes the state of the game by jumping (if possible) Peg1 over Peg2 into Hole. Jump calls can_jump.

out(Peg1, Peg2, Hole) - Prints message. Jump Peg1 over Peg2 into Hole.

play(N) - Loops N times to represent number of pegs, making a valid jump each time. Once N=1, write out 'Win!' or false if no valid jumps remain.
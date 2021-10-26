PDDLGeneration.py

Here we have a python script for generating problems for the peg-in-hole problem domain.
Three shapes may be generated, and a size, a starting empty hole and an ending peg hole
are given as parameter. 

May create problems by calling the method:
create_peg_problem(problem_name, domain, shape, size, empty, end_peg_hole)

SHAPES: 

Line - N-sized single straight line of holes. 

Triangle - N-sized triangle lattice where N is the size of the largest row.

Square - NxN-sized square lattice. 

USAGE EXAMPLE:

#Creates a triangle lattice where N=5. Hole 2 will start empty and hole 2 will house
#the final peg. 
    domain = "pegs"
    shape = "triangle"
    size = 5
    empty = 2
    end_peg_hole = 2

    problem_name = shape+str(size)+"_"+str(empty)+"_"+str(end_peg_hole)

    pddl_string = create_peg_problem(problem_name, domain, shape, size, empty, end_peg_hole)

    f = open(save_loc+"/"+shape+"/problem-"+problem_name+".pddl","w")
    f.write(pddl_string)
    f.close()
    print(pddl_string)
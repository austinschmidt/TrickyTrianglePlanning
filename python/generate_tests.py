from PDDLGeneration import create_peg_problem
import os, math

def get_num_pegs(shape, size):
    
    if(shape=="triangle"):
        holes = sum(range(1,size+1))

    elif(shape=="square"):
        holes = math.floor(size*size / 2) #first half same as the second half

    elif(shape=="rectangle"):
        holes = math.floor(size*(size*2) / 2) #same

    elif(shape=="line"):
        holes = size

    elif(shape=="diamond"):
        holes = size*size 

    elif(shape=="arrow"):
        holes = sum(range(1,size+3)) + size*size
    return holes

if __name__ == "__main__":
    problem_types = ['triangle', 'line', 'square', 'rectangle', 'diamond', 'arrow']
    sizes = [5]

    for problem in problem_types:
        for size in sizes:
            save_loc = os.path.normpath(os.getcwd() + os.sep + os.pardir + "/PDDL/pegsinholes")
            domain = "pegs"
            shape = problem
            num_pegs = get_num_pegs(shape, size)
            for empty in range (num_pegs-1):
                for end_peg_hole in range(num_pegs-1):
                    problem_name = shape+str(size)+"_"+str(empty)+"_"+str(end_peg_hole)

                    pddl_string = create_peg_problem(problem_name, domain, shape, size, empty, end_peg_hole)

                    f = open(save_loc+"/"+shape+"/problem-"+problem_name+".pddl","w")
                    f.write(pddl_string)
                    f.close()
                    print("Generating " + problem_name + "......")
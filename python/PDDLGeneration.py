import os

def gen_pegs_in_holes(shape, size, empty):
    if(shape=="triangle"):
        holes = sum(range(1,size+1))
        return pegs_in_holes(holes,empty)

    elif(shape=="square"):
        holes = size*size
        return pegs_in_holes(holes,empty)

    elif(shape=="line"):
        return pegs_in_holes(size,empty)

    else:
        return "Invalid Shape For Goal"
    
def pegs_in_holes(holes, empty):
    in_string = ""
    peg_counter=0
    for spot in range(holes):
        if(spot != empty):
            in_string+= "\t(in p" + str(peg_counter) + " h" +str(spot) + ")\n" 
            peg_counter+=1
    return in_string

def adjacency(shape, shape_size):
    if(shape=="triangle"):
        return triangle_adjacency(shape_size)

    elif(shape=="square"):
        return square_adjacency(shape_size)

    elif(shape=="line"):
        return line_adjacency(shape_size) 

    else:
        return "Invalid Shape For Goal"

def triangle_adjacency(shape_size):
    adj_string = ""
    peg_num = 0
    col_reduc=0
    for row in range(shape_size-1):
        row_num = shape_size-col_reduc
        for col in range(row_num):

            #horizontal adjacency
            if(col+1%(row_num)!=(row_num)):
                adj_string+= "\t(adjacent h" + str(peg_num) + " h" +str(peg_num+1) + ")\n" 
                adj_string+= "\t(adjacent h" + str(peg_num+1) + " h" +str(peg_num) + ")\n"
            
            #vertical_l adjacency
            if(col!=0):
                adj_string+= "\t(adjacent h" + str(peg_num) + " h" +str(peg_num+row_num-1) + ")\n" 
                adj_string+= "\t(adjacent h" + str(peg_num+row_num-1) + " h" +str(peg_num) + ")\n"
    
            #vertical_r adjacency
            if(col!=row_num-1):
                adj_string+= "\t(adjacent h" + str(peg_num) + " h" +str(peg_num+row_num) + ")\n" 
                adj_string+= "\t(adjacent h" + str(peg_num+row_num) + " h" +str(peg_num) + ")\n"

            peg_num+=1
        col_reduc+=1
    return adj_string

def square_adjacency(shape_size):
    adj_string = ""
    peg_num = 0
    for row in range(shape_size):
        for col in range(shape_size):

            #horizontal adjacency
            if(col!=shape_size-1):
                adj_string+= "\t(adjacent h" + str(peg_num) + " h" +str(peg_num+1) + ")\n" 
                adj_string+= "\t(adjacent h" + str(peg_num+1) + " h" +str(peg_num) + ")\n"
            
            #vertical adjacency
            if(row!=shape_size-1):
                adj_string+= "\t(adjacent h" + str(peg_num) + " h" +str(peg_num+shape_size) + ")\n" 
                adj_string+= "\t(adjacent h" + str(peg_num+shape_size) + " h" +str(peg_num) + ")\n"
    
            peg_num+=1
    return adj_string

def line_adjacency(shape_size):
    adj_string = ""
    for spot in range(shape_size-1):
        adj_string+= "\t(adjacent h" + str(spot) + " h" +str(spot+1) + ")\n" 
        adj_string+= "\t(adjacent h" + str(spot+1) + " h" +str(spot) + ")\n"
    
    return adj_string

def inline(shape, shape_size):
    if(shape=="triangle"):
        return triangle_inline(shape_size)

    elif(shape=="square"):
        return square_inline(shape_size)

    elif(shape=="line"):
        return line_inline(shape_size)
    else:
        return "Invalid Shape For Goal"

def triangle_inline(shape_size):
    inline_string = ""
    peg_num = 0
    col_reduc=0
    for row in range(shape_size-1):
        if (row==shape_size-1):
            n=""
        else:
            n="\n"

        row_num = shape_size-col_reduc
        for col in range(row_num):

            #horizontal line
            if(col+2%(row_num)<(row_num) and row<shape_size-2):
                inline_string+= "\t(inline h" + str(peg_num) + " h" + str(peg_num+1) + " h" + str(peg_num+2) + ")\n" 
                inline_string+= "\t(inline h" + str(peg_num+2) + " h" + str(peg_num+1) + " h" + str(peg_num) + ")\n"
            
            #vertical_l line
            if(col>1 and row<shape_size-2):
                inline_string+= "\t(inline h" + str(peg_num) + " h" + str(peg_num+row_num-1) + " h" + str(peg_num+row_num*2-3) + ")\n" 
                inline_string+= "\t(inline h" + str(peg_num+row_num*2-3) + " h" + str(peg_num+row_num-1) + " h" + str(peg_num) + ")\n" 
    
            #vertical_r line
            if(col<row_num-2 and row<shape_size-2):
                inline_string+= "\t(inline h" + str(peg_num) + " h" + str(peg_num+row_num) + " h" + str(peg_num+row_num*2-1) + ")\n" 
                inline_string+= "\t(inline h" + str(peg_num+row_num*2-1) + " h" + str(peg_num+row_num) + " h" + str(peg_num) + ")" + n

            peg_num+=1
        col_reduc+=1
    return inline_string

def square_inline(shape_size):
    inline_string = ""
    peg_num = 0
    for row in range(shape_size):
        if (row==shape_size-2):
            n=""
        else:
            n="\n"
        for col in range(shape_size):

            #horizontal line
            if(col%shape_size<shape_size-2):
                inline_string+= "\t(inline h" + str(peg_num) + " h" +str(peg_num+1) + " h" +str(peg_num+2) + ")\n" 
                inline_string+= "\t(inline h" + str(peg_num+2) + " h" +str(peg_num+1) + " h" +str(peg_num) + ")\n"
            
            #vertical line
            if(row<shape_size-2):
                inline_string+= "\t(inline h" + str(peg_num) + " h" +str(peg_num+shape_size) + " h" +str(peg_num+shape_size*2) +")\n" 
                inline_string+= "\t(inline h" + str(peg_num+shape_size*2) + " h" +str(peg_num+shape_size) + " h" +str(peg_num) + ")" + n

            peg_num+=1

    return inline_string

def line_inline(shape_size):
    inline_string = ""
    for spot in range(shape_size-2):
        if (spot==shape_size-3):
            n=""
        else:
            n="\n"
        inline_string+= "\t(inline h" + str(spot) + " h" + str(spot+1) + " h" + str(spot+2) + ")\n" 
        inline_string+= "\t(inline h" + str(spot+2) + " h" + str(spot+1) + " h" + str(spot) + ")" + n
    return inline_string

def gen_define (problem):
    return "(define (problem " + problem + ")\n"
    
def gen_domain (domain):
    return "(:domain "+ domain + ")\n"

def gen_objects(shape, size):
    if(shape=="triangle"):
        holes = sum(range(1,size+1))
        return objects(holes)

    elif(shape=="square"):
        holes = size*size
        return objects(holes)

    elif(shape=="line"):
        return objects(size)

    else:
        return "Invalid Shape For Goal"

def objects(holes):
    objects = "(:objects "
    for spot in range(holes):
        if(spot!=holes-1):
            if(spot%10==0):
                objects+="\n\t"
            objects+=("p"+str(spot)+" ")
        objects+=("h"+str(spot)+" ")
    objects+=")\n"
    return objects

def gen_init(shape, size, empty):
    init = "(:init\n\t(empty h"+ str(empty) +")\n" 
    init += gen_pegs_in_holes(shape, size, empty)
    init += adjacency(shape, size)
    init += inline(shape, size)
    init += ")\n"
    return init

def gen_goal(shape, size, not_empty):
    if(shape=="triangle"):
        holes = sum(range(1,size+1))
        return goal(holes, not_empty)

    elif(shape=="square"):
        holes = size*size
        return goal(holes, not_empty)

    elif(shape=="line"):
        return goal(size, not_empty)

    else:
        return "Invalid Shape For Goal"

def goal(holes, not_empty):
    if(holes>2):
        goal = "(:goal (and \n"
        m=")"
    else:
        goal = "(:goal \n"
        m=""

    for spot in range(holes):
        if(spot!=not_empty):
            goal+="\t(empty h"+str(spot)+")\n"
    
    goal+=")"+m
    return goal

def create_peg_problem(problem_name, domain, shape, size, empty, end_peg_hole):
    formatted_define = gen_define(problem_name)
    formatted_domain = gen_domain(domain)
    formatted_objects = gen_objects(shape, size)
    formatted_init = gen_init(shape, size, empty)
    formatted_goal = gen_goal(shape, size, end_peg_hole)

    final_pddl = formatted_define + formatted_domain + formatted_objects + formatted_init + formatted_goal + ")" #Closing ) to ensure all are wrapped by define
    return final_pddl

if __name__ == "__main__":
	
    save_loc = os.path.normpath(os.getcwd() + os.sep + os.pardir + "/PDDL/pegsinholes")
    domain = "pegs"
    shape = "square"
    size = 5
    empty = 1
    end_peg_hole = 12

    problem_name = shape+str(size)+"_"+str(empty)+"_"+str(end_peg_hole)

    pddl_string = create_peg_problem(problem_name, domain, shape, size, empty, end_peg_hole)

    f = open(save_loc+"/"+shape+"/problem-"+problem_name+".pddl","w")
    f.write(pddl_string)
    f.close()
    print(pddl_string)
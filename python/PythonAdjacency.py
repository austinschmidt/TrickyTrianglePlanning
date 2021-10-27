def set_holes(shape, size, holes):
    if(shape=="triangle"):
        return triangle_holes(size, holes)

    elif(shape=="square"):
        return ""
    elif(shape=="rectangle"):
        return ""

    elif(shape=="line"):
        return ""

    elif(shape=="diamond"):
        return ""

    elif(shape=="arrow"):
        return ""

    else:
        return "Invalid Shape For Goal"

def triangle_holes(size, holes):
    peg_num = 0
    col_reduc=0
    for row in range(size-1):
        row_num = size-col_reduc
        for col in range(row_num):

            #horizontal adjacency
            if(col+1%(row_num)!=(row_num)):
                holes[peg_num].add_adjacent(holes[peg_num+1])
                holes[peg_num+1].add_adjacent(holes[peg_num])
            
            #vertical_l adjacency
            if(col!=0):
                holes[peg_num].add_adjacent(holes[peg_num+row_num-1])
                holes[peg_num+row_num-1].add_adjacent(holes[peg_num])
    
            #vertical_r adjacency
            if(col!=row_num-1):
                holes[peg_num].add_adjacent(holes[peg_num+row_num])
                holes[peg_num+row_num].add_adjacent(holes[peg_num])

            peg_num+=1
        col_reduc+=1
    return holes


def set_lines(shape, size, lines, holes):
    if(shape=="triangle"):
        return triangle_inline(size, lines, holes)

    elif(shape=="square"):
        return ""
    elif(shape=="rectangle"):
        return ""

    elif(shape=="line"):
        return ""

    elif(shape=="diamond"):
        return ""

    elif(shape=="arrow"):
        return ""
    else:
        return "Invalid Shape For Goal"

def triangle_inline(size, lines, holes):
    peg_num = 0
    col_reduc=0
    for row in range(size-1):
        row_num = size-col_reduc
        for col in range(row_num):
            #horizontal line
            if(col+2%(row_num)<(row_num) and row<size-2):
                lines.append([holes[peg_num],holes[peg_num+1], holes[peg_num+2]])
                lines.append([holes[peg_num+2],holes[peg_num+1], holes[peg_num]])

            #vertical_l line
            if(col>1 and row<size-2):
                lines.append([holes[peg_num],holes[peg_num+row_num-1], holes[peg_num+row_num*2-3]])
                lines.append([holes[peg_num+row_num*2-3],holes[peg_num+row_num-1], holes[peg_num]])
    
            #vertical_r line
            if(col<row_num-2 and row<size-2):
                lines.append([holes[peg_num],holes[peg_num+row_num], holes[peg_num+row_num*2-1]])
                lines.append([holes[peg_num+row_num*2-1],holes[peg_num+row_num], holes[peg_num]])

            peg_num+=1
        col_reduc+=1
    return lines
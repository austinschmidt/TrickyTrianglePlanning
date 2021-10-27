def set_holes(shape, size, holes):
    if(shape=="triangle"):
        return triangle_holes(size, holes)

    elif(shape=="square"):
        return square_holes(size, size, holes)

    elif(shape=="rectangle"):
        return square_holes(size, size*2, holes)

    elif(shape=="line"):
        return line_holes(size, holes)

    elif(shape=="diamond"):
        return diamond_holes(size, holes)

    elif(shape=="arrow"):
        return arrow_holes(size, holes)

    else:
        return "Invalid Shape For Goal"

def set_lines(shape, size, lines, holes):
    if(shape=="triangle"):
        return triangle_inline(size, lines, holes)

    elif(shape=="square"):
        return square_inline(size, size, lines, holes)

    elif(shape=="rectangle"):
        return square_inline(size, size*2, lines, holes)

    elif(shape=="line"):
        return line_inline(size, lines, holes)

    elif(shape=="diamond"):
        return diamond_inline(size, lines, holes)

    elif(shape=="arrow"):
        return arrow_inline(size, lines, holes)
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

def square_holes(shape_size, rect_offset, holes):
    peg_num = 0
    for row in range(rect_offset):
        for col in range(shape_size):
            #horizontal adjacency
            if(col!=shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+1])
                holes[peg_num+1].add_adjacent(holes[peg_num])
            
            #vertical adjacency
            if(row!=rect_offset-1):                
                holes[peg_num].add_adjacent(holes[peg_num+shape_size])
                holes[peg_num+shape_size].add_adjacent(holes[peg_num])
    
            peg_num+=1
    return holes

def line_holes(shape_size, holes):
    for spot in range(shape_size-1):
        holes[spot].add_adjacent(holes[spot+1])
        holes[spot+1].add_adjacent(holes[spot])
    
    return holes

def diamond_holes(shape_size, holes):
    peg_num = 0
    col_reduc=shape_size-1
    for row in range(shape_size):
        row_num = shape_size-col_reduc
        for col in range(row_num):
            #horizontal adjacency
            if(col+1%(row_num)!=(row_num) and row_num!=1):
                holes[peg_num].add_adjacent(holes[peg_num+1])
                holes[peg_num+1].add_adjacent(holes[peg_num])
            
            #0 special case
            if(row == 0):
                holes[peg_num].add_adjacent(holes[peg_num+row_num])
                holes[peg_num+row_num].add_adjacent(holes[peg_num])
                holes[peg_num].add_adjacent(holes[peg_num+row_num+1])
                holes[peg_num+row_num+1].add_adjacent(holes[peg_num])

            #vertical_l adjacency
            if(col!=row_num-1 and row!=shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+row_num])
                holes[peg_num+row_num].add_adjacent(holes[peg_num])
    
            #vertical_r adjacency
            if(col!=row_num and row!=shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+row_num+1])
                holes[peg_num+row_num+1].add_adjacent(holes[peg_num])

            peg_num+=1
        col_reduc-=1
    peg_num-=shape_size #Resetting overcounted pegs
    col_reduc=0
    for row in range(shape_size-1):
        row_num = shape_size-col_reduc
        for col in range(row_num):
            #horizontal adjacency
            if(col+1%(row_num)!=(row_num) and col_reduc!=0):
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

def arrow_holes(shape_size, holes):
    peg_num = 0
    for row in range(shape_size):
        for col in range(shape_size):

            #horizontal adjacency
            if(col!=shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+1])
                holes[peg_num+1].add_adjacent(holes[peg_num])
            
            #vertical adjacency
            if(row!=shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+shape_size])
                holes[peg_num+shape_size].add_adjacent(holes[peg_num])
    
            if(row == shape_size-1):
                holes[peg_num].add_adjacent(holes[peg_num+shape_size+1])
                holes[peg_num+shape_size+1].add_adjacent(holes[peg_num])

            peg_num+=1
    col_reduc=0
    shape_size+=2
    for row in range(shape_size-1):
        row_num = shape_size-col_reduc
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

def square_inline(size, rect_offset, lines, holes):
    peg_num = 0
    for row in range(rect_offset):
        for col in range(size):
            #horizontal line
            if(col%size<size-2):
                lines.append([holes[peg_num],holes[peg_num+1], holes[peg_num+2]])
                lines.append([holes[peg_num+2],holes[peg_num+1], holes[peg_num]])
            
            #vertical line
            if(row<rect_offset-2):
                lines.append([holes[peg_num],holes[peg_num+size], holes[peg_num+size*2]])
                lines.append([holes[peg_num+size*2],holes[peg_num+size], holes[peg_num]])
            peg_num+=1

    return lines

def line_inline(size, lines, holes):
    for spot in range(size-2):
        if (spot==size-3):
            n=""
        else:
            n="\n"
        lines.append([holes[spot],holes[spot+1], holes[spot+2]])
        lines.append([holes[spot+2],holes[spot+1], holes[spot]])
    return lines

def diamond_inline(size, lines, holes):
    peg_num = 0
    col_reduc=size-1
    for row in range(size):
        row_num = size-col_reduc
        for col in range(row_num):
            #horizontal line
            if(col+2%(row_num)<(row_num) and row_num>2):
                lines.append([holes[peg_num],holes[peg_num+1], holes[peg_num+2]])
                lines.append([holes[peg_num+2],holes[peg_num+1], holes[peg_num]])
            
            #vertical_l line
            if(row<size-2):
                lines.append([holes[peg_num],holes[peg_num+row_num], holes[peg_num+row_num*2+1]])
                lines.append([holes[peg_num+row_num*2+1],holes[peg_num+row_num], holes[peg_num]])
            elif(row<size-1 and col>0):
                lines.append([holes[peg_num],holes[peg_num+size-1], holes[peg_num+size*2-2]])
                lines.append([holes[peg_num+size*2-2],holes[peg_num+size-1], holes[peg_num]])
    
            #vertical_r line
            if(row_num<size-1 and row_num>0):
                lines.append([holes[peg_num],holes[peg_num+row_num+1], holes[peg_num+row_num*2+3]])
                lines.append([holes[peg_num+row_num*2+3],holes[peg_num+row_num+1], holes[peg_num]])

            elif(row<size-1 and col<size-2):
                lines.append([holes[peg_num],holes[peg_num+size], holes[peg_num+size*2]])
                lines.append([holes[peg_num+size*2],holes[peg_num+size], holes[peg_num]])

            peg_num+=1
        col_reduc-=1

    peg_num-=size #Resetting overcounted pegs
    col_reduc=0
    for row in range(size-1):
        row_num = size-col_reduc
        for col in range(row_num):
            #horizontal line
            if(col+2%(row_num)<(row_num) and row<size-2 and row>0):
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

def arrow_inline(size, lines, holes):
    peg_num = 0
    for row in range(size):
        for col in range(size):
            #horizontal line
            if(col%size<size-2):
                lines.append([holes[peg_num],holes[peg_num+1], holes[peg_num+2]])
                lines.append([holes[peg_num+2],holes[peg_num+1], holes[peg_num]])
            
            #vertical line
            if(row<size-2):
                lines.append([holes[peg_num],holes[peg_num+size], holes[peg_num+size*2]])
                lines.append([holes[peg_num+size*2],holes[peg_num+size], holes[peg_num]]) 
            
            if(row<size-1):
                lines.append([holes[peg_num],holes[peg_num+size], holes[peg_num+size*2+1]])
                lines.append([holes[peg_num+size*2+1],holes[peg_num+size], holes[peg_num]])

            peg_num+=1
    size+=2
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
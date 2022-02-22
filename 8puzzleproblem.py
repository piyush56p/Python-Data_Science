
import sys
import copy


visited=[]
q=[]
def enqueue(x):
    global q
    global visited
    if x not in visited:
        q = q +[x]
        
    
def deqeue():
    global q
    new_state = q[0]
    del q[0]
    return new_state
    
def compare(s,goal):
    if(s==goal):
        return 1
    else:
        return 0
def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if(s[i][j] == 0):
                return [i,j]
        
def up(s,pos):
    
    row=pos[0]
    col = pos[1]
    if(row==0):
        return s
    else:
        
        s[row][col] = s[row-1][col]
        s[row-1][col] = 0
        
    return s
    pos = find_pos(s)
def down(s,pos):
    
    row=pos[0]
    col = pos[1]
    if(row==2):
        return s
    else:
        
        s[row][col] = s[row+1][col]
        s[row+1][col] = 0
        

    return s
    pos=find_pos(s)

def right(s,pos):
    right=[]
    row= pos[0]
    col = pos[1]
    if(col==2):
        return s
    else:
        s[row][col] = s[row][col+1]
        s[row][col+1] = 0
    return s
    pos=find_pos(s)

def left(s,pos):
    left=[]
    row = pos[0]
    col = pos[1]
    if(col==0):
        return s
    else:
        s[row][col] = s[row][col-1]
        s[row][col-1] = 0
    return s
    pos=find_pos(s)

def main():
    
    
    x=[[1,2,3],[8,0,4],[7,6,5]]
    goal = [[2,8,1],[0,4,3],[7,6,5]]
    
    y=find_pos(x)
    print(y)
    while(1):
    
    
    
 
    

        # for i in range(len(x)-1):
        #     if(x[i].index(0)):
        #         print('yes')
        #         break
        #     else:
        #         continue
        xup=copy.deepcopy(x)
        xup= up(xup,find_pos(xup))
        print(xup)
        
        
        
        xdown = copy.deepcopy(x)
        xdown = down(xdown,find_pos(xdown))
        print(xdown)

        xright = copy.deepcopy(x)
        xright = right(xright,find_pos(xright))
        print(xright)
        
        xleft = copy.deepcopy(x)
        xleft = left(xleft,find_pos(xleft))
        print(xleft)
    
        if(compare(xup,goal) or compare(xdown,goal) or compare(xright,goal) or compare(xleft,goal)):
            return 0
        else:
            q = enqueue(xup)
            q = enqueue(xdown)
            q = enqueue(xleft)
            q = enqueue(xright)
        
        print (q) 
        new_state = deqeue()
        print(new_state)   
        x=new_state
        global visited
        visited=visited+[x]
        print (len(visited))
        print(x)

        
        
        # xright=right(x,y)
        # xleft = left(x,y)     
        # print(xup)
        # print(xdown)
        # print(xright)
        # print(xleft)
    

if __name__ == "__main__":
    main()

# Recursive Python function to solve tower of hanoi 
  
moves = 0
linenumber = 1

def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    global moves
    global linenumber
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print(linenumber, "Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    moves += 1
    linenumber += 1
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
  
  
# Driver code 
N = 3
  
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 

print('total moves', moves)



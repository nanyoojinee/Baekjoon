import copy

def dfs(graph,x,y,position,n,num):
    xydic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    puzzle = [position]
    for i in range(4):
        nx = x + xydic[i][0]
        ny = y + xydic[i][1]
        
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            puzzle = puzzle + dfs(graph,nx,ny,[position[0]+xydic[i][0],position[1]+xydic[i][1]],n,num)
            
    return puzzle
            
def rotate(lst):
    n = len(lst)
    
    puzzle = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            puzzle[j][n-1-i] = lst[i][j]
    
    return puzzle
    
def solution(game_board, table):
    answer = 0
    game_board_copy = copy.deepcopy(game_board)
    
    n = len (game_board)
    block = []
    
    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j]==0:
                game_board_copy[i][j]=2
                result = dfs(game_board_copy,i,j,[0,0],n,0)[1:]
                block.append(result)
    
    for r in range(4):
        table = rotate(table)
        table_copy = copy.deepcopy(table)
        
        for i in range(n):
            for j in range(n):
                if table_copy[i][j]==1:
                    table_copy[i][j]=2
                    
                    result = dfs(table_copy,i,j,[0,0],n,1)[1:]
                    
                    if result in block :
                        block.pop(block.index(result))
                        answer += (len(result)+1)
                        
                        table = copy.deepcopy(table_copy)
                    else:
                        table_copy = copy.deepcopy(table)
                    
        
    return answer


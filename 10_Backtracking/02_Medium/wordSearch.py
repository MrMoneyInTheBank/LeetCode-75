

def exists(grid, word):
    R = len(grid)
    C = len(grid[0])
    seen = set()


    def dfs(r, c, i):
        if i == len(word):
            return True 
        
        if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != word[i] or (r, c) in seen:
            return False 
        
        seen.add((r, c))

        res = dfs(r+1, c, i + 1) or dfs(r-1, c, i + 1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
    
        seen.remove((r, c))

        return res 
    
    for r in range(R):
        for c in range(C):
            if dfs(r, c, 0):
                return True 
            
    
    return False 

# Every cell in the grid can be considered the starting point. Clearly we need a path finding algorithm like DFS but 
# implementing it is a bit tricky. We also have to use backtracking. The DFS function will tell us if we can find a sub
# section of the word (the word is a subsection of itself) from coordinates r, and c. If we have already found all letters
# and we know that they are the correct letters in the correct order, then we can return True. Otherwise, we check if we are 
# out of bounds, the current cell has already been visited, or if the current cell is the wrong letter. In all of those cases,
# we return False. Now we move on to the neighbours of the current cell but before this we must add that we have seen the current 
# cell. After traversing the neighbours and all of their paths, we must remove the current cell since if we haven't found the word
# there is a chance that the current cell might be used in a different path to complete the word. After implementing this funciton, 
# we just need to traverse every cell in the grid and call this DFS function on it. If we ever find the word, we return True. If the
# loop ends, that means we have no found the word yet. 


# Time | Space: O(k * (n * m) ** 4) | O(k) 
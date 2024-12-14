def task_1():
    # Read the grid from input.txt
    grid = []
    with open('input.txt', 'r') as file:
        for line in file:
            # Convert each line into a list of characters, removing whitespace
            row = [char for char in line.strip()]
            grid.append(row)
    
    rows = len(grid)
    cols = len(grid[0])
    word = 'XMAS'
    count = 0
    
    # Define all 8 directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
        (0, -1),           (0, 1),    # Left, Right
        (1, -1),  (1, 0),  (1, 1)    # Down-left, Down, Down-right
    ]
    
    # Check each cell as a potential starting point
    for row in range(rows):
        for col in range(cols):
            # Check each direction from this cell
            for dx, dy in directions:
                # Try to find word starting from this cell and direction
                if check_word(grid, word, row, col, dx, dy):
                    count += 1
    
    print(f"Found {count} matches of 'XMAS'")
    return count

def check_word(grid, word, row, col, dx, dy):
    rows = len(grid)
    cols = len(grid[0])
    
    # Check if word fits in this direction
    if not (0 <= row + dx*(len(word)-1) < rows and 
            0 <= col + dy*(len(word)-1) < cols):
        return False
    
    # Check each letter
    for i in range(len(word)):
        if grid[row + dx*i][col + dy*i] != word[i]:
            return False
            
    return True

def task_2():
    pass

if __name__ == "__main__":
    task_1()
    task_2()


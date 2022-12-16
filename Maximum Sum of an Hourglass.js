var maxSum = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let ans = 0;
    for(let r = 0; r < rows - 2; r++){
        for (let c = 0; c < cols - 2; c++){
            let curr_sum = grid[r][c] 
                        + grid[r][c+1]
                        + grid[r][c+2]
                        + grid[r+1][c+1]
                        + grid[r+2][c] 
                        + grid[r+2][c+1]
                        + grid[r+2][c+2];
            ans = Math.max(ans, curr_sum);
        }
    }

    return ans;
};

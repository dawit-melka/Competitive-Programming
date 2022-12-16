var transpose = function(matrix) {
    let rows = matrix.length;
    let cols = matrix[0].length;
    const transposed = Array(cols).fill().map(()=> Array(rows).fill(0));
    for(let r = 0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            transposed[c][r] = matrix[r][c];
        }
    }
    return transposed;
};

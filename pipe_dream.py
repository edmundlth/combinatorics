import numpy as np

def top_aligned_pipe_dream(perm):
    """
    Generate an N by N grid of binary numbers with 
    0 representing the 'elbow' and 
    1 representing the 'cross' in the top-aligned pipe dream
    for the input permutation 'perm' on the N-set. 
    
    Note: Input permutation has to be zero-indexed, 
          i.e. for permutation on N-set, it will have values
          that range from 0 to N -1. 
    """
    N = len(perm)
    # initiate N by N grid of zeros
    result = np.zeros((N, N), dtype=int)
    for i in range(N):
        row_num = i
        col_num = 0
        while col_num < perm[i]:
            if row_num == 0 or result[row_num - 1][col_num] == 1: 
                # if we are on the first row or the cell above is occupied
                # then we need a cross here, which gets us to the next column
                result[row_num][col_num] += 1
                col_num += 1
            else: 
                # otherwise we make a half-elbow turn
                # which gets us to the row above without changing column number
                row_num -= 1
                col_num += 1
    return result

def left_aligned_pipe_dream(perm):
    """
    We note that the left aligned pipe dream is
    simply the transpose of the top-aligned pipe dream
    of the inverse permutation
    """
    N = len(perm)
    inverse_perm = list(range(N)) # initiate array of length N
    for i in range(N): # compute inverse permutation 
        inverse_perm[perm[i]] = i
    # compute top-aligned pipe dream
    pipe_dream = top_aligned_pipe_dream(inverse_perm)
    # return its transpose
    return pipe_dream.transpose()

def inverse_permutation(perm):
    """
    Compute the inverse permutation. 
    """
    N = len(perm)
    inv = list(range(N))
    for i in range(N):
        inv[perm[i]] = i
    return inv

def draw_tikz_grid(n, m):
    """
    Output tikz commands that draws an n x m square grid. 
    """
    tikz_commands = ""
    for row in range(n):
        tikz_commands += "\\node at (-0.5, %.1f) {%i};" % (row + 0.5, n - row)
        tikz_commands += "\\draw (0, %i) -- (%i, %i); \n" % (row, m, row )
    for col in range(m):
        tikz_commands += "\\node at (%.1f, %.1f) {%i};" % (col + 0.5, n + 0.5, col + 1)
        tikz_commands += "\\draw (%i, 0) -- (%i, %i); \n" % (col, col, n)
        
    tikz_commands += "\\draw (0, %i) -- (%i, %i); \n" % (n, m, n)
    tikz_commands += "\\draw (%i, 0) -- (%i, %i); \n" % (m, m, n)
    return tikz_commands

def draw_tikz_pipe_dream(pipe_dream):
    """
    Output tikz command that draw the given 
    pipe dream (represented as binary N x N array). 
    """
    N = len(pipe_dream)
    tikz_commands = draw_tikz_grid(N, N)
    for i in range(N):
        for j in range(N - i):
            if pipe_dream[i][j]: 
                tikz_commands += "\\draw (%.1f, %.1f) -- (%.1f, %.1f); " % (j, N - i - 0.5, j + 1, N - i - 0.5)
                tikz_commands += "\\draw (%.1f, %.1f) -- (%.1f, %.1f); \n" % (j + 0.5, N - i, j + 0.5, N - i -1)
            else:
                tikz_commands += "\\draw (%.1f, %.1f) arc (-90:0: 0.5); \n" % (j, N - i - 0.5)
                if N - i != j +1:
                    tikz_commands += "\\draw (%.1f, %.1f) arc (90:180: 0.5); \n" % (j +1, N - i - 0.5)
    return tikz_commands

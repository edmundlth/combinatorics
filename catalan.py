

def tree_to_path(tree):
    """
    Recursively construct a binary path 
    by traversing the tree
    in the depth-first order. 
    
    Examples of complete binary trees (L for leaf):
      - [] 
      - [L, L]
      - [[L, L], L]
      - [[L, L], [[L, L], L]]
    
    Incomplete binary trees (None for missing child): 
      - [None, [L, L]]
      - [L, None]
    """
    if not tree: # empty tree
        return ""
    else: 
        left, right = tree
        leftword = ""
        rightword = ""
        if left is not None: 
            if left == 'L':
                leftword = "0"
            else: 
                leftword = "0" + tree_to_path(left)
        if right is not None:
            if right == 'L':
                rightword = "1"
            else: 
                rightword = "1" + tree_to_path(right)
        return leftword + rightword

    
def tree2path(tree):
    if not tree or tree == 'L': 
        return ""
    else: 
        return "E" + tree2path(tree[0]) + "N" + tree2path(tree[1])
    


def draw_path(binarypath):
    pathlength = len(binarypath)
    num_0 = binarypath.count("0")
    num_1 = binarypath.count("1")
    tikz_commands = ""
    for row in range(num_0):
        tikz_commands += "\\draw [dashed] (0, %i) -- (%i, %i); \n" % (row, num_1, row )
    for col in range(num_1):
        tikz_commands += "\\draw [dashed] (%i, 0) -- (%i, %i); \n" % (col, col, num_0)
    tikz_commands += "\\draw [dashed] (0, %i) -- (%i, %i); \n" % (num_0, num_1, num_0)
    tikz_commands += "\\draw [dashed] (%i, 0) -- (%i, %i); \n" % (num_1, num_1, num_0)
    tikz_commands += "\\draw [dashed] (0, 0) -- (%i, %i); \n" % (num_0, num_1)
    #tikz_commands = "\\draw (0, 0) -- (%i, 0); \n" % num_0
    #tikz_commands += "\\draw (0, 0) -- (0, %i); \n" % num_1
    #tikz_commands += "\\draw [dashed] (0, %i) -- (%i, %i); \n" % (num_1, num_0, num_1)
    #tikz_commands += "\\draw [dashed] (%i, 0) -- (%i, %i); \n" % (num_0, num_0, num_1)
    current_x = 0
    current_y = 0
    for step in binarypath:
        if step == "0" :
            tikz_commands += "\\draw [-> , line width=1mm, blue] (%i, %i) -- (%i, %i); \n" % (current_x, current_y, current_x + 1, current_y)
            current_x += 1
        elif step == "1":
            tikz_commands += "\\draw [-> , line width=1mm, red] (%i, %i) -- (%i, %i); \n" % (current_x, current_y, current_x, current_y + 1)
            current_y += 1
        else: 
            print("ERROR: Unrecognised step")
    return tikz_commands


def draw_catalan_arches(arches):
    N = len(arches) * 2
    tikz_commands = "\\draw [dashed] (-1, 0) -- (%i, 0); \n" % N
    for i in range(N):
        tikz_commands += "\\node at (%i, -0.3) {%i}; " % (i, i + 1)
        tikz_commands += "\\draw [fill=black] (%i, 0) circle [radius=0.1]; \n" % i
    for left, right in arches:
        radius = (right - left) / 2.0
        tikz_commands += "\\draw (%i, 0) arc (0:180:%s); \n" % (right -1, radius)
        
    return tikz_commands

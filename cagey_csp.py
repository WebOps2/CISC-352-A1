# =============================
# Student Names:
# Group ID:
# Date:
# =============================
# CISC 352
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all Variables in the given csp. If you are returning an entire grid's worth of Variables
they should be arranged linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional Variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 0.5/3 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
| n^2-n | n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '%' for modular addition
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
import itertools

def binary_ne_grid(cagey_grid):
    ##IMPLEMENT
    domain = []
    for i in range(1, cagey_grid[0] + 1):
        domain.append(i)
    var_array = []
    for r in range(cagey_grid[0]):
        var_array.append([])
        for c in range(cagey_grid[0]):
            var_array[r].append(Variable(f"Cell{r+1}{c+1}", domain))
            
    sat_tuples = []
    for pair in itertools.product(domain, domain):
        if pair[0] != pair[1]:
            sat_tuples.append(pair)
    var_lst = []
    for row in range(cagey_grid[0]):
        for col in range(cagey_grid[0]):
            var_lst.append(var_array[row][col])
    csp = CSP("Cagey", var_lst)
    
    for row in range(cagey_grid[0]):
        for col1 in range(cagey_grid[0]):
            for col2 in range(col1 + 1, cagey_grid[0]):
                con = Constraint(f"Row{row+1}", [var_array[row][col1], var_array[row][col2]])
                con.add_satisfying_tuples(sat_tuples)
                csp.add_constraint(con)
    for col in range(cagey_grid[0]):
        for row1 in range(cagey_grid[0]):
            for row2 in range(row1 + 1, cagey_grid[0]):
                con = Constraint(f"Col{col+1}", [var_array[row1][col], var_array[row2][col]])
                con.add_satisfying_tuples(sat_tuples)
                csp.add_constraint(con)
                
    return csp, var_lst


def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    """
    return a CSP and a 2D list of variables modeling Cagey grid (n-ary all-diff contraints)
    """
    n = cagey_grid[0]  # board size

    # variables for each cell
    domain = list(range(1, n + 1))
    var_array = [] # 2D array of variables
    variables = [] # all variables

    # create csp variables per cell, store in both var_array and variables
    for r in range(1, n + 1):
        row_vars = []
        for c in range(1, n + 1):
            v = Variable(f"V{r},{c}", domain)
            row_vars.append(v)
            variables.append(v)
        var_array.append(row_vars)

    csp = CSP("nary_ad_grid", variables)

    # all allowed tuples
    sat_tuples = list(itertools.permutations(domain, n))

    # row all-diffs
    for r in range(n):
        scope = var_array[r]
        con = Constraint(f"Row{r+1}", scope)
        con.add_satisfying_tuples(sat_tuples)
        csp.add_constraint(con)

    # columns
    for c in range(n):
        scope = [var_array[r][c] for r in range(n)]
        con = Constraint(f"Col{c+1}", scope)
        con.add_satisfying_tuples(sat_tuples)
        csp.add_constraint(con)

    return csp, var_array

def cagey_csp_model(cagey_grid):
    ##IMPLEMENT
    pass

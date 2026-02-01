# =============================
# Student Names: Remy Yoo, Daniel Wan, Kosi Amobi-Oleka
# Group ID: Group 30
# Date: 1/2/2026
# =============================
# CISC 352
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

1. ord_dh (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Degree heuristic

2. ord_mv (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Minimum-Remaining-Value heuristic


var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    Variables and constraints of the problem. The assigned Variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return next Variable to be assigned according to the Degree Heuristic '''
    # IMPLEMENT
    unassigned_vars = csp.get_all_unasgn_vars() #get all unassigned variables 
    if len(unassigned_vars) == 0: #no unassigned variables
        return None
    max_degree = -1 #initialize max constraint number 
    max_var = None #initialize variable with max degree
    for var in unassigned_vars:
        degree = 0 #count 
        for cons in csp.get_cons_with_var(var): #get constraints with variable
            if len(cons.get_unasgn_vars()) > 1:
                degree += 1
        if degree > max_degree:
            max_degree = degree #update max degree
            max_var = var
    return max_var #return variable with highest degree
        
           

    pass

def ord_mrv(csp):
    ''' return Variable to be assigned according to the Minimum Remaining Values heuristic '''
    # IMPLEMENT
    unassigned_vars = csp.get_all_unasgn_vars() #get all unassigned variables
    if len(unassigned_vars) == 0:
        return None
    min_var = None #initialize variable with minimum domain size
    min_domain_size = float('inf') #initialize the domain size to infinity
    for var in unassigned_vars:
        if var.cur_domain_size() < min_domain_size:
            min_var = var
            min_domain_size = var.cur_domain_size()         
    return min_var
    pass

from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE
import time

# Variables and their domains (possible values)
variables = ['A', 'B', 'C', 'D', 'E']
domains = {
    'A': [('international', 1), ('international', 2)],
    'B': [('international', 1)],
    'C': [('international', 2), ('international', 3), ('international', 4)],
    'D': [('international', 3), ('international', 4)],
    'E': [('domestic', 1), ('domestic', 2), ('domestic', 3), ('domestic', 4)]
}

# Constraints

# No two planes can land on the same runway at the same time
def constraint_no_overlap(variables, assignments):
    var1, var2 = variables
    if var1 in assignments and var2 in assignments:
        runway1, time1 = assignments[var1]
        runway2, time2 = assignments[var2]
        # If the runways and times are the same, the constraint is violated
        return not (runway1 == runway2 and time1 == time2)
    return True  # If we can't evaluate, there's no problem

# Plane D must land before plane C
def constraint_d_before_c(variables, assignments):
    var_c, var_d = variables
    if var_c in assignments and var_d in assignments:
        _, time_c = assignments[var_c]
        _, time_d = assignments[var_d]
        return time_d < time_c  # D's time must be less than C's time
    return True

# Plane B must land at time 1
def constraint_b_time(variables, assignments):
    var_b = variables[0]
    if var_b in assignments:
        _, time_b = assignments[var_b]
        return time_b == 1
    return True

# Plane D cannot land before time 3
def constraint_d_time(variables, assignments):
    var_d = variables[0]
    if var_d in assignments:
        _, time_d = assignments[var_d]
        return time_d >= 3
    return True

# Plane A must operate before time 2
def constraint_a_time(variables, assignments):
    var_a = variables[0]
    if var_a in assignments:
        _, time_a = assignments[var_a]
        return time_a <= 2
    return True

# Plane E can only land on the domestic runway
def constraint_e_runway(variables, assignments):
    var_e = variables[0]
    if var_e in assignments:
        runway_e, _ = assignments[var_e]
        return runway_e == 'domestic'
    return True

constraints = [
    # No two planes can land on the same runway at the same time
    (('A', 'B'), constraint_no_overlap),
    # ... (other constraints)
]

# Define the CSP problem
problem = CspProblem(variables, domains, constraints)

# Solve the CSP using backtracking with the most constrained variable heuristic
start_time = time.time()
solution = backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
end_time = time.time()
print(f"Backtracking search time: {end_time - start_time} seconds")
print("Solution:")
for var in variables:
    print(f"{var}: Runway - {solution[var][0]}, Time - {solution[var][1]}")
from simpleai.search import CspProblem, backtrack

# Variables (airplanes)
variables = ['A', 'B', 'C', 'D', 'E']

# Domains (runway, time slot)
domains = {
    'A': [('international', 1), ('international', 2)],
    'B': [('international', 1)],  # B must land in the first time slot
    'C': [('international', 2), ('international', 3), ('international', 4)],
    'D': [('international', 3), ('international', 4)],  # D cannot land before the 3rd time slot
    'E': [('domestic', 1), ('domestic', 2), ('domestic', 3), ('domestic', 4)]  # E can only use the domestic runway
}

# Constraints (problem requirements)
def different_time_and_runway(variables, assignments):
    # Two planes cannot land on the same runway at the same time
    if variables[0] in assignments and variables[1] in assignments:
        return assignments[variables[0]] != assignments[variables[1]]
    return True

def d_before_c(variables, assignments):
    # D must land before C
    if 'D' in assignments and 'C' in assignments:
        return assignments['D'][1] < assignments['C'][1]
    return True

# Define constraints
constraints = [
    # Runway and time slot constraints (two planes cannot land on the same runway at the same time)
    (('A', 'B'), different_time_and_runway),
    # ... (other constraints)
]

# Create the CSP problem
problem = CspProblem(variables, domains, constraints)

# Find the solution using backtracking algorithm
solution = backtrack(problem)

# Print the solution
print("Airplane scheduling solution:", solution)
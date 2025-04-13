from simpleai.search import CspProblem, backtrack

# Variables (regions)
variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Domains (colors)
domains = {
    'a': ['Red', 'Green', 'Blue'],
    'b': ['Red', 'Green', 'Blue'],
    'c': ['Red', 'Green', 'Blue'],
    'd': ['Red', 'Green', 'Blue'],
    'e': ['Red', 'Green', 'Blue'],
    'f': ['Red', 'Green', 'Blue'],
    'g': ['Red', 'Green', 'Blue'],
}

# Constraints (adjacent regions must have different colors)
def different_colors(variables, assignments):
    if variables[0] in assignments and variables[1] in assignments:
        return assignments[variables[0]] != assignments[variables[1]]
    return True

constraints = [
    (('a', 'g'), different_colors),
    (('a', 'd'), different_colors),
    # ... other constraints
]

# Create the CSP problem
problem = CspProblem(variables, domains, constraints)

# Find the solution using backtracking
solution = backtrack(problem)
print("Map coloring solution:", solution)
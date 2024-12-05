#part2
import math

def check(sarr):
    """Checks if a sequence is valid based on the given conditions."""
    flag_increasing = True
    flag_decreasing = True
    flag_constraints = True

    for j in range(1, len(sarr)):
        diff = math.fabs(sarr[j] - sarr[j - 1])
        if diff < 1 or diff > 3:  # Check difference constraint
            flag_constraints = False
        if sarr[j] < sarr[j - 1]:  # Check monotonic increasing
            flag_increasing = False
        if sarr[j] > sarr[j - 1]:  # Check monotonic decreasing
            flag_decreasing = False

    # Sequence is valid if it satisfies monotonicity and difference constraints
    return (flag_increasing or flag_decreasing) and flag_constraints

def check_with_one_removal(sarr):
    """Checks if the sequence becomes valid after removing one element."""
    for i in range(len(sarr)):
        # Create a new list excluding the current element
        temp_arr = sarr[:i] + sarr[i + 1:]
        if check(temp_arr):
            return True
    return False

count = 0

while True:
    s = input()
    if not s:  # Exit on empty input
        break

    # Convert input string to a list of integers
    sarr = list(map(int, s.split()))
    
    if check(sarr):  # Check if the sequence is already valid
        count += 1
    elif check_with_one_removal(sarr):  # Check if valid after removing one element
        count += 1

print(count)

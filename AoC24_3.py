#part2
import re

def calculate_sum_with_conditions(memory):
    total_sum = 0
    enabled = True  # At the start, `mul` instructions are enabled

    # Process the input string segment by segment
    while memory:
        # Find the positions of the next `do()` and `don't()` instructions
        index_do = memory.find("do()")
        index_dont = memory.find("don't()")

        if index_do != -1 and (index_dont == -1 or index_do < index_dont):
            # Process up to `do()`
            segment = memory[:index_do]
            memory = memory[index_do + len("do()"):]  # Move past the `do()`
            enabled = True  # Enable future `mul()` instructions
        elif index_dont != -1 and (index_do == -1 or index_dont < index_do):
            # Process up to `don't()`
            segment = memory[:index_dont]
            memory = memory[index_dont + len("don't()"):]  # Move past the `don't()`
            enabled = False  # Disable future `mul()` instructions
        else:
            # No more `do()` or `don't()`, process the remaining string
            segment = memory
            memory = ""

        # Extract and evaluate valid `mul()` instructions only if enabled
        if enabled:
            pattern_mul = r"mul\(\d{1,3},\d{1,3}\)"
            matches_mul = re.findall(pattern_mul, segment)

            for mul in matches_mul:
                # Extract the numbers inside the `mul(x, y)` instruction
                numbers = re.search(r"\d{1,3},\d{1,3}", mul).group()
                x, y = map(int, numbers.split(","))
                total_sum += x * y  # Add the product to the total sum

    return total_sum

# Example input
corrupted_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
result = calculate_sum_with_conditions(corrupted_memory)
print(result)

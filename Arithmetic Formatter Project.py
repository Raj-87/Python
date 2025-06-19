def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            # This case handles problems like "32+698" (missing spaces) or "32 + 698 +" (too many parts)
            # which wouldn't be caught by other checks later.
            return "Error: Invalid problem format." 

        first_num, operator, second_num = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(first_num)
        operators.append(operator)
        second_operands.append(second_num)

    # Now, format the lines for output
    arranged_lines = {
        'top': [],
        'bottom': [],
        'dashes': [],
        'answers': []
    }

    for i in range(len(problems)):
        first_num = first_operands[i]
        operator = operators[i]
        second_num = second_operands[i]

        # Determine the width needed for alignment for the current problem
        # It's the length of the longest operand + 2 (for operator and space)
        width = max(len(first_num), len(second_num)) + 2 

        # Top line: right-aligned first operand
        arranged_lines['top'].append(first_num.rjust(width))

        # Bottom line: operator followed by right-aligned second operand
        # The second operand needs to be right-aligned within (width - 1) characters
        # because the operator takes up one character at the start.
        arranged_lines['bottom'].append(operator + second_num.rjust(width - 1))

        # Dashes line: 'width' number of dashes
        arranged_lines['dashes'].append('-' * width)

        # Calculate and format answer if required
        if show_answers:
            if operator == '+':
                result = int(first_num) + int(second_num)
            else:
                result = int(first_num) - int(second_num)
            arranged_lines['answers'].append(str(result).rjust(width))

    # Join the lines with 4 spaces between each problem
    # The final output string is built by joining the respective lines.
    output_string = ""
    output_string += "    ".join(arranged_lines['top']) + "\n"
    output_string += "    ".join(arranged_lines['bottom']) + "\n"
    output_string += "    ".join(arranged_lines['dashes'])

    if show_answers:
        output_string += "\n" + "    ".join(arranged_lines['answers'])

    return output_string

# Example Usage:
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
print(f'\n{arithmetic_arranger(["32 * 8"])}') # Example of an error
print(f'\n{arithmetic_arranger(["10000 + 1"])}') # Example of an error
print(f'\n{arithmetic_arranger(["1 + 2", "3 + 4", "5 + 6", "7 + 8", "9 + 10", "11 + 12"])}') # Too many problems
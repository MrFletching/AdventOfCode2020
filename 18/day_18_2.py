#!/usr/bin/env python3

def main():
    total = 0

    with open('input.txt') as f:
        for line in f:
            expression = parse_expression(list(line))
            result = evaluate_expression(expression)
            total += result
    
    print(f'Total: {total}')

def parse_expression(expression_chars):
    expression = []

    is_value = False
    value = ''

    while len(expression_chars) != 0:
        char = expression_chars.pop(0)

        if char >= '0' and char <= '9':
            is_value = True
            value += char
        else:
            if is_value:
                is_value = False
                expression.append(int(value))
                value = ''

        if char == '*':
            expression.append('*')
        elif char == '+':
            expression.append('+')
        elif char == '(':
            expression.append(parse_expression(expression_chars))
        elif char == ')':
            break
    
    if is_value:
        expression.append(int(value))
    
    return expression


def evaluate_expression(expression):

    try:
        add_index = expression.index('+')
        term_from = add_index - 1
        term_to = add_index + 1
    except ValueError:
        term_from = 0
        term_to = 2

    term = expression[term_from:term_to+1]
    left_operand = term[0]
    operation = term[1]
    right_operand = term[2]

    expression = expression[:term_from] + expression[term_to+1:]

    if type(left_operand) is list:
        left_operand = evaluate_expression(left_operand)
    
    if type(right_operand) is list:
        right_operand = evaluate_expression(right_operand)

    if operation == '*':
        result = left_operand * right_operand
    elif operation == '+':
        result = left_operand + right_operand
    else:
        raise ValueError('Invalid expression')

    expression.insert(term_from,result)
    
    if len(expression) == 1:
        return result
    
    return evaluate_expression(expression)


if __name__ == '__main__':
    main()

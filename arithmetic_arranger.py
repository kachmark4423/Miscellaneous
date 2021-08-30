def arithmetic_arranger(problems, show_answer = False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        num1, operation, num2 = problem.split()
        if operation not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if operation == '+':
            answer = int(num1) + int(num2)
        else:
            answer = int(num1) - int(num2)
            
        max_length = max(len(num1), len(num2))
        
        if problem != problems[-1]: 
            line1 += f'{num1:>{max_length+2}}    '
            line2 += f'{operation} {num2:>{max_length}}    '
            line3 += '-' * (max_length + 2) + '    '
            line4 += f'{answer:>{max_length+2}}    '
        else:
            line1 += f'{num1:>{max_length+2}}'
            line2 += f'{operation} {num2:>{max_length}}'
            line3 += '-' * (max_length + 2) + '    '
            line4 += f'{answer:>{max_length+2}}'           
    line1 += '\n'
    line2 += '\n'
    
    if not show_answer:
        return line1 + line2 + line3
    else:
        line3 += '\n'
        return line1 + line2 + line3 + line4
        
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
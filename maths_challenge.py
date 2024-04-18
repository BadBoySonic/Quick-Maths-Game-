import random

OPERATORS = ["+","-","*"]
MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10
def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " "+ str(right)
    answer = eval(expr)
    print(expr,)
    return expr, answer


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
      
    
    

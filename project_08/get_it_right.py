import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTION = 5


def genrate_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr =  f"{left} {operator} {right}"
    answer = eval(expr)

    return expr, answer

wrong = 0 
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_QUESTION):
    expr, answer = genrate_question()
    while True:
        user_answer = input(f"Problem #{i+1}: {expr} = ")
        if user_answer == str(answer):
            break
        
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print(f"You have done 10 questions in {total_time:.1f}")
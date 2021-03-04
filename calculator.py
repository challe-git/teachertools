def calculate(oper, n1, n2):
  if oper == "+": summary = n1 + n2
  if oper == "-": summary = n1 - n2
  if oper == "*": summary = n1 * n2
  if oper == "/": summary = n1 / n2
 
calculate(char(input("pick a operator ( + , - , * , / )\n")), float(input("pick a number:\n")), float(input("pick a number:\n")))
print(f"summary = {calculate.summary}")


1
# def show_arguments(func):

#     def inner(*args, **kwargs):
#         print("Arguments: ", end="")
#         for i in args:

#             print(i, end=" ")
#         print("")
#         return func(*args)

#     return inner

# @show_arguments
# def multiply(a,b):
#     return a*b


# print(multiply(4,5))

2
# def frame(func):

#     def inner(*args, **kwargs):
#         return f"{"="*10}\n{func(*args)}\n{"="*10}"
#     return inner

# @frame
# def show(txt):

#     return txt

# print(show("python"))


3
# def double_result(func):

#     def inner(*args, **kwargs):
#         return func(*args)*2
#     return inner

# @double_result
# def get_n(number):
#     return number


# print(get_n(10))

4
# multiply = lambda a,b : a*b

# print(multiply(6,7))

5
# def count_calls(func):
#     cnt = 0
#     def inner(*args, **kwargs):
#         nonlocal cnt
#         cnt += 1
#         print(f"Call: {cnt}")
#         return func(*args)
#     return inner


# @count_calls
# def hello():
#     return "Hello"

# print(hello())
# print(hello())
# print(hello())

6
# def string_only(func):

#     def inner(*args, **kwargs):
#         res = func(*args)
#         if res == int(res):
#             return "A string is required"
#         return func(*args)
#     return inner

# @string_only
# def show(value):
#     return value

# print(show("100"))


7
# def adult_only(func):

#     def inner(*args, **kwargs):
#         if args[0] >= 18:
#             return func(*args)
#         return "Access denied"
#     return inner

# @adult_only
# def enter_club(age):
#     return "Welcome"


# print(enter_club(20))



8
# lict = [('Ali', 75), ('Sara', 92), ('Bob', 84)]
# sorted_students = sorted(lict, key=lambda s: s[1], reverse=True)
# print(sorted_students)


9
# def add_prefix(func):

#     def inner(*args, **kwargs):
#         return f"Result: {func(*args)}"
#     return inner


# @add_prefix
# def get_name(name):
#     return name

# print(get_name("Ali"))


10
# def check_division(func):

#     def inner(*args, **kwargs):
#         if args[1] == 0:
#             return "Cannot divide by zero"
#         return func(*args)
#     return inner


# @check_division
# def divide(a,b):
#     return a/b

# print(divide(10, 4))


11
# numbers = list(map(int, input().split()))

# result = filter(lambda x: x>0, numbers)

# print(list(result))



12
# add = lambda a,b : a+b
# subs = lambda a,b : a-b
# divide = lambda a,b: a/b
# multiply = lambda a,b: a*b

# operations = {
#     "add": add,
#     "multiple": multiply,
#     "subs": subs,
#     "divide": divide
# }

# def show_start(func):

#     def inner(*args, **kwargs):
#         print("Calculating...")
#         return func(*args)
#     return inner


# @show_start
# def calculate(a,b, op):
#     match op:
#         case "+":
#             return operations["add"](a,b)
#         case "-":
#             return operations["subs"](a,b)
#         case "*":
#             return operations["multiple"](a,b)
#         case "/":
#             try:
#                 return operations["divide"](a,b)
#             except ZeroDivisionError:
#                 return "Cannot divide by zero."
#         case _:
#             return "Unknown operation"

# while True:

#     a = input("Enter number 1: ")
#     b =  input("Enter number 2: ")
#     if a == "exit" or b == "exit":
#         break

#     if a.isdigit() and b.isdigit():
#         b = int(b)
#         a = int(a)
#     else:
#         print("Enter only numbers or 'exit' ")
#         continue
#     op = input("Enter operation: ")
#     if op == "exit":
#         break
#     print(calculate(a,b,op))
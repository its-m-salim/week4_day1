
1
# def add_welcome(func):

#     def inner(*args, **kwargs):
#         return f"Welcome! \n{args[0]}"

#     return inner


# @add_welcome
# def greet(name):
#     return name


# print(greet("Ali"))



2
# def goodbye(func):

#     def inner(*args, **kwargs):
#         return f"{args[0]} \nGoodbye!"
#     return inner

# @goodbye
# def show_city(city):
#     return city


# print(show_city("Dushanbe"))


3
# def repeat_three_times(func):
#     def inner(*args, **kwargs):
#         return f"{func()}\n" * 3

#     return inner


# @repeat_three_times
# def hello():
#     return "Hello"


# print(hello())


4
# def func_name(func):

#     def inner(*args, **kwargs):
#         return f"Function: add \n{func(*args)}"

#     return inner

# @func_name
# def add(a,b):
#     return a+b



# print(add(2,3))


5
# def uppercase_result(func):

#     def inner(*args, **kwargs):
#         return func(*args).upper()
#     return inner


# @uppercase_result
# def get_name(name):
#     return name


# print(get_name("Ali"))


6
# def positive_number(func):

#     def inner(*args, **kwargs):
#         if args[0] > 0:
#             return func(*args)
#         return "The number must be positive"
#     return inner


# @positive_number
# def square(number):
#     return number**2


# print(square(5))


7
# add = lambda a,b: a+b

# print(add(7,5))


8
# square = lambda a: a**2
# print(square(6))



9
# even = lambda a:  [i for i in a if i%2 ==0]


# print(even([1, 2, 3, 4, 5, 6]))



10
# srtd = [('Ali', 22), ('Sara', 19), ('Bob', 25)]
# sorted_students = sorted(srtd, key=lambda s: s[1])
# print(sorted_students)
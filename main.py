# is_login = True


# def check_login(func):
#     def inner(name):
#         if is_login:
#             # name = name.capitalize()
#             # res = func(name.capitalize())
#             res = func(name)

#             return res.title()
#         else:
#             return "Please login"
#     return inner



# @check_login
# def hello(name):
#     return f"hello {name}"


# print(hello("akbar"))



generator = lambda start, end: [i for i in range(start, end+1) if i%2 == 0]

print(generator(1, 7080))
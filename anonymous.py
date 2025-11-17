def is_ashari(x):
    return not(x == int(x))

a = [1, 2.3 , 34.3, 34, 667, 34.5]


print(list(filter(lambda x: not(x == int(x)), a)))
# i use a anonymous function (lambda) , and filter 
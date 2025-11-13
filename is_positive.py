def is_positivi(number):
    if number >= 0 :
        return True
    else :
        return  False
res = int(input("give me a number"))
print(is_positivi(res))


def is_positivi2(num):
    return num >= 0

res2 = int(input('give me number'))
print(is_positivi2(res2))
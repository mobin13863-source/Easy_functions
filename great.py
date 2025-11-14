a = int(input('give me a number'))
b = int(input('give me seconed number'))


def is_greater(a, b):
    '''this function gives a two number and if first number is biger 
    than seconed number return (True)
    '''
    
    if a > b :
        return True
    if a <= b :
        return False
    
print(is_greater(a, b))

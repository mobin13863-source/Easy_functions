def say_hello(name):
    '''
    this functions say hello to the name,/n
    to the lengh of the name,/n
    and print enumrete of name
    '''
    for i in range(len(name)):
        print(f"hello {name}")
        print(i, name[i], end="\n" )
        
say_hello("mobin")






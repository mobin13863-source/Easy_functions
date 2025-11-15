def pick_even(*args):
    res = []
    
    for i in args:
        if i % 2 == 0 :
            res.append(i)
        
            
    return res
   
            
print(pick_even())
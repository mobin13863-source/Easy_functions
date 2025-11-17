name = ["jadi", "mobin", "hasan", "farank", "sn"]

res = []
def bozorh(x):
    for i in x:
        if len(i) > 4:
            res.append(i)
    return res
        
    

print(bozorh(name))


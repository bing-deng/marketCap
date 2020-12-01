def soulution(A):
    rdict = {}
    rlist = []
    for i in A:
       c = A.count(i)
       rdict[i] = c
       rlist.append(c)
    print(rdict)
    
    rlist = list(set(rlist))
    rlist.sort()

    if len(rdict.keys()) == 2 :
        return len(A)
    elif len(rdict.keys()) == 1:
        print("-+-")
        return 2
    elif list(rdict.values()).count(2) == 2:
        c = 0
        for k, v in rdict.items():
            # print(k, v)
            if v == 2:
                c += A.count(k)
        return c

    else:
        print("--",rlist[0],rlist[1])
        r = rlist[0]+rlist[1]
        return r

a = [0,5,4,4,5,12]
a = [1,2,3,2]
# a = [4, 4]
# a = [4,2,2,4,2]
r = soulution(a)
print(r)




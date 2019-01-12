def trim(s):
    n = len(s) - 1
    start = 0
    end = 0
    if n == 0 :
        print('')
        return ''
    else: 
        for i in range(n):
            if s[i] != ' ':
                start = i
                break
        for j in range(n,-1,-1):
            if s[j] != ' ':
                end = j+1
                break
        print(s[start:end])
        return s[start:end]


    

#s = '  abc'
#(trim(s))
#s = 'efg  '
#print(trim(s) == 'efg')
s = '  abc efg  '
print(trim(s) == 'abc efg')

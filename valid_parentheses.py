def isValid(s):
        
    for i in s:
        if '()' in s:
            s= s.replace( '()','')
        elif '{}' in s :
            s = s.replace( '[]', '')
        elif '[]' in s :
            s = s.replace ( '{}', '')
            break
        else :
            return not s
s ='({[]})'
print(isValid(s))

    
    
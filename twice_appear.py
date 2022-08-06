#Given a string s consisting of lowercase English letters, return the first letter to appear twice.

def repeatedCharacter(s):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
                d[i] += 1
            if d[i] == 2:
                return i
            else:
               d[i] += 1

print(repeatedCharacter("alla"))
print(repeatedCharacter("restroom"))


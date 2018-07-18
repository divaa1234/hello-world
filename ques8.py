s = 'azcbobobegghakl'
max=0
c=s[0]
l=s[0]
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        c=c+s[i + 1]
        if len(c) > max:
            max = len(c)
            l = c
    else:
        c=s[i + 1]
        i=i+1
print ('Longest substring in alphabetical order is: ' + l)



      
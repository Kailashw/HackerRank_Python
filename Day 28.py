

import sys


N = int(input().strip())
names = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if (emailID.endswith('@gmail.com')):
        names.append(firstName)
        
for elem in sorted(names):
    print(elem)


# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(input().strip())

for i in range(0, n):
    S = input()
    even, odd = S[::2], S[1::2]
    print(even + " " + odd)


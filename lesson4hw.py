n = int(input("Please Enter A Number"))
a = n
num = str(n)
digits = len(num)
s=0
while a>0:
    d = a%10
    s = s + pow(d,digits)
    a = a//10
if (s==n):
    print("It is An Armstrong Number")
else:
    print("It is not An Armstrong Number")

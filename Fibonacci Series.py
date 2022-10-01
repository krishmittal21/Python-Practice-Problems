#Fibonacci series
N=int(input("Enter number of terms: "))
count=0
a=0
b=1
print(a,b,sep="/n")
while count<N-2:
    c=a+b
    print(c)
    a,b=b,c
    count+=1

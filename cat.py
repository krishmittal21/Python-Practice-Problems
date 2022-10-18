def main():
    n=times()
    meow(n)
def times():
    while True:
        n=int(input("Enter no: "))
        if n>0:
            return n
def meow(j):
    for i in range(j):
        print("meow")
main()
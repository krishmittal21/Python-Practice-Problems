#whether x is positive using functions
def main():
    x=int(input("What's x? "))
    if is_even(x):
        print("x is an even number ")
    else:
        print("x is not even")
def is_even(number1):
    return number1%2==0   
main()
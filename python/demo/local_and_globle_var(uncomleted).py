x=4
print(x)


def hello():
    x=5
    print(f"The local x is {x}")
    print("Hello Ak")

    print(f"The globle x is {x}")
    hello()
    print(f"the globle x is {x}")
hello()
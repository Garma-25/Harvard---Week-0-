#E=MC2
def main():
    M = int(input("M="))
    E = (M * square(300000000))

    print("E = "f"{E:,}")

def square(n):
    return n * n

main()

def convert(space):
    return space.replace(" ", "...")

def main():
    userinput = input(" ")
    print(convert(userinput))

if __name__ == "__main__":
    main()

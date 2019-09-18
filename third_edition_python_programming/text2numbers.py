#A program to convert a textual message into a sequence of numbers
# utilizing the underlying Unicode encoding


def main():
    message = str(input("Please enter the message to encode: "))

    for ch in message:
        print(ord(ch), end=" ")

    print()

main()


#A program to convert sequence of  Unicode numbers into a strings of text.

def main():
    unicode_msg = input("Please enter the unicode-encoded message\t")

    text_msg = ""

    for i in unicode_msg.split():
        codeNum = int(i)
        text_msg = text_msg + chr(codeNum)

    print(f"The Unicode-encoded message is : {text_msg}")


main()


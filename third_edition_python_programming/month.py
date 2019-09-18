#A program to print the abbreviation of a month, given its number.

def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a moth number (1-12)\t"))

    pos = (n - 1) * 3

    monthAbbrev = months[pos:pos+3]

    print(f"The month abbreviation is {monthAbbrev}")

main()
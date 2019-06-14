import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)


#  utf_string.encode()     to bytes
#  raw_bytes.decode()      decoding bytes to utf signs
#  error = strict -> the default error handler is 'strict' meaning that encoding errors raise ValueError

#raw_bytes = b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b' ----> in hexadecimal
# raw_bytes.decode() = **         ----> we may encode it (**) to this b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b'

#ASCII American Standart Code for Information Interchange


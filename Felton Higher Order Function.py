'''___Author___: David Kent Felton II
___Purpose___: To demonstrate the use of a higher order function'''


def shout(text):
    return text.upper()


enter = input("Capitalize these words: ")

if enter.isupper():
    print('You fool. The text is already capitalized.')
else:
    print(shout(enter))

yell = shout

enter2 = input("Capitalize these words too: ")

if enter2.isupper():
    print('You fool. The text is already capitalized.')
else:
    print(yell(enter2))

input()

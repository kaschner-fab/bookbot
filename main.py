def split_book(book):
    splited_book = book.split()
    return len(splited_book)

def letters (book):
    letter = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for char in book.lower():
        for let in letter:
            if char == let :
                letter[let] += 1

    return letter



with open ("books/frankenstein.txt") as f:
    file_content = f.read()


print (f"{split_book(file_content)} words found in document")
letter_list = []
for key, value in letters(file_content).items() :
    letter_list.append([key, value])

letter_list.sort(key = lambda x: x[1], reverse= True)

for letter in letter_list:
    print(f"The '{letter[0]}' character was found {letter[1]} times")

print("--- End report ---")
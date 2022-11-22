""" Write a program that can read PrideAndPrejudice.txt book in the books folder and analyse the
file as follows:
1.  How many positive integer numbers and how many negative integer numbers are in this book?
2.  How many float numbers are in this book?
3.  How many non-integer and non-float words are in this book?
4.  How many lines does this book have?
5.  How many words in total does this book contain?
6.  How many blank line does this book contain?

Write a program that can read the above book and extract the lines with more
than 10 words and write those lines into another file called PrideAndPrejudiceHighlights.txt."""

pos_int_amount = 0
neg_int_amount = 0
float_amount = 0
str_words_amount = 0
total_words = 0
total_lines = 0
total_blank_lines = 0

try:
    book = open("lab02/books/PrideAndPrejudice.txt", "r", encoding="utf-8")
    new_book = open("lab02/books/PrideAndPrejudiceHighlights.txt", "w", encoding="utf-8")

    line = book.readline()
    while line != "":
        words = line.split()
        total_lines += 1

        # blank lines
        if line == "\n":
            total_blank_lines += 1

        for word in words:
            total_words += 1
            try:
                # integers
                new_int = int(word)
                # positive ints
                if new_int > 0:
                    pos_int_amount += 1
                # negative ints
                if new_int < 0:
                    neg_int_amount += 1
            except ValueError as err:
                try:
                    # floats
                    new_float = float(word)
                    float_amount += 1
                except ValueError:
                    # strings
                    str_words_amount += 1
        
        # write into file
        if len(words) > 10:
            new_book.write(line)
        
        # next line
        line = book.readline()

    new_book.close()
    book.close()
except IOError as err:
    print(err)

print("Positive integers:", pos_int_amount)
print("Negative integers:", neg_int_amount)
print("Floats:", float_amount)
print("Strings:", str_words_amount)
print("Words:", total_words)
print("Lines:", total_lines)
print("Blank lines:", total_blank_lines)

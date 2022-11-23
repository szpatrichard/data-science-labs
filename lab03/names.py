"""Use an appropriate data structure and ask end-user to repeatedly enter some names. You need to
ensure that the items in that data structure can not be altered or updated later on."""

if __name__ == "__main__":
    my_list = list()
    for i in range(3):
        term = input('input a word')
        my_list.append(term)

    my_tuple = tuple(my_list)

    print(my_tuple)

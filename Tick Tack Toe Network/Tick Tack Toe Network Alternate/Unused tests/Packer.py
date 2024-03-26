index = ("N", "N", "N", "X", "X", "X", "O", "O", "O")


def pack(index):


    string = ""
    for i in index:
        string = string + str(i) + "@"

    return string


def unpack(string, length=9):

    current_item = ""
    current_number = 0

    listus = [""]*length

    for character in string:
        if character!="@":
            current_item = current_item + character
        elif character == "@":
            listus[current_number] = current_item
            current_number+=1
            current_item = ""


    return tuple(listus)

print(unpack(pack(index)))




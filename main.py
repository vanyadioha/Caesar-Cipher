from abcd import alphabet_list

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(dir, text, shft):
    end_text = ""
    if shft > 25:
        shft %= 26
    for letter in text:
        if letter not in alphabet_list:
            end_text += letter
        else:
            index = alphabet_list.index(letter)
            if dir.lower() == "encode":
                index += shft
            elif dir.lower() == "decode":
                index -= shft
            else:
                print("Something went wrong")
            new_letter = alphabet_list[index]
            end_text += new_letter
    print(end_text)


caesar(direction, message, shift)

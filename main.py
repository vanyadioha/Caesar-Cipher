from abcd import alphabet_list


def caesar(dir, text, shft):
    end_text = ""
    if shft > 25:
        shft %= 26
    for char in text:
        if char not in alphabet_list:
            end_text += char
        else:
            index = alphabet_list.index(char)
            if dir.lower() == "encode":
                index += shft
            elif dir.lower() == "decode":
                index -= shft
            else:
                print("Something went wrong")
            new_letter = alphabet_list[index]
            end_text += new_letter
    print(end_text)


run_again = True

while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, message, shift)
    ask = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
    if ask.lower() == "no":
        run_again = False
        print("Goodbye")

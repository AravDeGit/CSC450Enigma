#   First we need to get todays date
#   Second we nee to get the alphbet as a list
#   based on that list of 26 characters we will then rotate all text based on a
#   five d
#
char_set = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z", " "]

char_map = {char: i for i, char in enumerate(char_set)}


def crack_engigma(Message,date):


    date_squared=int(date)**2 # squares the date
    offset=str(date_squared)[-4:] #grabs last four digits we need to get a b c d offset
    aoffset = int(offset[0])
    boffset = int(offset[1])
    coffset = int(offset[2])
    doffset = int(offset[3])


    decrypted_ending = " end"  # the end message we know
    encrypted_ending = Message[-4:] # determines what the encrypted version of the last four charactera are
    keys= [] # empty list that will later store keys by using the bottom for loop
    decrypted_message = []# stores the decrypted message

    for i, enc_char in enumerate(encrypted_ending):
        shift_idx = i % 4 # determines what shift we use
        enc_pos = char_map[enc_char] # Detemines what character postion the encrpyted key is at
        dec_pos = char_map[decrypted_ending[i]] # determines what character posotion the decrpyted char is at
        total_shift = (enc_pos - dec_pos) % 27 # macthes the enc key to decpyted key to determine the total shift applied
        key = (total_shift - [aoffset, boffset, coffset, doffset][shift_idx]) % 27 # subtracts offset
        keys.append(key) # adds the new key to the list

    for i, enc_char in enumerate(Message):# using info from above determines what the message was
        shift_idx = i % 4 # detemines shift
        total_shift = (keys[shift_idx] + [aoffset, boffset, coffset, doffset][shift_idx]) % 27
        enc_pos = char_map[enc_char]
        dec_pos = (enc_pos - total_shift) % 27
        decrypted_message.append(char_set[dec_pos])



    return "".join(decrypted_message)



def main():
    encrypted_message = "keder ohulw tnw"
    date = "040895"
    decrypted_message =crack_engigma(encrypted_message, date)
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
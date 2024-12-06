import string

class EnigmaCipher:
    def __init__(self, key, date):
        self.char_set = list(string.ascii_lowercase) + [" "]
        self.char_map = {char: i for i, char in enumerate(self.char_set)}
        self.key = key
        self.date = date
        self.offsets = self.calculate_offsets()

    def calculate_offsets(self):
        date_squared = int(self.date) ** 2
        offset_digits = str(date_squared)[-len(self.char_set):]
        return [int(d) for d in offset_digits]

    def encrypt(self, plaintext):
        plaintext = plaintext.lower()
        encrypted_message = []

        for i, char in enumerate(plaintext):
            if char not in self.char_map:
                encrypted_message.append(char)
                continue

            shift_idx = i % len(self.offsets)
            total_shift = (self.key + self.offsets[shift_idx]) % len(self.char_set)
            char_pos = self.char_map[char]
            enc_pos = (char_pos + total_shift) % len(self.char_set)
            encrypted_message.append(self.char_set[enc_pos])

        return "".join(encrypted_message)

def main():
    date = "12032024"
    key = 7
    plaintext = "hello world"

    enigma = EnigmaCipher(key=key, date=date)
    encrypted_message = enigma.encrypt(plaintext)
    print(f"Encrypted Message: {encrypted_message}")

if __name__ == "__main__":
    main()
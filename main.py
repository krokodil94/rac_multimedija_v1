import sys
# preberemo datoteko, in jo pretvorimo v bitni niz
def get_bits(filepath):
    with open(filepath, 'rb') as f:
        file = f.read()
        return ''.join(format(byte, '08b') for byte in file)


# najdemo iskano sekvenco bitov v bitnem nizu

def find_sequence(bits, sequence):
    position = []
    pos = bits.find(sequence)
    while pos != -1:
        position.append(pos)
        pos = bits.find(sequence, pos + len(sequence))
    return position


# zamenjamo iskano sekvenco bitov z novo sekvenco bitov

def replace_sequence(bits, sequence, new_sequence):
    modified_bits = bits.replace(sequence, new_sequence)
    # dodamo ničle na koncu, zato da je dolžina bitnega niza deljiva s 8
    while len(modified_bits) % 8 != 0:
        modified_bits += '0'

    return modified_bits


def bits_to_file(filepath, bits):
    with open(filepath, 'wb') as f:
        for i in range(0, len(bits), 8):
            byte = int(bits[i:i + 8],2)
            f.write(byte.to_bytes(1, byteorder='big'))

def main():
    file = sys.argv[1]
    operation = sys.argv[2]
    if operation == "f":
        sequence = sys.argv[3]
        position = find_sequence(get_bits(file), sequence)
        if position:
            print(" ".join(map(str, position)))
        else:
            print("Sequence not found!")

    elif operation == "fr":
        sequence = sys.argv[3]
        new_sequence = sys.argv[4]
        bits = get_bits(file)
        new_bits = replace_sequence(bits, sequence, new_sequence)
        bits_to_file(file, new_bits)

if __name__ == "__main__":
    main()

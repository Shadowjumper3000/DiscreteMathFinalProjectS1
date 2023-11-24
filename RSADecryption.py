
def split_string(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def main():
    # Create Alphabet Library
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    library = {}
    for i, letter in enumerate(alphabet):
        library[i] = letter

    # Get Private Key
    PrivateKeyN = int(input("Enter n: "))
    PrivateKeyD = int(input("Enter d: "))

    # Calculate the block size
    k = 0
    l = str(len(library))
    while int(l) <= PrivateKeyN:
        l += str(len(library))
        k += 2
        if int(l) > PrivateKeyN:
            break

    # Get encoded message as list of ints
    encodedMessage = [str(i) for i in input("Enter encoded message: ").split()]
    if len(encodedMessage[0]) > k:
        encodedMessage = [int(encodedMessage[0][i:i+k]) for i in range(0, len(encodedMessage[0]), k)]

    decodedMessage = ""
    for i in encodedMessage:
        # Decrypt the block and convert it to a string
        print("encoded Message: " + str(i))
        decryptedBlock = str(pow(int(i), PrivateKeyD, PrivateKeyN))

        # Split the decrypted block into pairs of two characters
        pairs = split_string(str(decryptedBlock).zfill(k), 2)

        # Convert each pair to its corresponding letter using the alphabet library
        for pair in pairs:
            print("alphabet: " + str(pair))
            if pair != str(len(alphabet)+1):
                decodedMessage += library[int(pair)]
            
    print(decodedMessage)

main()
def split_string(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def main():
    # Create Alphabet Library
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    library = {}
    for i, letter in enumerate(alphabet):
        library[str(i).zfill(2)] = letter

    # Get Private Key
    PrivateKeyN = int(input("Enter n: "))
    PrivateKeyD = int(input("Enter d: "))

    # Calculate the block size
    k = 0
    l = str(len(library))
    while int(l) <= PrivateKeyN:
        l += str(len(library))
        k += 1
        if int(l) > PrivateKeyN:
            break

    # Get encoded message as a list of ints
    encodedMessage = input("Enter encoded message: ").strip("[]").split(", ")
    
    decodedMessage = ""
    for i in encodedMessage:
        try:
            decryptedBlock = str(pow(int(i), PrivateKeyD, PrivateKeyN))
        except ValueError:
            continue

        if len(decryptedBlock) < k:
            decryptedBlock = decryptedBlock.zfill(k)

        pairs = split_string(decryptedBlock, 2)

        for pair in pairs:
            if pair != str(len(alphabet)+1):
                decodedMessage += library[pair]
            
    print(decodedMessage)

main()

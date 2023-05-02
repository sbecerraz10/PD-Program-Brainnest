'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
def caesar_cipher(message, shift, mode):
    # Convert the message to uppercase
    message = message.upper()

    # Create an empty string to store the result
    result = ""

    # Iterate over each character in the message
    for char in message:
        # If the character is a letter, shift it by the specified amount
        if char.isalpha():
            if mode == "encode":
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            elif mode == "decode":
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                raise ValueError("Invalid mode. Must be 'encode' or 'decode'.")
            result += shifted_char
        # If the character is not a letter, leave it as is
        else:
            result += char

    return result


while True:
    message = "Do you want to (e)ncrypt or (d)ecrypt?"
    response = input(message)
    if response == 'e':
        key = int(input("Please enter the key (0 to 25) to use. \n"))
        my_message = input("Enter the message to encrypt. \n")
        encrypted = caesar_cipher(my_message, key, "encode")
        print(encrypted)
    elif response == 'd':
        key = int(input("Please enter the key (0 to 25) to use. \n"))
        my_message = input("Enter the message to decrypt. \n")
        decrypted = caesar_cipher(my_message, key, "decode")
        print(decrypted)
    elif response == 'b':
        print("Thanks for using our service")
        break
    else:
        print("wrong letter")
        continue

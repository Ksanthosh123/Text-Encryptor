def caesar_cipher(text, shift, mode):
    """
    Encrypt or decrypt a message using the Caesar cipher technique.

    Parameters:
    - text (str): The message to encrypt or decrypt
    - shift (int): The shift key for the Caesar cipher
    - mode (str): 'encrypt' or 'decrypt' mode

    Returns:
    - str: Encrypted or decrypted message
    """
    result = ''
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A'))
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Application!")
    try:
        while True:
            print("\nMenu:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Exit")
            
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                message = input("Enter the message to encrypt: ")
                shift = int(input("Enter the shift key (0-25): "))
                encrypted_message = caesar_cipher(message, shift, 'encrypt')
                print(f"Encrypted Message: {encrypted_message}")
            
            elif choice == '2':
                message = input("Enter the message to decrypt: ")
                shift = int(input("Enter the shift key (0-25): "))
                decrypted_message = caesar_cipher(message, shift, 'decrypt')
                print(f"Decrypted Message: {decrypted_message}")
            
            elif choice == '3':
                print("Exiting the Caesar Cipher Application. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a valid option (1/2/3).")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

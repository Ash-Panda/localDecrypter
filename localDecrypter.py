import os
import cryptography.fernet as fernet

def decrypt_files(key):
    """
    Decrypts all files in the current directory that have the ".encrypted" extension
    using the provided key.
    """
    f = fernet.Fernet(key)

    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if file.endswith('.encrypted'):
            with open(file, 'rb') as input_file:
                input_data = input_file.read()
            decrypted_data = f.decrypt(input_data)
            output_filename = f.decrypt(file[:-10].encode()).decode() # decrypt the filename
            with open(output_filename, 'wb') as output_file:
                output_file.write(decrypted_data)
            os.remove(file)

    print("Decryption complete!")

# Prompt the user for the key
key = input("Enter the key: ")

# Call the decrypt_files function
decrypt_files(key.encode())

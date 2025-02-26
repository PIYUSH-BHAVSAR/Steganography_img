import cv2
import numpy as np

# 1️⃣ Convert Image to Binary (RGB Format)
def image_to_binary(image_path):
    image = cv2.imread(image_path)  # Read image in color (RGB)
    binary_string = ''.join(format(pixel, '08b') for pixel in image.flatten())  # Convert each pixel to 8-bit binary
    return binary_string, image.shape

# 2️⃣ Encrypt Message Using XOR Key
def encrypt_message(message, key):
    message_bin = ''.join(format(ord(char), '08b') for char in message)  # Convert message to binary
    key_bin = ''.join(format(ord(k), '08b') for k in key)  # Convert key to binary
    key_len = len(key_bin)

    encrypted_bin = ''.join(str(int(message_bin[i]) ^ int(key_bin[i % key_len])) for i in range(len(message_bin)))
    return encrypted_bin

# 3️⃣ Embed Encrypted Message in Image Binary (LSB)
def embed_message(binary_string, encrypted_message):
    binary_list = list(binary_string)  # Convert binary string to a list for modification

    # Store message length as a 32-bit binary header
    message_length = format(len(encrypted_message), '032b')
    full_message = message_length + encrypted_message  # Append message length to encrypted data

    msg_index = 0
    for i in range(0, len(binary_list), 8):  # Modify LSB of each byte
        if msg_index < len(full_message):
            binary_list[i + 7] = full_message[msg_index]  # Replace LSB
            msg_index += 1
        else:
            break

    return ''.join(binary_list)

# 4️⃣ Convert Binary Back to Image (Stego Image)
def binary_to_image(binary_string, image_shape, output_filename="stego_image.png"):
    pixel_values = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
    image_array = np.array(pixel_values, dtype=np.uint8).reshape(image_shape)
    
    cv2.imwrite(output_filename, image_array)
    print(f"Stego Image saved as {output_filename}")

# 5️⃣ Convert Stego Image to Binary for Extraction
def stego_image_to_binary(image_path):
    image = cv2.imread(image_path)  # Read the stego image
    binary_string = ''.join(format(pixel, '08b') for pixel in image.flatten())  # Convert pixels to binary
    return binary_string

# 6️⃣ Extract Encrypted Message
def extract_encrypted_message(binary_string):
    # Extract message length from first 32 LSBs
    message_length_bin = ''.join([binary_string[i + 7] for i in range(0, 32 * 8, 8)])
    message_length = int(message_length_bin, 2)  # Convert binary to integer

    # Extract the actual message
    extracted_bits = [binary_string[i + 7] for i in range(32 * 8, (32 + message_length) * 8, 8)]
    return ''.join(extracted_bits)

# 7️⃣ Decrypt Message
def decrypt_message(encrypted_bin, key):
    key_bin = ''.join(format(ord(k), '08b') for k in key)  # Convert key to binary
    key_len = len(key_bin)

    decrypted_bin = ''.join(str(int(encrypted_bin[i]) ^ int(key_bin[i % key_len])) for i in range(len(encrypted_bin)))
    message = ''.join(chr(int(decrypted_bin[i:i+8], 2)) for i in range(0, len(decrypted_bin), 8))
    return message.strip()

# Example Usage
image_path = "image.jpg"
message = "Confidential Data"
encryption_key = "secure123"

# Step 1: Convert Image to Binary
binary_data, shape = image_to_binary(image_path)
print("Image converted to binary.")

# Step 2: Encrypt Message
encrypted_message = encrypt_message(message, encryption_key)
print("Message encrypted.")

# Step 3: Embed Encrypted Message into Image Binary
modified_binary = embed_message(binary_data, encrypted_message)
print("Message embedded in image.")

# Step 4: Save as Stego Image
binary_to_image(modified_binary, shape, "stego_image.png")
print("Stego image created.")

# Step 5: Extract Binary from Stego Image
stego_binary = stego_image_to_binary("stego_image.png")
print("Stego image converted back to binary.")

# Step 6: Extract Encrypted Message
extracted_encrypted_message = extract_encrypted_message(stego_binary)
print("Encrypted message extracted.")

# Step 7: Decrypt Message
retrieved_message = decrypt_message(extracted_encrypted_message, encryption_key)
print("Retrieved Message:", retrieved_message)

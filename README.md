# Steganography Image Project

## 📌 Project Description
This project implements **image-based steganography** using **Least Significant Bit (LSB) encoding** to hide encrypted messages within an image. The encryption is done using the **XOR cipher**, ensuring that the hidden message remains secure.

## 🗂 Folder Structure
```
Steganography_img/
│── Input_images/         # Folder containing input images
│── Output_images/        # Folder containing output (stego) images
│── Stegano.py            # Main Python script for steganography
│── requirements.txt      # List of dependencies
│── README.md             # Project documentation
```

## 🚀 Features
✅ **Image-to-Binary Conversion**: Converts an image into binary representation.  
✅ **Message Encryption**: Uses XOR cipher to encrypt the secret message.  
✅ **LSB Encoding**: Embeds the encrypted message into the least significant bits of the image.  
✅ **Stego Image Creation**: Saves the modified image with the hidden message.  
✅ **Message Extraction**: Extracts and decrypts the message from the stego image.  

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🖥️ Usage
### 🔹 Encoding a Message into an Image
Run the script and specify the image path, message, and encryption key:
```bash
python Stegano.py --mode encode --image Input_images/image.jpg --message "Secret Data" --key "secure123"
```
**Process:**
1. Converts image to binary.
2. Encrypts the message using the XOR cipher.
3. Embeds the encrypted message into the image using LSB encoding.
4. Saves the stego image in `Output_images/`.

### 🔹 Decoding a Message from an Image
To extract and decrypt the hidden message:
```bash
python Stegano.py --mode decode --image Output_images/stego_image.png --key "secure123"
```
**Process:**
1. Extracts encrypted message from the stego image.
2. Decrypts the message using the provided key.
3. Prints the retrieved message.

## 📷 Example Workflow
```python
# Step 1: Convert Image to Binary
binary_data, shape = image_to_binary("Input_images/sample.jpg")

# Step 2: Encrypt Message
encrypted_message = encrypt_message("Confidential Data", "secure123")

# Step 3: Embed Encrypted Message
modified_binary = embed_message(binary_data, encrypted_message)

# Step 4: Save Stego Image
binary_to_image(modified_binary, shape, "Output_images/stego_image.png")

# Step 5: Extract Encrypted Message
stego_binary = stego_image_to_binary("Output_images/stego_image.png")
extracted_encrypted_message = extract_encrypted_message(stego_binary)

# Step 6: Decrypt the Message
retrieved_message = decrypt_message(extracted_encrypted_message, "secure123")
print("Retrieved Message:", retrieved_message)
```

## 📌 Dependencies
The project requires the following Python libraries:
- **OpenCV** (`cv2`)
- **NumPy** (`numpy`)

These are listed in `requirements.txt` and can be installed using:
```bash
pip install -r requirements.txt
```

## 🙌 Acknowledgments
- Inspired by digital image processing techniques.
- Developed for learning purposes in cryptography and steganography.

## 📧 Contact
For any questions, feel free to reach out via [GitHub Issues](https://github.com/PIYUSH-BHAVSAR/Steganography_img/issues).


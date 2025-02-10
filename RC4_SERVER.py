import socket
def RC4(key,msg):
    S=[]
    for i in range(256):
        S.append(i)
    j=0
    for i in range(256):
        j=(j+S[i]+key[i%len(key)])%256
        S[i],S[j]=S[j],S[i]

    i1=0
    j1=0
    output_msg=[]
    for c in msg:
        i1=(i1+1)%256
        j1=(j1+S[i1])%256
        S[i1],S[j1]=S[j1],S[i1]
        k=(S[i1]+S[j1])%256
        output_msg.append(c^S[k])
    return bytes(output_msg)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))
    print("Server started")
    message, addr = server_socket.recvfrom(4096)
    print(f"Client_encrypted: {message}")
    enc_file = "encrypted.txt"
    with open(enc_file, 'w') as f:
        f.write(str(message))
    print(f"Encrypted message written to '{enc_file}'")
    dec_msg = RC4(b"srmapuni",message).decode()
    print(f"Decrypted message: {dec_msg}")
    output_file = "decrypted_output.txt"
    with open(output_file, 'w') as file:
        file.write(dec_msg)
    print(f"Decrypted message written to '{output_file}'")

start_server()
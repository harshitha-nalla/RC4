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
def Client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    file = input("Enter the file name: ")
    with open(file, "r") as f:
        plaintext = f.read()
        encrypted_data = RC4(b"srmapuni",plaintext.encode())
        client_socket.sendto(encrypted_data, ('localhost', 5000))
        print(f"Sent encrypted data from file: {file}")


Client()







import base64
import os

faggot = os.environ['COMPUTERNAME'] # im federal like that

print(f'hello, User {faggot}, here is a base64 encoder and decoder this is the encoderbye now.\n')

str = input('text: ') # input string you want to be encoded
s_str = str.encode('ascii') # encodes it in ascii form

strb64 = base64.b64encode(s_str) # base64 encoding
print(f'---\nOriginal text: {str}\nEncoded Text: {strb64}\n---', file=open("encoded.txt", "a")) # prints the encoded / decoded message to a text file

''' 
logs every encode / decode you do to the designated .\decoded.txt - ./encoded.txt everything is b64 encryption & decryption 
if u say this is skidded istg i hate you fags
also i added text because i know people are troglodytes who are skids and dont know what any of this is
'''

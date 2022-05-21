import base64
import os

faggot = os.environ['COMPUTERNAME'] # grabs hosts computer name that is in a variable later used for my print function because im federal ;3

print(f'hello, User {faggot}, here is a base64 encoder and decoder this is the decoderbye now.\n') # just hi :]

str = input('text > ') # string you want to decode in Base64 encoding

decode = base64.b64decode(str) # decodes the string inputed above

print(f'---\nEncoded Text (b64): {str}\nDecoded Text: {decode}\n---', file=open("decoded.txt", "a")) # prints the decoded / encoded string into the terminal

''' 
logs every encode / decode you do to the designated .\decoded.txt - ./encoded.txt everything is b64 encryption & decryption 
if u say this is skidded istg i hate you fags
also i added text because i know people are troglodytes who are skids and dont know what any of this is
'''
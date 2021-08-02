
# Given base64 string, decodes the message.

import base64


content = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

def base64Encoder(content):
    base64_bytes = base64.b64encode(content)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def base64Decoder(content):
    
    base64_bytes = content.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

def hexToBytes(content):
    result = bytearray.fromhex(content)
    return result

message_bytes = hexToBytes(content)
solution = base64Encoder(message_bytes)
print(f"solution: {solution}")

from binascii import unhexlify

def brute(input, key):
    if len(input) != len(key):
        return "Fallo"

    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Fuera de rango al decodificar"

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(data)
print("[-] CIPHER: {}".format(cipher))

# First Step
key_part = brute(cipher[:7], "crypto{".encode())
print("[-] LLAVE PARCIAL ENCONTRADA: {}".format(key_part))

# Second Step
key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key))/len(key))
key += key[:((len(cipher) - len(key))%len(key))]
print("[-] Decodificando usando la key: {}".format(key))

plain = brute(cipher, key)
print("\n[*] FLAG: {}".format(plain))
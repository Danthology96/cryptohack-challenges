
def xor_with_key(value, key):
    result = b''
    for b in value:
        result += bytes([b ^key])
    
    try:
        return result.decode("utf-8")
    except:
        return "Fuera de rango al decodificar"


decodedValue = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

xorResults = {}
for i in range(128):
    if(i!=1):
        xorResults[i] = xor_with_key(decodedValue,i)
        print(f'[-] XOR RESULTS[{i}]: {xorResults[i]}')

for value in xorResults.values():
    if("crypto" in value):
        print(f"[*] FLAG: {value}")
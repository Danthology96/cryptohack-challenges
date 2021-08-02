
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    array = []
    for i in range(len(matrix[0])):
        m = matrix[i]
        for j in range(len(m)):
            array.append(m[j])
    return array

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    result = []
    # llenar la matriz de 0s
    for i in range(len(s[0])):
        result.append([0]* len(s[0]))
    
    for i in range(len(s[0])):
        si = s[i]
        ki = k[i]
        for j in range(len(si)):
            result[i][j]= si[j] ^ ki[j]
    return result    

# codigo optimizado
def add_round_key2(s, k):
    return [s[i][j] ^ k[i][j] for i in range(4) for j in range(4)]

result = add_round_key2(state, round_key)
print(result)
# descomentar la sig linea para usar el código anterior
# flag = matrix2bytes(result)

# descomentar la sig linea para usar el código anterior
# print("".join(chr(c) for c in flag))

print("".join(chr(c) for c in result))


# Given an array, decodes the message.

content = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]


def asCIIDecode(content):
    print("Solution: ")
    print("".join(chr(value) for value in content)) 


asCIIDecode(content)
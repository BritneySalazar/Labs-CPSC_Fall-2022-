#Camryn and Britney

def replace_substring(string, remove, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index + len(remove)] == remove:
            index += len(remove)
            output.append(replacement)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

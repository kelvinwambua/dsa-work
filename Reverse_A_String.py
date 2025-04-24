initialString = "IloveDSA"
def reverse_a_string(string):
    newString = []
    for i in range((len(string)-1),-1,-1):
         newString.append(string[i])
    return "".join(newString)
print(reverse_a_string(initialString))




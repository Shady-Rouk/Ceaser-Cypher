import sys
def CaesarEncoder(shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    user_message = input("What is your message? ")
    message_check = ""
    output_str = ""
    res = ""
    for ch in user_message:
        if ch.lower() in alphabet:
            message_check += ch.upper()
    for l in message_check:
        if (ord(l) + shift) > 90:
            output_str += chr(ord(l) - (26 - shift))
        else:
            output_str += chr(ord(l) + shift)
    counter = 5
    clock = 0
    for i in range(0, len(output_str), 5):   
        res += output_str[i:counter]
        res += " "
        counter += 5
        clock += 1
        if (clock % 10) == 0:
            res += "\n"
    return res
  
a = int(sys.argv[1])
print(CaesarEncoder(a))





# Coding Challenge 2, morse.py
# Name: Sachin Jaglan
# Student No: 1925646

# Morse Encoder/Decoder

# Morse code translations, use this to perform encoding/decoding

MORSE_CODE = (
    ("-...", "B"),
    (".-", "A"),
    ("-.-.", "C"),
    ("-..", "D"),
    (".", "E"),
    ("..-.", "F"),
    ("--.", "G"),
    ("....", "H"),
    ("..", "I"),
    (".---", "J"),
    ("-.-", "K"),
    (".-..", "L"),
    ("--", "M"),
    ("-.", "N"),
    ("---", "O"),
    (".--.", "P"),
    ("--.-", "Q"),
    (".-.", "R"),
    ("...", "S"),
    ("-", "T"),
    ("..-", "U"),
    ("...-", "V"),
    (".--", "W"),
    ("-..-", "X"),
    ("-.--", "Y"),
    ("--..", "Z"),
    ("-----", "0"),
    (".----", "1"),
    ("..---", "2"),
    ("...--", "3"),
    ("....-", "4"),
    (".....", "5"),
    ("-....", "6"),
    ("--...", "7"),
    ("---..", "8"),
    ("----.", "9"),
    (".-.-.-", "."),
    ("--..--", ","),
    ("..--..", "?"),
    (".----.", "'"),
    ("-.-.--", "!"),
    ("-..-.", "/"),
    ("-.--.", "("),
    ("-.--.-", ")"),
    (".-...", "&"),
    ("---...", ":"),
    ("-.-.-.", ";"),
    ("-...-", "="),
    (".-.-.", "+"),
    ("-....-", "-"),
    ("..--.-", "_"),
    (".-..-.", '"'),
    ("...-..-", "$"),
    (".--.-.", "@"),
)

Dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "&",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@"} 

RDict = {v: k for k, v in Dict.items()}

# TODO: Write your code here!

def checkdecode(msg):
    n = len(msg)
    for i in range(n):
        if msg[i]=='.' or msg[i]=='-' or msg[i]==' ':
            continue
        else:
            return 0
    return 1

def decode(msg):
    ans = ""
    msglist = msg.split("   ")
    n = len(msglist)
    list1 = []
    for i in range(n):
        part = msglist[i].split(" ")
        m = len(part)
        for j in range(m):
            if part[j] in Dict:
                list1.append(Dict[part[j]])
            else:
                return "Invalid Input"
            #add error checking for unavailable characters
        if i+1 != n:
            list1.append(" ")
    ans = ans.join(list1)
    return ans


def checkdecodetg(msg):
    n = len(msg)
    for i in range(n):
        if msg[i]!='1' and msg[i]!='0':
            return 0
    return 1

def minzero(msg):
    zeroes = msg.split("1")
    zeroes = filter(None,zeroes)
    unit = len(min(zeroes))
    return unit

def decodetg(msg,unit):
    ans = ""
    n = len(msg)
    list1 = []
    l = 0
    temp = ""
    t=0
    while t<n and msg[t]=='0':
        t+=1
    i=t
    while i<n:
        while i<n and msg[i]=='1':
            i+=1
        if (i-l) == (3*unit):
            temp += "-"
        else:
            temp += "."
        l=i
        
        while i<n and msg[i]=='0':
            i+=1
  
        if (i-l) == (7*unit):
            list1.append(temp)
            temp = ""
        elif (i-l) == (3*unit):
            temp+=" "
        l=i
    list1.append(temp)
    temp = ""
    ans = ans.join(list1)
    #debugging
    #print(ans)
    return ans

def encode(msg):
    ans = ""
    msglist = msg.split(" ")
    n = len(msglist)
    list1 = []
    for i in range(n):
        x = msglist[i]
        m = len(x)
        for j in range(m):
            if x[j] in RDict:    
                list1.append(RDict[x[j]])
                list1.append(" ")
            else:
                ans = " "
                return ans
        list1.append("   ")
    ans = ans.join(list1)
    return ans

print("This program encodes and decodes Morse code.")
var = 1
while var==1:
    var2 = 1
    while var2 == 1:
        flag1 = 1
        code = input("Would you like to encode (e), decode (d) or decode telegraph (dt): ")
        if code=='e':
            #something
            valid = 0
            while valid == 0:
                msg = input("What message would you like to encode:")
                result = encode(msg.upper())
                if result == " ":
                    print("Invalid Input")
                else:
                    print(result)
                    break
        elif code=='d':
            valid = 0
            while valid == 0:
                msg = input("What message would you like to decode:")
                valid = checkdecode(msg)
                if valid == 0:
                    print("Invalid Input")
                else:    
                    unit = minzero(msg)
                    result = decode(msg,unit)
                    print(result)
                    break
        elif code=="dt":
            valid = 0
            while valid == 0:
                msg = input("What telegraph message would you like to decode:")
                valid = checkdecodetg(msg)
                if valid == 0:
                    print("Invalid Input")
                    #debug2
                    print("wtf")
                
                
                elif valid == 1:
                    unit = minzero(msg)
                    result = decodetg(msg,unit)
                    print(result)
                    ans = decode(result)
                    if ans == "Invalid Input":
                        print(ans)
                        print("Invalid valid input")
                        valid == 0
                    else:
                        print(ans)
                        break
                       
                    
        
        else:
            print("Invalid mode.")
            continue
        if flag1==1:
            break
    var3 = 1
    flag = 1
    while var3 == 1:
        loop = input("Would you like to encode/decode another message? (y/n):")
        if loop=='y':
            flag = 1
            break
        elif loop=='n':
            flag = 0
            print("Thanks for using the program, goodbye!")
            break
        else:
            print("Invalid response")
    if flag == 0:
        break

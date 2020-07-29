# Coding Challenge 2, morse.py
# Name: 
# Student No:

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
"""
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
        • Check if the message contains valid characters.
          If not, continue to prompt the user until a valid message is selected
          (dependent upon the mode selected).
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment brief.

Hints:
    • Use the tuple of tuples above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment brief for code examples.
"""

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
    for i in range(n):
        part = msglist[i].split(" ")
        m = len(part)
        for j in range(m):
            ans.join(Dict[part[j]])
            #add error checking for unavailable characters
        ans.join(" ")
    print(ans)
    return ans

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

print("This program encodes and decodes Morse code.")
var = 1
while var==1:
    var2 = 1
    while var2 == 1:
        code = input("Would you like to encode (e) or decode (d): ")
        if code=='e':
            #something
            valid = 0
            while valid == 0:
                msg = input("What message would you like to encode:")
                #encode(msg)
        elif code=='d':
            valid = 0
            while valid == 0:
                msg = input("What message would you like to decode:")
                #valid = checkdecode(msg)
                #if valid == 0:
                #    continue
                result = decode(msg)
                print(result)
        else:
            print("Invalid mode.")
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
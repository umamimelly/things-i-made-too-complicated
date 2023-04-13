
userInput = input("Enter Hexadecimal #: ").upper()
usr_List = []

for letter in userInput:
    usr_List.append(letter)

exponent = 0
decimalValue = 0  
hexNumber = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    #split the userInput into a dictionary, usrIP, and appends the indexed keys from userInput with the values from hexNumber. 
    #key = list(hexNumber.keys())[index #]


usrDict = {k: hexNumber[k] for k in usr_List if k in hexNumber}
val = list(usrDict.values()) 
#i want the keys in usrIP to have the corresponding values from hexNumber

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumber:
            return None
    
    if len(hexNum) == 3:
        return val[0]* 256 + [hexNum[1]] * 16 + [hexNum[2]]
    
    if len(hexNum) == 2:
        return [hexNum[0]] * 16 + [hexNum[1]]
    
    if len(hexNum) == 1:
        return [hexNum[0]]

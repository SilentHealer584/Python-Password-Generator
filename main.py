import random
char=input("Desired Characters (1.Uppercase 2.Lowercase 3.Numbers 4.Symbols  ex:134)")
tmplt=char.replace("1", "ABCDEFGHIJKLMNOPQRSTUVWXYZ").replace("2", "abcdefghijklmnopqrstuvwxyz").replace("4", "!%&*()-_=+/?.>,<':;[]").replace("3", "0123456789")
print("Generationg password from", tmplt)
lgth=input("Desired password length: (24+ recommended)")
for i in range(1,6):
    print("\nPassword generation", i, ":")
    for y in range(int(lgth)):
        char1=char.replace("1", "ABCDEFGHIJKLMNOPQRSTUVWXYZ").replace("2", "abcdefghijklmnopqrstuvwxyz").replace("4", "!%&*()-_=+/?.>,<':;[]").replace("3", "0123456789")
        charlen=len(char1)
        chr=random.randint(0, charlen-1)
        char2 = char1[chr]
        print(char2, end="")
    print("")

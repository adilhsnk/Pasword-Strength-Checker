#This is a password strength checker created by Adil Hassan.
#The password has three categories; Week, Medium, and Strong password.

nums = "1234567890"
symbs = "!@#$%&*()?<>"
chars = "abcdefghijklmnopqrstuvwxyz"
print("Welcome to our password checker program")
print ("Please note that this program doesn't store or send your password anywhere! See the source-code")
passwd = input("Please type your password: ")

has_number = False
has_symbol = False
has_letter = False

for ch in passwd:
    if ch in chars:
        has_letter = True
    if ch in nums:
        has_number = True
    if ch in symbs:
        has_symbol = True
if has_letter and has_number and has_symbol and len(passwd) >= 8:
    print("Password stregth: Strong!")
elif (has_letter and has_number) or (has_symbol and len(passwd) >= 8):
    print("Password stregth: Medium...!")
else:
    print("Password stregth: Week")
print("Relaunch the program to check another password")

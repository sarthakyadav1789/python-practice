# Program to count number of vowels, consonants and digits

sent = input("Enter the data/sentence :")
vow = 0
con = 0
dig = 0

for i in sent.lower():
    if i.isalpha():
        if i in "aeiou":
            vow+=1
        else :
            con+=1
    if i.isdigit():
        dig+=1

print(f"The number of vowels is {vow}\n The number of consonants is {con}\n The number of digits is : {dig}")
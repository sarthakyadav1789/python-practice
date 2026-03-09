# Program to find the frequency of characters

data = input("Enter the data to be processed :")
freq ={}

for i in data :
    if i in freq:
        freq[i]+=1
    else :
        freq[i]=1

print(freq)

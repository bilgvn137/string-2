# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    count=0
    for i in text:
        if i=="@":
            count+=1
        elif  i==".":
            count+=1
    if count>=2:
        print ("Valid")
    else:
        print("Invalid")
    pass

# Exercise 2
def remove_vowels(text):
    word=""
    for i in range(len(text)):
        if text[i] not in "aoueiAOUIE":
            word+=text[i]
    print(word)
    pass

# Exercise 3
def get_initials(text):
    a=""
    text1=text.split()
    a+=text1[0][0].upper()
    a+="."
    a+=text1[1][0].upper()
    a+="."
    print(a)
    pass

# Exercise 4
def extract_year(text):
    a=""
    for i in range(len(text)):
        if text[i] in "0123456789":
            a+=text[i]
    if len(a)<5 and len(a)>0:
        print(a)
    else:
        print("False")
    pass

# Exercise 5
def is_palindrome(text):
    text1=""
    for i in text:
        if i!=" ":
            text1+=i
    if text1.lower()==text1[::-1].lower():
        print(True)
    else:
        print(False)
    pass


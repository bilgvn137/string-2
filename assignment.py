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
        return "Valid"
    else:
        return "Invalid"
    pass

# Exercise 2
def remove_vowels(text):
    word=""
    for i in range(len(text)):
        if text[i] not in "aoueiAOUIE":
            word+=text[i]
    if len(word)==0:
        return ''
    return word
    pass

# Exercise 3
def get_initials(text):
    a=""
    text1=text.split()
    for i in range(len(text1)):
        a=a+text1[i][0].upper()+"."
    return a
    pass
# Exercise 4
def extract_year(text):
    a=""
    for i in range(len(text)):
        if text[i] in "0123456789":
            a+=text[i]
    if len(a)<5 and len(a)>0:
        return a
    else:
        return False
    pass

# Exercise 5
def is_palindrome(text):
    text1=""
    for i in text:
        if i not in " ?!;:.,'":
            text1+=i
    if text1.lower()==text1[::-1].lower():
        return True
    else:
        return False
    pass


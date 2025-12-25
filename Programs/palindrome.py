str='madam'

def palindrome(str):
    return str.lower()==str[::-1].lower()
print(palindrome(str))
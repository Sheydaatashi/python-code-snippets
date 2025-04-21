string=input()
string=string.lower()
if 'a' or 'e' or 'i' or 'o' or 'u' in string:
    string=string.replace('a','.')
    string=string.replace('e','.')
    string=string.replace('i','.')
    string=string.replace('o','.')
    string=string.replace('u','.')
    print(string)
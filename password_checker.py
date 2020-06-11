'''
Password must be:
    - At least 8 char long
    - Contain any sort of letters, numbers and $%#@
    - It has to end with a number
'''

import re

password_pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}[0-9]")
password = 'he3as%$#0'
print(password_pattern.fullmatch(password))


n = int(input())
email_pattern = re.compile(
    r"(^[a-zA-Z])([a-zA-Z0-9-._]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})")
emails = []
for i in range(n):
    emails.append(input().replace('>', '').split(' <'))
    if email_pattern.fullmatch(emails[i][1]):
        print(emails[i][0] + ' <' + emails[i][1] + '>')

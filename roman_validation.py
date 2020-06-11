import re

regex_pattern = re.compile(
    r"(M{1,3})?((C{1,3})|C(D|M)|D(C{0,3})|M)?((X{1,3})|X(C|L)|L(X{0,3})|C)?((I{1,3})|I(V|X)|V(I{0,3})|X)\b")

match = regex_pattern.match(input())
print(match)
print(str(bool(match)))

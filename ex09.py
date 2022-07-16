#문자형

s = ''
str1 = 'hello world'
str2 = "안녕 세상"

print(s, str1, str2)
print(type(s), type(str1), type(str2), sep=",")
print(isinstance(str2, str))

print("=====================================================")

s01 = "aaa"
s02 = "aaa"
print(id(s01))
print(id(s02))

s02 = "aaaa"
print(id(s01))
print(id(s02))

print("=====================================================")
str3 = '''ABCDEFG
abcdef
가나다라마
123456789'''
print(str3)

print("=====================================================")
print('Hello\nWorld\nI\'d Say "hello World" ')

print("Hello\nWorld\nI'd Say \"hello World\"")
print("=====================================================")
print("Hello\rWorld\raaaaa")
print("Hello\b\bWorld")
print("Hello\tWorld")




s="i like Python"

#대소문자 관련
print(s.upper()) #대문자
print(s.lower()) #소문자
print(s.swapcase()) #소-->대   대-->소
print(s.capitalize()) #첫글자만 대문자로 변환
print(s.title()) #단어의 첫글자를 대문자로
print(s*3)
print(s+s)

#검색관련
s = 'I Like Phyton. I Like Java Also'

print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("Like", 5, 40))

print(s.find("JS"))

print(s.rfind('Like'))  #마지막 index를 찾아줌
#print(s.lfind('Like'))  X

print(s.index("to"))

print(s.startswith("I Like"))     #포함하는지X   시작하는지O
print(s.startswith("I Like", 2))

print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))

#편집과 치환
s = '   spam and ham    '
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = '<><abc><><defg><><>'
print(s.strip("<>"))


s = 'Hello Java Java java'
print(s.replace("Java", "Python"))


print("========")
s = 'king and queen'
print(s.center(60))
print(s.center(60, "-"))
print(s.ljust(60, "-"))
print(s.rjust(60, "-"))

print("1234".isdigit())
print("afbdcde한".isalpha())

print("abcd".islower())
print("ABCD".isupper())

print("20".zfill(10))
print("1234".zfill(10))

print("==============================")
#공백 -문자열이 모두 공백이면 true
print(" ".isspace())
print("".isspace())

print("      -      ".isspace())

print("\n".isspace())
print("\t".isspace())
print(" \t\n".isspace())

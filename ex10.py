str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2)    # print(str1 + 10)  -->문자열 + 문자열 만 가능
print(str1*3)
print(str1[5])
print(str1[-4])
print(str1[2:5])     #[이상:미만]
print(str1[1:9:3])     #[이상:미만:증가]
print(str1[:9])
print(str1[2:])
print(len(str1))

print(str1[:])
print(str1[-6:-2])

print(str1[::-1])

name = "우영후"
name2 = name[:-1:]

print(name)
print(name2)


#if("토마토" == name[::-1]):
#    print("aaa")

str1[7]=a
print(str1)
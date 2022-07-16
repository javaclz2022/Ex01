#복소수


#복소수 타입의 객체는 실수부+허수부로 나뉘며 허수부에는 j 또는 J를 숫자 뒤에 붙인다.
a=4+5j
print(a, type(a))

a=4+5j
b=7-2j
print(a+b)

print(b.real)
print(b.imag)

c=4
d=5.4

f=complex(c)

print(type(complex(c)))
print(complex(d))

print(c) #원래값이 변한건 아니다
print(f, type(f))


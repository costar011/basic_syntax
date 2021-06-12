# 정수 타입은 sort가 가능하다.

# ASCII CODE
# char == ASCII CODE
# 한 글자만 저장된다.

txt1 = "ant"
txt2 = "mac"


print(txt1[0:1])

txt1_front_txt = ord(txt1[0:1])
# ord -> 문자를 아스키코드로 변환 하지만 한글자만 저장된다.
txt2_front_txt = ord(txt2[0:1])

print(txt1_front_txt)  # 97
print(txt2_front_txt)  # 109

if(txt1_front_txt < txt2_front_txt):
    print(txt1)
    print(txt2)
else:
    print(txt2)
    print(txt1)

# 여러개로 만들면 버블소트 라고 한다.

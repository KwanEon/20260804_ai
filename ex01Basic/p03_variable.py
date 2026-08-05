'''
정적타입 언어 : 자료형을 컴파일 타임에 결정하는 언어
동적타입 언어 : 자료형을 런타임(실행 시점)에 결정하는 언어
약타입 언어 : 자료형이 맞지 않을 시에 암묵적으로 타입을 변환하는 언어
강타입 언어 : 자료형이 맞지 않을 시에 에러 발생, 암묵적 변환을 지원하지 않음
Python은 동적타입이면서, 약타입 언어, 변수 타입을 강제 지정 불가
'''

print("=== 파이썬 변수의 자료형 ===")
'''
변수의 type
Scalar 타입 : int, float, None, bool 4가지: 단수의 값
Composite 타입 : str, list, tuple, dict, set: 복수의 값

불 자료형: True, False
숫자 자료형: int, float, complex
군집 자료형: str, list, tuple, dict, set
help(str) # 각타입별 설명 출력
'''

print("=== 변수의 명명규칙 ===")
'''
1) 변수나 함수는 Snake case, 클래스는 Pascal
2) _, 영문자(대소문자 구별), 숫자(시작 안됨) 사용, 그외 문자 불가
3) 예약어 안됨(if, for, ...)
4) 특수문자, 공백 X
5) null 대신 None을 사용
'''

# 변수의 재선언(O), 업데이트(O), 타입 고정(X)
a = 10
print(type(a))  # 객체지향적 언어
a = True
b = True
c = 3.14
print(type(a), type(b), type(c))

d = complex(3, -4)
print(d, type(d))
e = 10 + 3j + 5J
print(e, type(e))
print(type(d), type(e), d.real, d.imag)
s = 'hello'
print(s, type(s), )
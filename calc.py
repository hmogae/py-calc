import os

# Default
print("HYNStudio Calc (V1 Beta)")
os.system("title HYNStudio Calc (V1 Beta)")
os.system("color b")

# Input
a=int(input("첫번째 수: "))
b=int(input("두번째 수: "))

ab1 = a+b
ab2 = a-b
ab3 = a*b
ab4 = a/b

# Result
print("처리중입니다. 잠시만 기다려주세요...")
print("\n")

print(f'더하기: {a}+{b} = {ab1}')
print(f'빼기: {a}-{b} = {ab2}')
print(f'곱하기: {a}*{b} = {ab3}')
print(f'나누기: {a}/{b} = {ab4}')
os.system("pause")
import random;
answer = random.randint(1,101)
num=0

count=0

print("1~100 숫자 Up & Down 게임을 시작합니다")
print("-------------------------------")

print("숫자를 입력하세요.")
while True :
   num = int(input())
   count += 1
   if num>answer:
       print("더 낮은 수를 입력하세요")
   elif num<answer:
        print("더 높은 수를 입력하세요") 
   else  :
        print("정답입니다.")
        break;

print("-------------------------------")
print(count, "번 만에 정답을 맞추셨습니다!")

   
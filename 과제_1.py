# [문자열1]
print("문자열 : 나는 천재다!")
lenth = len("나는 천대다!")
print(f"문자열의 길이 : {lenth}")


# [if1]
number = int(input("월을 입력하세요 : "))
if 3 <= number <= 5:
    print(f"{number}월은 봄입니다.")
elif 6 <= number <= 8:
    print(f"{number}월은 여름입니다.")
elif 9 <= number <= 11:
    print(f"{number}월은 가을입니다.")
elif number == 1 or number == 2 or number == 12:
    print(f"{number}월은 겨울입니다.")
else:
    print("월은 1부터 12까지 있습니다.")


# [if2]
word_1 = input("'호랑이'의 영어 단어는 무엇일까요? : ").lower()
if word_1 == "tiger":
    print("딩동댕! 참 잘했어요~~~")
else:
    print("땡! 틀렸습니다.")
word_2 = input("'사과'의 영어 단어는 무엇일까요? : ").lower()
if word_2 == "apple":
    print("딩동댕! 참 잘했어요~~~")
else:
    print("땡! 틀렸습니다.")
word_3 = input("'컴퓨터'의 영어 단어는 무엇일까요? : ").lower()
if word_3 == "computer":
    print("딩동댕! 참 잘했어요~~~")
else:
    print("땡! 틀렸습니다.")


# [if~else]
print("아르바이트 급여 계산 프로그램")
wage = int(input("1(주간 근무) 또는 2(야간 근무)을 입력해주세요. : "))
time = int(input("근무 시간을 입력해주세요. : "))
if wage == 1:
    final_wage = time * 9500
    print(f"{time}시간 동안 일한 주간 급여는 {final_wage}원 이다.")
elif wage == 2:
    final_wage = time * 9500 * 1.5
    print(f"{time}시간 동안 일한 야간 급여는 {final_wage}원 이다.")
else:
    print("주간 근무라면 '1', 야간 근무라면 '2'를 입력해주세요.")


# [if~elif~else 1]
num_1 = int(input("첫 번째 정수를 입력하세요. : "))
num_2 = int(input("두 번째 정수를 입력하세요. : "))
num_3 = int(input("세 번째 정수를 입력하세요. : "))
if num_1 > num_2:
    if num_1 > num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_1} 입니다.")
    elif num_3 > num_1:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_3} 입니다.")
    elif num_1 == num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_1}, {num_3} 입니다.")

if num_2 > num_1:
    if num_2 > num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_2} 입니다.")
    elif num_3 > num_2:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_3} 입니다.")
    elif num_2 == num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_2}, {num_3} 입니다.")

if num_1 == num_2:
    if num_1 > num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_1}, {num_2} 입니다.")
    elif num_3 > num_1:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_3} 입니다.")
    elif num_1 == num_3:
        print(f"입려된 세 수 {num_1}, {num_2}, {num_3} 중에서 가장 큰 수는 {num_1}, {num_2}, {num_3} 입니다.")


# [if~elif~else 2]
score = int(input("점수를 입력해 주세요 : "))
print(f"성적 : {score}")
if 90 <= score <= 100:
    print("등급 : A")
elif 80 <= score <= 89:
    print("등급 : B")
elif 70 <= score <= 79:
    print("등급 : C")
elif 60 <= score <= 69:
    print("등급 : D")
elif 0 <= score <= 59:
    print("등급 : F")
else:
    print("점수는 0~100점 사이로 입력해주세요.")


# [if 중복 사용]
ID = input("아이디를 입력하세요 : ").lower()
level = int(input("회원 레벨을 입력해 주세요 : "))
if ID == "admin":
    print("해당 콘텐츠 이용이 가능합니다!")
elif 1 <= level <= 7:
    print("해당 콘텐츠 이용이 가능합니다!")
else:
    print("해당 콘텐츠 이용이 불가능합니다!")


# [for문 1]
sum = 0
for n in range(200, 301):
    if n % 2 == 1:
        sum += n
print(sum)


# [for문 2]
for i in range(10):
    print("*" * int((10 - i)))
    i += 1


# [리스트1]
Color = ['빨강','주황','노랑','초록','파랑','남색','보라']
print(Color[0])
print(Color[5])
print(Color[2:6])
print(Color[4])
print(Color[3:6])


# [리스트2]
lst = []
for i in range(1, 21):
    if i % 2 == 1:
        lst.append(i)
print(lst)


# [리스트3]
lst = ['빨간', '파란', '노란', '검정', '초록']
for i in range(0, 5):
    color = lst[i]
    print(f"나는 {color}색을 가장 좋아합니다~~~")


# [리스트4]
mylist = ["사과", "바나나", "파인애플", "포도"]
print(mylist[-2])


# [리스트5]
flowers = ['목련', '벚꽃', '장미', '백일홍']
print(flowers)
flowers[1] = '무궁화'
print(flowers)


# [리스트6]
seats = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1]]

for i in seats:
    for j in i:
        if j == 0:
            print("□", end=" a ")
        elif j == 1:
            print("■", end=" ")
    print()


# [리스트7]
s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87,
     87, 36, 82, 98, 84, 76, 63, 69, 53, 22]
# 수 : 90~100 / 우 : 80~89 / 미 : 70~79 / 양 : 60~69 / 가 : 0~59
count_su = 0
count_woo = 0
count_mi = 0
count_yang = 0
count_ga = 0

for i in s:
    if 90 <= i <= 100:
        count_su += 1

    if 80 <= i <= 89:
        count_woo += 1

    if 70 <= i <= 79:
        count_mi += 1

    if 60 <= i <= 69:
        count_yang += 1

    if 0 <= i <= 59:
        count_ga += 1

print(f"수 : {count_su}명")
print(f"우 : {count_woo}명")
print(f"미 : {count_mi}명")
print(f"양 : {count_yang}명")
print(f"가 : {count_ga}명")
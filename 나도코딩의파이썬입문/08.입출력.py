# 입출력

# ===== [ 1. 표준입출력 ] =====
# 표준입력 : input() 함수로 입력받음
# 표준출력 : print() 함수로 출력함

print("Python", "Java", sep=", ", end="? ")  # sep : 구분자, end : 끝 문자
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)  # 표준 출력
print("Python", "Java", file=sys.stderr)  # 표준 에러


# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # ljust : 왼쪽 정렬, rjust : 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ..., 020
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # zfill : 숫자 앞에 0을 채움

answer = input("아무 값이나 입력하세요 : ")  # input() 함수는 항상 문자열을 반환함
print("입력하신 값은 " + answer + "입니다.")

# ===== [ 2. 다양한 출력포맷 ] =====

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))  # 500을 오른쪽 정렬하고, 총 10자리 공간 확보

# 양수는 +로 표시, 음수는 -로 표시, 총 10자리 공간 확보
print("{0: >+10}".format(500))  # 양수는 +로 표시
print("{0: >+10}".format(-500))  # 음수는 -로 표시

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))  # 500을 왼쪽 정렬하고, 빈칸을 _로 채움

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))  # 3자리마다 콤마를 찍어주기

# 3자리마다 콤마를 찍어주고, 부호도 붙이기
print("{0:+,}".format(100000000000))  # 양수는 +로 표시
print("{0:+,}".format(-100000000000))  # 음수는 -로 표시

# 3자리마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000))  # 양수는 +로 표시, 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(-100000000000))  # 음수는 -로 표시, 빈 자리는 ^로 채우기

# 소수점 출력
print("{0:f}".format(5/3))  # 소수점 출력

# 소수점 특정 자리수까지만 표시(반올림)
print("{0:.2f}".format(5/3))  # 소수점 둘째 자리까지 출력


# ===== [ 3. 파일입출력 ] =====

score_file = open("score.txt", "w", encoding="utf8")  # 파일 열기(쓰기 모드)
print("수학 : 0", file=score_file)  # 파일에 쓰기
print("영어 : 50", file=score_file)
print("코딩 : 100", file=score_file)
score_file.close()  # 파일 닫기

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")  # 파일에 쓰기
score_file.write("\n코딩 : 100")  # 줄 바꿈 문자(\n)로 줄 바꿈
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  # 파일 전체 읽기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 줄을 읽어서 리스트로 저장
for line in lines:
    print(line, end="")  # 줄 바꿈 문자(\n)가 있기 때문에 end=""로 줄 바꿈 방지
score_file.close()

# ===== [ 4. pickle ] =====

import pickle
profile_file = open("profile.pickle", "wb")  # 바이너리 쓰기 모드로 파일 열기
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 데이터를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # file에 저장된 profile 데이터를 불러오기
print(profile)
profile_file.close()

# ===== [ 5. with ] =====

import pickle
with open("profile.pickle", "rb") as profile_file:  # with 구문을 사용하면 파일을 자동으로 닫아줌
    profile = pickle.load(profile_file)

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
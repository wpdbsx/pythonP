print("="*50)
print("="*5,"고객 관리 시스템","="*17)
print("="*5,"메뉴를 선택 하세요.","="*14)
start ="Y"
name=[]
age=[]
gender= []
namecount =1
agecount =1
gendercount =1
while start == "Y":
    print("="*5,"이름 입력 : 1, 나이 입력:2, 성별 입력 ; 3")
    menu = input("1, 2, 3 메뉴 중에 하나를 입력하세요 : ")
    if menu == '1':
        print("이름 시작")
        name.append(namecount)
        namecount +=1
    elif menu == '2' :
        print("나이 시작")
        age.append(agecount)
        agecount +=1
    elif menu == '3' :
        print("성별 시작")
        gender.append(gendercount)
        gendercount+=1
    start = input("계속 입력하시겠습니까? Y/N").upper()
print ("이름" ,name, "나이",age,"성별",gender)
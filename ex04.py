import pickle
import model
import view


# a = 0


model= model.model()
member=model.db_load() # db 내용 불러오기

# page= len(data)-1
view = view.view()
view.background1()

while True : 
    view.background2()
    menu = model.print01()    #메뉴 입력
    if menu == "I" :
        name = model.input_name()  #이름 입력
        gender = model.input_gender() # 성별 입력

        while True : 
            if gender != 'F' and gender != 'M':
                view.say_genderError()   #성별오류메세지
                gender = model.input_gender() #성별입력
                continue
            else:
                break

        while True :    
            email = model.input_email()
            find = email.find("@") #이메일 형식 조사
            if find == -1 :
                view.say_emailError() # 이메일 오류 메세지
            else :
                break
        while True :
            try :
                year = model.input_year()
                if year >=1000 and year < 10000 :
                    break       
                else :
                    view.say_yearError()
            except:
                view.say_inputError()
                
            
        member = model.input_list(member,name, gender, email, year)  #member 리스트에 값 추가하기
        
    if menu == "C" :
        
        print("고객정보는 ",len(member),"건 입니다.")
        if len(member) >0 :
            print("{0:^6} {1:^2} {2:^27} {3:^}".format("이름","성별","이메일","생년월일"))
        for i in member :
            이름 =i[0]
            성별 =i[1]
            이메일 =i[2]
            생년월일 = i[3]
            print("{0:^8} {1:^4} {2:^30} {3:<4}".format(이름,성별,이메일,생년월일))

    if menu == "Q":
        model.db_save(member)
        # with open('member.txt','wb') as f:
        #     pickle.dump(member,f)
        break

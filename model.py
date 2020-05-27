import pickle

class model() :

    def db_load(self):
        with open('member.txt','rb') as f :
            self.data = pickle.load(f)
        return self.data

    def db_save(self,member):
        with open('member.txt','wb') as f:
            self.member=member
            pickle.dump(self.member,f)
        
    def input_name(self):
        self.name =input('이름을 입력하시오.')
        return self.name
    def input_gender(self):
        self.gender = input('성별을 입력하시오.').upper()
        return self.gender
    def input_email(self):
        self.email =input('이메일을 입력하시오.') 
        return self.email
    def input_year(self):
        self.year= int(input('출생년도를 입력하시오.'))
        return self.year
    def input_list(self,member,name,gender,email,year):
        list = [name, gender, email, year]
        self.member.append(list)
        return self.member


    def print01(self):
        print0=input('I : 고객정보 입력, C : 고객정보 수 출력, Q : 프로그램 종료  ').upper()
        return print0
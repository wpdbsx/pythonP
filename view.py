class view:

    def background1(self):
        print ("★"*86)
        print("{0:★^80}".format("고객정보관리"))

    def background2(self):
        print(" "*13,end="   ")
    def say_genderError(self) :
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
    def say_emailError(self) :
        print("이메일 형식을 맞추시오")
    def say_yearError(self):
        print("1000~9999사이로 입력하시길 바랍니다")
    def say_inputError(self):
        print("숫자를 입력해주세요")
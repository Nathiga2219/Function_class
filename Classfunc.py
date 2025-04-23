class functions():
    def Subfields():
        sub_list=['Machine learning','Neural Networks','Vision','Robotics','Speech Processing','Natural language processing']
        print("Sub-fields in AI are:")
        for El in sub_list:
            print(El)
    def OddEven():
        Num=int(input("Enter a number:"))
        if((Num%2==0)):
            print(Num,"is Even number")
        else:
            print(Num,"is Odd number")
    def Eligible():
        Gender=str(input("Your Gender:"))
        Age=int(input("Your Age"))
        i='Male'
        j='Female'
        if(Gender==i and Age<21):
          print("Not Eligible for Marriage")
        elif(Gender==j and Age<18):
          print("Not Eligible for Marriage")
        else:
          print("Eligible for Marriage")
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        per=(Total/500)*100
        print("Percentage:",per)
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        AF=(H*B)/2
        print("Area of Triangle:",AF)
        He1=int(input("Height1:"))
        He2=int(input("Height2:"))
        He3=int(input("Height3:"))
        peri_for=He1+He2+He3
        print("Perimeter of Triangle:",peri_for)

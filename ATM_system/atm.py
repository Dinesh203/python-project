
from datetime import datetime

with open("kpbal.txt") as f:
    db = f.read()
    kbal=int(db)
with open("dinbal.txt") as f:
    db = f.read()
    dinbal=int(db)
with open("psbal.txt") as f:
    db = f.read()
    psbal=int(db)

with open("kppass.txt") as f:
    db = f.read()
    kpw=int(db)
with open("dinpass.txt") as f:
    db = f.read()
    dpw=int(db)
with open("pspass.txt") as f:
    db = f.read()
    ppw=int(db)


class User:
    def __init__(self, name, bblance,password):
        self.name=name
        self.balance=bblance
        self.password=password
        
    def withdrawl(self,amt):
       
        if amt <= self.balance:
            self.balance=self.balance-amt
        
           
    
    def deposite(self,amt):
    
        self.balance=self.balance+amt
        
    
    def changepassword(self):
        np=int(input("Enter 4 digit new password: "))
        self.password=np
    
def list():
    options = '''welcome
            1. Check balance
            2. Withdrawl
            3. Deposite
            4. Statement
            5. change password
            6. Back'''

    print(options)
            
                      

kp=User("kapil",kbal,kpw)
din=User("Dinesh",dinbal,dpw)
ps=User("Pushpendra",psbal,ppw)


today=datetime.now()
n=2
while True:
        try:
            for i in range(3):
                pw=int(input("Enter 4 digit Pin: "))
                
                if pw==kpw or pw==dpw or pw==ppw or qt==0:
                    while True:
                        if pw==kpw:
                            print("Hello Kapil")
                            list()
                            ch=int(input("Enter your choice: "))

                            if ch==1:
                                with open("kpbal.txt", "r") as f:
                                    check = f.readline()
                                    print(f"Available balance is RS.: {check}")

                            elif ch==2:
                                amt=int(input("Amount you want to withdrawl: "))
                                kp.withdrawl(amt)
                            
                                with open("kpbal.txt",'w') as f:
                                    f.write(str(kp.balance))
                                with open ("kpstatement.txt","a") as f:
                                    f.write("\n W  "  +(str(amt)))
                                    f.write("\t B  " + (str(kp.balance)))
                                    f.write("\n \t" + str(today))
                            
                                print(f"RS.{amt} withdral Successfully \tavailable balance is RS.{kp.balance}  ")


                            elif ch==3:
                                amt=int(input("Amount you want to deposite: "))
                            
                                kp.deposite(amt)
                                
                                with open("kpbal.txt",'w') as f:
                                    f.write(str(kp.balance))
                                with open ("kpstatement.txt","a") as f:
                                    f.write("\n D  "  +(str(amt)))
                                    f.write("\t B  " + (str(kp.balance)) )
                                    f.write("\n \t" + str(today))
                                print(f"RS.{amt} deposite available balance is RS.{kp.balance}  ")
                            elif ch==4:
                                with open("kpstatement.txt") as f:
                                    k=f.read()
                                    print(k)

                            elif ch==5:
                                kp.changepassword()
                                with open("kppass.txt",'w') as f:
                                    f.write(str(kp.password))
                            elif ch==6:
                                print("Thanks for coming")
                                break
                            else:
                                print("choice not available, please  choose given choices")

                        elif pw==dpw:
                            print("Hello Dinesh")
                            
                            list()
                            ch=int(input("Enter your choice: "))

                            if ch==1:
                                with open("dinbal.txt", "r") as f:
                                    check = f.readline()
                                    print(f"Available balance is RS.: {check}")

                            elif ch==2:
                                amt=int(input("Amount you want to withdrawl: "))
                                din.withdrawl(amt)
                                with open("dinbal.txt",'w') as f:
                                    f.write(str(din.balance))
                                
                                with open ("dinstatement.txt","a") as f:
                                    f.write("\n W  "  +(str(amt)))
                                    f.write("\t B  " + (str(din.balance)) )
                                    f.write("\n \t" + str(today))
                                print(f"RS.{amt} withdral available balance is RS.{din.balance}  ")
                            elif ch==3:
                                amt=int(input("Amount you want to deposite: "))
                            
                                din.deposite(amt)
                                with open("dinbal.txt",'w') as f:
                                    f.write(str(din.balance))
                                    
                                with open ("dinstatement.txt","a") as f:
                                    f.write("\n D  "  +(str(amt)))
                                    f.write("\t B  " + (str(din.balance)) )
                                    f.write("\n \t" + str(today))
                                print(f"RS.{amt} deposite available balance is RS.{din.balance}  ")
                            elif ch==4:
                                with open("dinstatement.txt") as f:
                                    k=f.read()
                                    print(k)
                            elif ch==5:
                                din.changepassword()
                                with open("dinpass.txt",'w') as f:
                                    f.write(str(din.password))
                            elif ch==6:
                                print("Thanks for coming")
                                break
                            else:
                                print("choice not available, please  choose given choices")

                        
                        elif pw==ppw:
                            print("Hello Pushpendra")
                            
                            list()
                            ch=int(input("Enter your choice: ")) 

                            if ch==1:
                                with open("psbal.txt", "r") as f:
                                    check = f.readline()
                                    print(f"Available balance is RS.: {check}")

                            elif ch==2:
                                amt=int(input("Amount you want to withdrawl: ")) 
                                ps.withdrawl(amt)
                                with open("psbal.txt",'w') as f:
                                    f.write(str(ps.balance))
                                    
                                with open ("psstatement.txt","a") as f:
                                    f.write("\n W  "  +(str(amt)))
                                    f.write("\t B  " + (str(ps.balance)) )
                                    f.write("\n \t" + str(today))
                                print(f"RS.{amt} withdral available balance is RS.{ps.balance}  ")
                            elif ch==3:
                                amt=int(input("Amount you want to deposite: "))
                                
                                ps.deposite(amt)
                                with open("psbal.txt",'w') as f:
                                    f.write(str(ps.balance))
                                
                                with open ("psstatement.txt","a") as f:
                                    f.write("\n D  "  +(str(amt)))
                                    f.write("\t B  " + (str(ps.balance)) )
                                    f.write("\n \t" + str(today))
                                print(f"RS.{amt} deposite available balance is RS.{ps.balance}  ")
                                    
                            elif ch==4:
                                with open("psstatement.txt") as f:
                                    k=f.read()
                                    print(k)
                            elif ch==5:
                                ps.changepassword()
                                with open("pspass.txt",'w') as f:
                                    f.write(str(ps.password))

                            elif ch==6:
                                print("Thanks for coming")
                                break
                            else:
                                print("choice not available, please  choose given choices")
                
                    break

                elif i == 2:
                    print("blocked")

                else:
                    c=n-i
                    print("wrong password try again")
                    print ("{} attempt remaining".format(c))


        except Exception:
            print("please enter valid input")


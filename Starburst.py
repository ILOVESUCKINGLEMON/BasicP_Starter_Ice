from random import randint

#ตัวแปร
Decision1 = 0
Weapons = 0
max_hit = 0
monhp = 65
i=1
#Damage each Weapons
damage_range = 0
damage = 0
#หนีพ้นไหม
Iamtheflash = 1
#กดออกเกม

Exit = False
Confirmation = False

while Iamtheflash == 1 :
    print("Slime // HP: 65 // Level: Easy")
        #First Decision
    Decision1 = int(input("Fight(1) / Run(2)"))
    if Decision1 == 2 :
        Iamtheflash = (1,2)
        Iamtheflash = randint(*Iamtheflash)
        if Iamtheflash == 1 :
            print (" คุณหนีพ้นแล้ว ")
            break
        else :
            print (" NOWHERE TO RUN!!!")
    else :
        break

#Weapons choosing
if Decision1 == 1 :
    while Exit == False  :
        print("\n----- โปรดเลือกอาวุธ -----")
        print("1. Wood stick | 1-5 damage | ตีได้ 5 ครั้ง")
        print("2. Laptop     | 5-10 damage | ตีได้ 3 ครั้ง")
        print("3. Excalibur  | 15-20 damage | ตีได้ 1 ครั้ง")
        print("           หากต้องการออกกด 4            ")
        
        Weapons = int(input("Wood stick (1)/Laptop (2)/Excalibur (3)")) 
        
        if Weapons == 4 :
            Exit == True
            break
        elif Weapons == 1 and Exit == False:
            max_hit = 5
            damage_range = (1, 5)
            break
        elif Weapons == 2 and Exit == False:
            max_hit = 3
            damage_range = (5, 10)
            break
        elif Weapons == 3 and Exit == False:
            max_hit = 1
            damage_range = (15, 20)
            break
        else:
            print("กรุณาเลือก 1, 2 หรือ 3 เท่านั้น")
        
        


#Fight
if Weapons == 1 :
    while True :
        hit = int(input("ตีกี่ครั้ง ? (สูงสุด 5 ครั้ง)"))
        if 1 <= hit <= 5 :
            while i <= hit and monhp > 0 :
                damage = randint(*damage_range)
                print(f"Hit ครั้งที่ {i} |", damage , "damage")
                monhp -= damage
                print(monhp)
                i += 1
        
        else :
            print ("กรุณากรอกเลข 1-5")
            

            

    if Weapons == 2 :
        print("ตีกี่ครั้ง ? (สูงสุด 3 ครั้ง)")
    if Weapons == 3 :
        print("ตีกี่ครั้ง ? (สูงสุด 1 ครั้ง)")

elif Exit == True :
    while True :
        Confirmation =  str(input("are you sure to leave? (y/n)"))
        if Confirmation == "y":
            break
        elif Confirmation == "n" :
            Exit == False
        else :
            print ("กรุณากรอกแค่ y กับ n")


    


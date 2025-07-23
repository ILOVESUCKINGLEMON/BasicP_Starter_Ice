from random import randint

#ตัวแปร
Decision1 = 0
Weapons = 0
hit = 0
monhp = 65
i=1
#Damage each Weapons
wood_stick_damage = 0



print("Slime // HP: 65 // Level: Easy")
Decision1 = int(input("Fight press (1)/Run press (2)"))
if Decision1 == 1 :
    print("-----โปรดเลือกอาวุธ-----")
    print("Wood stick|5 atk ")
    print("Laptop | 10 atk")
    print("Excalibur | 20 atk")
    Weapons = int(input("Wood stick (1)/Laptop (2)/Excalibur (2)"))
    if Weapons == 1 :
        hit = int(input("ตีกี่ครั้ง ? (สูงสุด 5 ครั้ง)"))
        if 1 <= hit <= 5 :
            while i <= hit and monhp <= 0 :
                wood_stick_damage = randint(1, 5)
                print(f"Hit ครั้งที่ {i} |", wood_stick_damage , "damage")
                monhp -= wood_stick_damage
                print(monhp)
                i += 1
        if monhp <= 0 :
            print("YOU WIN CONGRATULATIONS!!")
            

            

    if Weapons == 2 :
        print("ตีกี่ครั้ง ? (สูงสุด 3 ครั้ง)")
    if Weapons == 3 :
        print("ตีกี่ครั้ง ? (สูงสุด 1 ครั้ง)")

else :
    print("NOWHERE TO RUN!!")
    


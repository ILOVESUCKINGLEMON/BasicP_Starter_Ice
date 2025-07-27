from random import randint

#ตัวแปร
Decision1 = 0
Weapons = 0
max_hit = 0
monhp = 75
i=1
playerhp = 100
mon_dmg_range = (10,25)
mondmg = 0
keepfighting = True
#Damage each Weapons
damage_range = 0
damage = 0
#หนีพ้นไหม
Yourluck = (1,10)
Iamtheflash = 1
#กดออกเกม

Exit = False    
Confirmation = False

while True :
    print("Slime // HP: 75 // Level: Easy")
        #First Decision
    Decision1 = int(input("Fight(1) / Run(2)"))
    if Decision1 == 2 :
        Iamtheflash = randint(*Yourluck)
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
        print("1. ไม้กากๆ          | 3-12 damage | ตีได้ 5 ครั้ง")
        print("2. โน้ตบุ๊คAsus       | 5-9 damage | ตีได้ 3 ครั้ง")
        print("3. ไม้แขวนเสื้อของแม่  | 2-20 damage | ตีได้ 1 ครั้ง")
        print("           หากต้องการออกกด 4            ")
        
        Weapons = int(input("กิ่งไม้กากๆ (1)/โน้ตบุ๊คAsus (2)/ไม้แขวนเสื้อของแม่ (3)")) 
        
        if Weapons == 4 :
            Exit == True
            break
        elif Weapons == 1 and Exit == False:
            max_hit = 5
            damage_range = (3,12)
            break
        elif Weapons == 2 and Exit == False:
            max_hit = 3
            damage_range = (5,9)
            break
        elif Weapons == 3 and Exit == False:
            max_hit = 1
            damage_range = (2,20)
            break
        else:
            print("กรุณาเลือก 1, 2 หรือ 3 เท่านั้น")
        
        


#Fight
#Wood stick
if Weapons == 1 :
    while True:
        i = 1 #รีเซ็ทค่า i
        hit = int(input("ตีกี่ครั้ง ? (สูงสุด 5 ครั้ง) **กดเลข 8 เพื่อออกจากเกม"))
        if hit == 8 :
            break
        if 1 <= hit <= 5 :
            while i <= hit and monhp > 0 :
                damage = randint(*damage_range)
                print(f"Hit ครั้งที่ {i} |", damage , "damage")
                monhp -= damage
                print(monhp)
                print(f"เลือด Slime เหลือ |", monhp , "hp")
                i += 1
                
            if monhp <= 0:
                    print("คุณชนะแล้ว... CONGRATULATIONS!!")
                    break
            
            if monhp > 0:
                mondmg = randint(*mon_dmg_range)
                playerhp -= mondmg
                print(f"\nมอนสเตอร์โจมตีคุณ!! คุณได้รับความเสียหาย {mondmg} damage")
                print(f"เลือดคุณเหลือ {playerhp} HP\n")

                if playerhp <= 0:
                    print("คุณตายแล้ว... Game Over")
                    break
            
        else :
            print ("กรุณากรอกเลข 1-5")
    
            
            

           

            
#Laptop
if Weapons == 2 :
    while True:
        i = 1 #รีเซ็ทค่า i
        hit = int(input("ตีกี่ครั้ง ? (สูงสุด 3 ครั้ง) **กดเลข 8 เพื่อออกจากเกม"))
        if hit == 8 :
            break
        if 1 <= hit <= 3 :
            while i <= hit and monhp > 0 :
                damage = randint(*damage_range)
                print(f"Hit ครั้งที่ {i} |", damage , "damage")
                monhp -= damage
                print(monhp)
                print(f"เลือด Slime เหลือ |", monhp , "hp")
                i += 1
                
            if monhp <= 0:
                    print("คุณชนะแล้ว... CONGRATULATIONS!!")
                    break
            
            if monhp > 0:
                mondmg = randint(*mon_dmg_range)
                playerhp -= mondmg
                print(f"\nมอนสเตอร์โจมตีคุณ!! คุณได้รับความเสียหาย {mondmg} damage")
                print(f"เลือดคุณเหลือ {playerhp} HP\n")

                if playerhp <= 0:
                    print("คุณตายแล้ว... Game Over")
                    break
            
        else :
            print ("กรุณากรอกเลข 1-3")

#Excalibur
if Weapons == 3 :
    while True:
        hit = (input(" กด 1 เพื่อโจมตี | กด 2 เพื่อลองวิ่งหนี"))
        if hit == 2 :
            Iamtheflash = randint(*Yourluck)
            if Iamtheflash >= 8 :
                break
        elif hit == 1 :
            continue
        else :
            hit == 3

        if hit == 1 :
            while i <= hit and monhp > 0 :
                damage = randint(*damage_range)
                print(f"Hit ครั้งที่ {i} |", damage , "damage")
                monhp -= damage
                print(monhp)
                print(f"เลือด Slime เหลือ |", monhp , "hp")
                i += 1
       
            if monhp <= 0:
                    print("คุณชนะแล้ว... CONGRATULATIONS!!")
                    break
        if hit == 3 :    
            if monhp > 0:
                mondmg = randint(*mon_dmg_range)
                playerhp -= mondmg
                print(f"\nมอนสเตอร์โจมตีคุณ!! คุณได้รับความเสียหาย {mondmg} damage")
                print(f"เลือดคุณเหลือ {playerhp} HP\n")

                if playerhp <= 0:
                    print("คุณตายแล้ว... Game Over")
                    break
            
        else :
            print ("กรุณากรอกเลข 1 หรือ 2")

elif Exit == True :
    while True :
        Confirmation =  str(input("are you sure to leave? (y/n)"))
        if Confirmation == "y":
            break
        elif Confirmation == "n" :
            Exit == False
        else :
            print ("กรุณากรอกแค่ y กับ n")


    


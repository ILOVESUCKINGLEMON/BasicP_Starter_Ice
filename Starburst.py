from random import randint
import time
import sys
# ตัวแปร
Decision1 = 0
Weapons = 0
max_hit = 0
monhp = 75
i = 1
playerhp = 100
mon_dmg_range = (10, 25)
mondmg = 0
keepfighting = True
hit = 0

# Damage each weapon
damage_range = (0, 0)
damage = 0

# หนีพ้นไหม
Yourluck = (1, 10)
Iamtheflash = 1

# ออกจากเกม
Exit = False
Confirmation = False

# ------------------- First Decision -------------------
print("\n🟣 คุณเดินเข้ามาในป่าลึกลับ...")
time.sleep(2)
print("...ทันใดนั้น สิ่งมีชีวิตลึกลับก็กระเด้งเด้งเข้ามา!!!")
time.sleep(2)
print("\n🧪 พบเจอศัตรู: [ Slime สีม่วงเหนียวหนืด!! ]")
print("📊 HP: 75 | 🎯 ระดับความยาก: Easy\n")
time.sleep(1)

while True and Exit == False :
    print("คุณจะทำอย่างไร ?\n")
    print("⚔️  1. สู้แบบไม่กลัวตาย!")    
    print("🏃  2. หนีตายก่อนละกัน!")
    print("-- กด 3 เพื่อออกจากเกม --")
    try :
        Decision1 = int(input(">> กรุณาเลือก (1,2 หรือ 3): "))
        if Decision1 == 3:
            while True :
                Confirmation = input("แน่ใจหรือไม่ว่าจะออก? (y/n): ").lower()
                if Confirmation in ["y", "yes"]:
                    print("ลาก่อนนักผจญภัย...")
                    Exit = True
                    sys.exit()
                elif Confirmation in ["n", "no"]:
                    print("กลับเข้าสู่เกม!")
                    break
                else:
                    print("กรุณาพิมพ์ 'y หรือ 'n' เท่านั้น")

        if Exit :
            sys.exit()
        elif Decision1 == 2:
            Iamtheflash = randint(*Yourluck)
            if Iamtheflash >= 12:
                print("\n💨 คุณหนีพ้นแล้ว!! กลับบ้านไปกอดหมาได้ ✨")
                Exit == True
                break
            else:
                print("\n🚫 ไม่! Slime พุ่งมาขวางไว้!!")
                time.sleep(2)
                print("คุณไม่มีทางเลือก ต้องสู้เท่านั้น!\n")
                break
        elif Decision1 == 1:
            print("\n🗡️ คุณตัดสินใจสู้กับ Slime อย่างกล้าหาญ!")
            time.sleep(2)
            break
        else:
            print("❗ กรุณาเลือก 1 หรือ 2 เท่านั้น\n")           
    except ValueError :
            print("⚠️ กรุณากรอกตัวเลข 1 หรือ 2 เท่านั้น\n")
    
     
# ------------------- Weapon Selection -------------------
while Exit == False:
        print("\n----- โปรดเลือกอาวุธ -----")
        print("1. ไม้กากๆ          | 3-12 damage | ตีได้ 5 ครั้ง")
        print("2. โน้ตบุ๊คAsus       | 5-9 damage  | ตีได้ 3 ครั้ง")
        print("3. ไม้แขวนเสื้อของแม่  | 2-20 damage | ตีได้ 1 ครั้ง")
        print("4. ออกจากเกม")
        Weapons = int(input("เลือกอาวุธ (1/2/3) หรือออก (4): "))

        if Weapons == 4:
            while True :
                Confirmation = input("แน่ใจหรือไม่ว่าจะออก? (y/n): ").lower()
                if Confirmation in ["y", "yes"]:
                    print("ลาก่อนนักผจญภัย...")
                    exit()
                elif Confirmation in ["n", "no"]:
                    print("กลับเข้าสู่เกม!")
                    break
                else:
                    print("กรุณาพิมพ์ 'y' หรือ 'n' เท่านั้น")
        elif Weapons == 1:
            max_hit = 5
            damage_range = (3, 12)
            break
        elif Weapons == 2:
            max_hit = 3
            damage_range = (5, 9)
            break
        elif Weapons == 3:
            max_hit = 1
            damage_range = (2, 20)
            break
        else:
            print("กรุณาเลือก 1, 2, 3 หรือ 4 เท่านั้น")

# ------------------- Battle -------------------
while monhp > 0 and playerhp > 0 and Exit == False:
    if Weapons in [1, 2]:
        try:
            hit = int(input(f"\nตีกี่ครั้ง? (สูงสุด {max_hit} ครั้ง) **กดเลข 8 เพื่อออกจากเกม: "))
            if hit == 8:
                break
            if not (1 <= hit <= max_hit):
                print(f"กรุณากรอกเลข 1 - {max_hit}")
                continue
        except:
            print("กรอกตัวเลขเท่านั้น")
            continue

        for i in range(1, hit + 1):
            damage = randint(*damage_range)
            print(f"Hit ครั้งที่ {i} | {damage} damage")
            monhp -= damage
            if monhp < 0:
                monhp = 0
            print(f"เลือด Slime เหลือ | {monhp} HP")
            if monhp == 0:
                break

    elif Weapons == 3:
        choice = input("\nกด 1 เพื่อโจมตี | กด 2 เพื่อลองหนี: ")
        if choice == "2":
            Iamtheflash = randint(*Yourluck)
            if Iamtheflash >= 8:
                print("คุณหนีพ้น!!")
                break
            else:
                print("คุณหนีไม่รอด!! สู้ต่อไป...")
        elif choice == "1":
            damage = randint(*damage_range)
            print(f"Hit | {damage} damage")
            monhp -= damage
            if monhp < 0:
                monhp = 0
            print(f"เลือด Slime เหลือ | {monhp} HP")
        else:
            print("กรุณากดแค่ 1 หรือ 2 เท่านั้น")
            continue

    if monhp <= 0:
        print("\nคุณชนะแล้ว... CONGRATULATIONS!! 🎉")
        break

    # Slime โจมตี
    mondmg = randint(*mon_dmg_range)
    playerhp -= mondmg
    if playerhp < 0 :
        playerhp = 0
    print(f"\nมอนสเตอร์โจมตีคุณ!! คุณได้รับความเสียหาย {mondmg} damage")
    print(f"เลือดคุณเหลือ {playerhp} HP\n")

    if playerhp <= 0:
        print("คุณตายแล้ว... Game Over ☠️")
        break

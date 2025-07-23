Decision1 = 0
Weapons = 0
hit = 0

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
    if Weapons == 2 :
        print("ตีกี่ครั้ง ? (สูงสุด 3 ครั้ง)")
    if Weapons == 3 :
        print("ตีกี่ครั้ง ? (สูงสุด 1 ครั้ง)")

else :
    print("NOWHERE TO RUN!!")
    


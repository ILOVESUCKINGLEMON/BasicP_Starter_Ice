x = int(input("ระยะทางกี่กิโล"))
vat = x*(7/100) 
y = 0
if x < 5:
  print("ส่งฟรีจร้า")
elif x >= 5 and x <= 50 :
  y = 10
  print("10 บาท")
elif x >= 51 and x <= 100:
  y = 15
  print("15 บาท")
elif x >= 101 and x <= 300:
  print("25 บาท")
  y = 25
elif x >= 301 and x <= 500:
  print("35 บาท")
  y = 35
else :
  y = 45
  print("45 บาท")
  
print("ระยะทาง =", x, "km")
print("Vat = ", vat, "Bath") 
net = (y+vat)
print("Net =", net, "Bath")

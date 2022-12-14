while 1 == 1:
    
  width = int(input("width_cm"))
  length = int(input("length_cm"))
  height = int(input("height_cm"))
  size = [width, length, height]
  dins = max(size)
  if dins <= 15:
     print("Коробка №1")
  elif 15 < dins < 50:
     print("Коробка №2")
  elif dins > 200:
     print("Упаковка для лыж")
  else:
     print("Коробка №3")
  break
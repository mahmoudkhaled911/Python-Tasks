print("""
Mahmoud Khaled Ewiss Issa
BNS5_AIS2_S2 AI&ML
""")
print("!!!!_______________________________________________________________________!!!!")
name = "Amit_ml@gmail.edu"
Search1 = name.count("@")
print(Search1)
search2 = name.count(".")
print(search2)
if Search1 == 1 and search2 == 1:
    print("Invalid email")
print("!!!!_______________________________________________________________________!!!!")
code1 = name[0:7:1]
print(code1)
print("!!!!_______________________________________________________________________!!!!")
code2 = name[8:13:1]
print(code2)
print("!!!!_______________________________________________________________________!!!!")
search3 = name.endswith((".edu"))
print("Educational" , search3)
print("!!!!_______________________________________________________________________!!!!")
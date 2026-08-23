print("""
Mahmoud Khaled Ewiss Issa
BNS5_AIS2_S2 AI&ML
""")
print("!!!!_______________________________________________________________________!!!!")
def is_prime(num):
    if num < 2:
        return False
    for div in range(2,num):
        if num % div==0:
            return False
    return True
for i in range(2,1000):
    if is_prime(i) and is_prime(i+2):
        print(i,"and",i+2)
print("!!!!_______________________________________________________________________!!!!")
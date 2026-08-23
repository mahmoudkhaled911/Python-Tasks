print("""
Mahmoud Khaled Ewiss Issa
BNS5_AIS2_S2 AI&ML
""")
print("!!!!_______________________________________________________________________!!!!")
def prime_fact(num):
    fact=[]
    div=2
    while num > 1:
        if num % div == 0:
            fact.append(div)
            num=num // div
        else:
            div +=1
    return fact
print(prime_fact(56))
print("!!!!_______________________________________________________________________!!!!")
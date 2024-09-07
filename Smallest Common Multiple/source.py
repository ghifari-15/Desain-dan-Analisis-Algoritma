def kpk(a, b):
    #conditional to determine max value 
    if a > b:
        max_value = a
    else:
        max_value = b

    # iterate untill get that a and b can be divided by to zero 
    while True:
        if(max_value % a == 0) and (max_value % b == 0):
            kpk = max_value
            break
        else:
            max_value += 1
    
    return kpk

def main(): 
    bilangan_1 = int(input("Masukkan bilangan pertama: "))
    bilangan_2 = int(input("Masukkan bilangan pertama: "))
    
    hasil_kpk = kpk(bilangan_1, bilangan_2)

    print(f"KPK dari {bilangan_1} dan {bilangan_2} adalah {hasil_kpk}")

main()
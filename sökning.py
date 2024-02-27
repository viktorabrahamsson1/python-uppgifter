import random


# 1
def hitta_tal():
    list = []
    while len(list) < 20:
        list.append(random.randint(1,100))
    print(list)

    while True: 
        gissning = int(input("gissa på ett tal i listan: "))
        if gissning in list:
            print(f"Talet {gissning} finns på plats {list.index(gissning)}")
            return
        
        if gissning not in list:
            print(f"Talet {gissning} finns inte i listan")


"""hitta_tal()"""

# 3

def gissa():
    random_tal = random.randint(1,99)
    antal_gissningar = 0
    while True:
        antal_gissningar = antal_gissningar + 1
        gissning = int(input("Gissa på ett tal mellan 1-99: "))
        if gissning > random_tal:
            print("För högt")
        elif gissning < random_tal:
            print("För lågt")
        else:
            print(f"Rätt gissat på {antal_gissningar} försök")
            return


"""gissa()"""

# 5


    
def binär_sökning(list):
    low = 0
    high = len(list) - 1

    num = int(input("Mata in ett tal som ska letas upp i listan: "))

    while low <= high:
        print(low,high)
        mid = (low + high) // 2
        mid_num = list[mid]

        if num == mid_num:
            print(f"Talet finns på plats {list.index(num)}")
            return
        
        if num > mid_num:
            low = mid + 1
        else:
            high = mid - 1

    print("Talet finns inte i listan.")
    return

"""binär_sökning([1,2,3,4,5,6,8])"""



def binär_rekrusiv(list,low,high,target):
    if high >= low:
        mid = (low+high) // 2
        mid_num = list[mid]

        if target == mid_num:
            print(f"Talet finns på index {list.index(mid_num)}")
            return

        if target > mid_num:
            return binär_rekrusiv(list,mid + 1,high,target)

        else:
            return binär_rekrusiv(list,low,mid - 1, target)

    else:
        print("Talet finns inte i listan")
        return -1 

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
low = 0
high = len(list) - 1
target = int(input("Mata in ett tal som ska sökas efter i listan: "))

"""binär_rekrusiv(list,low,high,target) """
        



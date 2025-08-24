# ₱ Chips 
piattos = 25
nova = 23
cheezy = 18

# ₱ Softdrinks 
coke = 20
royal = 22
mountainDew = 24 

# ₱ Energy drinks 
monsterWhite = 93
monsterMango = 89
sting = 25

customerName = input("Name: ").strip().capitalize()
print(f"\nHello {customerName}, welkam sa aking sari-sari store.")
response = input("Ano ba ang iyong bibilhin? 'Chips', 'Softdrinks', o 'EnergyDrink'?: ").strip().lower()

if response == "chip" or response == "chips":
    print("\nAreh ang aking listahan ng presyo ng aming chips:")
    print(f"\nPiattos: ₱{piattos} \nNova: ₱{nova} \nCheezy: ₱{cheezy}\n")
    response = input("Alin ba sa tatlong chips ang iyong nagugustuhan?: ").strip().lower()
    
    if response == "piattos":
        quantity = int(input("Ilan ba bibilhin mong piattos? [NUMBER]: "))
        babayaran = quantity * piattos
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    elif response == "nova":
        quantity = int(input("Ilan ba bibilhin mong nova? [NUMBER]: "))
        babayaran = quantity * nova
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
        
    elif response == "cheezy":
        quantity = int(input("Ilan ba bibilhin mong cheezy? [NUMBER]: "))
        babayaran = quantity * cheezy
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    else:
        print("\nTatlong klase lang binebenta namin! Kaya pumili ka lang sa tatlo; kung 'Piattos', 'Nova', o 'Cheezy'")
        
elif response == "softdrink" or response == "softdrinks":
    print("\nAreh ang aking listahan ng presyo ng aming softdrinks:")
    print(f"\nCoke: ₱{coke} \nRoyal: ₱{royal} \nMountainDew: ₱{mountainDew}\n")
    response = input("Alin ba sa tatlong softdrinks ang iyong nagugustuhan?: ").strip().lower()
    
    if response == "coke":
        quantity = int(input("Ilan ba bibilhin mong coke? [NUMBER]: "))
        babayaran = quantity * coke
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    elif response == "royal":
        quantity = int(input("Ilan ba bibilhin mong royal? [NUMBER]: "))
        babayaran = quantity * royal
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
        
    elif response == "mountaindew":
        quantity = int(input("Ilan ba bibilhin mong mountaindew? [NUMBER]: "))
        babayaran = quantity * mountainDew
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    else:
        print("\nTatlong klase lang binebenta namin! Kaya pumili ka lang sa tatlo; kung 'Coke', 'Royal', o 'MountainDew'")

elif response == "energydrink" or response == "energydrinks":
    print("\nAreh ang aking listahan ng presyo ng aming energydrinks:")
    print(f"\nMonsterWhite: ₱{monsterWhite} \nMonsterMango: ₱{monsterMango} \nSting: ₱{sting}\n")
    response = input("Alin ba sa tatlong energydrinks ang iyong nagugustuhan?: ").strip().lower()
    # start
    if response == "monsterwhite":
        quantity = int(input("Ilan ba bibilhin mong monsterwhite? [NUMBER]: "))
        babayaran = quantity * monsterWhite
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    elif response == "monstermango":
        quantity = int(input("Ilan ba bibilhin mong monstermango? [NUMBER]: "))
        babayaran = quantity * monsterMango
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
        
    elif response == "sting":
        quantity = int(input("Ilan ba bibilhin mong sting? [NUMBER]: "))
        babayaran = quantity * sting
        print(f"\nBale, ang nabili mo ay {response}. \nTapos ang babayaran mo ay: ₱{babayaran}")
    
    else:
        print("\nTatlong klase lang binebenta namin! Kaya pumili ka lang sa tatlo; kung 'MonsterWhite', 'MonsterMango', o 'Sting'")
    
else:
    print("\nTatlong klase lang binebenta namin! Kaya pumili ka lang sa tatlo; kung 'Chips', 'Softdrinks', o 'EnergyDrink'")

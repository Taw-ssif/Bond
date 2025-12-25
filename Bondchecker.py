def check_bond():
    while True:
        a = input("Enter bond number to check: ")
        if a == '0':
            break
        elif len(a) != 7:
            print("Bond number must be 7 digits")
            continue
        else:
            with open("Bonds.txt", "r") as f:
                bonds = f.read().splitlines()
                if a in bonds:
                    print("You won this bond!: ", a)

def addBond():
    bond = []
    while True:
        a = input("Bond number(0 to end): ")
        if a == '0':
            break
        elif len(a) != 7:
            print("Bond number must be 7 digits")
            continue
        else:
            bond.append(a)
    with open("Bonds.txt", "a") as f:
        for b in bond:
            f.write(b + "\n")
    return bond

print("Welcome to the Bond Checker")
checker = input("Do you want to (1) Check a bond or (2) Add a bond?: ")
if checker == '1':
    check_bond()
elif checker == '2':
    addBond()

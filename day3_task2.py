target = int(input("Enter target units: "))
worker = int(input("Enter workers per shift: "))
defect = int(input("Enter defect rate (%): "))
total = 0

for shift in range(1,4):
    print("\nShift", shift)
    produced = 0
    defective = 0
    for machine in range(1,21):
        for worker in range(1,worker + 1):
            if total == target:
                break
            num = machine + worker
            if num % 10 < defect:
                defective += 1
                continue
            total +=1
            produced += 1
        if total == target:
            break
        print("Produced =", produced)
        print("Deffective =", defective)
        if total == target:
            print("Target reached")
            break
        print("Total =", total)
              

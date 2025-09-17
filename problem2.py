def hanoi(n, source, helper, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
    else:
        hanoi(n-1, source, target, helper)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n-1, helper, source, target)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            print("Items compared:", [arr[j], arr[j+1]], end=" ")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("➔ swapped", [arr[j], arr[j+1]])
            else:
                print("➔ not swapped")
        print("Iteration #", i+1, arr)
    return arr

#Main
print("Choose a program:")
print("1 - Tower of Hanoi")
print("2 - Bubble Sort")
choice = int(input("Enter choice: "))

if choice == 1:
    n = int(input("Enter number of disks: "))
    hanoi(n, "A", "B", "C")
elif choice == 2:
    values = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input values =", values)
    sorted_values = bubble_sort(values)
    print("Output values =", sorted_values)
else:
    print("Invalid choice")


import math

def square():
    side = float(input("Enter the side length of the square: "))
    perimeter = 4 * side
    area = side ** 2
    print(f"Square Perimeter: {perimeter}, Area: {area}")

def rectangle():
    long_side = float(input("Enter the long side of the rectangle: "))
    short_side = float(input("Enter the short side of the rectangle: "))
    perimeter = 2 * (long_side + short_side)
    area = long_side * short_side
    print(f"Rectangle Perimeter: {perimeter}, Area: {area}")

def circle():
    radius = float(input("Enter the radius of the circle: "))
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    print(f"Circle Perimeter: {perimeter:.2f}, Area: {area:.2f}")

def triangle():
    print("For the triangle, you can enter three side lengths or the base and height.")
    choice = input("1: Three side lengths, 2: Base and height: ")
    if choice == "1":
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))
        perimeter = side1 + side2 + side3
        s = perimeter / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print(f"Triangle Perimeter: {perimeter}, Area: {area:.2f}")
    elif choice == "2":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = (base * height) / 2
        print(f"Triangle Area: {area}")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nWhich shape's perimeter and area do you want to calculate?")
        print("1: Square\n2: Rectangle\n3: Circle\n4: Triangle\n5: Exit")
        choice = input("Make your choice (1-5): ")

        if choice == "1":
            square()
        elif choice == "2":
            rectangle()
        elif choice == "3":
            circle()
        elif choice == "4":
            triangle()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


def main():
    x = float(input("Enter the number of cars: "))
    one: float = 55.5*4 + 20.*4 + 15.3*4 + 10.16*2 + 150. + 40.
    ans: float = x * one
    print(f"The total cost will be: ${ans:.2f}")

if __name__ == "__main__":
    main()
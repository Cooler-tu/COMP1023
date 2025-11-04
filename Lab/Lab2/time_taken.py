def main():
    x = float(input("Enter the number of cars: "))
    cnt = float(8. * 4 + 5.8 * 4 + 5 * 4 + 10.5 * 2 + 20. + 12.7 + 30.)
    ans = float(x*cnt)
    print(f"The total time taken will be: {ans:.2f} second(s)")

if __name__ == "__main__":
    main()
def main():
    """
    Main function to run the point-of-sale program.
    """
    # Task 1: Get product information from user input
    # In this task, you need to define six variables that holds the two products' names, quantities and costs.
    # The values of these variables should be acquired via user input and type conversions.
    # You can assume the input is always valid, i.e. type conversions should not raise an error.
    # The variables should be as follows:
    # `product1_name` (string): The name of the first product.
    # `product1_qty` (integer): The initial quantity of the first product.
    # `product1_cost`  (float): The individual cost of the first product.
    # `product2_name` (string): The name of the second product.
    # `product2_qty` (integer): The initial quantity of the second product.
    # `product2_cost`  (float): The individual cost of the second product.
    # --- TODO below ---
    product1_name = str(input("Enter the name of the first product: "))
    product1_qty = int(input("Enter the initial quantity of the first product: "))
    product1_cost = float(input("Enter the individual cost of the first product: "))
    product2_name = str(input("Enter the name of the second product: "))
    product2_qty = int(input("Enter the initial quantity of the second product: "))
    product2_cost = float(input("Enter the individual cost of the second product: "))

    # --- TODO above ---
    
    # Task 2: Calculate the total cost of one kind of item.
    # For each product, calculate the total cost by multiplying its quantity and cost.
    # --- TODO below ---

    product1_tot = float(product1_cost * product1_qty)
    product2_tot = float(product2_cost * product2_qty)

    # --- TODO above ---

    # Task 3: Calculate the total cost of both items.
    # Calculate the total cost of both products by summing up their individual total costs.
    # --- TODO below ---

    tot = float(product1_tot + product2_tot)

    # --- TODO above ---

    # Task 4: Display the product information and total cost
    # In this task, you are required to output some basic calculated values using the `print()` function.
    # For example, if you have:
    # Name: Apple,  Quantity: 2, Cost: $5
    # Name: Banana, Quantity: 5, Cost: $8
    # Then you should try to write code so that the output is:
    # Number of Apple bought: 2
    # Cost of Apple: $5
    # Number of Banana bought: 5
    # Cost of Banana: $8
    # Total cost: $50
    # --- TODO below ---

    print(f"Number of {product1_name} bought: {product1_qty}")
    print(f"Cost of {product1_name}: ${product1_cost}")
    print(f"Number of {product2_name} bought: {product2_qty}")
    print(f"Cost of {product2_name}: ${product2_cost}")
    print(f"Total cost: ${tot}")

    # --- TODO above ---

if __name__ == "__main__":
    main()

# Stephanie Abdullah
# CIS 103
# September 23, 2025;
# Program calculates the sales tax and total cost


# Formulas:
# Sales tax = product cost multiplies sales tax rate
# Total cost = product cost adds sales tax

# Define our variables from assignment
# User prompts for input data**
salesman_name = input("Enter the name of the salesman: ")
product_cost = int(input("Enter the amount of the product costs: "))
sales_tax_rate = float(input("Enter the sales tax rate: "))

# Formulas to calculate sales tax and total cost
sales_tax = product_cost * sales_tax_rate
total_cost = product_cost + sales_tax

#Display outputs
print(f" The salesman: {salesman_name}")
print(f" The sales tax is: {sales_tax}")
print(f" The total cost is: {total_cost}")

#Alternative Print statements 
#Display outputs 
print("the salesman name is: ", salesman_name)
print(" The sales tax is: ", sales_tax)
print(" The total cost is: ", total_cost)



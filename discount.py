#!/usr/bin/python3

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        print("Sorry no discount offered less that 20% you'll need to pay " + str(round(price)) + ". Apologies for incovencience!!!")
        return price

def main():
    while True:
        flag=False
        try:
            original_price = int(input("Enter the original price: "))
            discount_percentage = int(input("Enter the discount percentage: "))
            print()

            final_price = calculate_discount(original_price, discount_percentage)
            flag = True
            discount = original_price - final_price
            if not final_price == original_price:
                print("Congratulations!!! You've won a discount of " + str(round(discount)) + " So You'll Pay " + str(round(final_price)))
            if flag:
                break

        except ValueError:
            print("Invalid input. Please enter an integer")

if __name__ == '__main__':
    main()

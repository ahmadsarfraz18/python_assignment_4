
def main():
    fruits = {
        'apple': 1.5,
        'grapes': 50,
        'watermelon': 80,
        'kiwi': 1,
        'banana': 1.5,
        'mango': 5,
    }

    total_cost = 0

    for fruit_name, price in fruits.items():
        amount_bought = int(input(f'How many ({fruit_name}) do you want to buy ? '))
        total_cost += price * amount_bought

    print(f'Your total amount is ${total_cost}')
    

if __name__ == "__main__":
    main()








from datetime import datetime

def main():
    print("🍎 Welcome to the Fruit Store! 🛒")

    # Step 1: Choose currency
    currency = input("Enter your currency (USD/PKR): ").strip().upper()
    if currency not in ['USD', 'PKR']:
        print("Invalid currency selected. Defaulting to USD.")
        currency = 'USD'

    # Step 2: Fruit price list
    fruits = {
        'apple': 1.5,
        'grapes': 50,
        'watermelon': 80,
        'kiwi': 1,
        'banana': 1.5,
        'mango': 5,
    }

    total_cost = 0.0
    receipt_lines = []
    
    receipt_lines.append("🧾 Receipt - Fruit Store")
    receipt_lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    receipt_lines.append("-" * 35)

    for fruit_name, price in fruits.items():
        try:
            amount_bought = float(input(f'How many {fruit_name}s do you want to buy? '))
            if amount_bought < 0:
                print("❌ Quantity cannot be negative. Skipping this fruit.")
                continue
        except ValueError:
            print("❌ Invalid input. Skipping this fruit.")
            continue

        cost = price * amount_bought
        total_cost += cost
        receipt_lines.append(f"{fruit_name.title():<12} x {amount_bought:<5} = {cost:.2f} {currency}")

    # Step 3: Apply discount if total > 100
    discount = 0
    if total_cost > 100:
        discount = total_cost * 0.10
        total_cost -= discount
        receipt_lines.append(f"\n🎉 Discount Applied: -{discount:.2f} {currency}")

    receipt_lines.append("-" * 35)
    receipt_lines.append(f"Total Amount: {total_cost:.2f} {currency}")
    receipt_lines.append("🛍️ Thank you for shopping with us!")

    # Step 4: Print final output
    print("\n".join(receipt_lines))

    # Step 5: Save receipt as text file
    with open("fruit_store_receipt.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(receipt_lines))
        print("\n📄 Receipt saved as 'fruit_store_receipt.txt'")

if __name__ == "__main__":
    main()

def calculate_discount():
    while True:
        print("\n--- Shopping Discount Calculator ---")
        try:
            # Take user inputs
            original_amount = float(input("Enter the total shopping bill amount ($): "))
            discount_percentage = float(input("Enter the discount percentage (0-100%): "))

            # Manually trigger a ValueError if inputs are logically invalid
            if original_amount < 0 or discount_percentage < 0:
                raise ValueError("Numbers cannot be negative.")
            if discount_percentage > 100:
                raise ValueError("Discount percentage cannot exceed 100%.")

        except ValueError as e:
            # Catches letters/symbols mixed in inputs OR manual logical errors
            print(f"❌ Input Error: Invalid number entered. ({e})")
            print("Please try again.")

        except ZeroDivisionError:
            # Included for structural demonstration, though rare in this specific math setup
            print("❌ Math Error: Division by zero occurred.")
            print("Please try again.")

        except Exception as e:
            # Catch-all for any other unexpected errors
            print(f"❌ Unexpected Error: {e}")
            print("Please try again.")

        else:
            # Executes ONLY if no exceptions were raised in the try block
            discount_amount = original_amount * (discount_percentage / 100)
            final_bill = original_amount - discount_amount

            print("\n✅ Calculation Successful!")
            print(f"Original Bill: ${original_amount:,.2f}")
            print(f"Discount applied: {discount_percentage}% (-${discount_amount:,.2f})")
            print(f"Final Amount to Pay: ${final_bill:,.2f}")
            
            break  # Exit the loop since valid details were entered

        finally:
            # Executes EVERY time the loop runs, regardless of success or failure
            print("-------------------------------------")

# Run the program
calculate_discount()


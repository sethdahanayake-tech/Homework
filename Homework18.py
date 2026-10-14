import math
import random


def show_menu():
    print("\n" + "=" * 35)
    print("      🎉 RANDOM FUN CALCULATOR 🎉")
    print("=" * 35)
    print("1. 🍀 Get Your Lucky Number")
    print("2. 🎯 Choose a Random Activity")
    print("3. 🎲 Play a Guessing Game")
    print("4. 🔼 Ceil (Round Up)")
    print("5. 🔽 Floor (Round Down)")
    print("6. 📏 Fabs (Absolute Value)")
    print("7. 🤝 GCD (Greatest Common Divisor)")
    print("8. ❌ Exit")
    print("=" * 35)


def fun_calculator():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            # 1. Lucky Number (random integer)
            low = int(input("Enter minimum range: "))
            high = int(input("Enter maximum range: "))
            if low > high:
                low, high = high, low
            lucky_num = random.randint(low, high)
            print(f"\n🔮 Your lucky number in range [{low}, {high}] is: **{lucky_num}**")

        elif choice == "2":
            # 2. Random Activity (random.choice)
            activities = [
                "Go for a 15-minute walk outside 🌿",
                "Learn 5 new words in a foreign language 🗣️",
                "Do 10 push-ups or stretch 🧘",
                "Bake a quick mug cake 🧁",
                "Call a friend you haven't talked to in a while 📱",
                "Read one chapter of a book 📖",
                "Listen to your favorite song and dance 💃"
            ]
            print(f"\n🎯 Your chosen activity is: **{random.choice(activities)}**")

        elif choice == "3":
            # 3. Guessing Game
            secret = random.randint(1, 20)
            print("\n🎲 I'm thinking of a number between 1 and 20. You have 5 attempts!")
            
            for attempt in range(1, 6):
                try:
                    guess = int(input(f"Attempt {attempt}/5 - Enter guess: "))
                    if guess == secret:
                        print(f"🎉 Correct! You guessed it in {attempt} tries.")
                        break
                    elif guess < secret:
                        print("Too low! 👇")
                    else:
                        print("Too high! 👆")
                except ValueError:
                    print("Please enter a valid integer.")
            else:
                print(f"😢 Game over! The number was **{secret}**.")

        elif choice == "4":
            # 4. math.ceil()
            num = float(input("Enter a decimal number to round UP: "))
            print(f"🔼 math.ceil({num}) = **{math.ceil(num)}**")

        elif choice == "5":
            # 5. math.floor()
            num = float(input("Enter a decimal number to round DOWN: "))
            print(f"🔽 math.floor({num}) = **{math.floor(num)}**")

        elif choice == "6":
            # 6. math.fabs()
            num = float(input("Enter a number to find its absolute value: "))
            print(f"📏 math.fabs({num}) = **{math.fabs(num)}**")

        elif choice == "7":
            # 7. math.gcd()
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            print(f"🤝 math.gcd({a}, {b}) = **{math.gcd(a, b)}**")

        elif choice == "8":
            print("\n👋 Thanks for using the Random Fun Calculator! Goodbye!")
            break
        else:
            print("\n❌ Invalid option. Please select a number from 1 to 8.")


# Run the program
if __name__ == "__main__":
    fun_calculator()


python# Ask the primary holiday question
holiday_type = input("What kind of holiday are you looking for? (beach, mountain, city): ").strip().lower()

# Nested if-else statements to determine the itinerary
if holiday_type == "beach":
    activity_level = input("Do you want to relax or be active? (relax, active): ").strip().lower()
    
    if activity_level == "relax":
        print("Your Itinerary: Lounge by the pool with a book, followed by a sunset massage and seaside dinner.")
    elif activity_level == "active":
        print("Your Itinerary: Morning surfing lessons, afternoon snorkeling, and a beach volleyball tournament.")
    else:
        print("Invalid choice! Please choose 'relax' or 'active'.")

elif holiday_type == "mountain":
    weather = input("What weather do you prefer? (snow, sunny): ").strip().lower()
    
    if weather == "snow":
        print("Your Itinerary: All-day skiing, followed by hot chocolate and relaxing in a mountainside spa.")
    elif weather == "sunny":
        print("Your Itinerary: Sunrise hike to the summit, alpine lake kayaking, and stargazing by a campfire.")
    else:
        print("Invalid choice! Please choose 'snow' or 'sunny'.")

elif holiday_type == "city":
    pace = input("Do you prefer culture or nightlife? (culture, nightlife): ").strip().lower()
    
    if pace == "culture":
        print("Your Itinerary: Guided museum tours, architectural walking tour, and a fine dining experience.")
    elif pace == "nightlife":
        print("Your Itinerary: Dinner at a trendy rooftop restaurant, followed by a local pub crawl and live music.")
    else:
        print("Invalid choice! Please choose 'culture' or 'nightlife'.")

else:
    print("Invalid choice! Please pick 'beach', 'mountain', or 'city'.")

    

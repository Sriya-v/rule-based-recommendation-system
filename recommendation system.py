# Rule-Based Personal Recommendation System

print("=== Personal Recommendation System ===")

print("\nChoose your preference:")
print("1. Food Recommendation")
print("2. Movie Recommendation")
print("3. Career Recommendation")
print("4. Book Recommendation")

choice = int(input("\nEnter your choice (1-4): "))

if choice == 1:
    food = input("Enter your food preference (veg/non-veg): ").lower()

    if food == "veg":
        print("Recommended: Dosa, Paneer Curry, Vegetable Biryani")
    elif food == "non-veg":
        print("Recommended: Chicken Curry, Fish Fry, Chicken Biryani")
    else:
        print("Please enter valid preference")

elif choice == 2:
    genre = input("Enter movie genre (action/comedy/romance): ").lower()

    if genre == "action":
        print("Recommended Movies: Avengers, Mission Impossible")
    elif genre == "comedy":
        print("Recommended Movies: The Mask, Home Alone")
    elif genre == "romance":
        print("Recommended Movies: Titanic, The Notebook")
    else:
        print("No recommendation available")

elif choice == 3:
    interest = input("Enter your interest (ai/web/data): ").lower()

    if interest == "ai":
        print("Recommended Career: AI Engineer, ML Engineer")
    elif interest == "web":
        print("Recommended Career: Frontend Developer, Full Stack Developer")
    elif interest == "data":
        print("Recommended Career: Data Analyst, Data Scientist")
    else:
        print("No recommendation available")

elif choice == 4:
    category = input("Enter book category (technology/fiction): ").lower()

    if category == "technology":
        print("Recommended Books: Artificial Intelligence Basics, Python Programming")
    elif category == "fiction":
        print("Recommended Books: Harry Potter, The Alchemist")
    else:
        print("No recommendation available")

else:
    print("Invalid choice")

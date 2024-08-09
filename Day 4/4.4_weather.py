# ---------- WEATHER
print("----- WEATHER -----")

weather = input("Enter the weather: ").lower()

if weather == "sunny":
    print("It's sunny today")
elif weather == "cloudy":
    print("It's cloudy today")
elif weather == "rainy":
    print("It's rainy today")
elif weather == "snowy":
    print("It's snowy today")
else:
    print("Sorry, I don't understand")

# Better solution 1 (if user can write long answer)

if "sunny" in weather:
    print("It's sunny today")
elif "cloudy" in weather:
    print("It's cloudy today")
elif "rainy" in weather:
    print("It's rainy today")
elif "snowy" in weather:
    print("It's snowy today")
else:
    print("Sorry, I don't understand")

# Better solution 2 (if user can write "sunny", "cloudy", "rainy" or "snowy")

weather_variants = {
    "sunny": "It's sunny today",
    "cloudy": "It's cloudy today",
    "rainy": "It's rainy today",
    "snowy": "It's snowy today"
}

print(weather_variants.get(weather, "Sorry, I don't understand"))

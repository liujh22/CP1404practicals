
COLOR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50", "Amber": "#ffbf00",
                 "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                 "Apricot": "#fbceb1", "Aqua": "#00ffff"}

print(COLOR_TO_CODE)

color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(f"{color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid name")
    color_name = input("Enter color name: ").title()

for i in COLOR_TO_CODE:
    print(f"{i:<20} is {COLOR_TO_CODE[i]}")


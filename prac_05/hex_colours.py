COLOR_TO_CODE = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "Asparagus": "#87a96b",
                 "Beaver": "#9f8170",
                 "Beige": "#f5f5dc",
                 }

color_name = input("Enter the color name: ").title()
while color_name != "":
    if color_name not in COLOR_TO_CODE.keys():
        print("Invalid color name")
        color_name = input("Enter the color name: ").title()
    else:
        print(f"The {color_name} corresponds to code {COLOR_TO_CODE[color_name]}.")
    color_name = input("Enter the color name: ").title()

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [name1["name"] for name1 in spicy_foods]
    return names 
    
def get_spiciest_foods(spicy_foods):    
    spiciest =[item for item in spicy_foods if item["heat_level"] > 5]
    return spiciest


def print_spicy_foods(spicy_foods):
    num3 = [(item["name"]) + " " + "("+ item["cuisine"]+ ")" + " | " + "Heat Level:" +" " + item["heat_level"]* "🌶" for item in spicy_foods]
    print(*num3,sep='\n')
 
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    ev = None
    for item in spicy_foods:
        if item["cuisine"]==cuisine:
         ev = item
         break
    return ev
    
def print_spiciest_foods(spicy_foods):
    spiciest2 = [(item["name"]) + " " + "("+ item["cuisine"]+ ")" + " | " + "Heat Level:" +" " + item["heat_level"]* "🌶" for item in spicy_foods if item["heat_level"] >5]
    print (*spiciest2, sep='\n') 
    
    
def get_average_heat_level(spicy_foods):
    pavg = sum([item["heat_level"] for item in spicy_foods])/len(spicy_foods)
    return pavg

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)   
    return spicy_foods
    

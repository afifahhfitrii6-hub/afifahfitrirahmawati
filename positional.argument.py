def create_sorcerer(name, age, race, era): 
    return { 
        "name": name, 
        "age": age, 
        "race": race, 
        "era": era, 
    } 

obj1 = create_sorcerer("Sukuna", 1000, "incarnation", "heian") 
print(obj1) 
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'}
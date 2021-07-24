print (" Mad Libs is starting!")
name = input(str("Enter a name: "))
adj1 = input("Enter an adjective: ")
adj2 = input("Enter a second adjective: ")
adj3 = input("Enter one more adjective: ")

verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a second noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

STORY = f"This morning {name} woke up feeling {adj1}. It is going to be a {adj2} day! Outside, a bunch of {animal}s were protesting to keep {food}s in stores.They began to {verb} to the rhythm of the {noun1}, which made all the {fruit} very {adj3}.Concerned,{name} texted {superhero}, who flew {name} to {country} and dropped {name} in a puddle of frozen {dessert}.{name} woke up in the year {year}, in a world where {noun2}s ruled the world."

print (STORY)
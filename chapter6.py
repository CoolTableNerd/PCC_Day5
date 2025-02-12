"""
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.

"""

favoritePlayer = {
    'Name': 'Kobe Bryant',
    'Jersey Number': 24,
    'Team': 'Los Angeles'
}

print(f"Name: {favoritePlayer['Name']}")
print(f"Age: {favoritePlayer['Jersey Number']}")
print(f"City: {favoritePlayer['Team']}\n")

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

"""

favoriteNumbers = {
    'Daryl Corbin': 4, 
    'Kobe Bryant': 8,
    'Jim Halpert': 12, 
    'Stone Cold': 316,
}

print(f"Name: Daryl Corbin\t Number: {favoriteNumbers['Daryl Corbin']}")
print(f"Name: Kobe Bryant\t Number: {favoriteNumbers['Kobe Bryant']}")
print(f"Name: Jim Halpert\t Number: {favoriteNumbers['Jim Halpert']}")
print(f"Name: Stone Cold\t Number: {favoriteNumbers['Stone Cold']}\n")

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

"""

definitions = {
    'happy': 'feeling or showing pleasure', 
    'sad': 'feeling or showing sorrow', 
    'angry': 'feeling or showing strong annoyance',
    'proud': 'having or showing high opinion of oneself or someone else'
}

print(f"Happy: {definitions['happy']}\n")
print(f"Sad: {definitions['sad']}\n")
print(f"Angry: {definitions['angry']}\n")
print(f"Proud: {definitions['proud']}\n")

"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

"""

definitions = {
    'happy': 'feeling or showing pleasure', 
    'sad': 'feeling or showing sorrow', 
    'angry': 'feeling or showing strong annoyance',
    'proud': 'having or showing high opinion of oneself or someone else'
}

for key, value in definitions.items(): 
    print(f"{key}: {value}\n")

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.

"""

rivers = {
    'Nile River': 'Egypt', 
    'Amazon River': 'South America', 
    'Mississippi River': 'United States'
}

# print sentence about each river 
for river, location in rivers.items():
    print(f"the {river} runs through {location}")

print("\n")

# print the name of each river 
print("Name of river:")
for name in rivers.keys():
    print(name)

print("\n")

# print the name of each country
print("Name of country:")
for location in rivers.values():
    print(location.title())

print("\n")

"""
6-6. Polling: Use the code in favorite_languages.py.
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

"""

favorite_languages = {
    'Steve Jobs': 'C++', 
    'Mark Zuck': 'C++',
    'Daryl Corbin': 'Python',
    'Sarah': 'Javascript',
    'Edward': 'Rust', 
    'Ben': 'Python',
}

takePoll = ["Dwight","Sarah","Kelly", "Pam", "Andy","Edward"]

for name in takePoll:
    if name not in favorite_languages:
        print(f"Hi, {name}! you need to take the poll.\n")
    else:
        print(f"thank you for taking poll, {name}\n")

"""
6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionar- ies in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person

"""
favoritePlayer = {
    'Name': 'Kobe Bryant',
    'Jersey Number': 24,
    'Team': 'Los Angeles'
}

favoriteActor = {
    'Name': 'Leonardo Decaprio',
    'Best Movies': 'Inception',
    'Birth Place': 'Los Angeles, CA'
}

favoriteArtist = {
    'Name': 'Kanye West',
    'Best Album': 'My Dark Twisted Fantasy',
    'Birth Place': 'Chicago, IL'
}

people = [favoritePlayer,favoriteActor,favoriteArtist]

for person in people:
    print(person)

print("\n")

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a differ- ent pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

"""

pets = []

pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")


print("\n")

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

"""

favorite_places = {
    'Andy Benard': ['Cornell', 'Scanton'],
    'Michael Scott': ['New York', 'Colorado'],
    'Dwight Schute': ['Beat Farm', 'The Office']
}

for name, locations in favorite_places.items():
    print(f"{name}'s favorite places are: ")
    for location in locations: 
        print(f"- {location}")

print("\n")

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.

"""

favoriteNumbers2 = {
    'Daryl Corbin': [4,28], 
    'Kobe Bryant': [8,24],
    'Michael Jordan':[23,45], 
    'Stone Cold': [3,16]
}

for name, numbers in favoriteNumbers2.items():
    print(f"{name}'s favorite numbers:")
    for number in numbers:
        print(f"#{number}")


print("\n")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the infor- mation you have stored about it.

"""

cities = {
    'New Brunswick': {
        'Country': 'Unites States',
        'Population': 55846,
        'Fun Fact': 'headquarters of Johnson & Johnson'
    }, 

    'Los Angeles': {
        'Country': 'United States', 
        'Population': 3821000,
        'Fun Fact': 'Los Angeles was part of Mexico for 27 years'
    }, 

    'London': {
        'Country': 'England',
        'Population': 88660000,
        'Fun Fact': 'London is the smallest country in England.'
    }
}

for city,cityInfo in cities.items():
    country = cityInfo['Country'].title()
    population = cityInfo['Population']
    funFact = cityInfo['Fun Fact']

    print(f"{city} is located in {country}")
    print(f"the population in {city} is {population:,}")
    print(f"a fun fact about {city} is {funFact}")

    print("\n")


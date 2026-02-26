# DICTIONARY AND SET (BUILT-IN-DATA TYPE IN PYTHON)
# DICTIONARY
            # It is store to data value in pair like KEY:VALUE

info = {
    "Name": "Mohammad Asif",
    "Roll no": 40,
    "Branch": "Information Technology",
    "subjects": {
        "English": 99,
        "Hindi" : 100,
        "Physics": 98,
        "Chemisty": 97
    }
}
# print(info)
# print(info["Name"]) # indexing ki jagah aise likh skte value ko access krne ke liye 

# Dictionay methods( like function)

# print(info.values()) # dictionary ki sari values o/p ho jaygi 
# print(info.keys())
# print(len(list(info.keys())))

# info.update({"City": "Akbarpur"}) #use curly braces to insert new key:value with .update() method
# print(info)


# SETS : COLLECTION OF UNORDERED ITEMS. ITEMS MUST BE UNIQUE AND IMMUTABLE SO LIST AND DICT IS NOT ACCEPTABLE IN SET

sets = { 1, 4, 2, 5, 2}
print(sets)
print(type(sets))
print(sets)
print(len((sets)))

asif = set() # syntax for empty set in python 
print(asif)
print(type(asif))

asif = {}  # Empty dictionary syntax
print(asif)
print(type((asif)))


empty_set = set()
empty_set.add(16)
empty_set.add(19)
empty_set.add(11)
empty_set.add(13)
empty_set.add(15)
empty_set.add(12)
print(empty_set)

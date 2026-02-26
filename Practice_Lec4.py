# FIGURE OUT A WAY TO STORE 9 AND 9.0 AS SEPARATE VALUES IN SET

# val = { 9, 9.0} # we can take help of the built-in data type
# val = set()
# val.update("9")
# val.update(("9.0"))
# print(val)


value = {
    ("float", 9.0), ("int", 9)
}

print(value)
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])
# y = 4*x 
# z = -4*x 


# plt.plot(x, y)
# plt.plot(x, z)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # x = np.array(["A", "B", "C", "D"])

# x = np.array([12, 170, 45])
# # y = np.array([1, 2, 3, 4])

# # plt.bar(x, y)
# # plt.show()
# plt.hist(x)
# plt.show()




# import matplotlib.pyplot as plt

# languages = [ "Python ", "Java ", "C++", "JavaScript","Ruby"]
# popularity = [ 30, 25, 20, 15, 10]


# plt.pie(popularity , labels = languages, autopct = '%1.1f%%', startangle=90)

# plt.title("Popularity of the programming languages")

# plt.show()


# import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

Food = [ "Meat ", "Banana ", "Avocados", "Sweet Potatoes","Spinach","Watermelon", "Coconut water","Beans", "Legumes", "Tomato"]
Calories = [ 250, 130, 140, 120, 20 , 20, 10, 50, 40 , 19]
Potassium = [ 40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
Fat = [ 8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

# construct plot 

plt.plot(Food, Calories , label = "Calories")

plt.plot(Food, Potassium, label = "Potassium ")
plt.plot(Food, Fat , label = " Fat")

plt.xlabel("Food")
plt.ylabel("Values/Data/Number")

plt.title("Food data plot")

plt.legend()
plt.show()




# import matplotlib.pyplot as plt

# Food = ["Meat", "Banana", "Avocados", "Sweet Potatoes",
#         "Spinach", "Watermelon", "Coconut water",
#         "Beans", "Legumes", "Tomato"]

# Calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]

# Potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]

# Fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

# # Construct plot

# plt.plot(Food, Calories, label="Calories")
# plt.plot(Food, Potassium, label="Potassium")
# plt.plot(Food, Fat, label="Fat")

# plt.xlabel("Food")
# plt.ylabel("Values")

# plt.title("Food Data Plot")

# plt.legend()

# plt.show()
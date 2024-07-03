
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Food': ['Apple', 'Banana', 'Orange', 'Broccoli', 'Carrot', 'Chicken_Breast', 'Salmon', 'Eggs', 
             'Almonds', 'Milk', 'Bread', 'Cheese', 'Peanut_Butter', 'Yogurt', 'Avocado', 'Beef', 
             'Tofu', 'Pasta'],
    'Calories': [95, 105, 62, 55, 25, 165, 206, 78, 164, 149, 79, 113, 188, 59, 160, 250, 76, 131],
    'Proteins': [0.5, 1.3, 1.2, 3.7, 0.6, 31, 22, 6, 6, 8, 3, 7, 8, 10, 2, 26, 8, 5],
    'Fat': [0.3, 0.4, 0.2, 0.6, 0.1, 3.6, 13, 5, 14, 8, 1, 9, 16, 0.4, 15, 15, 4, 1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 12))

sns.scatterplot(data=df, x="Calories", y="Proteins", size="Fat", sizes=(20, 500),
                hue="Fat", palette=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c4e17f", "#76D7C4", "#E59866", "#AF7AC5", "#F7DC6F"])

plt.title("Food & Nutrition: Calories, Proteins, and Fat", fontsize=18)
plt.xlabel("Calories", fontsize=14)
plt.ylabel("Proteins (g)", fontsize=14)

plt.legend(title="Fat (g)", loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Food Item': ["Apple", "Banana", "Orange", "Broccoli", "Carrot", "Almonds", "Chicken Breast", 
                  "Salmon", "Avocado", "Egg", "Oatmeal", "Sweet Potato", "Spinach", "Blueberries",
                  "Greek Yogurt", "Quinoa", "Dark Chocolate", "Tofu", "Lentils", "Peanut Butter"],
    'Calories': [95, 105, 62, 55, 25, 160, 165, 233, 234, 78, 154, 103, 23, 84, 100, 222, 170, 76, 230, 188]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(18, 12))
colors = ["#3498db", "#e74c3c", "#f39c12", "#2ecc71", "#9b59b6", "#34495e", "#e67e22", "#1abc9c", "#8e44ad", "#2c3e50", "#d35400", "#16a085", "#7f8c8d", "#2980b9", "#c0392b", "#27ae60", "#e84393", "#fdcb6e", "#00b894", "#6c5ce7"]
squarify.plot(sizes=df['Calories'], label=df['Food Item'], alpha=0.8, color=colors)
plt.title('Calorie Content in Common Foods', fontsize=20, pad=25)
plt.axis('off')
plt.show()
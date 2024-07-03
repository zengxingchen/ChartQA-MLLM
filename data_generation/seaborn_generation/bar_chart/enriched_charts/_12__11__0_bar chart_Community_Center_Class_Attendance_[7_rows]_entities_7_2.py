
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age_Group': ['Under 18', '18-25', '26-35', '36-45', '46-55', '56-65', '65 and over'],
    'Average_Daily_Fruit_Consumption': [2.5, 3, 3.5, 4, 3.8, 3.2, 3]
}

df = pd.DataFrame(data)

colors = ["#2E8B57", "#4682B4", "#FF6347", "#FFD700", "#6A5ACD", "#FF4500", "#8B008B"]

plt.figure(figsize=(14, 8))

barplot = sns.barplot(
    y='Age_Group',
    x='Average_Daily_Fruit_Consumption',
    data=df,
    palette=colors
)

for bar in barplot.patches:
    bar.set_height(0.4)

plt.title('Average Daily Fruit Consumption by Age Group', fontsize=16)
plt.xlabel('Average Daily Fruit Consumption (Servings)', fontsize=14)
plt.ylabel('Age Group', fontsize=14)

plt.tight_layout()
plt.show()
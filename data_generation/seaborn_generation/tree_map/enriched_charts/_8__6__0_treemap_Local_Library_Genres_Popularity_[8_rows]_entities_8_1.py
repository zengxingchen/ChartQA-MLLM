
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

data = {
    'Category': ['Cardio Workouts', 'Strength Training', 'Yoga', 'Pilates', 'Cycling', 'Swimming', 'Running',
                 'Hiking', 'CrossFit', 'Dance', 'Martial Arts', 'HIIT', 'Rowing', 'Boxing', 'Stretching'],
    'Value': [100, 75, 50, 40, 60, 45, 70, 30, 55, 35, 25, 65, 20, 15, 10]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20, 12))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#FF8C33", "#33FF8C",
          "#FF5733", "#A833FF", "#33FFDA", "#5733FF", "#FF8E33", "#33FFC1",
          "#57FF33", "#FF33D4", "#33FF57"]

squarify.plot(sizes=df['Value'], label=df['Category'], color=colors, alpha=0.7)
plt.title('Distribution of Popular Fitness Activities', fontsize=24)
plt.axis('off')
plt.show()
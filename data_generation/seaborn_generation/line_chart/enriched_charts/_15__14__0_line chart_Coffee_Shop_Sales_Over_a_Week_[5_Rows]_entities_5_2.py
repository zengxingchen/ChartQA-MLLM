
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Distance": [5.2, 6.3, 4.8, 7.1, 5.9, 6.5, 7.3]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(10, 6)) # Changed width & height
sns.lineplot(x="Day", y="Distance", data=df, marker='o', color="#FF6347") # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Distance[i] + 0.2, f"{df.Distance[i]} km", horizontalalignment='center')

# Set the title
plt.title("Weekly Running Distance", pad=20)

plt.show()
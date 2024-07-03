
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Exercise_Hours": [1.5, 2.0, 1.0, 2.5, 3.0, 2.0, 1.8]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(10, 6))  # Changed width & height
sns.lineplot(x="Day", y="Exercise_Hours", data=df, marker='o', color="#1E90FF")  # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Exercise_Hours[i] + 0.1, f"{df.Exercise_Hours[i]}h", horizontalalignment='center')

# Set the title
plt.title("Weekly Hours of Exercise Over One Week", pad=20)

plt.show()
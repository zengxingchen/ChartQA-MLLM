
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Temperature_Celsius": [22.5, 23.0, 19.5, 20.0, 21.5, 24.0, 25.5]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 8))  # Changed width & height
sns.lineplot(x="Day", y="Temperature_Celsius", data=df, marker='o', color="#FF6347")  # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Temperature_Celsius[i] + 0.2, f"{df.Temperature_Celsius[i]}°C", horizontalalignment='center')

# Set the title
plt.title("Average Daily Temperature Over a Week", pad=20)

plt.show()
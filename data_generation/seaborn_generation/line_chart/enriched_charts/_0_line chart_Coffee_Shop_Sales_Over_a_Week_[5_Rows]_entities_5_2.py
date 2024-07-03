
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Temperature": [20, 19, 17, 15, 14, 16, 18]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(10, 6)) # Changed width & height
sns.lineplot(x="Day", y="Temperature", data=df, marker='o', color="#2F4F4F") # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Temperature[i] + 0.2, f"{df.Temperature[i]}°C", horizontalalignment='center')

# Set the title
plt.title("Average Daily Temperature Over One Week")

plt.show()
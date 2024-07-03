
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Calories_Burned": [250, 300, 280, 320, 310, 350, 330]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 8)) # Changed width & height
sns.lineplot(x="Day", y="Calories_Burned", data=df, marker='o', color="#FF6347") # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Calories_Burned[i] + 5, f"{df.Calories_Burned[i]} cal", horizontalalignment='center')

# Set the title
plt.title("Calories Burned Throughout the Week", fontsize=16, pad=20)

plt.show()
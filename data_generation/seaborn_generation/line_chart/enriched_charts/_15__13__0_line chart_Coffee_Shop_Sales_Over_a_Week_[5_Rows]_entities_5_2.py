
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Water_Intake": [2.0, 2.5, 1.8, 2.2, 2.8, 3.0, 2.6]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(14, 8))  # Changed width & height
sns.lineplot(x="Day", y="Water_Intake", data=df, marker='o', color="#1f77b4")  # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Water_Intake[i] + 0.1, f"{df.Water_Intake[i]}L", horizontalalignment='center')

# Set the title
plt.title("Daily Water Intake Over One Week", pad=20)

plt.show()
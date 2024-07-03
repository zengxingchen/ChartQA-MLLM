
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Stock_Price": [150, 155, 160, 158, 162, 165, 170]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 7))  # Changed width & height
sns.lineplot(x="Day", y="Stock_Price", data=df, marker='o', color="#FF5733")  # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Stock_Price[i] + 0.5, f"${df.Stock_Price[i]}", horizontalalignment='center')

# Set the title
plt.title("Weekly Stock Prices Over One Week", pad=20)

plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Amount_Spent': [120, 150, 100, 90, 130, 140, 110, 160, 170, 180, 150, 200, 130, 140, 190, 170, 160, 150, 140, 130, 120, 110, 150, 180, 170, 160, 150, 140, 130, 160, 170]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 7))
plt.fill_between(df['Month'], df['Amount_Spent'], color='#FFA07A', alpha=0.7)
plt.plot(df['Month'], df['Amount_Spent'], color='#FF4500')

# Annotations
for i in range(len(df)):
    plt.text(df['Month'][i], df['Amount_Spent'][i] + 5, str(df['Amount_Spent'][i]), ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Monthly Expenditure on Fashion Items', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Amount Spent ($)', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data in a pandas DataFrame
data = pd.DataFrame({
    'Entertainment_Spending': [120, 300, 450, 620, 700, 890, 950, 1020, 1150, 1230, 1340, 1500, 1580, 1650, 1780, 1890, 
                               2000, 2120, 2250, 2340, 2500, 2600, 2720, 2850, 2900, 3050, 3180, 3300, 3450, 3580, 3700, 
                               3890, 4000, 4120, 4250, 4390, 4500, 4650, 4800, 4900, 5020, 5150, 5300, 5450, 5600, 5720, 
                               5850, 6000, 6120, 6250, 6400, 6550, 6700, 6850, 7000, 7150, 7300, 7450, 7600, 7750, 7900, 
                               8050, 8200, 8350, 8500, 8650, 8800, 8950, 9100, 9250, 9400, 9550, 9700, 9850, 10000]
})

# Set the size of the seaborn plot
plt.figure(figsize=(10, 14))

# Plot a horizontal histogram with specified bin height and color
sns.histplot(data, x='Entertainment_Spending', binwidth=700, color="#3498DB")

# Set chart title and labels
plt.title('Monthly Entertainment Spending Distribution')
plt.ylabel('Count')
plt.xlabel('Entertainment Spending ($)')

# Show the plot
plt.show()
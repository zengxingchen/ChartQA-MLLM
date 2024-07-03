
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000],
    'Profit': [5000, 4800, 5100, 5200, 5300, 5500, 5400, 5600, 5700, 5800, 5900, 6000]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Revenue', y='Profit', data=df,
                palette=['#1f77b4', '#ff7f0e'])

plt.title('Monthly Revenue vs. Profit', fontsize=20, pad=20, loc='left')
plt.xlabel('Revenue ($)', fontsize=16)
plt.ylabel('Profit ($)', fontsize=16)

# Display the plot
plt.show()
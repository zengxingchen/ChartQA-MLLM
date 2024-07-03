
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stock_Price': [150, 155, 160, 162, 158, 165, 170, 172, 168, 175, 180, 185],
    'Trading_Volume': [50000, 52000, 48000, 51000, 47000, 49000, 53000, 55000, 50000, 52000, 54000, 56000]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(16, 12))
sns.scatterplot(x='Stock_Price', y='Trading_Volume', data=df,
                palette=['#1f77b4', '#ff7f0e'])

plt.title('Monthly Stock Prices vs Trading Volume', fontsize=18, pad=20)
plt.xlabel('Stock Price ($)', fontsize=16)
plt.ylabel('Trading Volume', fontsize=16)

# Display the plot
plt.show()
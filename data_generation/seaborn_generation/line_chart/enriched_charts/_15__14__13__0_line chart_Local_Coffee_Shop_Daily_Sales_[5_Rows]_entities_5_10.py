
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "AverageStockPrice": [150.2, 155.8, 160.5, 162.3, 168.4, 172.9, 170.6, 169.8, 165.3, 160.1, 158.7, 157.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(14, 7))
sns.lineplot(x="Month", y="AverageStockPrice", data=df, marker='o', color='#2A9D8F')

# Annotate each point with the stock price value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['AverageStockPrice'][i] + 0.5, s=f"{df['AverageStockPrice'][i]} USD", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Stock Prices in a Financial Year', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Average Stock Price (USD)')

# Show the plot
plt.show()
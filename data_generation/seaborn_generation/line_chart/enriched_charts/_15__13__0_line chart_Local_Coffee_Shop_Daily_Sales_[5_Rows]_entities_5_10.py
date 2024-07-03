
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "StockPrice": [135.4, 128.7, 140.2, 145.0, 152.6, 158.8, 162.3, 155.7, 149.0, 154.6, 159.3, 164.1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(16, 8))
sns.lineplot(x="Month", y="StockPrice", data=df, marker='o', color='#2ca02c')

# Annotate each point with the stock price value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['StockPrice'][i] + 2, s=f"${df['StockPrice'][i]}", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Stock Price of XYZ Corporation', fontsize=18)
plt.xlabel('Month')
plt.ylabel('Stock Price (USD)')

# Show the plot
plt.show()
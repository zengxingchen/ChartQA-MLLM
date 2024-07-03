
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate a DataFrame with the data
data = {
    'Month': [i for i in range(1, 53)],
    'Average_Stock_Price': [
        50, 52, 55, 60, 58, 65, 70, 68, 75, 80, 78, 85, 90, 92, 95, 100, 98, 105, 
        110, 108, 115, 120, 118, 125, 130, 135, 140, 145, 150, 155, 160, 165, 
        170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 
        240, 245, 250, 255, 260, 265
    ]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create and size the seaborn lineplot
plt.figure(figsize=(14, 7))
plot = sns.lineplot(x='Month', y='Average_Stock_Price', data=df, linewidth=2.5, color="#1f77b4")

# Annotate a specific point with a peak price
plt.annotate('Peak price', 
             xy=(52, df.loc[51, 'Average_Stock_Price']), 
             xycoords='data',
             xytext=(40, 280),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

# Annotate a specific point with a notable dip
plt.annotate('Notable dip', 
             xy=(5, df.loc[4, 'Average_Stock_Price']), 
             xycoords='data',
             xytext=(15, 30),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

# Set the title and labels
plt.title('Monthly Average Stock Price of XYZ Corp.')
plt.xlabel('Month')
plt.ylabel('Average Stock Price (USD)')

# Show the plot
plt.show()
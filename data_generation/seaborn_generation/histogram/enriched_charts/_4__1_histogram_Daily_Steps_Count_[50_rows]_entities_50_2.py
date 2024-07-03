
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame with daily stock prices
data = {
    'Price': [
        150.5, 152.2, 147.8, 149.1, 153.4, 148.9, 151.2, 155.4, 157.6, 149.0,
        151.9, 152.5, 158.7, 154.3, 150.1, 151.7, 156.8, 149.2, 150.3, 154.5,
        159.1, 152.3, 150.4, 148.7, 153.6, 155.8, 149.5, 150.7, 152.1, 157.2
    ]
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Set the figure size for better clarity
plt.figure(figsize=(12, 8))

# Plotting the histogram using seaborn
sns.histplot(df['Price'], 
             bins=20, 
             kde=False, 
             color='#33FF57', 
             binwidth=2,
             orientation='horizontal'
            )

# Set the title and labels for the chart
plt.title('Histogram of Daily Stock Prices Over a Month', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Stock Price ($)', fontsize=14)

# Show the plot
plt.show()
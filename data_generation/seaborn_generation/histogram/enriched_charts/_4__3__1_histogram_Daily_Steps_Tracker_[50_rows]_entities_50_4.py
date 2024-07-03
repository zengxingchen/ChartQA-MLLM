
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for the price of gadgets
data = {
    'Price': [
        100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create the histogram
sns.histplot(data=df, y='Price', bins=8, color='#4682b4', binwidth=50)

# Customizing the plot's aesthetics
plt.title('Histogram of Gadget Prices', loc='left')
plt.xlabel('Number of Gadgets')
plt.ylabel('Price in USD')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stock Price': [100, 105, 98, 110, 115, 120, 125, 130, 135, 140, 145, 150]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
plt.fill_between(df['Month'], df['Stock Price'], color='#1f77b4', alpha=0.6)
plt.plot(df['Month'], df['Stock Price'], color='#ff7f0e', linewidth=2)

# Annotations
plt.annotate('Highest Price', xy=('December', 150), xytext=('October', 160),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Lowest Price', xy=('March', 98), xytext=('January', 70),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Stock Prices in 2023', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Stock Price (USD)', fontsize=14)

# Show plot
plt.show()
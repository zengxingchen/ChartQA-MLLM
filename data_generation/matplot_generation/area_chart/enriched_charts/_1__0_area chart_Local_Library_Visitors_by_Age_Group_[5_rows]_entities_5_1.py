
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [1500, 1800, 2100, 2500, 2400, 2200, 2600, 2800, 3000, 3200, 3400, 3600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
plt.fill_between(df['Month'], df['Sales'], color='#1f77b4', alpha=0.6)
plt.plot(df['Month'], df['Sales'], color='#1f77b4', linewidth=2)

# Annotations
plt.annotate('Highest Sales', xy=('December', 3600), xytext=('October', 3700),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Lowest Sales', xy=('January', 1500), xytext=('March', 1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Sales Data', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales ($)', fontsize=14)

# Show plot
plt.show()
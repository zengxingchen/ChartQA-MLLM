
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Subscribers': [1200, 1300, 1400, 1450, 1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(df['Month'], df['Subscribers'], color='#ff7f0e', alpha=0.7)
plt.plot(df['Month'], df['Subscribers'], color='#ff7f0e', linewidth=2)

# Annotations
plt.annotate('Peak Subscribers', xy=('December', 1950), xytext=('October', 2100),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Start of Growth', xy=('January', 1200), xytext=('March', 1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Subscribers Growth in Tech Magazine', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Subscribers', fontsize=14)

# Show plot
plt.show()
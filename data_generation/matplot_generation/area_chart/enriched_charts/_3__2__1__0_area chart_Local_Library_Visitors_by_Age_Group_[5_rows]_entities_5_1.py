
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [3000, 3200, 3500, 3600, 3900, 4200, 4500, 4700, 4900, 5100, 5300, 5500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
plt.fill_between(df['Month'], df['Visitors'], color='#00BFFF', alpha=0.6)
plt.plot(df['Month'], df['Visitors'], color='#0000FF', linewidth=2)

# Annotations
plt.annotate('Highest Visitors', xy=('December', 5500), xytext=('October', 5800),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Lowest Visitors', xy=('January', 3000), xytext=('March', 2700),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Museum Visitors in 2023', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Show plot
plt.show()
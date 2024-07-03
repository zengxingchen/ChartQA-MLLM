
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [3000, 3200, 4000, 3700, 4500, 4700, 5200, 5400, 5000, 4800, 5100, 5500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(df['Month'], df['Visitors'], color='#ff5733', alpha=0.6)
plt.plot(df['Month'], df['Visitors'], color='#c70039', linewidth=2)

# Annotations
plt.annotate('Peak Season', xy=('December', 5500), xytext=('October', 6000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Low Season', xy=('January', 3000), xytext=('March', 2000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Visitor Statistics', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Number of Visitors', fontsize=16)

# Show plot
plt.show()
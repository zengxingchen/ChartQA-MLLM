
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Travelers': [3500, 4000, 4500, 4800, 5000, 5200, 5500, 5800, 6000, 6200, 6400, 6600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(df['Month'], df['Travelers'], color='#FF5733', alpha=0.6)
plt.plot(df['Month'], df['Travelers'], color='#C70039', linewidth=2)

# Annotations
plt.annotate('Peak Season', xy=('December', 6600), xytext=('October', 6800),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Low Season', xy=('January', 3500), xytext=('March', 3000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Titles and labels
plt.title('Monthly Travelers Data in 2023', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Travelers', fontsize=14)

# Show plot
plt.show()
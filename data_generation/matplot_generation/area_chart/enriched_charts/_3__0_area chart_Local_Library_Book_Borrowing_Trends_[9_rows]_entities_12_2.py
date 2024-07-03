
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Rainfall': [78, 56, 89, 110, 130, 150, 170, 160, 140, 100, 85, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Plotting
plt.figure(figsize=(14, 7))
plt.fill_between(df.Month, df.Rainfall, color='#6495ED', alpha=0.6)
plt.plot(df.Month, df.Rainfall, color='#4169E1', lw=2)

# Adding annotation
for line in range(0, df.shape[0]):
     plt.text(df.Month[line], df.Rainfall[line], df.Rainfall[line], 
              horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
plt.title('Monthly Rainfall in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Rainfall (mm)', fontsize=14)
plt.ylim(0, 200)

# Show final result
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
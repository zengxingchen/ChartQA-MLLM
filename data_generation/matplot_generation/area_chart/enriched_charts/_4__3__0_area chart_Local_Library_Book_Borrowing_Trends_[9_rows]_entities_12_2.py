
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Arrivals': [1500, 1800, 2200, 2500, 2800, 3200, 3500, 3400, 3000, 2700, 2300, 1900]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Plotting
plt.figure(figsize=(16, 8))
plt.fill_between(df.Month, df.Arrivals, color='#FFA07A', alpha=0.6)
plt.plot(df.Month, df.Arrivals, color='#FF4500', lw=2)

# Adding annotation
for line in range(0, df.shape[0]):
    plt.text(df.Month[line], df.Arrivals[line], df.Arrivals[line], 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
plt.title('Monthly Tourist Arrivals in City ABC', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Tourist Arrivals', fontsize=14)
plt.ylim(0, 4000)

# Show final result
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 7, 10, 14, 18, 22, 24, 23, 20, 15, 10, 6]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Temperature', sort=False, lw=1)
plt.fill_between(df.Month, df.Temperature, color="#89CFF0")

# Assign annotation
plt.text(df.Month[df.Temperature.idxmax()], df.Temperature.max(), 'Highest\nTemp', horizontalalignment='center', verticalalignment='bottom', fontsize=10, color='black')

# Customize the plot with title, labels and limit
plt.title('Average Monthly Temperatures in City XYZ', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
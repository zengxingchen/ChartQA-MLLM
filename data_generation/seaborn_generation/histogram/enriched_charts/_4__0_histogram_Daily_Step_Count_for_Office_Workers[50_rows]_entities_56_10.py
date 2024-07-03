
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data points for daily temperature over 30 days
data = {
    'Day': [day for day in range(1, 31)], 
    'Temperature': [68, 72, 65, 70, 74, 78, 81, 76, 79, 83, 
                    85, 69, 75, 77, 80, 82, 88, 90, 84, 86, 
                    87, 73, 71, 74, 78, 81, 83, 85, 80, 79]
}

# Transform data into a Pandas DataFrame
df = pd.DataFrame(data)

# Create a Seaborn histogram, adjust visual elements and figure size
plt.figure(figsize=(10, 8))
sns.histplot(data=df, x='Temperature', bins=15, color="#FF5733", kde=False, edgecolor='black', linewidth=1.2)

plt.title('Histogram of Daily Temperature Variations (n=30)', fontsize=18, pad=20)
plt.xlabel('Temperature (°F)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.show()
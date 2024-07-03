
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Constructing dataframe from given data
data = {
    'calories': [
        2000, 2200, 1800, 2400, 2600, 2500, 2300, 2700, 2800, 3000,
        2900, 3100, 3200, 3400, 3500, 3300, 3700, 3600, 3800, 4000,
        3900, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 5000,
        4900, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000,
        6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000,
        7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000,
        8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000,
        9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000,
        10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000,
        11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000
    ]
}

df = pd.DataFrame(data)

# Set the style of seaborn
sns.set(style="whitegrid")

# Enlarging the plot
plt.figure(figsize=(12, 8))

# Creating the histogram with modifications
sns.histplot(data=df, y='calories', color="#e74c3c", binwidth=500, kde=False, orientation='vertical')

# Additional modifications: set the title and labels
plt.title('Calorie Intake Distribution', pad=20)
plt.ylabel('Frequency')
plt.xlabel('Calories')

# Show the plot
plt.show()
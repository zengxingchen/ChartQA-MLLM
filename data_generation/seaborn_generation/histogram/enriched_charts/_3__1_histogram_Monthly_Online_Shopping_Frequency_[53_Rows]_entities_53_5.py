
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the dataset
data = {
    'calories': [
        150, 200, 180, 220, 250, 275, 300, 320, 350, 400, 420, 450, 470, 500, 530, 550,
        580, 600, 630, 650, 680, 700, 720, 750, 770, 800, 820, 850, 870, 900, 930, 950,
        970, 1000, 1020, 1050, 1070, 1100, 1130, 1150, 1180, 1200, 1230, 1250, 1280, 1300,
        1330, 1350, 1380, 1400, 1430, 1450, 1480, 1500, 1530, 1550, 1580, 1600, 1630, 1650,
        1680, 1700, 1730, 1750, 1780, 1800, 1830, 1850, 1880, 1900, 1930, 1950, 1970, 2000,
        2020, 2050, 2080, 2100, 2130, 2150, 2180, 2200, 2230, 2250, 2280, 2300, 2330, 2350,
        2380, 2400, 2430, 2450, 2480, 2500, 2530, 2550, 2580, 2600, 2630, 2650, 2680, 2700,
        2730, 2750, 2780, 2800, 2830, 2850, 2880, 2900, 2930, 2950, 2980, 3000
    ]
}
df = pd.DataFrame(data)

# Set the style and the figure size
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))

# Create the histogram chart
sns.histplot(
    data=df, 
    y="calories", 
    binwidth=150, 
    kde=False, 
    color="#4c72b0"
)

# Adjusting further aesthetics of the plot
plt.title("Distribution of Calories Consumed")
plt.ylabel("Calories")
plt.xlabel("Frequency")
plt.ylim(100, 3100)  # Assuming our range of interest in calories is from 100 to 3100
plt.yticks(range(100, 3101, 500))  # Setting the y-axis ticks to be every 500 calories

# Display the plot
plt.show()
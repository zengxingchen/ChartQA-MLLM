
import pandas as pd
import matplotlib.pyplot as plt

# Preparing the dataset
data = {
    "Year": [i for i in range(2000, 2022)],
    "ExoplanetsDiscovered": [
        20, 25, 30, 35, 50, 55, 60, 70, 75, 80, 
        90, 100, 110, 130, 150, 170, 200, 220, 
        250, 280, 310, 340
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the area chart
plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['ExoplanetsDiscovered'], alpha=0.4, color='#4682B4')
plt.plot(df['Year'], df['ExoplanetsDiscovered'], color='#104E8B', linewidth=2)

# Customize the plot with labels and change in visual aspects
plt.title('Number of Exoplanets Discovered Over Time', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Exoplanets Discovered', fontsize=16)

# Annotate the last data point
plt.annotate(f'{df.iloc[-1]["ExoplanetsDiscovered"]}',
             xy=(df.iloc[-1]['Year'], df.iloc[-1]['ExoplanetsDiscovered']),
             xytext=(df.iloc[-2]['Year'], df.iloc[-1]['ExoplanetsDiscovered'] + 20),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=14)

plt.grid(visible=True)
plt.show()
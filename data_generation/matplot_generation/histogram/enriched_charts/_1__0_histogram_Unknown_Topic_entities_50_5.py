
import matplotlib.pyplot as plt

# Data: Calorie content in food items
calories = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100, 4150, 4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000]

# Create the histogram with the specified modifications:
plt.figure(figsize=(10, 8))  # Reasonable size change (width and height of the chart)
n, bins, patches = plt.hist(calories, bins=15, color='#FF4500', rwidth=0.7)  # Color scheme & width of histograms

# Customize histogram
for i, patch in enumerate(patches):
    patch.set_facecolor("#%06x" % ((i * 123456) % 0xFFFFFF))  # Varied colors for each bar

plt.title('Calorie Content Distribution in Food Items')  # Changed headline/topic
plt.xlabel('Calorie Range')  # Adjust for the vertical histogram; originally ylabel
plt.ylabel('Frequency')  # Adjust for the vertical histogram; originally xlabel

# Display the plot
plt.show()
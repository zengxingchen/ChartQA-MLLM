
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data (hypothetical temperatures in Celsius over a year)
data = {
    "Temperature": [
        15, 16, 15, 17, 16, 18, 19, 20, 21, 19, 17, 18, 18, 21, 22, 23, 25, 26, 24,
        22, 20, 20, 21, 19, 17, 15, 16, 18, 17, 16, 15, 16, 16, 15, 17, 18, 20, 22,
        21, 19, 24, 25, 27, 28, 26, 24, 22, 23, 25, 27, 20, 21, 19, 18, 17, 16, 15,
        14, 13, 15, 17, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 12, 14, 16, 18, 19
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create a histogram with specified bin width, color, and other properties
sns.histplot(df['Temperature'], bins=18, color='#1f77b4', kde=False, binwidth=1)

# Set title and labels for the plot
plt.title("Yearly Distribution of Daily Average Temperatures")
plt.xlabel("Temperature (Celsius)")
plt.ylabel("Frequency")

# Show the plot
plt.show()
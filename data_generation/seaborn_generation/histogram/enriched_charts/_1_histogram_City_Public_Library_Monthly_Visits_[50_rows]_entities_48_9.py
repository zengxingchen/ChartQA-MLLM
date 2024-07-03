
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    'Temperature': [
        -3, 0, 1, 2, 5, 7, 9, 12, 15, 17, 20, 22, 25,
        27, 29, 30, 32, 34, 34, 33, 31, 28, 26, 23,
        21, 18, 15, 13, 10, 8, 5, 3, 1, 0, -2, -4
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with custom bin width and modified aesthetics
sns.histplot(data=df, x="Temperature", binwidth=1, kde=True, color="#3498db")

# Customizing the aesthetics
sns.set_style("whitegrid")
plt.title("Distribution of Average Monthly Temperatures")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

# Show the plot
plt.show()
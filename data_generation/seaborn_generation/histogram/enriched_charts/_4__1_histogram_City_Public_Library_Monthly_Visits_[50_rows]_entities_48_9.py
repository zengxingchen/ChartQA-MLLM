
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    'Weight': [
        70, 75, 80, 85, 60, 65, 90, 95, 100, 105, 50, 55, 110, 115, 120,
        125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185,
        190, 195, 200, 205, 210, 215, 220, 225, 230
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 14))

# Plot the histogram with custom bin width and modified aesthetics
sns.histplot(data=df, y="Weight", binwidth=10, kde=True, color="#2ecc71")

# Customizing the aesthetics
sns.set_style("darkgrid")
plt.title("Distribution of Weights in a Fitness Program")
plt.xlabel("Frequency")
plt.ylabel("Weight (kg)")

# Show the plot
plt.show()
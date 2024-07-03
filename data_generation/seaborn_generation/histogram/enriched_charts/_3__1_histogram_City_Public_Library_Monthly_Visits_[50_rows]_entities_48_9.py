
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    'Income': [
        1500, 2000, 2200, 2500, 2700, 2900, 3200, 3400, 3500, 3700,
        4000, 4200, 4500, 4800, 5000, 5300, 5500, 5800, 6000, 6200,
        6500, 6800, 7000, 7200, 7500, 7800, 8000, 8200, 8500, 8700,
        9000, 9200, 9400, 9700, 10000, 10300, 10600
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the histogram with custom bin width and modified aesthetics
sns.histplot(data=df, y="Income", binwidth=1000, kde=True, color="#ff6347")

# Customizing the aesthetics
sns.set_style("whitegrid")
plt.title("Distribution of Monthly Household Incomes", pad=20)
plt.xlabel("Frequency")
plt.ylabel("Income (USD)")

# Show the plot
plt.show()
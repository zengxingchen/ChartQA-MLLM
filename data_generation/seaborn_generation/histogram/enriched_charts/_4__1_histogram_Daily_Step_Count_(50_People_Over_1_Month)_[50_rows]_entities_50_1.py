
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame directly from the data provided
data = {
    'Step_Count': [
        6534, 7241, 8123, 8540, 9112, 9234, 10010, 10845, 10550, 9901,
        8650, 7512, 7345, 6850, 6452, 8970, 9125, 9870, 9760, 9642,
        8890, 8500, 7934, 7123, 8567, 8740, 9210, 10567, 10980, 11234,
        10345, 9650, 8750, 8234, 7430, 6901, 6734
    ]
}
df = pd.DataFrame(data)

# Customize the plot size
plt.figure(figsize=(12, 8))

# Plot the histogram with custom bin width and color
sns.histplot(df['Step_Count'], bins=12, color='#e74c3c', kde=False, binwidth=500)

# Customize the plot labels and title
plt.title('Daily Step Counts Distribution')
plt.xlabel('Step Count')
plt.ylabel('Frequency')

# Show the plot
plt.show()
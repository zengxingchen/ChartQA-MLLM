import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Vitamin A': [25, 28, 32, 35, 40, 42, 45, 50, 55, 58, 62, 65],
    'Vitamin C': [30, 32, 35, 38, 42, 45, 48, 52, 56, 60, 65, 68],
    'Vitamin D': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative intake
cumulative_intake = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(14, 8))

# Plotting the data
plt.stackplot(df.index, cumulative_intake['Vitamin A'],
              cumulative_intake['Vitamin C'],
              cumulative_intake['Vitamin D'],
              labels=['Vitamin A', 'Vitamin C', 'Vitamin D'],
              colors=['#FFA07A', '#20B2AA', '#778899'], alpha=0.8)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Highest Intake', xy=('Q4-2023', cumulative_intake.loc['Q4-2023', 'Vitamin D']),
             xytext=(-80, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Quarterly Vitamin Intake (in milligrams)', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Intake (mg)')

# Display the plot
plt.tight_layout()
plt.show()
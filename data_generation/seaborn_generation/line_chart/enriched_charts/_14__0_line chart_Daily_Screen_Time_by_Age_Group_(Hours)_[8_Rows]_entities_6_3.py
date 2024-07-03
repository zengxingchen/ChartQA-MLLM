
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame using the provided table data
data = {
    'Day': [i for i in range(1, 32)],
    'Protein_Intake': [45, 47, 46, 48, 49, 51, 50, 52, 53, 55, 54, 56, 55, 57,
                       58, 57, 56, 58, 59, 61, 60, 59, 58, 57, 55, 54, 53, 52, 51, 50, 49]
}

df = pd.DataFrame(data)

# Customizing plot size
plt.figure(figsize=(16, 7))

# Creating a line plot
sns.lineplot(x='Day', y='Protein_Intake', data=df, color='#FF6347')

# Adding annotations
for day, intake in zip(data['Day'], data['Protein_Intake']):
    if day == 20:  # example of specific annotation on Day 20
        plt.text(day, intake, f"{intake}g", fontsize=9, ha='center')

# Setting plot title and labels
plt.title('Daily Average Protein Intake over a Month', fontsize=18, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Protein Intake (g)', fontsize=14)

# Display the plot
plt.show()
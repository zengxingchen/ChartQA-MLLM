
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories_Intake': [2000, 2200, 2100, 2300, 2500, 2400, 2600, 2700, 2800, 2900, 3000, 3100],
    'Protein_Intake': [50, 60, 55, 58, 65, 62, 70, 72, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Calories_Intake', y='Protein_Intake', data=df,
                palette=['#FF5733', '#33FF57'])

plt.title('Monthly Nutrition Consumption', fontsize=16, pad=20)
plt.xlabel('Calories Intake (kcal)', fontsize=14)
plt.ylabel('Protein Intake (g)', fontsize=14)

# Display the plot
plt.show()
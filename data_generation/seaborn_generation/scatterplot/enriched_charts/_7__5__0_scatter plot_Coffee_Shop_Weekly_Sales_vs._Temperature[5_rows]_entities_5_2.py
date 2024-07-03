
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Age': [20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
            40, 42, 44, 46, 48, 50, 52, 54, 56, 58,
            60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80],
    'DailyCaloricIntake': [2500, 2600, 2550, 2700, 2750, 2650, 2800, 2900, 2500, 2750,
                           2600, 3000, 3100, 2400, 3200, 2550, 3300, 2750, 3050, 3150,
                           2650, 2800, 2950, 3100, 3200, 2800, 2750, 3100, 3250, 3350, 3400],
    'ExerciseHours': [0.5, 1.0, 1.5, 0.5, 2.0, 2.5, 1.5, 3.0, 0.5, 2.5,
                      3.5, 3.0, 4.0, 0.3, 4.5, 1.0, 5.0, 2.0, 3.5, 4.5,
                      1.5, 2.0, 2.5, 3.0, 3.5, 1.5, 2.3, 3.8, 4.0, 3.7, 4.2]
}

df = pd.DataFrame(data)

# Plotting code
plt.figure(figsize=(14, 8))
scatter_plot = sns.scatterplot(
    x='Age',
    y='DailyCaloricIntake',
    hue='ExerciseHours',
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF'],
    data=df,
    legend="full",
    s=100  # size of the markers
)
scatter_plot.set_title('Daily Caloric Intake by Age and Exercise Hours in Sports & Fitness', fontsize=16, pad=20)
scatter_plot.set_xlabel('Age (Years)')
scatter_plot.set_ylabel('Daily Caloric Intake (kcal)')

# Adjust legend title
plt.legend(title='Daily Exercise Hours', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
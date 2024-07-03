
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data (as it would be in a dataframe)
data = {
    'Age': [20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
            40, 42, 44, 46, 48, 50, 52, 54, 56, 58,
            60, 62, 64, 66, 68, 70],
    'DailyCaloricIntake': [2500, 2600, 2550, 2700, 2750, 2650, 2800, 2900, 2500, 2750,
                           2600, 3000, 3100, 2400, 3200, 2550, 3300, 2750, 3050, 3150,
                           2650, 2800, 2950, 3100, 3200, 2800],
    'ExerciseHours': [0.5, 1.0, 1.5, 0.5, 2.0, 2.5, 1.5, 3.0, 0.5, 2.5,
                      1.5, 3.0, 4.0, 0.3, 4.5, 1.0, 5.0, 2.0, 3.5, 4.5,
                      1.5, 2.0, 2.5, 3.0, 3.5, 1.5]
}

df = pd.DataFrame(data)

# Plotting code
plt.figure(figsize=(12, 7))
scatter_plot = sns.scatterplot(
    x='Age',
    y='DailyCaloricIntake',
    hue='ExerciseHours',
    palette=['#FF4500', '#1E90FF', '#3CB371', '#FFD700', '#9370DB'],
    data=df,
    legend="full",
    s=100  # size of the markers
)
scatter_plot.set_title('Daily Caloric Intake by Age and Exercise Hours')
scatter_plot.set_xlabel('Age (Years)')
scatter_plot.set_ylabel('Daily Caloric Intake (kcal)')

# Adjust legend title
plt.legend(title='Daily Exercise Hours')

plt.show()
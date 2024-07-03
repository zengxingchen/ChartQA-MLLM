
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Hours_of_Exercise': [15, 12, 18, 20, 22, 25, 28, 30, 27, 24, 21, 19],
    'Caloric_Intake': [2100, 1950, 2250, 2300, 2400, 2500, 2600, 2700, 2550, 2450, 2350, 2200]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Hours_of_Exercise', y='Caloric_Intake', data=df,
                palette=['#FF5733', '#33FF57'])

plt.title('Monthly Exercise and Caloric Intake', fontsize=16)
plt.xlabel('Hours of Exercise per Month')
plt.ylabel('Caloric Intake per Month (kcal)')

# Display the plot
plt.show()
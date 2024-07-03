
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electricity_Consumption': [300, 270, 320, 280, 310, 355, 400, 390, 370, 340, 320, 310],
    'Water_Consumption': [40, 35, 37, 38, 42, 44, 48, 46, 43, 41, 39, 40]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Electricity_Consumption', y='Water_Consumption', data=df,
                palette=['#348ABD', '#A60628'])

plt.title('Monthly Utilities Consumption')
plt.xlabel('Electricity Consumption (kWh)')
plt.ylabel('Water Consumption (cubic meters)')

# Display the plot
plt.show()
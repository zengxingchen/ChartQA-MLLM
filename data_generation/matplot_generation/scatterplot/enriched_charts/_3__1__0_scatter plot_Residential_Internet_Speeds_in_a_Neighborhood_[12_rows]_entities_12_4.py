
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
fruit_consumption = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 4.8, 4.3, 3.8, 3.5, 2.8]
vitamin_intake = [30, 40, 50, 55, 60, 70, 80, 75, 65, 55, 50, 40]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(14, 7))
plt.scatter(month_numbers, fruit_consumption, c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                 '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                                 '#bcbd22', '#17becf', '#aec7e8', '#ffbb78'],
            s=vitamin_intake, alpha=0.7)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Fruit Consumption (kg)')
plt.title('Monthly Fruit Consumption and Vitamin Intake', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()
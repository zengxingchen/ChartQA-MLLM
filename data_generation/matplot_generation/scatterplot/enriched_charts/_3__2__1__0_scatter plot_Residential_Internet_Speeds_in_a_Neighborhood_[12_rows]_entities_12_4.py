
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
expenditure = [40, 50, 60, 75, 90, 110, 100, 85, 75, 65, 55, 50]
revenue = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2100, 1900, 1700, 1500, 1300]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(16, 8))
plt.scatter(month_numbers, expenditure, c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                           '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                           '#bcbd22', '#17becf', '#ffbb78', '#98df8a'],
            s=[x/10 for x in revenue], alpha=0.8)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Expenditure ($1000)')
plt.title('Monthly Business Expenditure and Revenue', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
         'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12',
         'Week 13', 'Week 14', 'Week 15', 'Week 16', 'Week 17', 'Week 18',
         'Week 19', 'Week 20', 'Week 21', 'Week 22', 'Week 23', 'Week 24', 
         'Week 25', 'Week 26', 'Week 27', 'Week 28', 'Week 29', 'Week 30',
         'Week 31', 'Week 32', 'Week 33', 'Week 34', 'Week 35', 'Week 36',
         'Week 37', 'Week 38', 'Week 39', 'Week 40', 'Week 41', 'Week 42',
         'Week 43', 'Week 44', 'Week 45', 'Week 46', 'Week 47', 'Week 48',
         'Week 49', 'Week 50', 'Week 51', 'Week 52']
hours_studied = [3, 5, 4, 6, 7, 8, 9, 7, 8, 6, 5, 7, 8, 9, 10, 11, 12, 10, 9, 8, 7, 6, 8, 9, 10, 11, 12, 10, 9, 8, 7, 6, 8, 9, 10, 11, 12, 10, 9, 8, 7, 6, 8, 9, 10, 11, 12, 10, 9, 8, 7, 6]

plt.figure(figsize=(14, 7))
plt.fill_between(weeks, hours_studied, color='#FF5733')
plt.title('Weekly Study Hours Throughout the Year', fontsize=16, loc='left')
plt.xlabel('Week')
plt.ylabel('Hours Studied')
plt.grid(True)
for i, txt in enumerate(hours_studied):
    plt.annotate(txt, (weeks[i], hours_studied[i]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.show()
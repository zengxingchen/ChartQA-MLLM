
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
weekly_savings = [50, 60, 55, 70, 75, 80, 90, 85, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 
                  155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 
                  245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310]

plt.figure(figsize=(16, 8))
plt.fill_between(weeks, weekly_savings, color='#4CAF50')
plt.title('Weekly Savings Throughout the Year', fontsize=18, loc='left')
plt.xlabel('Week')
plt.ylabel('Weekly Savings ($)')
plt.grid(True)
for i, txt in enumerate(weekly_savings):
    plt.annotate(txt, (weeks[i], weekly_savings[i]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.show()

import matplotlib.pyplot as plt

months = ['Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023', 
          'Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024', 
          'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025']
revenue = [500, 480, 520, 550, 530, 540, 560, 580, 570, 590, 610, 630]

plt.figure(figsize=(10, 5))

plt.plot(months, revenue, color='#1f77b4', linewidth=2)

plt.annotate('Highest Revenue', xy=('Q4-2025', 630), xytext=('Q3-2025', 610),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

plt.title('Quarterly Revenue Trends', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (in USD)', fontsize=12)
plt.gca().invert_yaxis()

plt.show()
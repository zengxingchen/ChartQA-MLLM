
import matplotlib.pyplot as plt

quarters = [
    'Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
    'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
    'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'
]
politics = [10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]
governance = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
economics = [15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000]

plt.figure(figsize=(14, 10))

plt.stackplot(quarters, politics, governance, economics,
              colors=['#4B0082', '#FF7F50', '#4682B4'],
              labels=['Politics', 'Governance', 'Economics'])

plt.legend(loc='upper right')

plt.title('Quarterly Engagement in Politics, Governance, and Economics', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Engagement Level')

for i, p in enumerate(politics):
    total_engagement = p + governance[i] + economics[i]
    plt.text(quarters[i], total_engagement, f'{total_engagement}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
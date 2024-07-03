
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Entry Level', 'Junior Level', 'Mid Level', 'Senior Level', 'Executive Level'],
    'Salary': [20, 25, 30, 35, 40],
    'Job Satisfaction': [25, 30, 20, 25, 30],
    'Work-Life Balance': [30, 20, 25, 20, 20],
    'Job Security': [15, 15, 10, 10, 5],
    'Work Environment': [10, 10, 15, 10, 5]
}

categories = data['Category']
salary = np.array(data['Salary'])
job_satisfaction = np.array(data['Job Satisfaction'])
work_life_balance = np.array(data['Work-Life Balance'])
job_security = np.array(data['Job Security'])
work_environment = np.array(data['Work Environment'])

barWidth = 0.8

r = range(len(categories))

plt.figure(figsize=(10, 12))

plt.bar(r, salary, color='#ff9999', edgecolor='white', width=barWidth, label='Salary')
plt.bar(r, job_satisfaction, bottom=salary, color='#66b3ff', edgecolor='white', width=barWidth, label='Job Satisfaction')
plt.bar(r, work_life_balance, bottom=salary + job_satisfaction, color='#99ff99', edgecolor='white', width=barWidth, label='Work-Life Balance')
plt.bar(r, job_security, bottom=salary + job_satisfaction + work_life_balance, color='#ffcc99', edgecolor='white', width=barWidth, label='Job Security')
plt.bar(r, work_environment, bottom=salary + job_satisfaction + work_life_balance + job_security, color='#c2c2f0', edgecolor='white', width=barWidth, label='Work Environment')

plt.ylabel('Percentage')
plt.xlabel('Career Level')
plt.title('Work Satisfaction Factors Across Career Levels')
plt.xticks(r, categories, rotation=45)
plt.legend(loc='upper right')

plt.show()
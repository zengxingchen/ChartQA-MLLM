
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Category': ['Mental Health', 'Cardiology', 'Neurology', 'Oncology', 'Pediatrics', 'Orthopedics', 'Endocrinology', 'Gastroenterology', 'Psychiatry', 'Dermatology', 'Immunology', 'Radiology', 'Nephrology', 'Hematology', 'Rheumatology'],
    'Research_Expenditure': [25000, 32000, 27000, 35000, 22000, 20000, 28000, 24000, 30000, 26000, 33000, 29000, 31000, 27000, 23000],
    'Impact_Score': [180, 220, 200, 250, 150, 140, 190, 160, 210, 170, 230, 200, 210, 195, 160],
    'Participants': [5000, 8000, 6000, 7000, 4000, 3000, 4500, 5000, 6000, 3500, 7000, 5500, 6000, 4000, 3000],
    'Study_Influence': [85, 90, 88, 92, 80, 78, 87, 84, 89, 81, 91, 86, 88, 83, 82]
})

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=data,
    x='Research_Expenditure',
    y='Impact_Score',
    size='Participants',
    hue='Study_Influence',
    palette=['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#FFD700', '#DC143C', '#00CED1', '#FF4500', '#DAA520', '#ADFF2F', '#F08080', '#20B2AA', '#87CEFA', '#9370DB', '#FFB6C1'],
    sizes=(100, 2500),
    alpha=0.6
)

plt.legend(title='Study Influence Rating', loc='upper left', bbox_to_anchor=(1, 1))
plt.title('Research Expenditure vs Impact Score in Health Studies', fontsize=18, pad=20)
plt.xlabel('Research Expenditure in Thousands USD', fontsize=14)
plt.ylabel('Impact Score', fontsize=14)

plt.show()
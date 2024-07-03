
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Cardiovascular Diseases': [22, 21, 20, 19, 18, 17, 16, 15, 14, 14, 13],
    'Respiratory Diseases': [18, 19, 19, 18, 18, 19, 19, 18, 17, 17, 16],
    'Diabetes': [10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18],
    'Cancer': [20, 19, 19, 18, 17, 17, 16, 16, 15, 15, 14],
    'Mental Disorders': [15, 14, 14, 16, 16, 17, 17, 18, 18, 17, 17],
    'Infectious Diseases': [15, 16, 16, 17, 18, 16, 17, 18, 20, 20, 22]
}

years = data['Year']
cardio = data['Cardiovascular Diseases']
respiratory = data['Respiratory Diseases']
diabetes = data['Diabetes']
cancer = data['Cancer']
mental = data['Mental Disorders']
infectious = data['Infectious Diseases']

barWidth = 0.75
barHeight = 0.85

r = np.arange(len(years))

plt.figure(figsize=(10, 14))

plt.bar(r, cardio, color='#FF9999', edgecolor='white', width=barWidth, label='Cardiovascular Diseases')
plt.bar(r, respiratory, bottom=cardio, color='#66B2FF', edgecolor='white', width=barWidth, label='Respiratory Diseases')
plt.bar(r, diabetes, bottom=np.array(cardio)+np.array(respiratory), color='#99FF99', edgecolor='white', width=barWidth, label='Diabetes')
plt.bar(r, cancer, bottom=np.array(cardio)+np.array(respiratory)+np.array(diabetes), color='#FFCC99', edgecolor='white', width=barWidth, label='Cancer')
plt.bar(r, mental, bottom=np.array(cardio)+np.array(respiratory)+np.array(diabetes)+np.array(cancer), color='#FFB266', edgecolor='white', width=barWidth, label='Mental Disorders')
plt.bar(r, infectious, bottom=np.array(cardio)+np.array(respiratory)+np.array(diabetes)+np.array(cancer)+np.array(mental), color='#B3B3CC', edgecolor='white', width=barWidth, label='Infectious Diseases')

plt.ylabel('Percentage')
plt.xlabel('Year')
plt.title('Prevalence of Major Health Conditions (2010-2020)', pad=20)
plt.xticks(r, years)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.tight_layout()
plt.show()
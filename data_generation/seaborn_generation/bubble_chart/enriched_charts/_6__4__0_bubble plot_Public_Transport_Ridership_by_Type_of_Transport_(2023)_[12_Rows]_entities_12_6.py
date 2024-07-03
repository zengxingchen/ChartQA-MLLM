
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Condition': ['Diabetes', 'Hypertension', 'Asthma', 'Depression', 'Obesity', 
                  'Arthritis', 'Cancer', 'Heart Disease', 'Anxiety', 'Stroke'],
    'Patients': [24.3, 18.7, 12.9, 16.4, 21.1, 15.3, 14.7, 13.9, 17.8, 10.2],
    'ResearchFunding': [5.2, 3.8, 2.4, 4.5, 4.1, 3.2, 6.8, 5.6, 4.3, 4.9],
    'SatisfactionScore': [4.5, 4.2, 4.0, 3.9, 4.1, 3.8, 4.4, 4.3, 3.7, 4.2]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))

bubble = sns.scatterplot(data=df, x='SatisfactionScore', y='Patients', size='ResearchFunding', 
                         hue='Condition', palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                                                   '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                                   '#bcbd22', '#17becf'],
                         sizes=(100, 2500), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Health Conditions by Patient Numbers and Research Funding in 2023', weight='bold', size=18, pad=20)
bubble.set_xlabel('Patient Satisfaction Score', weight='bold', size=14)
bubble.set_ylabel('Patients (in millions)', weight='bold', size=14)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.show()

import matplotlib.pyplot as plt

data = {
    'Disorder': ['Anxiety', 'Depression', 'Bipolar Disorder', 'Schizophrenia', 'OCD', 
                 'PTSD', 'Eating Disorders', 'ADHD', 'Autism', 'Substance Use Disorders', 
                 'Borderline Personality Disorder', 'Dementia', 'Phobias', 'Somatic Symptom Disorder', 
                 'Panic Disorder', 'Social Anxiety Disorder'],
    'Prevalence (%)': [18.1, 6.7, 2.8, 1.1, 1.2, 3.5, 5.0, 8.4, 1.0, 7.7, 1.6, 0.8, 9.1, 6.0, 2.7, 6.8],
    'Treatment Cost ($)': [2500, 2000, 10000, 15000, 3000, 4500, 5000, 1500, 10000, 3500, 7000, 20000, 1000, 2500, 3000, 2000],
    'Severity (1-10)': [8, 9, 7, 10, 8, 9, 7, 6, 9, 8, 10, 10, 5, 6, 7, 8]
}

fig, ax = plt.subplots(figsize=(18, 12))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8F33', 
          '#FF3333', '#8D33FF', '#33FFF4', '#FF333F', '#33FF8A', 
          '#FF333B', '#FFBE33', '#FF3361', '#7D33FF', '#FF3375', 
          '#33D4FF']

for i in range(len(data['Disorder'])):
    ax.scatter(data['Prevalence (%)'][i], data['Treatment Cost ($)'][i], 
               s=(data['Severity (1-10)'][i] ** 3) * 10, 
               alpha=0.6,
               color=colors[i])

ax.set_title('Mental Health Disorders: Prevalence vs Treatment Cost with Severity as Bubble Size', fontsize=20, pad=30)
ax.set_xlabel('Prevalence (%)', fontsize=16)
ax.set_ylabel('Treatment Cost ($)', fontsize=16)
ax.grid(True)

plt.show()
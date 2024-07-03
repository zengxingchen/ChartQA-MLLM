
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Age Group': ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75'],
    'Running': [30, 25, 20, 15, 10, 5],
    'Swimming': [25, 20, 15, 10, 10, 5],
    'Cycling': [20, 25, 30, 20, 15, 10],
    'Weightlifting': [15, 20, 25, 35, 40, 40],
    'Yoga': [10, 10, 10, 20, 25, 40]
}

labels = data['Age Group']
running = np.array(data['Running'])
swimming = np.array(data['Swimming'])
cycling = np.array(data['Cycling'])
weightlifting = np.array(data['Weightlifting'])
yoga = np.array(data['Yoga'])

width = 0.5
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(labels, running, width, label='Running', color='#1f77b4')
ax.bar(labels, swimming, width, bottom=running, label='Swimming', color='#ff7f0e')
ax.bar(labels, cycling, width, bottom=running + swimming, label='Cycling', color='#2ca02c')
ax.bar(labels, weightlifting, width, bottom=running + swimming + cycling, label='Weightlifting', color='#d62728')
ax.bar(labels, yoga, width, bottom=running + swimming + cycling + weightlifting, label='Yoga', color='#9467bd')

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Physical Activities Among Age Groups')
ax.legend(loc='upper right')

plt.show()
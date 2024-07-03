
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Age Group': ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75'],
    'Jazz': [20, 25, 30, 20, 15, 10],
    'Rock': [25, 30, 20, 10, 15, 20],
    'Classical': [10, 15, 20, 30, 25, 35],
    'Pop': [30, 20, 15, 10, 20, 25],
    'Hip-Hop': [15, 10, 15, 30, 25, 10]
}

labels = data['Age Group']
jazz = np.array(data['Jazz'])
rock = np.array(data['Rock'])
classical = np.array(data['Classical'])
pop = np.array(data['Pop'])
hip_hop = np.array(data['Hip-Hop'])

width = 0.7
fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(labels, jazz, width, label='Jazz', color='#4B0082')
ax.bar(labels, rock, width, bottom=jazz, label='Rock', color='#FF6347')
ax.bar(labels, classical, width, bottom=jazz + rock, label='Classical', color='#FFD700')
ax.bar(labels, pop, width, bottom=jazz + rock + classical, label='Pop', color='#ADFF2F')
ax.bar(labels, hip_hop, width, bottom=jazz + rock + classical + pop, label='Hip-Hop', color='#20B2AA')

ax.set_ylabel('Percentage')
ax.set_title('Music Genre Preferences Among Age Groups', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
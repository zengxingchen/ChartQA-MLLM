import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Primary School', 'Middle School', 'High School', 'Undergraduate', 'Postgraduate'],
    'Reading': [25, 30, 20, 15, 10],
    'Writing': [35, 30, 25, 20, 15],
    'Listening': [20, 25, 30, 35, 40],
    'Speaking': [20, 15, 25, 30, 35]
}

categories = data['Category']
reading = np.array(data['Reading'])
writing = np.array(data['Writing'])
listening = np.array(data['Listening'])
speaking = np.array(data['Speaking'])

barWidth = 0.6

r = range(len(categories))

# Create a stacked bar chart
plt.figure(figsize=(12, 8))

plt.barh(r, reading, color='#1f77b4', edgecolor='white', height=barWidth, label='Reading')
plt.barh(r, writing, left=reading, color='#ff7f0e', edgecolor='white', height=barWidth, label='Writing')
plt.barh(r, listening, left=reading + writing, color='#2ca02c', edgecolor='white', height=barWidth, label='Listening')
plt.barh(r, speaking, left=reading + writing + listening, color='#d62728', edgecolor='white', height=barWidth, label='Speaking')

# Add labels
plt.xlabel('Percentage')
plt.ylabel('Education Level')
plt.title('Distribution of Language Skills Across Education Levels')
plt.yticks(r, categories)
plt.legend(loc='lower right')

plt.show()
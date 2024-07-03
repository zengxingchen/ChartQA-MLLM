
import matplotlib.pyplot as plt

# Data
data = [
    {'Transportation Mode': 'Bus', 'Percentage of Commuters': 25},
    {'Transportation Mode': 'Subway', 'Percentage of Commuters': 20},
    {'Transportation Mode': 'Car', 'Percentage of Commuters': 30},
    {'Transportation Mode': 'Bicycle', 'Percentage of Commuters': 10},
    {'Transportation Mode': 'Walking', 'Percentage of Commuters': 5},
    {'Transportation Mode': 'Motorcycle', 'Percentage of Commuters': 2},
    {'Transportation Mode': 'Rideshare', 'Percentage of Commuters': 6},
    {'Transportation Mode': 'Telecommuting', 'Percentage of Commuters': 2}
]

modes = [d['Transportation Mode'] for d in data]
percentages = [d['Percentage of Commuters'] for d in data]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=modes, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Commuters by Transportation Mode')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()
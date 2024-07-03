
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = [{'Activity': 'Swimming', 'Percentage': '20%'},
        {'Activity': 'Fitness Classes', 'Percentage': '15%'},
        {'Activity': 'Soccer', 'Percentage': '12%'},
        {'Activity': 'Basketball', 'Percentage': '10%'},
        {'Activity': 'Yoga', 'Percentage': '9%'},
        {'Activity': 'Running Groups', 'Percentage': '8%'},
        {'Activity': 'Cycling', 'Percentage': '7%'},
        {'Activity': 'Tennis', 'Percentage': '6%'},
        {'Activity': 'Community Gardening', 'Percentage': '5%'},
        {'Activity': 'Book Clubs', 'Percentage': '4%'},
        {'Activity': 'Dance Workshops', 'Percentage': '2%'},
        {'Activity': 'Pottery Classes', 'Percentage': '2%'}]

# Process data
activities = [item['Activity'] for item in data]
percentages = [float(item['Percentage'].strip('%')) for item in data]
colors = sns.color_palette('hsv', len(activities))  # Get a diversified color palette

# Convert percentages to fractions
fractions = [p / 100 for p in percentages]

# Create pie chart using Matplotlib
plt.figure(figsize=(10, 8))
plt.pie(fractions, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Activity Participation Distribution')

# Enhance with Seaborn's styling
sns.set_context('talk')
sns.set_style('whitegrid')

plt.show()
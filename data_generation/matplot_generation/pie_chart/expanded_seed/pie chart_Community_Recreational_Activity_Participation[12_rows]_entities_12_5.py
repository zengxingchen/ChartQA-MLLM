
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Activity': 'Soccer', 'Number of Participants': 150},
    {'Activity': 'Basketball', 'Number of Participants': 120},
    {'Activity': 'Swimming', 'Number of Participants': 200},
    {'Activity': 'Yoga', 'Number of Participants': 180},
    {'Activity': 'Cycling', 'Number of Participants': 90},
    {'Activity': 'Running', 'Number of Participants': 160},
    {'Activity': 'Tennis', 'Number of Participants': 70},
    {'Activity': 'Golf', 'Number of Participants': 40},
    {'Activity': 'Hiking', 'Number of Participants': 130},
    {'Activity': 'Dance', 'Number of Participants': 110},
    {'Activity': 'Gymnastics', 'Number of Participants': 50},
    {'Activity': 'Martial Arts', 'Number of Participants': 60}
]

# Extracting the activities and number of participants from the data
activities = [entry['Activity'] for entry in data]
participants = [entry['Number of Participants'] for entry in data]

# Setting up colors and explode values for the pie chart
colors = plt.cm.Paired(range(len(activities)))
explode = [0.05] * len(activities)  # Slightly separate each slice

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(participants, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# Add a title to the chart
plt.title('Distribution of Participants Across Activities')

# Show the pie chart
plt.show()
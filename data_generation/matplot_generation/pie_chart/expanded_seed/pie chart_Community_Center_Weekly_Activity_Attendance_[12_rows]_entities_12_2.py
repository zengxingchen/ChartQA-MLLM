
import matplotlib.pyplot as plt

# Given data
data = [{'Activity': 'Yoga Class', 'Number of Attendees': 45}, 
        {'Activity': 'Salsa Dancing', 'Number of Attendees': 30},
        {'Activity': 'Water Aerobics', 'Number of Attendees': 25},
        {'Activity': 'Cooking Workshop', 'Number of Attendees': 20},
        {'Activity': 'Book Club', 'Number of Attendees': 18},
        {'Activity': 'Language Lessons', 'Number of Attendees': 12},
        {'Activity': 'Meditation Group', 'Number of Attendees': 10},
        {'Activity': 'Knitting Circle', 'Number of Attendees': 8},
        {'Activity': 'Photography Class', 'Number of Attendees': 7},
        {'Activity': 'Computer Skills', 'Number of Attendees': 5},
        {'Activity': 'Gardening Club', 'Number of Attendees': 10},
        {'Activity': 'Toddler Storytime', 'Number of Attendees': 15}]

# Extracting 'Activity' and 'Number of Attendees' as separate lists
activities = [item['Activity'] for item in data]
attendees = [item['Number of Attendees'] for item in data]

# Colors for each slice of the pie chart
colors = plt.cm.Paired(range(len(activities)))

# Creating the pie chart
plt.figure(figsize=(10, 8))  # This size can be adjusted depending on your display needs
plt.pie(attendees, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})

# Adding a legend
plt.legend(activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Adding a title to the plot
plt.title('Attendance of Various Activities')

# Show the plot
plt.show()
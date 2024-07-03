
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Month': 'January', 'Innovations': 90, 'Publications': 40, 'Conferences': 60, 'Workshops': 30, 'Webinars': 50},
    {'Month': 'February', 'Innovations': 85, 'Publications': 42, 'Conferences': 62, 'Workshops': 28, 'Webinars': 55},
    {'Month': 'March', 'Innovations': 100, 'Publications': 38, 'Conferences': 64, 'Workshops': 32, 'Webinars': 60},
    {'Month': 'April', 'Innovations': 95, 'Publications': 45, 'Conferences': 66, 'Workshops': 35, 'Webinars': 58},
    {'Month': 'May', 'Innovations': 110, 'Publications': 47, 'Conferences': 70, 'Workshops': 37, 'Webinars': 65},
    {'Month': 'June', 'Innovations': 105, 'Publications': 49, 'Conferences': 75, 'Workshops': 40, 'Webinars': 68},
    {'Month': 'July', 'Innovations': 115, 'Publications': 50, 'Conferences': 78, 'Workshops': 42, 'Webinars': 72},
    {'Month': 'August', 'Innovations': 120, 'Publications': 52, 'Conferences': 80, 'Workshops': 45, 'Webinars': 75},
    {'Month': 'September', 'Innovations': 125, 'Publications': 55, 'Conferences': 82, 'Workshops': 48, 'Webinars': 78},
    {'Month': 'October', 'Innovations': 130, 'Publications': 57, 'Conferences': 85, 'Workshops': 50, 'Webinars': 80},
    {'Month': 'November', 'Innovations': 128, 'Publications': 58, 'Conferences': 88, 'Workshops': 52, 'Webinars': 82},
    {'Month': 'December', 'Innovations': 135, 'Publications': 60, 'Conferences': 90, 'Workshops': 55, 'Webinars': 85}
]

# Extracting months
months = [record['Month'] for record in data]

# Extracting data for each type of event
innovations = [record['Innovations'] for record in data]
publications = [record['Publications'] for record in data]
conferences = [record['Conferences'] for record in data]
workshops = [record['Workshops'] for record in data]
webinars = [record['Webinars'] for record in data]

# Start plotting
plt.figure(figsize=(18, 12))

# Plotting each type of event
plt.plot(months, innovations, label='Innovations', marker='o', linestyle='-', color='#4B0082')
plt.plot(months, publications, label='Publications', marker='X', linestyle='--', color='#FF1493')
plt.plot(months, conferences, label='Conferences', marker='^', linestyle='-.', color='#00CED1')
plt.plot(months, workshops, label='Workshops', marker='s', linestyle=':', color='#FFD700')
plt.plot(months, webinars, label='Webinars', marker='D', linestyle='-', color='#ADFF2F')

# Adding titles and labels
plt.title('Monthly Technological Advancements', pad=20)
plt.xlabel('Month')
plt.ylabel('Count of Events')

# Add a legend
plt.legend(loc='upper left')

# Annotate a specific data point
plt.annotate('Peak Innovation', xy=('December', 135), xytext=('November', 140),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Invert y-axis
plt.gca().invert_yaxis()

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()
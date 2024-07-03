
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Month': 'January', 'Online Courses': 500, 'Workshops': 350, 'Webinars': 600, 'Seminars': 400, 'Conferences': 300},
    {'Month': 'February', 'Online Courses': 520, 'Workshops': 360, 'Webinars': 590, 'Seminars': 410, 'Conferences': 310},
    {'Month': 'March', 'Online Courses': 530, 'Workshops': 370, 'Webinars': 580, 'Seminars': 420, 'Conferences': 320},
    {'Month': 'April', 'Online Courses': 540, 'Workshops': 380, 'Webinars': 570, 'Seminars': 430, 'Conferences': 330},
    {'Month': 'May', 'Online Courses': 550, 'Workshops': 390, 'Webinars': 560, 'Seminars': 440, 'Conferences': 340},
    {'Month': 'June', 'Online Courses': 560, 'Workshops': 400, 'Webinars': 550, 'Seminars': 450, 'Conferences': 350},
    {'Month': 'July', 'Online Courses': 570, 'Workshops': 410, 'Webinars': 540, 'Seminars': 460, 'Conferences': 360},
    {'Month': 'August', 'Online Courses': 580, 'Workshops': 420, 'Webinars': 530, 'Seminars': 470, 'Conferences': 370},
    {'Month': 'September', 'Online Courses': 590, 'Workshops': 430, 'Webinars': 520, 'Seminars': 480, 'Conferences': 380},
    {'Month': 'October', 'Online Courses': 600, 'Workshops': 440, 'Webinars': 510, 'Seminars': 490, 'Conferences': 390},
    {'Month': 'November', 'Online Courses': 610, 'Workshops': 450, 'Webinars': 500, 'Seminars': 500, 'Conferences': 400},
    {'Month': 'December', 'Online Courses': 620, 'Workshops': 460, 'Webinars': 490, 'Seminars': 510, 'Conferences': 410}
]

# Extracting months
months = [record['Month'] for record in data]

# Extracting data for each category
online_courses = [record['Online Courses'] for record in data]
workshops = [record['Workshops'] for record in data]
webinars = [record['Webinars'] for record in data]
seminars = [record['Seminars'] for record in data]
conferences = [record['Conferences'] for record in data]

# Start plotting
plt.figure(figsize=(16, 10))

# Plotting each category
plt.plot(months, online_courses, label='Online Courses', marker='o', linestyle='-', color='#1f77b4')
plt.plot(months, workshops, label='Workshops', marker='X', linestyle='--', color='#ff7f0e')
plt.plot(months, webinars, label='Webinars', marker='^', linestyle='-.', color='#2ca02c')
plt.plot(months, seminars, label='Seminars', marker='s', linestyle=':', color='#d62728')
plt.plot(months, conferences, label='Conferences', marker='D', linestyle='-', color='#9467bd')

# Adding titles and labels
plt.title('Monthly Participation in Educational Events', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Participants')

# Add a legend
plt.legend(loc='upper left')

# Annotate a specific data point
plt.annotate('Highest Participation', xy=('December', 620), xytext=('November', 650),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()
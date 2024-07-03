
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
online_courses = [800, 950, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600]
workshops_and_seminars = [1500, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400]
study_groups = [900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900]
private_tutoring = [700, 850, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]

# Plot
plt.figure(figsize=(18, 10))
plt.stackplot(years, online_courses, workshops_and_seminars, study_groups, private_tutoring, 
              colors=['#FF5733', '#33A1FF', '#FF33A6', '#33FF57'])

# Customize the plot
plt.title('Participation in Education Programs from 2012 to 2022', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Participants', fontsize=16)
plt.legend(['Online Courses', 'Workshops and Seminars', 'Study Groups', 'Private Tutoring'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{online_courses[i]}', (y, online_courses[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{workshops_and_seminars[i]}', (y, online_courses[i] + workshops_and_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{study_groups[i]}', (y, online_courses[i] + workshops_and_seminars[i] + study_groups[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{private_tutoring[i]}', (y, online_courses[i] + workshops_and_seminars[i] + study_groups[i] + private_tutoring[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()

import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
primary_education = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
secondary_education = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215]
higher_education = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165]
vocational_training = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]

# Creating a stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, primary_education, secondary_education, higher_education, vocational_training, 
              colors=['#FFA07A', '#20B2AA', '#778899', '#FF6347'])

# Adding labels and title
plt.title('Student Enrollment Trends (2010-2023)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Students (in thousands)', fontsize=14)

# Adding a legend
plt.legend(['Primary Education', 'Secondary Education', 'Higher Education', 'Vocational Training'], loc='lower right')

# Annotating the last data point for Higher Education
plt.annotate(f'{higher_education[-1]}k Students',
             (years[-1], sum([primary_education[-1], secondary_education[-1], higher_education[-1], vocational_training[-1]])),
             textcoords="offset points",
             xytext=(-15,10),
             ha='center',
             fontsize=12,
             color='#778899')

plt.show()
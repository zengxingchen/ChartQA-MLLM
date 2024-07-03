
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
admissions = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
tuition = [220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
faculty_salaries = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
research = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Stacking data
tuition_bottom = [admissions[i] for i in range(len(admissions))]
faculty_salaries_bottom = [tuition_bottom[i] + tuition[i] for i in range(len(tuition))]
research_bottom = [faculty_salaries_bottom[i] + faculty_salaries[i] for i in range(len(faculty_salaries))]

# Setting figure size
plt.figure(figsize=(14, 8))

# Plotting data
bar_height = 0.5
plt.barh(years, admissions, height=bar_height, color='#1f77b4', edgecolor='white', label='Admissions')
plt.barh(years, tuition, left=admissions, height=bar_height, color='#ff7f0e', edgecolor='white', label='Tuition')
plt.barh(years, faculty_salaries, left=tuition_bottom, height=bar_height, color='#2ca02c', edgecolor='white', label='Faculty Salaries')
plt.barh(years, research, left=faculty_salaries_bottom, height=bar_height, color='#d62728', edgecolor='white', label='Research')

# Adding numerical labels
for i in range(len(years)):
    plt.text(admissions[i] / 2, i, str(admissions[i]), ha='center', va='center', color='white')
    plt.text(admissions[i] + tuition[i] / 2, i, str(tuition[i]), ha='center', va='center', color='white')
    plt.text(admissions[i] + tuition[i] + faculty_salaries[i] / 2, i, str(faculty_salaries[i]), ha='center', va='center', color='white')
    plt.text(admissions[i] + tuition[i] + faculty_salaries[i] + research[i] / 2, i, str(research[i]), ha='center', va='center', color='white')

# Adding titles and labels
plt.xlabel('Annual Budget (in millions)')
plt.ylabel('Year')
plt.title('University Annual Budget by Department over Years', pad=20)
plt.legend(loc='lower right')

# Display the plot
plt.tight_layout()
plt.show()
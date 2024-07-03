
import matplotlib.pyplot as plt

# Data for scatterplot
countries = ["USA", "China", "Japan", "Germany", "India", "Australia", "UK", 
             "Russia", "Brazil", "France", "Canada", "Italy", "Spain", 
             "South Korea", "Mexico", "Turkey", "Netherlands", "Greece", 
             "Argentina", "Nigeria", "South Africa", "Indonesia", "Thailand", "Egypt"]
students_enrolled = [450, 380, 270, 220, 200, 230, 180, 170, 160, 140, 120, 130, 110, 
                     100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5]
average_study_hours_per_week = [37.5, 28.4, 29.3, 32.7, 25.0, 31.5, 30.2, 27.8, 24.5, 
                                33.1, 34.7, 26.9, 25.4, 35.0, 22.3, 23.6, 28.9, 24.1, 
                                21.8, 22.0, 27.5, 26.3, 30.0, 23.1]

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(students_enrolled, average_study_hours_per_week, c=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], s=100)

# Customize plot
plt.title('Students Enrolled vs. Average Study Hours per Week in Major Countries', fontsize=18, pad=20)
plt.xlabel('Students Enrolled (in thousands)', fontsize=14)
plt.ylabel('Average Study Hours per Week', fontsize=14)

# Annotate data points
for i, country in enumerate(countries):
    plt.annotate(country, (students_enrolled[i], average_study_hours_per_week[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()
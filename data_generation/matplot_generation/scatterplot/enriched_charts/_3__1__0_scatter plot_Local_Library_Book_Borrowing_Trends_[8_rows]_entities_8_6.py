
import matplotlib.pyplot as plt

# Data for scatterplot
sports = ["Basketball", "Football", "Baseball", "Soccer", "Tennis", "Golf", "Boxing", 
          "Cricket", "Rugby", "Ice Hockey", "Track and Field", "Swimming", "Cycling", 
          "MMA", "eSports", "Gymnastics", "Volleyball", "Handball"]
average_salary_millions = [8, 7, 6, 9, 5, 4, 12, 3, 4, 6, 3, 2, 1, 8, 1, 2, 1.5, 1]
year = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2015, 2016, 2017, 2018, 
        2019, 2020, 2021, 2022, 2023]

# Size of each point will be proportional to the average salary
sizes = [salary * 10 for salary in average_salary_millions]

# Different colors for different sports
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8C33', '#33FF8C', '#8C33FF', 
          '#FF3333', '#33FFA8', '#8CFF33', '#A833FF', '#33A8FF', '#A8FF33', '#FF338C', 
          '#338CFF', '#33FF33', '#FF33FF', '#33FF57']

# Create scatterplot
plt.figure(figsize=(16, 10))  # Adjust width and height for better visual
plt.scatter(sports, year, s=sizes, c=colors, alpha=0.8)

# Chart details
plt.title('Popular Sports and Average Salaries of Athletes by Year', fontsize=15, pad=20)
plt.xlabel('Sport')
plt.ylabel('Year')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Show the chart
plt.show()

import matplotlib.pyplot as plt

# Data for plotting
countries = ["USA", "UK", "Canada", "Australia", "Germany", "France",
             "Japan", "China", "India", "Brazil", "South Korea", "Spain",
             "Italy", "Russia", "Mexico", "Netherlands", "Saudi Arabia", "Switzerland",
             "Turkey", "Argentina", "Nigeria", "Egypt", "Pakistan", "Vietnam", "Indonesia"]
book_sales = [500, 450, 300, 250, 400, 350, 600, 700, 650, 220, 480, 280, 260, 330, 210, 290, 270, 310, 230, 190, 150, 170, 200, 180, 160]  # in millions
online_courses = [350, 300, 200, 150, 250, 220, 400, 450, 430, 170, 320, 190, 180, 240, 160, 210, 200, 230, 170, 150, 120, 130, 160, 140, 125]  # in thousands
reading_index = [0.92, 0.88, 0.90, 0.85, 0.87, 0.89, 0.94, 0.80, 0.78, 0.75, 0.91, 0.82, 0.81, 0.76, 0.74, 0.83, 0.79, 0.86, 0.73, 0.70, 0.65, 0.67, 0.69, 0.68, 0.66]

# Convert Reading Index to a size for the plot, with an arbitrary scale factor
sizes = [s * 1000 for s in reading_index]

# Create the Bubble Chart
plt.figure(figsize=(20, 16))
for i in range(len(countries)):
    plt.scatter(online_courses[i], book_sales[i], s=sizes[i], alpha=0.6,
                c=[f'#{int((1-reading_index[i])*255):02x}{int(reading_index[i]*255):02x}66'],
                edgecolors='w', linewidth=0.5)

plt.title('Book Sales vs Online Courses with Reading Index as Bubble Size', pad=20)
plt.xlabel('Online Courses in Thousands')
plt.ylabel('Book Sales in Millions')
plt.grid(True)

# Add country labels to bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (online_courses[i], book_sales[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center', fontsize=8, color='#444444')

plt.show()

import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
steps = [5000, 7000, 8000, 10000, 12000, 13000, 9000, 11000, 10000, 9500, 
         10500, 11500, 12000, 13000, 11000, 12500, 13500, 14000, 14500, 
         15000, 15500, 16000, 17000, 18000, 17500, 16500, 15500, 14000, 
         13000, 12000]
calories = [200, 300, 350, 450, 500, 550, 400, 470, 450, 420, 480, 510, 530, 
            550, 460, 520, 560, 590, 600, 620, 630, 640, 670, 700, 680, 650, 
            630, 600, 570, 540]

# Create a scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(days, steps, c="#1f77b4", label="Steps (Units)")
plt.scatter(days, calories, c="#ff7f0e", label="Calories Burned (kcal)")

# Customize the chart
plt.title("Daily Physical Activity")
plt.xlabel("Day of the Month")
plt.ylabel("Steps/Calories Burned")
plt.legend(loc="upper left")
plt.grid(True)

# Show the scatterplot
plt.show()

import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
steps = [5000, 6000, 7000, 8000, 10000, 12000, 11000, 9000, 8000, 7000, 6000, 5500]
calories_burned = [200, 250, 300, 350, 400, 450, 420, 380, 350, 300, 250, 220]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(12, 6))
plt.scatter(month_numbers, steps, c=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99',
                                     '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666',
                                     '#c6d3e6', '#f0e68c', '#dda0dd', '#e9967a'],
            s=calories_burned, alpha=0.6)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Steps')
plt.title('Monthly Steps and Calories Burned', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()
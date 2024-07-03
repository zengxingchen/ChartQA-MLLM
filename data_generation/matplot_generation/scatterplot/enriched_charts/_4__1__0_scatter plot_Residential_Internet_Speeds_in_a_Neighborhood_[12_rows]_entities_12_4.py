
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
books_read = [3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 6, 5]
hours_spent_reading = [15, 20, 22, 24, 30, 35, 40, 45, 38, 32, 28, 25]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(14, 8))
plt.scatter(month_numbers, books_read, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A1',
                                          '#A133FF', '#33FFF5', '#F5FF33', '#FF8F33',
                                          '#8FFF33', '#33FF8F', '#FF3333', '#3333FF'],
            s=hours_spent_reading, alpha=0.7)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Books Read')
plt.title('Monthly Books Read and Hours Spent Reading', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()
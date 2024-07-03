
import matplotlib.pyplot as plt

years = list(range(2010, 2024))
fiction = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
mystery = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
non_fiction = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
biography = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

plt.figure(figsize=(18, 12))
plt.stackplot(years, fiction, mystery, non_fiction, biography, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6'])

plt.title('Library Book Genre Popularity (2010-2023)', fontsize=20, pad=40)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Books Checked Out (in thousands)', fontsize=16)

plt.legend(['Fiction', 'Mystery', 'Non-Fiction', 'Biography'], loc='upper left')

plt.annotate(f'{biography[-1]}k Books',
             (years[-1], sum([fiction[-1], mystery[-1], non_fiction[-1], biography[-1]])),
             textcoords="offset points",
             xytext=(0,10),
             ha='center',
             fontsize=14,
             color='#FF33A6')

plt.show()
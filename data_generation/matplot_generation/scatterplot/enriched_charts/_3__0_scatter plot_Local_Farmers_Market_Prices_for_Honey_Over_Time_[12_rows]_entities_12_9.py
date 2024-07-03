
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
book_sales = [150, 200, 180, 220, 170, 210, 230, 240, 250, 260, 270, 280, 290, 
              300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 
              430, 440, 450, 460]
online_readers = [300, 320, 290, 340, 310, 330, 350, 360, 370, 380, 390, 400, 
                  410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 
                  530, 540, 550, 560, 570, 580]

plt.figure(figsize=(10, 6))
plt.scatter(book_sales, online_readers, color='#2E86C1')

plt.xlabel('Book Sales (Units)')
plt.ylabel('Online Readers (Thousands)')
plt.title('Book Sales vs Online Readers')

plt.show()
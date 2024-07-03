
import matplotlib.pyplot as plt

dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
likes = [120, 130, 125, 140, 135, 145, 130, 125, 150, 145, 135, 140, 155, 150, 140, 145, 160, 155, 150, 145, 150, 160, 155, 145, 140, 150, 130, 160, 155, 170, 165]
comments = [15, 20, 18, 22, 17, 25, 19, 16, 28, 23, 19, 21, 30, 24, 18, 22, 32, 26, 24, 20, 25, 35, 29, 21, 18, 27, 16, 34, 28, 38, 33]

plt.figure(figsize=(16, 12))
plt.scatter(likes, comments, color='#FF5733')
plt.xlabel('Likes')
plt.ylabel('Comments')
plt.title('Engagement on Social Media Posts Over a Month', pad=20)
plt.show()
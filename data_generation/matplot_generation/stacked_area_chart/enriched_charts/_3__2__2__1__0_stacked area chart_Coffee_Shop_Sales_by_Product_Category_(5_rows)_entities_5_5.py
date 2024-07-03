
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Online Courses': [150, 170, 200, 230, 250, 270, 290, 310, 330, 350, 370, 390],
    'In-person Workshops': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420],
    'Webinars': [180, 190, 210, 220, 240, 260, 280, 300, 320, 340, 360, 380],
}

df = pd.DataFrame(data)
x = df['Month']

plt.figure(figsize=(16, 10))
plt.stackplot(x, df['Online Courses'], df['In-person Workshops'], df['Webinars'], 
              colors=['#FF6347', '#4682B4', '#9ACD32'])

plt.title('Monthly Participation in Different Educational Activities', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Number of Participants', fontsize=16)

plt.annotate('Growth in Online Courses', xy=(11, df['Online Courses'][11] + df['In-person Workshops'][11] + df['Webinars'][11]), 
             xytext=(8, 1000), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.annotate('Webinars Popularity Surge', xy=(3, df['Webinars'][3] + df['In-person Workshops'][3] + df['Online Courses'][3]), 
             xytext=(1, 650), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.legend(['Online Courses', 'In-person Workshops', 'Webinars'], loc='upper left', fontsize=14)
plt.show()
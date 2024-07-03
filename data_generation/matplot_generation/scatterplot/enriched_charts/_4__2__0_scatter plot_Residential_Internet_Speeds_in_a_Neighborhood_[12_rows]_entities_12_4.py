
import matplotlib.pyplot as plt

Country = ['USA', 'UK', 'Canada', 'Australia', 'France', 'Germany', 'South Korea', 'Spain',
           'Brazil', 'Japan', 'India', 'Mexico', 'Netherlands', 'Sweden', 'Italy', 'Russia', 
           'Argentina', 'Nigeria']
Artist = ['Billie Eilish', 'Dua Lipa', 'Shawn Mendes', 'Tones and I', 'Christine and the Queens', 
          'Zedd', 'BTS', 'Rosalía', 'Anitta', 'Kenshi Yonezu', 'Arijit Singh', 'Camila Cabello', 
          'Martin Garrix', 'Zara Larsson', 'Laura Pausini', 'Nyusha', 'Lali', 'Tiwa Savage']
Event_Year = [2019, 2020, 2020, 2019, 2018, 2017, 2021, 2019, 2018, 2019, 2020, 2020, 2018, 2019, 
              2018, 2017, 2019, 2020]
Social_Media_Followers = [700, 600, 650, 500, 450, 430, 900, 400, 470, 520, 680, 620, 580, 530, 490, 460, 480, 510]
Online_Engagement = [520, 480, 510, 390, 370, 360, 780, 350, 380, 400, 450, 500, 470, 410, 380, 350, 360, 430]

plt.figure(figsize=(14, 10))
plt.scatter(Event_Year, Social_Media_Followers, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A1',
                                                    '#A133FF', '#33FFA1', '#FF5733', '#33A1FF',
                                                    '#A1FF33', '#5733FF', '#FF3357', '#33FF57',
                                                    '#3357FF', '#FF5733', '#33FF57', '#3357FF',
                                                    '#FF33A1', '#A133FF'], 
            s=Online_Engagement, alpha=0.6)

plt.xticks(range(2017, 2022))
plt.xlabel('Event Year')
plt.ylabel('Social Media Followers (thousands)')
plt.title('Social Media Followers vs Online Engagement of Artists', pad=20)
plt.xlim(2016.5, 2021.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
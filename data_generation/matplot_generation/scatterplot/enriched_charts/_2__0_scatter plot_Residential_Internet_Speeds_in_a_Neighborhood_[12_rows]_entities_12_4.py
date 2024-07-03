
import matplotlib.pyplot as plt

Country = ['USA', 'UK', 'Canada', 'Australia', 'France', 'Germany', 'South Korea', 'Spain',
           'Brazil', 'Japan', 'India', 'Mexico', 'Netherlands', 'Sweden', 'Italy', 'Russia', 
           'Argentina', 'Nigeria']
Artist = ['Taylor Swift', 'Ed Sheeran', 'Drake', 'Sia', 'David Guetta', 'Zedd', 'BTS', 'Enrique Iglesias', 
          'Anitta', 'Kenshi Yonezu', 'Arijit Singh', 'Thalía', 'Martin Garrix', 'Zara Larsson', 'Lorenzo Jovanotti', 
          'Nyusha', 'TINI', 'WizKid']
Song_Release_Year = [2017, 2017, 2018, 2016, 2017, 2019, 2018, 2016, 2019, 2018, 2017, 2016, 2018, 2019, 
                     2017, 2018, 2019, 2018]
Digital_Streams= [300, 350, 450, 220, 210, 230, 480, 340, 260, 400, 370, 270, 390, 280, 240, 310, 290, 350]
MV_Views = [200, 250, 370, 150, 180, 210, 500, 290, 200, 420, 310, 230, 360, 260, 180, 250, 220, 330]

plt.figure(figsize=(12, 8))
plt.scatter(Song_Release_Year, Digital_Streams, c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                                    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e',
                                                    '#2ca02c', '#d62728', '#9467bd', '#8c564b',
                                                    '#e377c2', '#7f7f7f'], 
            s=MV_Views, alpha=0.6)

plt.xticks(range(2016, 2020))
plt.xlabel('Song Release Year')
plt.ylabel('Digital Streams (millions)')
plt.title('Digital Streams vs MV Views Per Song', pad=20)
plt.xlim(2015.5, 2019.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

countries = ["France", "Italy", "Germany", "Spain", "United Kingdom", 
             "Netherlands", "United States", "Japan", "Canada", "Australia", 
             "South Korea", "Brazil", "India", "Mexico", "Russia", 
             "China", "Turkey", "Argentina", "South Africa", "Egypt"]
art_gallery_count = [1200, 1000, 900, 800, 750, 
                     600, 500, 450, 400, 350, 
                     300, 250, 200, 150, 100, 
                     90, 80, 70, 60, 50]
visitors_per_year = [30000, 25000, 22000, 20000, 18000, 
                     15000, 16000, 14000, 13000, 12000, 
                     11000, 9000, 7000, 5000, 4000, 
                     6000, 3000, 2000, 1000, 1500]
population = [67.3, 60.4, 83.1, 47.4, 67.1, 
              17.4, 331.0, 126.3, 38.0, 25.7, 
              51.8, 213.3, 1391.0, 128.9, 144.1, 
              1441.0, 84.3, 45.4, 60.0, 104.0]
average_income = [40000, 35000, 42000, 33000, 45000, 
                  44000, 60000, 37000, 46000, 47000, 
                  39000, 9000, 2100, 9200, 11400, 
                  10400, 9600, 8600, 5200, 3100]

sizes = [ai / 1000 for ai in average_income]

plt.figure(figsize=(20, 15))
for i in range(len(countries)):
    plt.scatter(art_gallery_count[i], visitors_per_year[i], s=sizes[i], alpha=0.5,
                c='#%02x%02x%02x' % (int((average_income[i]-min(average_income))/(max(average_income)-min(average_income))*255), 
                                     0, 
                                     int((1-(average_income[i]-min(average_income))/(max(average_income)-min(average_income)))*255)))

plt.title('Art Gallery Count vs Visitors Per Year with Average Income as Bubble Size', pad=20)
plt.xlabel('Art Gallery Count')
plt.ylabel('Visitors Per Year (in Thousands)')
plt.grid(True)

for i, country in enumerate(countries):
    plt.annotate(country, (art_gallery_count[i], visitors_per_year[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

plt.show()
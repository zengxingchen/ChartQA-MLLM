
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Artwork': ['Starry Night', 'Mona Lisa', 'The Persistence of Memory', 'Girl with a Pearl Earring', 'The Scream',
                'The Last Supper', 'Guernica', 'American Gothic', 'The Birth of Venus', 'Whistler\'s Mother',
                'Night Watch', 'The Kiss', 'The Arnolfini Portrait', 'A Sunday Afternoon on the Island of La Grande Jatte',
                'The School of Athens', 'The Garden of Earthly Delights', 'Liberty Leading the People', 'The Swing',
                'Oath of the Horatii', 'The Hay Wain'],
    'Year': [1889, 1503, 1931, 1665, 1893, 1498, 1937, 1930, 1486, 1871, 1642, 1908, 1434, 1886, 1511, 1515, 1830, 1767, 1784, 1821],
    'Price': [1000000, 780000000, 5500000, 30000000, 120000000, 450000000, 200000000, 7000000, 200000000, 4500000,
              200000000, 180000000, 140000000, 10000000, 150000000, 300000000, 200000000, 8500000, 175000000, 10000000],
    'Viewers': [2500000, 6000000, 1200000, 500000, 2300000, 3500000, 1800000, 600000, 2000000, 450000,
                4000000, 1700000, 1100000, 900000, 2500000, 3200000, 2100000, 850000, 1500000, 1000000],
    'Exhibition_Popularity': [95, 99, 85, 75, 90, 97, 88, 70, 92, 65, 96, 87, 80, 78, 93, 98, 91, 76, 82, 77]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))

sns.scatterplot(data=df, x="Year", y="Price", size="Viewers", sizes=(100, 2000),
                hue="Exhibition_Popularity", palette=["#8e44ad", "#2980b9", "#27ae60", "#f39c12",
                                                      "#d35400", "#c0392b", "#2ecc71", "#1abc9c"])

plt.title("Famous Artworks: Year, Price, and Exhibition Popularity", fontsize=18)
plt.xlabel("Year Created", fontsize=14)
plt.ylabel("Price (USD)", fontsize=14)

plt.legend(title="Exhibition Popularity (%)", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.show()
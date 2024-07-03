
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Country": ["France", "France", "France", "France",
                "Italy", "Italy", "Italy", "Italy",
                "Spain", "Spain", "Spain", "Spain",
                "Germany", "Germany", "Germany", "Germany",
                "UK", "UK", "UK", "UK",
                "Netherlands", "Netherlands", "Netherlands", "Netherlands",
                "Greece", "Greece", "Greece", "Greece"],
    "Destination": ["Paris", "Nice", "Lyon", "Marseille",
                    "Rome", "Venice", "Milan", "Florence",
                    "Barcelona", "Madrid", "Seville", "Valencia",
                    "Berlin", "Munich", "Hamburg", "Frankfurt",
                    "London", "Edinburgh", "Manchester", "Liverpool",
                    "Amsterdam", "Rotterdam", "Utrecht", "The Hague",
                    "Athens", "Santorini", "Mykonos", "Crete"],
    "Number of Visitors": [1500, 800, 500, 450, 
                           1400, 900, 600, 500, 
                           1300, 1200, 700, 600, 
                           1100, 800, 700, 500, 
                           1600, 900, 800, 700, 
                           1000, 700, 500, 400, 
                           800, 600, 500, 400]
}

df = pd.DataFrame(data)
grouped_data = df.groupby("Destination").sum().reset_index()

colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0","#ffb3e6","#c4e17f","#76D7C4","#ffcccb","#c2f0c2",
          "#ff6666","#ffb366","#99ccff","#66cccc","#ffccff","#ff99cc","#66c2ff","#99ffcc","#cc99ff","#ccffcc",
          "#e6b3b3","#e6b333","#b3b3cc","#b33333","#b3e6cc","#cc6666","#99e699","#ff8080"]

plt.figure(figsize=(14, 10))
squarify.plot(sizes=grouped_data['Number of Visitors'], label=grouped_data['Destination'], alpha=0.8, color=colors)
plt.title('Top Travel Destinations in Europe by Visitor Numbers')
plt.axis('off')
plt.show()
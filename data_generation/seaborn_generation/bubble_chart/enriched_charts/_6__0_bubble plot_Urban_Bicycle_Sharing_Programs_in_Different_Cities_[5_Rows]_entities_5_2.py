
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Manufacturer": ["Marvel Studios", "Warner Bros", "Universal Pictures", "Disney", "Paramount",
                     "Sony Pictures", "20th Century Studios", "Lionsgate", "MGM", "New Line Cinema",
                     "DreamWorks", "Focus Features", "STX Entertainment", "A24", "Blumhouse"],
    "Revenue": [2200, 1500, 1200, 1000, 900, 800, 700, 600, 500, 400, 300, 250, 200, 150, 100],
    "Budget": [200, 150, 100, 80, 60, 50, 40, 30, 20, 10, 8, 5, 4, 3, 2],
    "BoxOffice": [2800, 2200, 1700, 1600, 1400, 1200, 900, 800, 700, 500, 400, 350, 300, 250, 200],
    "MoviesReleased": [3, 4, 5, 2, 3, 4, 3, 5, 2, 3, 1, 2, 1, 3, 4],
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=data, x="Budget", y="Revenue", size="MoviesReleased",
                               sizes=(100, 1000), alpha=0.7, palette=["#FF5733", "#33FF57", "#3357FF", 
                               "#8357FF", "#FF57B9", "#57FFC8", "#FFDA57", "#7CFF57",
                               "#578AFF", "#EF57FF", "#FF5757", "#57FFBE", "#57D2FF",
                               "#FF9D57", "#A7FF57"])

bubble_chart.set_xlabel("Average Movie Budget ($ Millions)")
bubble_chart.set_ylabel("Total Revenue ($ Millions)")
bubble_chart.set_title("Movie Industry Financials by Major Studios in 2023", pad=20)

h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Movies Released", borderpad=1, loc='upper left', labelspacing=1.5)

plt.show()
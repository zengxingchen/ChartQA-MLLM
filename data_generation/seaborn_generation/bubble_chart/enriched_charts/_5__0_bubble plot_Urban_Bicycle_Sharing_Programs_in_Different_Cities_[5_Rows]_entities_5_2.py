
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Topic": ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", 
              "Romance", "Historical Fiction", "Biography", "Self-Help", "Young Adult", 
              "Thriller", "Graphic Novel", "Poetry", "Children's Books", "Horror"],
    "Author": ["J.K. Rowling", "Malcolm Gladwell", "Isaac Asimov", "J.R.R. Tolkien", "Agatha Christie", 
               "Nicholas Sparks", "Hilary Mantel", "Michelle Obama", "James Clear", "Suzanne Collins", 
               "Stephen King", "Alan Moore", "Rupi Kaur", "Dr. Seuss", "H.P. Lovecraft"],
    "BooksSold": [500, 350, 200, 450, 300, 250, 150, 400, 350, 320, 450, 150, 100, 400, 200],
    "Price": [20, 15, 25, 22, 18, 17, 20, 19, 14, 16, 21, 23, 10, 12, 18],
    "Rating": [4.9, 4.8, 4.7, 4.9, 4.6, 4.5, 4.4, 4.8, 4.7, 4.7, 4.8, 4.7, 4.6, 4.9, 4.5]
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=data, x="Price", y="Rating", size="BooksSold",
                               sizes=(100, 1000), alpha=0.7, palette=["#1f77b4", "#ff7f0e", "#2ca02c", 
                               "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
                               "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e", "#2ca02c",
                               "#d62728", "#9467bd"])

bubble_chart.set_xlabel("Average Book Price ($)")
bubble_chart.set_ylabel("Average Rating (out of 5)")
bubble_chart.set_title("Top Authors by Genre: Book Sales, Price, and Rating", fontsize=16, pad=20)

h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Books Sold (Thousands)", borderpad=1, loc='upper right', labelspacing=1.5)

plt.show()
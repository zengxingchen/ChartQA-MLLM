
import matplotlib.pyplot as plt

# Data for scatterplot
genres = ["Fiction", "Non-Fiction", "Children's", "Mystery", "Romance", "Science Fiction", 
          "Fantasy", "Historical", "Horror", "Thriller", "Biography", "Self-Help", 
          "Cookbooks", "Graphic Novels", "Poetry", "Classics", "Drama", "Adventure", 
          "Memoir", "Essays", "Humor", "Religion", "True Crime", "Travel"]
books_sold_millions = [25, 15, 30, 20, 18, 12, 22, 17, 10, 15, 8, 9, 11, 6, 7, 14, 16, 19, 13, 8, 9, 11, 7, 10]
publication_year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                    2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Size of each point will be proportional to the books sold
sizes = [sold * 10 for sold in books_sold_millions]

# Different colors for different genres
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', 
          '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', 
          '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#f7b6d2', 
          '#8c564b', '#ff9896', '#9467bd']

# Create scatterplot
plt.figure(figsize=(14, 9))  # Adjust width and height for better visual
plt.scatter(genres, publication_year, s=sizes, c=colors, alpha=0.8)

# Chart details
plt.title('Books Sold and Publication Years by Genre', fontsize=15, pad=20)
plt.xlabel('Genre')
plt.ylabel('Publication Year')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Show the chart
plt.show()
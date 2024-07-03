
import matplotlib.pyplot as plt

data = {
    'Category': ['Thriller', 'Comedy', 'Drama', 'Action', 'Romance', 'Documentary', 'Horror', 
                 'Sci-Fi', 'Animation', 'Mystery', 'Biography', 'Fantasy', 'Musical', 'Adventure', 
                 'Crime', 'Family', 'Western', 'War', 'Historical', 'Sport', 'Superhero', 'Anime', 
                 'Independent', 'Experimental', 'Period', 'Film-Noir'],
    'Calories': [300, 400, 500, 350, 250, 150, 450, 350, 300, 275, 200, 400, 500, 450, 375, 
                 275, 350, 425, 300, 375, 475, 325, 275, 225, 350, 250],
    'Protein (g)': [10, 8, 12, 15, 5, 7, 6, 13, 9, 11, 10, 14, 16, 13, 12, 8, 10, 11, 9, 14, 15, 
                    10, 7, 8, 11, 6],
    'Satisfaction Score': [85, 78, 82, 90, 70, 75, 65, 88, 80, 76, 74, 92, 84, 89, 77, 73, 79, 86, 
                           81, 88, 91, 79, 72, 65, 80, 68]
}

size = [value * 10 for value in data['Calories']]

plt.figure(figsize=(18, 12))

scatter = plt.scatter(data['Protein (g)'], data['Satisfaction Score'], 
                      s=size, alpha=0.6, 
                      c=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#FFBF33', '#FF33EC', 
                         '#9933FF', '#33FFA7', '#FF3339', '#33A1FF', '#A1FF33', '#F533FF', '#33FFDA', 
                         '#BF33FF', '#33FF85', '#FFA733', '#FF3383', '#33CFFF', '#FF5733', '#33FFAD', 
                         '#FF6F33', '#3390FF', '#FFD833', '#FF333C', '#33E1FF'])

plt.title('Movie Genre Popularity and Nutritional Comparison', pad=20)
plt.xlabel('Average Rating (out of 10)')
plt.ylabel('Audience Satisfaction Score')

for index, category in enumerate(data['Category']):
    plt.text(data['Protein (g)'][index], data['Satisfaction Score'][index], 
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Topic': ['Portrait Painting', 'Sculpture', 'Digital Art', 'Photography', 'Graphic Design', 'Architecture', 
              'Industrial Design', 'Fashion Design', 'Textile Design', 'Ceramics', 'Jewelry Design', 
              'Interior Design', 'Illustration', 'Printmaking', 'Video Art'],
    'Viewership': [4200, 3800, 3400, 3200, 3000, 2800, 2600, 2400, 2200, 2000, 1800, 1600, 1400, 1200, 1000],
    'Category': ['Art', 'Art', 'Art', 'Art', 'Design', 'Design', 'Design', 'Design', 'Design', 'Art', 
                 'Design', 'Design', 'Art', 'Art', 'Art']
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
cmap = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76D7C4', 
        '#ff7f50', '#4682B4', '#DA70D6', '#32CD32', '#B22222', '#FF6347', '#FFD700']

squarify.plot(sizes=df['Viewership'], label=df['Topic'], color=cmap, alpha=0.8)

plt.title('Popular Art & Design Topics by Interest', fontsize=18)
plt.axis('off')

plt.show()
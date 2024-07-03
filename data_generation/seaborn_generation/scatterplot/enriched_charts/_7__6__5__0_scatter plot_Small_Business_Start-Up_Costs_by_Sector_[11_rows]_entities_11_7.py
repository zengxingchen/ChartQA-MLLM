
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Data points
data = {
    'Category': ['Luxury_Brands', 'Streetwear', 'Athleisure', 'Casual_Wear', 'Formal_Wear', 'Vintage_Fashion', 'Eco_Fashion', 
                 'Fast_Fashion', 'High_Street', 'Handmade_Fashion', 'Bohemian', 'Gothic', 'Punk', 'Retro', 'Hip_Hop', 
                 'Grunge', 'Preppy', 'Minimalist', 'Avant_Garde', 'Sportswear', 'Business_Casual', 'Y2K', 'Loungewear', 
                 'Indie', 'Artisanal', 'Haute_Couture', 'Techwear', 'Costume_Design', 'Glam', 'Beachwear'],
    'Popularity_Rating': [90, 85, 80, 75, 70, 65, 95, 60, 55, 50, 88, 58, 78, 68, 83, 62, 73, 77, 92, 87, 72, 67, 82, 66, 71, 93, 81, 74, 79, 76],
    'Sales_Figure': [500, 450, 400, 350, 300, 250, 550, 200, 150, 100, 480, 180, 380, 280, 420, 220, 330, 370, 520, 460, 320, 270, 410, 260, 310, 530, 400, 340, 390, 360]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(18, 14))

# Draw a seaborn scatter plot
sb.scatterplot(data=df, x="Popularity_Rating", y="Sales_Figure", palette=['#FF4500', '#1E90FF'], s=100)

# Additional customizations
plt.title('Popularity vs. Sales in Fashion Categories', pad=20)
plt.xlabel('Popularity Rating')
plt.ylabel('Sales Figure')
plt.grid(True)

# Show the plot
plt.show()
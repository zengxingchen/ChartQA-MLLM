
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
organic_search = [12000, 15000, 18000, 20000, 22000, 25000, 27000, 30000, 28000, 26000, 24000, 23000]
social_media = [5000, 6000, 6500, 7000, 7200, 7500, 7700, 8000, 8500, 9000, 9500, 10000]
email = [8000, 7500, 9000, 9500, 10000, 11000, 11500, 12000, 12500, 10500, 10000, 9500]
referral = [3000, 3500, 3700, 4000, 4500, 4700, 5000, 5300, 5500, 5800, 6000, 6500]

plt.figure(figsize=(14, 8))
plt.stackplot(months, organic_search, social_media, email, referral, 
              colors=['#FF6347', '#3CB371', '#FFD700', '#1E90FF'])

plt.title('Monthly Website Traffic Sources', fontdict={'fontsize': 18})
plt.xlabel('Month')
plt.ylabel('Visitors')

peak_organic_month = months[organic_search.index(max(organic_search))]
peak_organic_value = max(organic_search)
plt.text(peak_organic_month, peak_organic_value, 'Peak for Organic Search', ha='center', va='bottom')

plt.show()
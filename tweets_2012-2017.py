import pandas, matplotlib.pyplot as plt

# pandas.read_csv('tweets.csv', usecols=['timestamp'], index_col=0).to_csv('tweet_timestamps.csv')
tweets_archive = pandas.DataFrame(pandas.read_csv('tweet_timestamps.csv'))
timestamps = pandas.to_datetime(tweets_archive.timestamp)

tweets_timestamps = []

for ts in timestamps.dt.year:
    tweets_timestamps.append(ts)

tweets_timestamps = list(tweets_timestamps.__reversed__())

count2017 = tweets_timestamps.count(2017)
count2016 = tweets_timestamps.count(2016)
count2015 = tweets_timestamps.count(2015)
count2014 = tweets_timestamps.count(2014)
count2013 = tweets_timestamps.count(2013)
count2012 = tweets_timestamps.count(2012)

tweets_count = [count2012, count2013, count2014, count2015, count2016, count2017]
years = [2012, 2013, 2014, 2015, 2016, 2017]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(years, tweets_count)
ax2.bar(years, tweets_count)

ax1.set_title('Line Plot')
ax1.set_xlabel('Year')
ax1.set_ylabel('# of Tweets')

ax2.set_title('Bar Plot')
ax2.set_xlabel('Year')
ax2.set_ylabel('# of Tweets')

plt.show()

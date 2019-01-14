import pandas, matplotlib.pyplot as plt

# pandas.read_csv('tweets.csv', usecols=['timestamp'], index_col=0).to_csv('tweet_timestamps.csv')
tweets_archive = pandas.read_csv('tweet_timestamps.csv')

timestamps = tweets_archive['timestamp']

tweets_timestamps = []

for ts in timestamps:
    ts = str(ts).strip('+0000')
    ts = ts.rsplit(' ')[0]
    ts = ts.rsplit('-')[0]

    tweets_timestamps.append(int(ts))

tweets_timestamps = list(tweets_timestamps.__reversed__())

count2017 = tweets_timestamps.count(2017)
count2016 = tweets_timestamps.count(2016)
count2015 = tweets_timestamps.count(2015)
count2014 = tweets_timestamps.count(2014)
count2013 = tweets_timestamps.count(2013)
count2012 = tweets_timestamps.count(2012)

tweets_count = [count2012, count2013, count2014, count2015, count2016, count2017]
years = [2012, 2013, 2014, 2015, 2016, 2017]

fig = plt.figure()

bar_plot = fig.add_subplot(1, 2, 1)
bar_plot.bar(years, tweets_count, color='w', edgecolor='k')
_ = plt.xlabel('Year')
_ = plt.ylabel('# of Tweets')
_ = plt.title('Tweets Over The Years')

line_plot = fig.add_subplot(1, 2, 2)
line_plot.plot(years, tweets_count, color='r')
_ = plt.xlabel('Year')
_ = plt.ylabel('# of Tweets')
_ = plt.title('Tweets Over The Years')

plt.show()
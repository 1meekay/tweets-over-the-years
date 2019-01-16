# tweets-over-the-years

A data visualization of the amount of tweets and retweets on my Twitter account since its creation using my Twitter export data

Using a .csv file of exported Twitter data I requested from Twitter sometime two years ago, I created my first Data visualization project to simply show the amount of tweets and retweets on my account since its creation in 2012.

To hide info such as tweet IDs, tweet URLs, and the tweets themselves from the .csv, I used pandas to convert the timestamps column into a .csv of its own.

The program produces a side by side of a bar chart and line plot representation of the number of tweets and retweets over the 6 year span.

================================================================

tweets_2012-2017.py   -- main program

tweet_timestamps.csv  -- truncated Twitter export .csv file

================================================================

updated 1/16

changed this:

    for ts in timestamps:
        ts = str(ts).strip('+0000')
        ts = ts.rsplit(' ')[0]
        ts = ts.rsplit('-')[0]

        tweets_timestamps.append(int(ts))

into this:

    for ts in timestamps.dt.year:
        tweets_timestamps.append(ts)

using:

    timestamps = pandas.to_datetime(timestamps)

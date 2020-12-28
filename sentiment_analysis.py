import tweepy,sys,re
from textblob import TextBlob
import credential
import matplotlib.pyplot as plt

class Tweet_analysis():
    def percentage(self,part,whole):
        self.part = part
        self.whole = whole
        return float(100*(part/whole))

    def clean_tweet(self,tweets):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(\w+:\/\/\S+)", " ", tweets).split())

    def analyze(self):
        auth = tweepy.OAuthHandler(credential.CONSUMER_KEY,credential.CONSUMER_SECRET)
        auth.set_access_token(credential.ACCESS_TOKEN,credential.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        topic = input('enter the topic or profile you want to search about')
        no_of_search = int(input('enter number of tweets'))

        tweets_list = []
        for tweets in tweepy.Cursor(api.home_timeline,id=topic).items(no_of_search):
            tweets_list.append(tweets.text)
        print(tweets_list)


        #declaring variables negative,positive and neutral

        negative = 0
        positive = 0
        neutral = 0

        for i in tweets_list:
            analysis = TextBlob(i)
            if analysis.polarity > 0.00:
                positive = positive+1
            elif analysis.polarity < 0.00:
                negative = negative+1
            elif analysis.polarity==0:
                neutral = neutral+1

        positive_percentage = Tweet_analysis.percentage(self,part=positive, whole=no_of_search)
        print(positive_percentage)
        negative_percentage = Tweet_analysis.percentage(self, part=negative, whole=no_of_search)
        print(negative_percentage)
        neutral_percentage = Tweet_analysis.percentage(self, part=neutral, whole=no_of_search)
        print(neutral_percentage)
        '''negative = Tweet_analysis.percentage(self,part=negative, whole=no_of_search)
        neutral = Tweet_analysis.percentage(self,part=neutral, whole=no_of_search)
        polarity = Tweet_analysis.percentage(self,part=polarity,whole=no_of_search)

        positive = format(positive,'.2f')
        negative = format(negative, '.2f')
        neutral = format(neutral, '.2f')


        print('how people are reacting to', topic,'by analyzing',no_of_search,'tweets')

        if(polarity==0):
            print('Neutral')
        elif(polarity<0.00):
            print('Negative')
        elif(polarity>0.00):
            print('Positive')'''

        label = ['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
        sizes = [positive,neutral,negative]
        colors = ['yellow','green','red']
        patches,text = plt.pie(sizes,colors=colors,startangle=90)
        plt.legend(patches,label,loc="best")
        plt.title('tweet analysis')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()



        '''for tweet in tweepy.Cursor(api.user_timeline,id=topic).items(no_of_search):
            tweets.append(tweet)
        print(tweets)'''

tweet_analyzer = Tweet_analysis()
tweet_analyzer.analyze()

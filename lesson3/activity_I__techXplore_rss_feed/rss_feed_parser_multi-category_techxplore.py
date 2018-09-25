import feedparser
import pymysql
 
 
#mysql
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')
# sort by unique or duplicated articles
articles = []
#base_url = 'http://rss.infozine.com/kc/'
techxplore_base_url ='https://techxplore.com/rss-feed/'
#https://techxplore.com/feeds/
techxplore_categories_url_list = ['automotive-news',
						'business-tech-news',
						'computer-sciences-news',
						'consumer-gadgets-news',
						'energy-green-tech-news',
						'engineering-news',
						'hardware-news',
						'hi-tech-news',
						'internet-news',
						'robotics-news',
						'security-news',
						'semiconductors-news',
						'software-news',
						'telecom-news']


for category_url in techxplore_categories_url_list:
	feed_url = techxplore_base_url + category_url +'/'
	# obtain feed data from the url
	feed = feedparser.parse(feed_url)

	# infozine.com
	for article in feed.entries:
		row_list = []
		title = article.title
		description = article.description
		link = article.link
		category = article.category
		pubDate = article.published
		unique_article_id = article.guid[4:]
		 
		row_list.extend((title, description, link, category, pubDate, unique_article_id))
		articles.append(row_list)

#add all posts to write to the db with 
with conn.cursor() as cur:
	for row in articles:
		cur.execute("CREATE TABLE IF NOT EXISTS all_techxplore_articles (id INTEGER NOT NULL AUTO_INCREMENT, title VARCHAR(350), \
														description VARCHAR(2000), \
														link VARCHAR(350),\
									                    category VARCHAR(350),\
									                    pubDate VARCHAR(150),\
									                    unique_article_id INTEGER NOT NULL, 			\
									                    PRIMARY KEY (unique_article_id), \
									                    KEY (id) );")
		cur.execute("INSERT IGNORE INTO linkedTopicDB2.all_techxplore_articles (title, description, link, category, pubDate, unique_article_id) VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
	conn.commit()
	conn.close()

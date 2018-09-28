import feedparser
import pymysql
#mysql connection 
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port=<port number>, #eg. 3306
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')

feed_url = 'http://rss.infozine.com/kc/music.xml'
# obtain feed data from the url
feed_object = feedparser.parse(feed_url)
# create an empty list
articles_list = []
# infozine.com
for article in feed_object.entries:
	row_list = []
	title = article.title
	description = article.description
	link = article.link
	category = feed_object.channel.category[:-1]
	pubDate = article.published
	unique_article_id = article.guid[-6:-1]
	# extend()-Iterates arguments adding RSS element to the row_list
	row_list.extend((title, description, link, category, pubDate, unique_article_id))
	# append() - Appends objects at the end off the articles_list
	articles_list.append(row_list)
#add all posts to write to the db with 
with conn.cursor() as cur:
	for row in articles_list:
		cur.execute("CREATE TABLE IF NOT EXISTS infozine_articles (\
			id int NOT NULL auto_increment, \
			title VARCHAR(350), \
			description VARCHAR(2000), \
			link VARCHAR(350),\
            category VARCHAR(350),\
            pubDate VARCHAR(150),\
            unique_article_id VARCHAR(150), 			\
            PRIMARY KEY (id));")
		cur.execute("INSERT INTO \
			<enter your db name>.infozine_articles \
			(title, description, link, category, pubDate, unique_article_id) \
			VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
	conn.commit()
	conn.close()

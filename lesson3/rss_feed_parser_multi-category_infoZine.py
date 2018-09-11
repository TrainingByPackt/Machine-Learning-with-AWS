import feedparser
import pymysql
from bs4 import BeautifulSoup 
import requests
import re 

#mysql connection 
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')

# use_unicode=True,
# charset='utf8'
# UnicodeEncodeError: 'latin-1' codec can't encode 
# character '\u2019' in position 237: ordinal
#  not in range(256)

base_url = 'http://rss.infozine.com/kc/'


categories_url_list = ['arts.xml',
					'business.xml',
					'community.xml',
					'computer.xml',
					'consumer.xml',
					'dance.xml',
					'education.xml',
					'environment.xml',
					'family.xml',
					'farmers_market.xml',
					'features.xml',
					'film.xml',
					'food.xml',
					'gallery.xml',
					'health.xml',
					'internet.xml',
					'kids.xml',
					'literature.xml',
					'music.xml',
					'national.xml',
					'pets.xml',
					'politics.xml',
					'recipes.xml',
					'science.xml',
					'sports.xml',
					'theatre.xml',
					'travel.xml',
					'international.xml']

# create an empty list
articles_list = []


for category_url in categories_url_list:
	feed_url = base_url + category_url
	# obtain feed data from the url
	feed_object = feedparser.parse(feed_url)

	# infozine.com
	for article in feed_object.entries:
		row_list = []
		title = article.title
		description = article.description
		link = article.link
		category = category_url[:-4]
		pubDate = article.published

		# #parse article_content
		headers={'User-Agent':'Mozilla/5.0'}
		resp = requests.get(link, headers=headers)
		soup = BeautifulSoup(resp.content, 'lxml')
		contentArticle = soup.find('div', attrs={"class" : "contentArticle"})
		total_article_content = contentArticle.text
		 
		# slice articel content after (- infoZine -) is 12 characters long
		index_of_infoZine_substring = total_article_content.rfind('- infoZine -')
		index_to_start_slice = index_of_infoZine_substring + 12
		article_content = total_article_content[index_to_start_slice:]

		# extend()
		# Iterates over its arguments adding RSS elements to the  row_list
		row_list.extend((title, description, link, article_content, category, pubDate))
		# append() - Appends objects at the end off the list (i.e. articles_list).
		articles_list.append(row_list)


# import all articles to MySQL database
# avoid importing duplicate articles 
with conn.cursor() as cur:
	for row in articles_list:
		cur.execute("CREATE TABLE IF NOT EXISTS \
			all_infozine_articles \
			(id INTEGER NOT NULL AUTO_INCREMENT, \
			title VARCHAR(350), \
			description VARCHAR(2000), \
			link VARCHAR(350) NOT NULL,\
            article_content VARCHAR(8000), \
            category VARCHAR(350),\
            pubDate VARCHAR(150),\
            PRIMARY KEY (link), \
            KEY id (id) );") 
		cur.execute("INSERT IGNORE INTO \
			linkedTopicDB2.all_infozine_articles \
			(title, description, link, article_content, category, pubDate) \
			VALUES \
			(%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
	conn.commit()
	conn.close()
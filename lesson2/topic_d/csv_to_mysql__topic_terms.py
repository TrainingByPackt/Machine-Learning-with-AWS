import csv
import os
import pymysql
row_list = []
#mysql
conn = pymysql.connect(db='<your db name>',  # eg. linkedTopicsDB2
						host='<your host name > ',   # eg. 'linkedtopicsdbinstance2.hslfhsmwlcww.us-east-1.rds.amazonaws.com'
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')
 
# manual CSV export from MySQL
with open('topic-terms.csv', 'r', encoding="utf-8") as in_file:
	for row in in_file:
		
		readCSV = csv.reader(in_file)
		for row in readCSV:
			topic = row[0]
			term = row[1]
			weight = row[2]
			row_list.append(row)
#import all articles to MySQL database
with conn.cursor() as cur:
	for row in row_list:
		cur.execute("CREATE TABLE IF NOT EXISTS known_structure__topic_terms (\
			id INTEGER NOT NULL AUTO_INCREMENT, \
			topic INTEGER NOT NULL, \
			term VARCHAR(400) NOT NULL, \
			weight FLOAT NOT NULL,\
            PRIMARY KEY (id) );") 
		cur.execute("INSERT IGNORE INTO \
			linkedTopicDB2.known_structure__topic_terms \
			(topic, term, weight) \
			VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
	conn.commit()
	conn.close()
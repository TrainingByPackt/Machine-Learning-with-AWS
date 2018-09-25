import csv
import os
import pymysql
row_list = []
#mysql
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')
###############################################################
#  topic-terms
###############################################################
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
		cur.execute("CREATE TABLE IF NOT EXISTS \
			known_structure_topic_terms \
			(id INTEGER NOT NULL AUTO_INCREMENT,  \
			topic INTEGER, \
			term VARCHAR(800) NOT NULL, \
			weight FLOAT NOT NULL,\
            PRIMARY KEY (id) );") 
		cur.execute("INSERT IGNORE INTO \
			linkedTopicDB2.known_structure_topic_terms \
			(topic, term, weight) \
			VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
	conn.commit()
	conn.close()
#############################################################
#  doc-topics
##############################################################
with open('doc-topics.csv', 'r', encoding="utf-8") as in_file:
	for row in in_file:
		
		readCSV = csv.reader(in_file)
		for row in readCSV:
			docname = row[0]
			topic = row[1]
			proportion = row[2]
			row_list.append(row)
#import all articles to MySQL database
with conn.cursor() as cur:
	for row in row_list:
		cur.execute("CREATE TABLE IF NOT EXISTS \
			known_structure_doc_topics \
			(id INTEGER NOT NULL AUTO_INCREMENT, \
			docname VARCHAR(256) NOT NULL, \
			topic INTEGER NOT NULL, \
			proportion FLOAT NOT NULL,\
            PRIMARY KEY (id) );") 
		cur.execute("INSERT IGNORE INTO \
			linkedTopicDB2.known_structure_doc_topics \
			(docname, topic, proportion) \
			VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
	conn.commit()
	conn.close()
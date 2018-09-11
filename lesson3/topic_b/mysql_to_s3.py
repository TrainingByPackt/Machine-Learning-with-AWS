import pymysql
import os

#local text file to s3 python modules
import boto
from boto.s3.key import Key


####################################################################
# mysql to local text files
####################################################################
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')

article_result_list = []

text_file_directory_output = os.getcwd() + "\\<input directory>\\"

with conn.cursor() as cur:
	cur.execute("""SELECT * FROM <input db name>.<input table name>""")
	for row in cur:
		article_result_list.append(list(row))

	for line in article_result_list:
		#article_description = line[2]
		article_content = line[5]
		articleId = line[7]
		category = line[4]
		out_file = open(text_file_directory_output + \
			"category_{0}__articleID_{1}.txt".format(category, articleId), 'w+', encoding="utf-8")
		#out_file.write(article_description)
		out_file.write(articleContent)
out_file.close() 


############################################################
# local text files to S3
############################################################
AWS_ACCESS_KEY_ID = '<>'
AWS_SECRET_ACCESS_KEY = '<>'
END_POINT = '<>'     # eg. us-east-1
S3_HOST = '<>'       # eg. s3.us-east-1.amazonaws.com
BUCKET = '<>'
BUCKET_DIRECTORY = '<input directory>/'             
        

conn = boto.s3.connect_to_region(
			END_POINT,
			aws_access_key_id=AWS_ACCESS_KEY_ID,
			aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
			host=S3_HOST)


LOCAL_PATH = os.getcwd() +'\\<input directory>\\'
text_files_list = [f for f in os.listdir(LOCAL_PATH) if f.endswith('.txt')]


for file in text_files_list:
	bucket_obj = conn.get_bucket(BUCKET)
	k = Key(bucket_obj)
	k.key = BUCKET_DIRECTORY + file
	k.set_contents_from_filename(LOCAL_PATH + file)

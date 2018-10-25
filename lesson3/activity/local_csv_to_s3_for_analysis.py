import boto3

# import pandas and assign to the popular 'pd' convention
import pandas as pd 

# Create an S3 client
s3 = boto3.client('s3')

# Creates a variable with the bucket name
bucket_name = '<insert a unique bucket name>' 

# Creates a new bucket 
s3.create_bucket(Bucket=bucket_name)

# Create a list of file names
filenames_list = ['doc-topics.csv', 'topic-terms.csv']

# Iterates on each file in the  filenames_list
for filename in filenames_list:
	# Uploads each CSV to the created bucket
	s3.upload_file(filename, bucket_name, filename)
	# checks if the filename is 'doc-topics.csv'
	if filename == 'doc-topics.csv':
		# gets the 'doc-topics.csv' file as an object
		obj = s3.get_object(Bucket=bucket_name, Key=filename)
		# reads the csv and assigns to doc_topics 
		doc_topics = pd.read_csv(obj['Body'])
		
	else:
		obj = s3.get_object(Bucket=bucket_name, Key=filename)
		topic_terms = pd.read_csv(obj['Body'])
		

# merge files on topic column to obtain the most common terms per document
merged_df = pd.merge(doc_topics, topic_terms, on='topic')

# print the merged_df to the console
print(merged_df) 

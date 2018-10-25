import os
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Creates a variable with the bucket name
BUCKET_NAME = '<insert a unique bucket name>'   #
BUCKET_FOLDER = 'negative_movie_review_files/' 

LOCAL_PATH = os.getcwd() +'\\local_folder__negative_movie_review_files\\'
text_files_list = [f for f in os.listdir(LOCAL_PATH) if f.endswith('.txt')]

for filename in text_files_list:
	print(filename)
	s3.upload_file(LOCAL_PATH + filename, BUCKET_NAME, BUCKET_FOLDER + filename)

print("completed uploading files.")

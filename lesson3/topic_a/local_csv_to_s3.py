import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Creates a variable with the bucket name
bucket_name = '<insert bucket name>'  

# Creates a new bucket 
s3.create_bucket(Bucket=bucket_name)

# Create a list of file names
filenames_list = ['doc-topics.csv', 'topic-terms.csv']

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
for filename in filenames_list:
	s3.upload_file(filename, bucket_name, filename)
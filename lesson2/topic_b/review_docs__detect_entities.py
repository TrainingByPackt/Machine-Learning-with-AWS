# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json
import os

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='<input region>')

 
textfile_list = []
cwd = os.getcwd()

for name in os.listdir(".\\review_documents"):
	if name.endswith(".txt"):
		textfile_list.append(name)

#print(json.dumps(comprehend.batch_detect_dominant_language(TextList = textfile_list), sort_keys=True, indent=4))
print('Calling BatchDetectDominantLanguage')

for file in textfile_list:
	path_and_file = cwd + "\\review_documents\\" + file
	f = open(path_and_file, "r", encoding='utf8')
	file = f.read()
	print(json.dumps(comprehend.detect_entities(Text = file, LanguageCode='en'), sort_keys=True, indent=4))
 
 
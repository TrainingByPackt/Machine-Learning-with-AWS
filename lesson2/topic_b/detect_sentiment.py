# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='<input region>')

# provide a text string to analyze
english_string = 'Today is my birthday, I am so happy.'

print('Calling DetectSentiment')
# json.dumps() writes JSON data to a Python string
print('english_string results:')
print(json.dumps(comprehend.detect_sentiment(Text = english_string, 
											LanguageCode='en'), 
											sort_keys=True, 
											indent=4))
print('End of DetectSentiment\n')
# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='<input region>') #us-east-1

# provide english text to analyze
english_string = 'robert redfords a river runs through is not a film i watch often. \
		it is a masterpiece, one of the better films of recent years. The acting and direction is top-notch \
		 never sappy , always touching.'

print('Calling DetectKeyPhrases')
# json.dumps() writes JSON data to a Python string
print(json.dumps(comprehend.detect_key_phrases(Text = english_string, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')
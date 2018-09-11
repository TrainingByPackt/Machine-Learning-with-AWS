# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='<input region>')

# provide english and spanish text to analyze
english_string = 'Machine Learning is fascinating.'
spanish_string = 'El aprendizaje automático es fascinante.'

print('Calling DetectDominantLanguage')

print('english_string result:')
# json.dumps() writes JSON data to a Python string
print(json.dumps(comprehend.detect_dominant_language(Text = english_string), sort_keys=True, indent=4))

print('\n spanish_string result:')
print(json.dumps(comprehend.detect_dominant_language(Text = spanish_string), sort_keys=True, indent=4))
print('End of DetectDominantLanguage\n')
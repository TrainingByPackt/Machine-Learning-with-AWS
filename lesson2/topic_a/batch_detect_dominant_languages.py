# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='<input region>')

# provide english and spanish text to analyze
english_string_list = ['Machine Learning is fascinating.', 'Studying Artificial Intelligence is my passion.'] 
spanish_string_list = ['El aprendizaje automático es fascinante.', 'Estudiar Inteligencia Artificial es mi pasión.']

print('Calling BatchDetectDominantLanguage')

print('english_string_list results:')
# json.dumps() writes JSON data to a Python string
print(json.dumps(comprehend.batch_detect_dominant_language(TextList = english_string_list), sort_keys=True, indent=4))

print('\nspanish_string_list results:')
print(json.dumps(comprehend.batch_detect_dominant_language(TextList = spanish_string_list), sort_keys=True, indent=4))
print('End of BatchDetectDominantLanguage\n')
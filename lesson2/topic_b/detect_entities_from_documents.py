# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json
# import glob to find text files with .txt ending - https://docs.python.org/3.6/library/glob.html
import glob
# import os to obtain current working directory - https://docs.python.org/3.6/library/os.html
import os

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', 
						region_name='<input region>')  # e.g. 


data_dir = os.getcwd() + '\\reviews__neg\\*.txt'
file_list = glob.glob(data_dir)


for file in file_list:
	with open(file, 'r', encoding="utf-8") as f:
		file_as_str = f.read()
		print('Calling detect_entities')
		# json.dumps() writes JSON data to a Python string
		print(json.dumps(comprehend.detect_entities(Text = file_as_str, LanguageCode='en'), sort_keys=True, indent=4))
		print('End of detect_entities\n')




#####################################################################
#  Optional: Additional detect_entities functionality to review 
#####################################################################

# english_string = "I enjoy studying machine learning in seattle on tuesday."
# # detect_entities
# print('Calling DetectEntities')
# # json.dumps() writes JSON data to a Python string
# print(json.dumps(comprehend.detect_entities(Text = english_string, LanguageCode='en'), sort_keys=True, indent=4))
# print('End of DetectEntities\n')



# # batch_detect_entities
# english_string_list = ["I enjoy studying machine learning in seattle on tuesday.", "I love writing about artificial intelligence on monday in Seattle."]
# print('Calling DetectEntities')
# # json.dumps() writes JSON data to a Python string
# print(json.dumps(comprehend.batch_detect_entities(TextList = english_string_list, LanguageCode='en'), sort_keys=True, indent=4))
# print('End of DetectEntities\n')

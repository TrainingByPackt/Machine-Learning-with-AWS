import boto3

def lambda_handler(event, context):
	# create a s3 object
    s3 = boto3.client("s3")
    # assign the specific bucket to the 'bucket' variable
    bucket = "<input your bucket name here>"
    # assign the text file to examine to the variable 'key'
    key = "test_s3trigger_configured.txt"
    
    # create the file object
    file_obj = s3.get_object(Bucket = bucket, Key = key)
    
    # access the file_obj's body. Invoke the read() function and convert to a str object. 
    # assign to the variable 'body_str_obj' 
    body_str_obj = str(file_obj['Body'].read())
    
    # create a comprehend object
    comprehend = boto3.client(service_name="comprehend", region_name='<input region_name eg: us-east-1>')
    
    # call detect_sentiment()
    sentiment_response = comprehend.detect_sentiment(Text = body_str_obj, LanguageCode = "en")
    print("sentiment_response: \n", sentiment_response)
    
    # call detect_entities()
    entity_response = comprehend.detect_entities(Text = body_str_obj, LanguageCode = "en")
    print("\n\nentity_response: \n", entity_response)
    
    # call detect_key_phrases()
    key_phases_response = comprehend.detect_key_phrases(Text = body_str_obj, LanguageCode = "en") 
    print("\n\nkey_phases_response: \n", key_phases_response)
  
    return 'Hello from Lambda'

import boto3

def lambda_handler(event, context):
    # create a s3 object
    s3 = boto3.client("s3")
    
    # check if an event is True 
    if event:
        # enter the specific bucket name to the 'bucket' variable
        bucket = "<input bucket name>"
        
        # event – AWS Lambda uses this parameter to pass in event data to the handler. This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type
        text_file_obj = event["Records"][0]
        # assign the uploaded text file name to the 'filename' variable 
        filename = str(text_file_obj['s3']['object']['key'])
        
        # print the filename 
        print("filename: ", filename)

        # create the file object
        file_obj = s3.get_object(Bucket = bucket, Key = filename)
        
        # access the file_obj's body. Invoke the read() function and convert to a str object. 
        # assign to the variable 'body_str_obj' 
        body_str_obj = str(file_obj['Body'].read())
        
        # create a comprehend object
        comprehend = boto3.client(service_name="comprehend", region_name='<input region>') #us-east-1
        
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

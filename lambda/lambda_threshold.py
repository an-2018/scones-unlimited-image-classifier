import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    body = json.loads(event['body'])
    inferences = body['inferences']
    inferences_cleaned = inferences.strip('[]')
    
    inferences_list = [float(i) for i in inferences_cleaned.split(',')]

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(i > THRESHOLD for i in inferences_list)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
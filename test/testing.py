import boto3
import io
from PIL import Image           

# You should have Boto3 and Pillow Installed in your machine

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

image_path = input("Enter path of the image to check: ")

image = Image.open(image_path)
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(
        CollectionId='face_recognition',    # change to your Rekonize collection name
        Image={'Bytes':image_binary}                                       
        )

found = False
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(
        TableName='face_tab_recognition',       # Change to your DDB table name
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print ("Found Person: ",face['Item']['FullName']['S'])
        found = True

if not found:
    print("Person cannot be recognized")
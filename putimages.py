import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Elon_Musk.jpg','Elon Musk'),
      ('Elon_Muskvin.jpg','Elon Musk'),
      ('Bill_Gates.jpg','Bill Gates'),
      ('Sundar_Pichai.jpg','Sundar Pichai'),
      ('Sunder_Pichaibhai.jpg','Sundar Pichai')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('vip-images-rekonize', 'index/' + image[0])    # change to your s3 bucket name
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})

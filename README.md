# Follow This Doc to Rekognize images using Python in AWS Env.

Flow Diagram 
![Project-FLow](https://github.com/vinod-kha/face_rekonize/assets/87168769/bdea97a2-beee-4315-94bc-fd94a11dc515)


- Install aws-shell
```
pip install aws-shell
```

- Configure
```
aws configure
```

- Create a collection on aws rekognition
```
aws rekognition create-collection --collection-id face_recognition --region us-east-1
```

- Create table on DynamoDB
```
aws dynamodb create-table --table-name face_tab_recognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region us-east-1
```

- Create S3 bucket
```
aws s3 mb s3://vip-images-rekonize --region us-east-1
```

##IAM Policy for role to attach Lambda

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-name/*"       
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem"
            ],
            "Resource": [
                "arn:aws:dynamodb:aws-region:account-id:table/family_collection"     
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:IndexFaces"
            ],
            "Resource": "*"
        }
    ]
}

```

* Create a lambda function and attach the role your created .
* Add trigger the s3 bucket.
* Copy lamdafunction.py script and paste in your lambda code.
* Once Dynamdb table, s3 bucket , Lambda is successfully created and Integrated now Upload and test.
* Run 'putimages.py' python script to upload images from local to s3 bucket.
* Images are stored in s3 and metadata are strored in Dyanamodb.
* Navigate to DDB and click on PartiQL editor and run below command  and you can see the results.

```
select * from face_tab_recognition;
```

* Once the images are uploaded then test it.
* We have testing.py python script to test the images we uploaded.
* run testing.py script and give person name , unknown name to check weather it is rekognizing correctly or not.


Note: Modify with your Dynamdb, s3 and Rokognize collection name which your given in the scripts.



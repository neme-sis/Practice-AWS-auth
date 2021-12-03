#Accessing User's credentials for signing in to the process, go to get_user.py

import os
import boto3
from dotenv import load_dotenv
load_dotenv()


username= 'ghoshsayan894@gmail.com'     #email id
password='Sayan02@'      

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))

response = client.initiate_auth(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    AuthFlow = 'USER_PASSWORD_AUTH',
    AuthParameters = {
        'USERNAME': username,
        'PASSWORD': password
    }
)
#print(response)

# print(response['AuthenticationResult']['AccessToken'])
# print(response['AuthenticationResult']['RefreshToken'])
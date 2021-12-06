#Accessing User's credentials for signing in to the process, go to get_user.py

import os
import boto3
from dotenv import load_dotenv
load_dotenv()


username= input("Enter your mail id: ")     #email id
password= input("Enter your password: ")  #user defined password   

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))

try:
    response = client.initiate_auth(
        ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
        AuthFlow = 'USER_PASSWORD_AUTH',
        AuthParameters = {
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    access_token= response['AuthenticationResult']['AccessToken']

    attr_sub= None
    for attr in response['UserAttributes']:
        if attr['Name'] == 'sub':
            attr_sub = attr['Value']
            break
except:
    print("Unrecognized User")

#print(response)

# print(response['AuthenticationResult']['AccessToken'])
# print(response['AuthenticationResult']['RefreshToken'])
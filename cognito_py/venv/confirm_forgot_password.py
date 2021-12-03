#Forgot password confirmation code verification

import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= 'ghoshsayan894@gmail.com' 
confirmation_code = '024510'
password = 'Sayan02#'

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.confirm_forgot_password(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username,
    ConfirmationCode = confirmation_code,
    Password= password
)
print(response)
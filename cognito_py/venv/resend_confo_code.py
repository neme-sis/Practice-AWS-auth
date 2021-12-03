#Unable to access confirmation code, resend once again

import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= 'ghoshsayan894@gmail.com'     #email id
password='Sayan02@'                     #user defined password

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.resend_confirmation_code(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username
)

# print(response)
#save response.UserSub in database to save info about the client
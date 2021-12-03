#New user should give the confirmation code to enable the new account created after signup

import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= 'ghoshsayan894@gmail.com'     #email id
confirmation_code= '666423'

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.confirm_sign_up(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username,
    ConfirmationCode = confirmation_code
)

# print(response)
#save response.UserSub in database to save info about the client
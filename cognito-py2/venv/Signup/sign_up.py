#The first time user is creating an account

import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= input("Enter your mail id: ")     #email id
password= input("Enter a password of atleast 6 characters \
consisting both upper and lower case letters: ")  #user defined password

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.sign_up(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username,
    Password = password
)

# print(response)
confirmation_code = input("Enter conformation code sent to your registered mail: ")

try:
    response = client.confirm_sign_up(
        ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
        Username = username,
        ConfirmationCode = confirmation_code
    )
    print("Successfully Signed Up")
except:
    print("Process Failed")
    
print("Process Exited")
#save response.UserSub in database to save info about the client
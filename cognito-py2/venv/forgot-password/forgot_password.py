#User forgot password, urging request to reset it, next go to confirm_forgot_password.py


import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= input("Enter your mail id: ")     #email id

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.forgot_password(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username
)

confirmation_code = input("Enter Confimation code sent to \
your registered mail: ")

password= input("Enter a new password of atleast 6 characters \
consisting both upper and lower case letters: ")  #user defined password

try:
    response = client.confirm_forgot_password(
        ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
        Username = username,
        ConfirmationCode = confirmation_code,
        Password= password
    )
except:
    print("Process Failed, try again")

print("Process Exited")
# print(response)
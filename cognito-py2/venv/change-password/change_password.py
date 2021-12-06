#Change the password of the user by the user

import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username= input("Enter your mail id: ")     #email id
password= input("Enter your password: ")  #user defined password   

client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))

response = client.initiate_auth(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    AuthFlow = 'USER_PASSWORD_AUTH',
    AuthParameters = {
        'USERNAME': username,
        'PASSWORD': password
    }
)

access_token= response['AuthenticationResult']['AccessToken']

previousPassword = password
newPassword = password= input("Enter a new password of atleast 6 characters \
consisting both upper and lower case letters: ")  #user defined password

# access_token = 'eyJraWQiOiJoQkdPVElQY1pXenJYNVB5RHlnaEJvYW9ZbHpOUlBkUWo5YlBRdVwvYWtlZz0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNDAzODZjNjUtNzcwMC00ZDViLWJmOWMtMmRlYTlkMDU5NjM3Iiwic3ViIjoiYjgyNmUzMzQtYjNlMC00NTA3LWE5NzItYWNiZDQ4OTUxM2ZiIiwiZXZlbnRfaWQiOiJmZTQzMGQ4ZC04MDhkLTRkODYtOTQ2Yi0yZjk0MTNiOTJiNDEiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjM4NTcwNDk1LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX3JXZVhzaXN5eCIsImV4cCI6MTYzODU3NDA5NSwiaWF0IjoxNjM4NTcwNDk1LCJqdGkiOiJhMTU2Y2JlMi1lNjhmLTQ4M2EtOGQwNi0yNDRhNjNhM2Q2YWEiLCJjbGllbnRfaWQiOiIxY2U0aHFlYjIza3JrNzU4ZDVuc3NvNDNkdCIsInVzZXJuYW1lIjoiYjgyNmUzMzQtYjNlMC00NTA3LWE5NzItYWNiZDQ4OTUxM2ZiIn0.ejDtyRlklH6OBkWhbPsvj4KJts9XbOPDOeL4oTkjM6o22TEjkzC3dniawyi9eIEE_kyqa7qLEQ7rmv29CFpzW_Tw1fFSRwt1B0ASknI78T3DPZyJiqD0EaZeGnaN_eaHTXTPF87yx9OVYZD49JWrvb-3qr82kPxy3XDG37JgPoydMs8xE2zJ73oP7tA0LL8xt5528GcoHYF1zR0wWDfw7joy2ugtXvZWJPgBUAz3puiN0Z_E2RXXUmWqcbm5WxO9bn82zjbMpn6AB5h5Tkluq-IYYZyDvIvtsYGVp1u32Ra3ai6Yv-0ohuI6uKNMww4Bj5cQ2itvD-ZCiht9D97vrA'


client = boto3.client('cognito-idp', region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.change_password(
    PreviousPassword = previousPassword,
    ProposedPassword = newPassword,
    AccessToken =access_token
)
print(response)
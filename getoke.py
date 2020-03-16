#!/usr/bin/python

import argparse
import os

from warrant import Cognito

parser = argparse.ArgumentParser(description="""
    Add these environment variables and you have a quick token refresher:
    
    * AWS_COGNITO_POOL_ID
    * AWS_COGNITO_CLIENT_ID
    * AWS_COGNITO_SECRET_KEY
    * COGNITO_USER
    * COGNITO_PASSWORD
""")
args = parser.parse_args()


def do_work():

    user_pool_id = os.environ['AWS_COGNITO_POOL_ID']
    client_id = os.environ['AWS_COGNITO_CLIENT_ID']
    client_secret = os.environ.get('AWS_COGNITO_SECRET_KEY')
    username = os.environ.get('COGNITO_USER')
    password = os.environ['COGNITO_PASSWORD']
    u = Cognito(
        user_pool_id=user_pool_id,
        client_id=client_id,
        client_secret=client_secret,
        username=username
    )
    u.authenticate(password=password)
    print(u.access_token)


if __name__ == '__main__':
    do_work()

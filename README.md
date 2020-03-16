GeToke is a simple script to get your auth token.  Keep your expectations low. :D

### Installation

* Download or clone this repo

```
cd getoke
pip install -r requirements.txt
```

Add these environment variables and you have a quick token refresher:

* AWS_COGNITO_POOL_ID
* AWS_COGNITO_CLIENT_ID
* AWS_COGNITO_SECRET_KEY (defaults to blank)
* COGNITO_USER
* COGNITO_PASSWORD

### Usage

```
python getoke.py
```

It will output your access token, so you can paste that into postman or whatever you need to use
code_verifier = code_challenge = "k2oDwJxT8paNY1JwtNxRbS8yotMo8nc3C66AGAcNBtevi3-Kxz8sShBexxJarvxXpFnMUGVXJc9p4f27ZhdQ0LVX-wOBFusqCBfeLXhRbS1MyJMn-JRihVEIoupScbk"
import requests  # Importing module

STOCK = "TSLA"  # Set constatn var 
API_URL = "https://myanimelist.net/v1/oauth2/authorize"   # API endpoint
API_KEY = "09CN7MDZJTQKKB4U"    # API key

# Creating dic with explicit type annotation
parameteres = {
    "response_type": "code",
    "client_id": "412ac077d2f7ff148be33d2ffe97b854",
    "code_challenge": code_challenge,
    
}

response = requests.get(url=API_URL, params=parameteres)
raw_data = response.content
print(raw_data)

# Base URL: https://myanimelist.net/v1/oauth2/authorize (GET request)
# Parameter response_type: must be set to "code". (REQUIRED)
# Parameter client_id: your Client ID. (REQUIRED)
# Parameter code_challenge: the Code Challenge generated during the previous step. (REQUIRED)
# Parameter state: a string which can be used to maintain state between the request and callback. It is later returned by the MAL servers to the API client. (RECOMMENDED)
# Parameter redirect_uri: the URL to which the user must be redirected after the authentication. (OPTIONAL)
# Parameter code_challenge_method: defaults to "plain". No other option is currently available. (OPTIONAL)

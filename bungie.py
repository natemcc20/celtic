import requests
import os
import json
from requests_oauthlib import OAuth2Session

url_base = "https://www.bungie.net/platform/Destiny2/"
redirect_url = "https://tekksparrow-programs.github.io/website"
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
token_url = "https://www.bungie.net/platform/app/oauth/token/"

membership_id = "4611686018438415462"
membership_type = "2"
client_id = "45259"
client_secret = "wyuyRR71k0gA7Og0useiWCzvJ2VGZ.UaJ5Kv6FgI2Wg"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_link = session.authorization_url(base_auth_url)

print(f"Authorization Link: {auth_link[0]}")

redirect_response = input(f"Paste url here----->")

session.fetch_token(
    client_id=client_id,
    client_secret=client_secret,
    token_url=token_url,
    authorization_response=redirect_response
)

header = {"X-API-Key": f'{os.getenv("BUNGIE_KEY")}'}
resp = session.get("https://www.bungie.net/Platform/Social/Friends", headers=header)
print(resp.status_code, resp.reason, resp.text)
print(1)




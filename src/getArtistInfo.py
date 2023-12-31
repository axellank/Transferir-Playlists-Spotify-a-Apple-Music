# Codigo de prueba para obtener informacion de un un artista usando su ID
import requests
import base64
import json
from dotenv import load_dotenv #Ocultar keys usando varianbles del sistema
import os

load_dotenv()

# Your client credentials
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Artist ID
artist_id = '1McMsnEElThX1knmY4oliG'

# Base64 encode the client_id and client_secret
credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'client_credentials'
}

# Make a POST request to get the access token
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

if response.status_code == 200:
    access_token = response.json().get('access_token')
else:
    print(f'Error: {response.status_code}')
    access_token = None

if access_token:
    actualAccessToken = {
        'Authorization': f'Bearer {access_token}',
    }

    # Make a GET request to get the artist data
    responseArtistData = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}', headers=actualAccessToken)

    if responseArtistData.status_code == 200:
        print(json.dumps(responseArtistData.json(), indent=4)) #Usar JSON para que los datos no se impriman en una sola linea
    else:
        print(f'Error: {responseArtistData.status_code}')

import requests
import json
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.options import Options

# WEB SCRAPER --> GET STATUS SEASONAL WOW SERVER ""

BASE_URL = "https://worldofwarcraft.blizzard.com/en-us/game/status/classic1x-us"


     
def get_sha_256():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    for request in driver.requests:
        
        if request.response and request.url == 'https://worldofwarcraft.blizzard.com/graphql':
                data = request.body
                data = json.loads(data)
                return data



def get_seasonal_server_status_us(server_name):
    data = get_sha_256()
    GRAPHQL_URL="https://worldofwarcraft.blizzard.com/graphql"

    response = requests.post(url=GRAPHQL_URL, json=data)

    realms = response.json()["data"]["Realms"]
    for realm in realms:
        if realm["name"] == server_name:
            print(f"Realm: {realm['name']} | Type: {realm['type']['name']} | Population: {realm['population']['name']} | Status: {'Online' if realm['online'] else 'Offline'}")
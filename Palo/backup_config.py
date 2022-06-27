import os
import requests

# The FQDN of the device: Update as needed
device = '10.126.140.2'

# Get the API Key from OS environment variables
key = os.environ.get("API_Key")

# Build the URL
api = "https://" + device + "/api/"
type = "export"
category = "configuration"
url = api + "?type=" + type + "&category=" + category + "&key=" + key

# Send a GET to the Palo Alto (assuming you have a valid certificate)
response = requests.get(url, verify=False)
print("Response: ", response.status_code)

# Save the backup (relative to the location the script is run)
print("Saving backup...")
file = open("pa-backup.xml", "wb")
file.write(response.content)
file.close

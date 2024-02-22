import requests

# Define your Datadog API and APP keys
DD_API_KEY = "YOUR_DD_API_KEY"
DD_APP_KEY = "YOUR_DD_APP_KEY"

# Define the endpoint URL
url = "https://api.datadoghq.com/api/v1/hosts"

# Define headers with your API and APP keys
headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": "307e06a3dce1c3a74aca04a082c3e7ab",
    "DD-APPLICATION-KEY": "9ff2e1e489bc0035ec677566a0fddb324e86db07"
}

# Make a GET request to the endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Process the response data as needed
    print(data)
else:
    print("Error:", response.text)


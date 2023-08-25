import requests

# Replace with your Office 365 credentials and API endpoint
tenant_id = 'your-tenant-id'
client_id = 'your-client-id'
client_secret = 'your-client-secret'
old_domain = '@madhive.onmicrosoft.com'
new_domain = '@madhive.com'

# Define the Microsoft Graph API endpoint for users
api_url = f'https://graph.microsoft.com/v1.0/users'

# Authenticate using client credentials flow
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': 'https://graph.microsoft.com',
}
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

if not access_token:
    print("Failed to obtain access token.")
    exit()

# Define headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Get the list of users
response = requests.get(api_url, headers=headers)
users = response.json().get('value', [])

if not users:
    print("No users found.")
else:
    for user in users:
        # Update the user's userPrincipalName
        old_username = user['userPrincipalName']
        if old_domain in old_username:
            new_username = old_username.replace(old_domain, new_domain)
            update_data = {
                'userPrincipalName': new_username,
            }
            update_response = requests.patch(f"{api_url}/{user['id']}", headers=headers, json=update_data)

            if update_response.status_code == 200:
                print(f"Updated username for {user['displayName']} to {new_username}")
            else:
                print(f"Failed to update username for {user['displayName']}")


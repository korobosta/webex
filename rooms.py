import requests

# Your Webex API access token
access_token = 'YOUR_TOKEN'

# Base URL for Webex API
base_url = 'https://webexapis.com/v1'

# Function to create a Webex room
def create_room(room_name):
    endpoint = f'{base_url}/rooms'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'title': room_name
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    print(response)
    if response.status_code == 200:
        room_info = response.json()
        print(f"Room '{room_name}' created. Room ID: {room_info['id']}")
        return room_info['id']
    else:
        print(f"Failed to create room. Status code: {response.status_code}")
        return None

# Function to get details of a Webex room
def get_room_details(room_id):
    endpoint = f'{base_url}/rooms/{room_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        room_info = response.json()
        print(f"Room Details: {room_info}")
    else:
        print(f"Failed to get room details. Status code: {response.status_code}")

# Function to update a Webex room
def update_room(room_id, new_name):
    endpoint = f'{base_url}/rooms/{room_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'title': new_name
    }
    response = requests.put(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Room '{room_id}' updated with new name '{new_name}'")
    else:
        print(f"Failed to update room. Status code: {response.status_code}")

# Function to delete a Webex room
def delete_room(room_id):
    endpoint = f'{base_url}/rooms/{room_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.delete(endpoint, headers=headers)
    if response.status_code == 204:
        print(f"Room '{room_id}' deleted")
    else:
        print(f"Failed to delete room. Status code: {response.status_code}")

# Example usage:
# Create a room
room_id = create_room('My Python Room')

# Get room details
if room_id:
    get_room_details(room_id)

# Update room name
if room_id:
    update_room(room_id, 'Renamed Python Room')

# Delete room
# if room_id:
#     delete_room(room_id)

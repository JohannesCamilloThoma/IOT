import time
import requests



api_key = 'XFBQP70RE0ISM1W4'
channel_id = 2385350
url = f"https://api.thingspeak.com/update?api_key={api_key}"


def upload_to_thingspeak(data):
    payload = {"field1": data}  # Use field1, field2, ..., field8 based on your ThingSpeak channel configuration
    response = requests.post(url, params=payload)

    if response.status_code == 200:
        print(f"Data uploaded successfully: {data}")
    else:
        print(f"Failed to upload data. Status code: {response.status_code}")

# Example: Upload a random value to field1 every 15 seconds
while True:
    value_to_upload = 42  # Replace with your actual data
    upload_to_thingspeak(value_to_upload)
    time.sleep(15)

# Read last thingsspeak message
def get_last_entry(channel_id, read_api_key, field_name='field1'):
    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=1'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the HTTP response

        data = response.json()
        if 'feeds' in data and data['feeds']:
            last_entry = data['feeds'][0]
            if field_name in last_entry:
                return last_entry[field_name]
            else:
                print(f"Field '{field_name}' not found in the last entry.")
        else:
            print("No entries found in the channel.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    pass






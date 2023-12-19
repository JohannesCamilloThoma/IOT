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

if __name__ == "__main__":
    pass






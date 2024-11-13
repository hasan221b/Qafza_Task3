import requests

url = "http://127.0.0.1:8000/price"

cart = int(input("Enter Diamond Cart: "))
x = int(input("Enter X diamention: "))
y = int(input("Enter Y diamention: "))
z= int(input("Enter Z diamention: "))

testing_data = {
    "cart": cart,
    "x": x,
    "y": y,
    "z": z 
    }


response = requests.post(url, json=testing_data)

if response.status_code == 200:

    print(response.json()[1],response.json()[0])

else:
    print(f"Error: {response.status_code}, {response.text}")
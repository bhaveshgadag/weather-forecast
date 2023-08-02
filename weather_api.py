import requests as r

API_KEY = "72239d9d2567f6e66c8803309b81f901"

def get_data(place, days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = r.get(url)
    data = response.json()['list'][:8 * days]
    return data


if __name__ == '__main__':
    response = get_data("Mumbai", 1)
    print(response)
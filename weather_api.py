import requests as r

API_KEY = "72239d9d2567f6e66c8803309b81f901"

def get_data(place, days=1):
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
            f"q={place}" \
            f"&appid={API_KEY}" \
            "&units=metric"

    response = r.get(url)
    json_data = response.json()
    if json_data['cod'] == '404':
        return json_data['cod']
    data = json_data['list'][:8 * days]
    return data


if __name__ == '__main__':
    response = get_data("Mumbai", 1)
    print(response)
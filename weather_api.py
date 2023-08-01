import requests as r

API_KEY = "72239d9d2567f6e66c8803309b81f901"

def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = r.get(url)
    data = response.json()['list']
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in data]
    return filtered_data[:8 * days]


if __name__ == '__main__':
    response = get_data("Mumbai", 1, 'Temperature')
    print(response)
    response = get_data("Mumbai", 1, 'Sky')
    print(response)
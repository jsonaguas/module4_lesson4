# Weather Forecast Application Script
class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        raw_data = self.weather_data.get(city, "Weather data not available")
        return raw_data
        

class DataParser:

    def parse_weather_data(self, raw_data):
        # Function to parse weather data
        if not raw_data or raw_data == "Weather data not available":
            return "Weather data not available"
        city = raw_data.get("city", "Unknown")
        temperature = raw_data.get("temperature", "Unknown")
        condition = raw_data.get("condition", "Unknown")
        humidity = raw_data.get("humidity", "Unknown")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        fetcher = WeatherDataFetcher()
        detailed_weather = fetcher.fetch_weather_data(city)
        return self.parse_weather_data(detailed_weather)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        fetcher = WeatherDataFetcher()
        raw_data = fetcher.fetch_weather_data(city)
        if raw_data == "Weather data not available":
            print(f"Weather data not available for {city}")
        else:
            print(self.parse_weather_data(raw_data))



def main():
    parser = DataParser()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = parser.get_detailed_forecast(city)
        else:
            forecast = parser.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()


# Cs50_Weather Information API

#### Video Demo: <URL HERE>

The **Weather Information API** is a powerful tool that provides accurate, real-time weather data from around the globe. This API allows users to access essential weather information such as temperature, humidity, wind speed, and weather conditions. It retrieves data from the trusted [OpenWeatherMap API](https://openweathermap.org/api), ensuring high-quality, reliable information.

## Purpose

The main purpose of this API is to provide developers with easy access to detailed and current weather information. Whether for building weather applications, monitoring environmental conditions, or integrating weather data into other services, this API offers a simple, yet robust solution.

## Features

- **Weather Status**: The API provides general weather conditions such as "sunny", "cloudy", "rainy", and others. These conditions are essential for understanding the general climate of a location at any given moment.
- **Maximum and Minimum Temperature**: This feature allows users to view the highest and lowest temperatures of the day, providing a clear understanding of daily temperature fluctuations.
- **Feels Like Temperature**: This feature accounts for variables like humidity and wind, providing the "feels like" temperature. This can be particularly useful in areas with extreme weather conditions.
- **Location Search**: The API allows users to search for a location by name and returns its corresponding **longitude** and **latitude**. This geographic data is used to fetch weather information for the specific location.

The integration with OpenWeatherMap ensures that the API always provides accurate and up-to-date weather data, sourced from one of the most widely used weather services worldwide.

## Database Integration

The project includes a secure database for storing **usernames** and **passwords**. This database uses encryption techniques to protect sensitive information and is designed with high efficiency and scalability in mind. The system ensures that user data is handled according to best practices, safeguarding privacy and preventing unauthorized access.

## Technologies Used

This project is built using a combination of modern technologies:
- **Backend Framework**: (Flask.)
- **Database**: (sqllite3.)
- **External API**: OpenWeatherMap API for retrieving weather data.

## How to Use

To integrate the Weather Information API into your application:
1. Obtain an API key from OpenWeatherMap.
2. Call the appropriate endpoints to fetch weather data.
3. Use the response to display weather conditions, temperatures, or any other data you require.

## Example

Here’s an example of how to fetch weather data for a city:

1. **Request**: You send a `GET` request to the API with the location (in this case, "London"):

```bash
GET https://api.weather.com/data?location=London

Response: The API will return a JSON response containing weather information such as:

{
  "temperature": 18,
  "feels_like": 16,
  "humidity": 65,
  "weather": "cloudy"
}


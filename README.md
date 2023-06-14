## RpiWeatherDisplay

RpiWeatherDisplay is a project that displays weather information on a Raspberry Pi using the Weather Icons by Erik Flowers. It fetches weather data from the weatherapi.com API and uses Pexels for fetching relevant images. The project is licensed under the MIT License.

### Installation

To install and use RpiWeatherDisplay, follow these steps:

1. Clone the repository to your Raspberry Pi:

 ```bash
 git clone https://github.com/Lutz-Pfannenschmidt/RpiWeatherDisplay.git
 ```

2. Install the required dependencies:

 ```bash
 pip install -r requirements.txt
 ```
 
3. Obtain API keys:

- Sign up on [weatherapi.com](https://www.weatherapi.com/) to get an API key.
- Visit [Pexels API](https://www.pexels.com/api/) to acquire a Pexels API key.

4. Configure the API keys:

- Copy the `settings.example.py` file and rename it to `settings.py`.
- Replace `<weatherapi_key>` with your weatherapi.com API key.
- Replace `<pexels_key>` with your Pexels API key.
- Replace `<your_city>` with your city name.
- Replace `<your_language>` with the language you want to use.

5. Run the application:

 ```bash
 python app.py
 ```

6. Access the weather display:

- Open a web browser on your Raspberry Pi.
- Navigate to `http://localhost:5000` to view the weather display.
- in the future, you will have the option to enable autostart
f you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request on the GitHub repository.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments

- Weather Icons by Erik Flowers: [https://erikflowers.github.io/weather-icons/](https://erikflowers.github.io/weather-icons/)
- weatherapi.com API: [https://www.weatherapi.com/](https://www.weatherapi.com/)
- Pexels API: [https://www.pexels.com/api/](https://www.pexels.com/api/)


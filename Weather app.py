import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        layout = QVBoxLayout()

        # Input Field
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name")
        layout.addWidget(self.city_input)

        # Search Button
        self.search_button = QPushButton("Get Weather", self)
        self.search_button.clicked.connect(self.get_weather)
        layout.addWidget(self.search_button)

        # Weather Info Label
        self.weather_label = QLabel("Weather info will be shown here", self)
        layout.addWidget(self.weather_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            self.weather_label.setText("Please enter a city name")
            return

        api_key = "1d50fe7f28e954e67b2c65fd8e2dd9c6"  # Replace with your OpenWeatherMap API Key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                self.weather_label.setText(f"Temperature: {temperature}°C\nDescription: {description.capitalize()}")
            else:
                self.weather_label.setText("City not found!")
        except Exception as e:
            self.weather_label.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

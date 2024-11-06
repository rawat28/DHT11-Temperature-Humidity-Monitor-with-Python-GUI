# DHT11 Temperature & Humidity Monitor with Python GUI

This project involves interfacing a DHT11 temperature and humidity sensor with an Arduino to read temperature and humidity values, and display them on a Python dashboard in real-time.

## Project Overview

The main goal of this project is to:

- Interface a DHT11 temperature and humidity sensor with an Arduino.
- Read the sensor data and send it to a Python application via serial communication.
- Display the temperature and humidity data on a graphical user interface (GUI) in real-time using the Python Tkinter library.

### Features:

- **Arduino Code**: Collects temperature and humidity data from the DHT11 sensor and sends it via Serial to a Python program.
- **Python GUI**: Displays the real-time temperature and humidity data in an easy-to-read format.

---

## Hardware Requirements

1. **Arduino Uno** (or any compatible Arduino board)
2. **DHT11 Temperature and Humidity Sensor**
3. **Jumper Wires**
4. **USB Cable** for Arduino connection to PC

### DHT11 Sensor Pinout:

- **VCC**: 5V or 3.3V (depending on your Arduino board)
- **GND**: Ground
- **Data Pin**: Pin 2 (or any other digital I/O pin of your choice)

---

## Software Requirements

1. **Arduino IDE**: For writing and uploading code to the Arduino.
2. **Python 3.x**: For running the GUI application.
3. **Python Libraries**:
    - `tkinter`: For creating the GUI.
    - `pyserial`: For serial communication between Arduino and Python.

---

## Installation Instructions

### 1. Arduino Setup

1. **Connect the DHT11 sensor** to the Arduino as follows:
    - **VCC** to 5V
    - **GND** to Ground
    - **Data Pin** to Pin 2 (or your preferred pin)

2. **Upload the Arduino Code**:
    - Open the Arduino IDE and paste the following code:

    ```cpp
    #include <DHT.h>

    #define DHTPIN 2      // Pin where the DHT22 is connected
    #define DHTTYPE DHT22 // Define the sensor type as DHT22
    
    DHT dht(DHTPIN, DHTTYPE);
    
    void setup() {
      Serial.begin(9600);
      dht.begin();
    }
    
    void loop() {
      float temperature = dht.readTemperature(); // Read temperature in Celsius
      float humidity = dht.readHumidity();       // Read humidity
    
      if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
      } else {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.println(" °C");
    
        Serial.print("Humidity: ");
        Serial.print(humidity);
        Serial.println(" %");
      }
      
      delay(2000); // Delay for 2 seconds
    }

    ```

3. **Upload the code** to your Arduino board.

### 2. Python Setup

1. **Install Required Libraries**:
    - Ensure you have Python 3.x installed.
    - Install the required libraries by running the following commands in your terminal:

    ```bash
    pip install pyserial tkinter
    ```

2. **Run the Python GUI Application**:
    - Download or clone the repository to your local machine.
    - Navigate to the project directory.
    

---

## How the Python GUI Works

- The GUI is built using **Tkinter** and displays the temperature and humidity data in real-time.
- The `pyserial` library is used to read the serial data from the Arduino.
- Every 2 seconds, the Python GUI is updated with new readings from the Arduino.
- The temperature value is displayed in **green**, and the humidity value is displayed in **blue** for easy distinction.

---

## Expected Results

- **Arduino Code**: Reads the temperature and humidity data from the DHT11 sensor and prints it to the Serial Monitor.
- **Python GUI**: Displays the real-time data from the sensor and updates it every 2 seconds.

---

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes. If you find any issues or have suggestions, please open an issue in the repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the **Arduino community** for providing a great platform for hardware development.
- Tkinter and PySerial for creating the Python GUI and communication interface.


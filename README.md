# EspMoistureSensor

A frontend application designed to connect with multiple ESP32 microcontrollers to monitor plant soil moisture levels, helping you determine the perfect time to water your plants.

## Overview

The EspMoistureSensor project combines hardware and software to create an efficient plant care system. By utilizing ESP32 microcontrollers equipped with moisture sensors, this project allows you to track soil moisture levels in real-time. The frontend app provides a user-friendly interface to visualize the data collected from multiple ESP32 devices, ensuring your plants stay healthy and hydrated.

## Features

- **Multi-Device Support**: Connect and monitor multiple ESP32 devices simultaneously.
- **Real-Time Monitoring**: Get live updates on soil moisture levels for each connected plant.
- **User-Friendly Interface**: A clean and intuitive frontend app to view and manage moisture data.
- **Custom Alerts**: Receive notifications when moisture levels drop below a set threshold (optional feature, if implemented).
- **Scalable Design**: Easily add more ESP32 sensors as your plant collection grows.

## Hardware Requirements

- **ESP32 Microcontroller(s)**: Any ESP32 development board (e.g., ESP32-WROOM, NodeMCU ESP32).
- **Soil Moisture Sensor(s)**: Capacitive or resistive sensors compatible with ESP32.
- **Power Supply**: USB or battery power for the ESP32 boards.
- **Wi-Fi Network**: For ESP32 devices to transmit data to the frontend app.

## Software Requirements

- **Frontend App**: Built with [insert framework/language, e.g., React, Vue.js, or HTML/CSS/JS].
- **ESP32 Firmware**: Custom code to read sensor data and send it over Wi-Fi (e.g., using Arduino IDE or PlatformIO).
- **Backend (Optional)**: A server to aggregate data from ESP32 devices (e.g., Node.js, Flask) if implemented.

## Installation

### 1. Hardware Setup
1. Connect the soil moisture sensor to the ESP32:
   - VCC to 3.3V
   - GND to GND
   - Signal pin to an analog input pin (e.g., GPIO 34)
2. Power the ESP32 via USB or battery.
3. Ensure the ESP32 is connected to your Wi-Fi network.

### 2. Firmware Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Kaonashie/EspMoistureSensor.git

# 🚽 Smart AI Health Monitoring Toilet

An AI + IoT based prototype for monitoring simulated urinary health patterns using sensor data, MQTT communication, machine learning, and an interactive Streamlit dashboard.

## 🌟 Project Overview

The Smart AI Health Monitoring Toilet is an AI + IoT prototype designed to collect simulated health-related sensor parameters, transmit the data using MQTT, process the readings using Python, and classify the resulting pattern using a Machine Learning model.

The system demonstrates how IoT data can be combined with Machine Learning to identify patterns that may require further evaluation.

> ⚠️ This is an educational prototype and does not provide medical diagnosis or replace professional medical testing.

---

## ✨ Key Features

- 📡 ESP32-based IoT simulation
- 🧪 Simulated urine pH monitoring
- 💧 Urine volume monitoring
- 🌡️ Temperature monitoring
- 🚻 Frequency monitoring
- ☁️ MQTT-based real-time communication
- 🐍 Python data processing
- 🧠 Random Forest Machine Learning model
- 📊 Interactive Streamlit dashboard
- 🔄 Automatic dashboard refresh
- 📈 Historical sensor-data visualization
- 📋 Recent sensor readings
- 📥 CSV data download
- 🌐 Cloud deployment using Streamlit Community Cloud

---

## 🏗️ System Architecture

```text
ESP32 / Wokwi
     │
     │ Sensor Data
     ▼
   MQTT Broker
     │
     ▼
Python MQTT Receiver
     │
     ▼
CSV Data Storage
     │
     ▼
Random Forest ML Model
     │
     ▼
Streamlit Dashboard
     │
     ▼
AI Pattern Detection
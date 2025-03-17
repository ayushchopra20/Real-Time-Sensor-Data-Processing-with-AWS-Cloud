# Real-Time-Sensor-Data-Processing-with-AWS-Cloud

## Overview
This project demonstrates a temperature monitoring system using AWS IoT Core, a Raspberry Pi, and AWS Lambda. The system collects temperature data from a sensor, sends it to AWS IoT Core, processes it with a Lambda function, and triggers email notifications for high temperatures.

## Features
- Register and configure an IoT device on AWS IoT Core.
- Publish temperature data to AWS IoT.
- Process data using an AWS Lambda function.
- Trigger email alerts for high temperatures.
- Monitor system logs via AWS CloudWatch.

## Prerequisites
- AWS Account
- Raspberry Pi (or Virtual Machine)
- Python 3.x installed
- AWS CLI installed and configured
- Adafruit DHT11 sensor
- AWS IoT Device SDK for Python

## Setup Instructions

### 1. AWS IoT Device Shadow Setup
- Register a device on AWS IoT Core.
- Create and manage an IoT Thing.
- Attach security policies and download certificates.

### 2. Publishing Sensor Data
- Simulate or collect temperature data from the DHT11 sensor.
- Publish the data to AWS IoT Core.
- Use MQTT test client to verify data transmission.

### 3. AWS Lambda Function
- Create a Lambda function to process received data.
- Implement email notifications using Amazon SES.
- Assign IAM roles to grant necessary permissions.

### 4. Setting Up Message Routing
- Create an AWS IoT Rule to route sensor data to the Lambda function.
- Use SQL queries to filter incoming data.

### 5. Testing the System
- Run the temperature monitoring script.
- Subscribe to MQTT topics to verify data reception.
- Monitor Lambda execution logs in CloudWatch.

## Running the Program
```sh
python3 Temperature_Sensing_Sending.py
```

## Expected Output
- Sensor data is published to AWS IoT.
- Lambda processes data and sends email alerts.
- Logs are available in AWS CloudWatch.

## Contributors
- **Aayush Chopra** - Developer & Maintainer

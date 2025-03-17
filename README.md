# Real-Time-Sensor-Data-Processing-with-AWS-Cloud

# AWS IoT Sensor Data Pipeline

## Overview
This project demonstrates an end-to-end IoT data processing pipeline using AWS IoT, AWS Lambda, and AWS CloudWatch. The system collects sensor data, publishes it to AWS IoT, processes it using AWS Lambda, and provides alerts based on predefined conditions.

## Features
- **AWS IoT Device Shadow Setup**: Registers a Raspberry Pi (physical or virtual) with AWS IoT and manages its device shadow.
- **Publishing Sensor Data**: Simulates or collects real sensor data and publishes it to AWS IoT for processing.
- **AWS Serverless Function**: Uses AWS Lambda to process sensor updates, trigger email alerts, or perform other automated actions.
- **Testing & Documentation**: Validates the functionality using test cases, measures execution latency, and provides logs/screenshots.

## Architecture
1. **IoT Device (Raspberry Pi or Simulator)**: Collects or simulates temperature data.
2. **AWS IoT Core**: Acts as a broker to receive sensor data.
3. **AWS Lambda**: Processes data and triggers alerts (e.g., sending emails using Amazon SES).
4. **CloudWatch**: Monitors logs and performance.

## Setup Instructions
### 1. AWS IoT Device Shadow Setup
- Register a Raspberry Pi (or virtual device) in AWS IoT.
- Create and configure an AWS IoT Device Shadow.
- Provide screenshots of the setup.

### 2. Publishing Sensor Data
- Use Python and AWS SDK (Boto3) to publish sensor data.
- Ensure data is correctly transmitted to AWS IoT.
- Provide implementation screenshots.

### 3. AWS Serverless Function
- Implement an AWS Lambda function to process incoming sensor data.

## Requirements
- AWS Account with IoT Core, Lambda, and SES enabled
- Raspberry Pi or a simulated device
- Python with Boto3 library
- DHT11 - Temperature and Humidity Sensor

## Running the Project
1. Set up the AWS IoT device and shadow.
2. Run the Python script to publish sensor data.
3. Configure AWS Lambda to process data.
4. Monitor execution logs in CloudWatch.

## Contributors
- **Aayush Chopra** - Developer & Maintainer



# Working with Streaming Data using Kafka

## Overview

This is Proof of Concept for creating a data pipeline using Kafka.

## PoC Complexity Level

Medium

## Tech Stack

- Apache Kafka (Open Source)
- Python

## Use Case

Use Python client with Kafka broker and create a data pipeline.

## Kafka Architecture

![image](https://github.com/user-attachments/assets/ac7c2f7a-93fd-4ad7-8172-28052af249d4)

- Brokers: The dedicated servers to receive, store, process and distribute events
- Topics: The containers or databases of events
- Partitions: Divide topics into different brokers
- Replications: Duplicate partitions into different brokers
- Producers: Kafka client applications that publish events into topics
- Consumers: Kafka client applications that subscribe to topics and read events from them

## Solution

Create a Kafka topic (admin.py). Then create a producer (producer.py) to send messages to Kafka topic. Finally, create a consumer (consumer.py) to read messages from Kafka topic.

# Data Streaming | End-to-End Data Engineering Project (How to Build on Windows Version)

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What You'll Learn](#what-youll-learn)
- [Technologies](#technologies)
- [Getting Started](#getting-started)

## Introduction

This project was originally created by airscholar and you can find it [here](https://github.com/airscholar/e2e-data-engineering/tree/main). I have modified this project to run completely containerized on a Windows environment with the specific modifications needed. Most systems are Linux based however, so you may want to follow the original instructions instead.

Like the original project, this serves as an example on how to build a complete end-to-end data pipeline that goes through the typical process: ingestion, processing, and storage. 

The tech stack is the same as the original which includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Docker is used to demonstrate ease of deployment and the ability to modify settings for scalability.

## System Architecture

![System Topology](https://github.com/LukeForData/data_engineering_projects/blob/main/end2nd-airflow-streaming-project/Data%20engineering%20architecture.png)

Definition of components used:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.

## What I learned (and what you can learn too!)

- Installing Docker on Windows Environment
- Setting up a data pipeline with Apache Airflow
- Real-time data streaming with Apache Kafka
- Distributed synchronization with Apache Zookeeper
- Data processing techniques with Apache Spark
- Data storage solutions with Cassandra and PostgreSQL
- Containerizing your entire data engineering setup with Docker
- Modifying original project to work agnostically of a particular OS


## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

## Pre-Requisites

 - Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/LukeForData/data_engineering_projects/tree/main/end2nd-airflow-streaming-project
    ```

2. Navigate to the project directory:
    ```bash
    cd end2nd-airflow-streaming-project
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose -f docker-compose-zoo.yaml up -d
    ```

4. With Docker Container Running and all Services Started/Healthy
    ```bash
    docker-compose -f docker-compose-zoo.yaml exec spark-master bash
    ```

    ```bash
    "spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,com.datastax.spark:spark-cassandra-connector_2.12:3.5.0 \
  /opt/spark/spark_stream.py"
    ```
   
   A successful run will show "Keyspace created successfully!" and "Table created successfully!" in the terminal

![Terminal-Spark](https://github.com/LukeForData/data_engineering_projects/blob/main/end2nd-airflow-streaming-project/docker-terminal-spark.png)

5. Open up Airflow and manually start the DAG to Stream Data
   
   - go to [http://localhost:8080](http://localhost:8080) in your browser
   - user: admin , password: admin
   - click on unpause next to user_automation dag
   - click on user_automation and click on Trigger Dag arrow

![Dag1](https://github.com/LukeForData/data_engineering_projects/blob/main/end2nd-airflow-streaming-project/dag1.png)

![Dag2](https://github.com/LukeForData/data_engineering_projects/blob/main/end2nd-airflow-streaming-project/dag2.png)

6. Open up a new terminal in the original project directory and Open Cassandra to verify data has arrived

    ```bash
    docker-compose -f docker-compose-zoo.yaml exec spark-master bash
    ```

    ```bash
    describe spark_streams.created_users;
    ```

    ```bash
    select * from spark_streams.created_users;
    ```

![Cassandra](https://github.com/LukeForData/data_engineering_projects/blob/main/end2nd-airflow-streaming-project/cassandra-output.png)
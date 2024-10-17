# Virtual Pet Monitoring System

This project demonstrates a basic setup for monitoring a simple Virtual Pet API using Prometheus and Grafana. It's designed to showcase fundamental knowledge of Flask, Prometheus, Grafana, and Docker.

## Project Overview

The system consists of three main components:

1. **Virtual Pet API**: A Flask-based API that simulates a virtual pet with feeding and playing functionalities.
2. **Prometheus**: Monitors and collects metrics from the API.
3. **Grafana**: Visualizes the collected metrics in customizable dashboards.

All components are containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Directory Structure

```
project_root/
│
├── docker-compose.yml
├── README.md
│
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
├── prometheus/
│   ├── Dockerfile
│   └── prometheus.yml
│
└── grafana/
    ├── Dockerfile
    └── datasource.yml
```

## Setup and Running

1. Clone the repository:
   ```
   git clone https://github.com/your-username/virtual-pet-monitoring.git
   cd virtual-pet-monitoring
   ```

2. Start the services:
   ```
   docker-compose up -d
   ```

3. Access the services:
   - Virtual Pet API: http://localhost:5000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000 (default credentials: admin/admin)

## API Endpoints

- `GET /feed`: Feed the virtual pet
- `GET /play`: Play with the virtual pet
- `GET /status`: Get the current status of the pet
- `GET /metrics`: Prometheus metrics endpoint

## Creating a Grafana Dashboard

1. Log into Grafana (http://localhost:3000) using the default credentials (admin/admin).
2. Click "Create your first dashboard".
3. Add a new panel.
4. Choose Prometheus as the data source.
5. Use PromQL queries to visualize metrics, e.g., `pet_feeds_total`, `pet_plays_total`, `pet_happiness`, `pet_hunger`.
6. Save your dashboard.

## Stopping the Project

To stop and remove all containers:

```
docker-compose down
```

To also remove volumes:

```
docker-compose down -v
```

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

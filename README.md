# Ubisoft Game Status Exporter
[![Docker Hub](https://img.shields.io/docker/pulls/ewpratten/ubisoft_status_exporter)](https://hub.docker.com/r/ewpratten/ubisoft_status_exporter)

A [Prometheus](https://prometheus.io/) exporter that reports the status of [Ubisoft](https://www.ubisoft.com) game servers.

## Usage

```sh
docker run -p 8000:8000 ewpratten/ubisoft_status_exporter:latest
```

Metrics will be available on [localhost:8000/metrics](http://localhost:8000/metrics).

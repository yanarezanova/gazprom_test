from locust import HttpUser, task, between
import datetime
import random

class DeviceStatisticUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def post_statistic(self):
        payload = {
            "device_id": "device_123",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "x": random.uniform(0, 100),
            "y": random.uniform(0, 100),
            "z": random.uniform(0, 100)
        }
        self.client.post("/api/statistics", json=payload)

    @task
    def get_statistics(self):
        self.client.get("/api/statistics/device/device_123")

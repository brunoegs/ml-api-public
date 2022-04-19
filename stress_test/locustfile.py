import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        self.client.get('/')

    @task(3)
    def predict_neutral(self):
        self.client.post('/predict', params={'text': 'guerra'})

    @task(1)
    def predict_negative(self):
        self.client.post('/predict', params={'text': 'dolar'})

    @task(1)
    def predict_positive(self):
        self.client.post('/predict', params={'text': 'dolar mep'})

    def on_start(self):
        pass

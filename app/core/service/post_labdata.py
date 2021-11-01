import requests


class LabData:
    BASE_URL = 'http://192.168.182.132:8080/openmrs/ws/rest/v1'

    def __init__(self, base_url):
        self.BASE_URL = base_url

    def post_data(self, data):
        pass

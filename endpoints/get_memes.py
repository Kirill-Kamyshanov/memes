from endpoints.endpoint import Endpoint
import requests

class GetAllMemes(Endpoint):
    def get_all_memes(self, token):
        headers = {"Authorization": token}
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()

        print(self.response)
        print(self.status_code)
        print(self.response_body)

import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        loads_list =[]
        loads = json.loads(self.get_response_body())
        return loads
    
        # loads_list =[]
        # loads=json.loads(self.get_response_body())
        # for load in loads:
        #     loads_list.append(load["name", "occupation"])

        # return loads_list
    

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()


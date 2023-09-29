import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

class Desk:
    def __init__(self):
        self.__url_auth = os.getenv("END_POINT_AUTH")
        self.__url_relatorio = os.getenv("END_POINT_RELATORIO")
        self.__auth = self.authentication()

    def authentication(self):
        headers = {
            "Authorization": os.getenv("CHAVE_DESK_ADM")
            }
        data_json = {
            "PublicKey": os.getenv("CHAVE_DESK_AMBIENTE")
            }
        try:
            response = requests.post(self.__url_auth, json=data_json, headers=headers)
        except:
            print("Error na resposta da rota autenticar")
            time.sleep(14)
            self.authentication()
            
        if (response.status_code == 200) and (len(response.json()) == 59):
            return response.json()
        else:
            print("Error na resposta da rota autenticar")

    def relatorio(self, id) -> dict:
        headers = {
            "Authorization": self.__auth
        }

        data_json = {
            "Chave": id
        }
        try:
            response = requests.post(
                self.__url_relatorio,
                json=data_json,
                headers=headers
            )
        except:
            print("Error na resposta da rota relatário")
            time.sleep(60)
            self.__auth = self.authentication()
            self.relatorio(id)
        
        if (response.status_code == 200) and (response.json().get("root")):
            return response.json()
        else:
            print("Error na resposta da rota relatário")
            self.__auth = self.authentication()
            self.relatorio(id)



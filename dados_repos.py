import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class DadosRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_TOKEN')

        if not self.access_token:
            raise ValueError("O token de acesso do GitHub não foi encontrado. Certifique-se de que a variável de ambiente GITHUB_TOKEN está definida.")
        
        self.headers = {
            'Authorization': 'Bearer' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def lista_repositorios(self):
        repos_list = []
        for page in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.username}/repos?per_page=100&page={page}'
                response = requests.get(url, headers=self.headers)
                repos_list.extend(response.json())
            except:
                repos_list.append(None)
        return repos_list
    

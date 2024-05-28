"""Module for Data Funcitionality"""

import sys
import os
from openai import OpenAI
from bundle import Bundle
from identifier import Identifier

class TalkingService:
    """Class for talking to external platforms"""
    def __init__(self):
        print(sys.version)

        self.oai = OpenAI(api_key = os.environ.get("CHATGPT_GOODPLACE", ""))

    def find(self, data):
        """Function to find"""

        print(data)

        ai_response = self.oai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": f'{data}'
            }
        ],
        )

        result = Bundle()

        oai_identifier = Identifier(system=ai_response.model, value=ai_response.id)

        result.identifier = oai_identifier

        print(ai_response)

        return result

    def append(self, data):
        """Function adds data"""
        print('Adding Data')
        return data

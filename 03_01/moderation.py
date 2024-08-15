from pprint import pprint

from openai import OpenAI
client = OpenAI()

response = client.moderations.create(input="Sample text goes here.")

output = response.results[0]

pprint(output.dict())
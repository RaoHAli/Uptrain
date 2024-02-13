from uptrain import APIClient, Evals, CritiqueTone
from api_request import get_response
import json

UPTRAIN_API_KEY = "up-6a0d513bbffb49ccb712ee6d0ea9e743" 

with open('test_data.json', 'r') as file:
    data = json.load(file)

for entry in data:
    entry['response'] = get_response(entry['question'])

client = APIClient(uptrain_api_key=UPTRAIN_API_KEY)
results = client.log_and_evaluate(
    project_name="Test LLM",
    data=data,
    checks=[
        Evals.FACTUAL_ACCURACY,
        Evals.RESPONSE_RELEVANCE,
        Evals.RESPONSE_COMPLETENESS,
        Evals.RESPONSE_CONCISENESS,
        CritiqueTone(llm_persona="teacher")
    ]
)

print(json.dumps(results, indent=3))


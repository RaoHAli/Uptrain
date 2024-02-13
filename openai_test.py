from uptrain import EvalLLM, Evals
from api_request import get_response
import json

OPENAI_API_KEY = "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"

# Load data from the input JSON file
with open('test_data.json', 'r') as file:
    data = json.load(file)

for entry in data:
    entry['response'] = get_response(entry['question'])

eval_llm = EvalLLM(openai_api_key=OPENAI_API_KEY)

results = eval_llm.evaluate(
    data=data,
    checks=[
        Evals.FACTUAL_ACCURACY,
        Evals.RESPONSE_RELEVANCE,
        Evals.RESPONSE_COMPLETENESS,
        Evals.RESPONSE_CONCISENESS
    ]
)

print(json.dumps(results, indent=3))
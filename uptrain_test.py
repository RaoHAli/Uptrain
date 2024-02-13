from uptrain import APIClient, Evals, CritiqueTone
from api_request import get_response
import json

UPTRAIN_API_KEY = "up-6a0d513bbffb49ccb712ee6d0ea9e743" 

data = [{
    "question": "What are the four largest moons of Jupiter?",
    "context": "Jupiter's largest moons, known as the Galilean moons—Io, Europa, Ganymede, and Callisto—stand out for their unique features. Io showcases active volcanoes, while Europa intrigues with a potential subsurface ocean. Ganymede, the largest moon, has an icy surface and magnetic field, and Callisto boasts ancient, cratered terrain.",
    "response": "The four largest moons of Jupiter, known as the Galilean moons, are Io, Europa, Ganymede, and Callisto."
}]

client = APIClient(uptrain_api_key=UPTRAIN_API_KEY)
results = client.log_and_evaluate(
    project_name="Test LLM",
    data=data,
    checks=[
        Evals.FACTUAL_ACCURACY
       
    ]
)

print(json.dumps(results, indent=3))


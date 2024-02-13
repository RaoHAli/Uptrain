import requests
import json
import time


def get_response(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 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'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check for rate limit exceeded (429) response
    if response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 10))
        print(f"Rate limit exceeded. Waiting for {retry_after} seconds.")
        time.sleep(retry_after)
        # Retry the request
        return get_response(prompt)

    # Check for successful response
    elif response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    
    # Handle other error cases
    else:
        error_message = f"Request failed with status code {response.status_code}."
        return error_message



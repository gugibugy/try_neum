import requests

CREATE_WORKFLOW_ENDPOINT = "https://api.tryneum.com/v1/workflows"
REQUEST_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json"
}

def main():
    summarize_text_block = {
        "name":"summarize_text",
        "ai_model_config": {
            "llm_model":"gpt-4",
            "use_chat_history":"true",
            "prompt":{
                "prompt_template":"Pretend you are a news anchor summarizing the latest news"
            }
        }
    }
    workflow_request = {
        "user_email":"davidjose96@hotmail.com",
        "name": "News Summary",
        "blocks": [
            {
                "name": "query_serp"
            },
            summarize_text_block
        ]
    }
    resp = requests.post(CREATE_WORKFLOW_ENDPOINT, json=workflow_request, headers=REQUEST_HEADERS)
    if not resp.ok:
        print(f'There was an issue reaching neum: {resp.reason}')
        return
    workflow_id = resp.json()['workflow_id']

    print(workflow_id)

if __name__ == "__main__":
    main()
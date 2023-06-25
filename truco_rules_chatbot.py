import requests

CREATE_WORKFLOW_ENDPOINT = "https://api.tryneum.com/v1/workflows"
REQUEST_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json"
}

def main():
    query_doc_block = {
        "name":"query_doc",
        "data_source": "https://drive.google.com/file/d/1qbO8-eIrg4rrpys7xoFRolaNZ5cgz3et/view",
        "ai_model_config": {
            "llm_model":"gpt-4",
            "use_chat_history":"true",
            "prompt":{
                "prompt_template":"Eres un chatbot que ayuda a las personas " +
                "con sus preguntas sobre las reglas de truco venezolano"
            }
        }
    }
    workflow_request = {
        "user_email":"davidjose96@hotmail.com",
        "name": "Truco Rules Chatbot",
        "blocks": [
            query_doc_block
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
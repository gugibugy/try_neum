import argparse
import requests

RUN_WORKFLOW_ENDPOINT = "https://api.tryneum.com/v1/run-workflow"
REQUEST_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json"
}

def run_workflow(workflow_id: str, user_message: str, session_id:str):
    request = {
        "user_message": user_message,
        "session_id": session_id if session_id else "",
        "workflow_id": workflow_id
    }
    resp = requests.post(RUN_WORKFLOW_ENDPOINT, json=request, headers=REQUEST_HEADERS)
    if not resp.ok:
        print(f'Something when wrong when running the workflow: {resp.reason}')
        return
    resp_content = resp.json()
    print(resp_content['output'])

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-wid", "--workflow_id", help="The Id of the workflow you wish to run", required=True)
    argParser.add_argument("-um", "--user_message", help="Prompt that you would like to give the workflow", required=True)
    argParser.add_argument("-sid", "--session_id", help="The Id of the session you wish to run in", required=True)
    args = argParser.parse_args()
    run_workflow(args.workflow_id, args.user_message, args.session_id)
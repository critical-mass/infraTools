import requests
import argparse

OKTA_API_BASE_URL = "https://your-okta-domain.okta.com/api/v1/"

def get_app_assignments(app_id, api_token):
    headers = {
        "Authorization": f"SSWS {api_token}",
        "Accept": "application/json"
    }

    assignments_url = OKTA_API_BASE_URL + f"apps/{app_id}/groups"
    response = requests.get(assignments_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve app assignments: {response.text}")
        return []

    return response.json()

def convert_to_individual(app_id, group_id, api_token):
    headers = {
        "Authorization": f"SSWS {api_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    individual_assignment_url = OKTA_API_BASE_URL + f"apps/{app_id}/groups/{group_id}"
    response = requests.delete(individual_assignment_url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully converted group assignment to individual for group ID: {group_id}")
    else:
        print(f"Failed to convert group assignment for group ID: {group_id}. Error: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert app assignments from group to individual in Okta.")
    parser.add_argument("application_id", type=str, help="Application ID for which assignments need to be converted.")
    parser.add_argument("group_id", type=str, help="Group ID to be converted to an individual assignment.")
    parser.add_argument("api_token", type=str, help="Okta API Token.")

    args = parser.parse_args()

    app_assignments = get_app_assignments(args.application_id, args.api_token)

    if not app_assignments:
        print("No assignments found for the given application.")
    else:
        for assignment in app_assignments:
            if assignment["id"] == args.group_id:
                convert_to_individual(args.application_id, args.group_id, args.api_token)
                break
        else:
            print("Group ID not found in the application assignments.")
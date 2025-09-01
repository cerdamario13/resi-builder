import json
import os

def build_user_history_file(file_name: str = 'user_history.json') -> str:
    """
    Build the user history json file

    :param file_name: Name or path of the file that will contain the user history. File must be json.
    """

    # Ensure that the file is always json
    base, ext = os.path.splitext(file_name)
    if ext.lower() != '.json':
        file_name = f"{base}.json"


    resume_template = {
    "contact_info": {
        "name": "",
        "phone": "",
        "email": "",
        "linkedIn": ""
    },
    "education": [
        {
            "school": "",
            "degree": "",
            "field_of_study": "",
            "location": ""
        }
    ],
    "history": [
        {
            "role": "",
            "company": "",
            "dates": "",
            "experience": [],
            "industry": []
        }
    ],
    "activities_and_interests": "",
    "profile": "",
    "skills": []
    }

    # Save as a JSON file
    with open(file_name, "w") as f:
        json.dump(resume_template, f, indent=2)
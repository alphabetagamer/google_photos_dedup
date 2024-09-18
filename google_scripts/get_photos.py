from os.path import join, dirname
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

SCOPES = "https://www.googleapis.com/auth/photoslibrary.readonly"

store = file.Storage(join(dirname(__file__), "token-for-google.json"))
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(
        join(
            dirname(__file__),
            "client_secret.json",
        ),
        scope=SCOPES,
    )
    creds = tools.run_flow(flow, store)
google_photos = build(
    "photoslibrary", "v1", http=creds.authorize(Http()), static_discovery=False
)


def append_to_json(new_data):
    # Read the existing data from the JSON file
    # Rename the file name for the account you are reading from
    try:
        with open("./files_account.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Ensure the data is a list
    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list at the root level.")

    # Append the new data
    data.extend(new_data)

    # Write the updated list back to the JSON file
    with open("./files_account.json", "w") as file:
        json.dump(data, file, indent=4)


nextpagetoken = "Dummy"
while nextpagetoken != "":
    nextpagetoken = "" if nextpagetoken == "Dummy" else nextpagetoken
    results = (
        google_photos.mediaItems()
        .search(
            body={
                # "filters": {
                #     "dateFilter": {
                #         "dates": [{"day": day, "month": month, "year": year}]
                #     }
                # },
                "pageSize": 100,
                "pageToken": nextpagetoken,
            }
        )
        .execute()
    )
    # The default number of media items to return at a time is 25. The maximum pageSize is 100.
    items = results.get("mediaItems", [])
    nextpagetoken = results.get("nextPageToken", "")

    append_to_json(items)
    for item in items:
        print(
            f"{item['filename']} {item['mimeType']}"
            f" {item['mediaMetadata']['creationTime']}\nURL: {item['productUrl']}"
        )

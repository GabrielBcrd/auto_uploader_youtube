import os
from google.oauth2.credentials import Credentials
import google.auth.transport.requests
import google_auth_oauthlib.flow
import googleapiclient.discovery

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube(username):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client_secrets_file = "client.json"
    # Create token folder if it doesn't exist
    token_dir = "token"
    os.makedirs(token_dir, exist_ok=True)
    
    token_file = os.path.join(token_dir, f"token_{username}.json")

    credentials = None

    if os.path.exists(token_file):
        credentials = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(google.auth.transport.requests.Request())
            except Exception:
                credentials = None

        if not credentials:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES)
            credentials = flow.run_local_server()

        with open(token_file, 'w') as token:
            token.write(credentials.to_json())

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube


def upload_video(youtube):
    request_body = {
        "snippet": {
            "categoryId": "22",
            "title": "Uploaded from Python",
            "description": "This is the most awsome description ever",
            "tags": ["test","python", "api" ]
        },
        "status":{
            "privacyStatus": "private"
        }
    }

    # put the path of the video that you want to upload
    media_file = os.path.join("videos","video.mp4")

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True)
    )

    response = None 

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress()*100)}%")

        print(f"Video uploaded with ID: {response['id']}")

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    youtube = authenticate_youtube(username)
    upload_video(youtube)
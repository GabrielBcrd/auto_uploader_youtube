# YouTube Video Upload Script

This repository contains a Python script to upload videos to YouTube using the YouTube Data API v3.  
It handles user authentication, video metadata setup, and the upload process automatically.


## 🧩 Purpose

This script is used in a Discord bot context. It enables members of a private Discord server to authenticate with their Google accounts and upload videos directly to their own YouTube channels.


## 🔐 Privacy and Security

- Only the `https://www.googleapis.com/auth/youtube.upload` scope is requested.
- No other user data (e.g., viewing history, analytics, comments) is accessed.
- OAuth tokens are stored locally in `token_<username>.json`.
- No data is sent to any external server or stored in the cloud.
- You may revoke access at any time at: [Google Account Permissions](https://myaccount.google.com/permissions).


## ✅ Prerequisites

Before using the script:

1. **Google Cloud Project** with the YouTube Data API v3 enabled.
2. **OAuth 2.0 Credentials** downloaded as a JSON file.
3. **Python 3.x** installed on your system.

---
## Getting Started

### Step 1: Set Up Google Developer Console

1. **Navigate to the Developer Console**: Go to [Google Developer Console](https://console.developers.google.com/).
2. **Create a New Project**: Click on "Select Project" at the top, then "New Project". Give it a name and create it.
3. **Enable YouTube Data API v3**: Go to "API & Services Dashboard" and click on "Enable APIs and Services". Search for "YouTube Data API v3" and enable it.
4. **Set Up OAuth Consent Screen**: Go to "OAuth consent screen" on the left, select "External", and fill in the required details.
5. **Create OAuth 2.0 Credentials**: Go to "Credentials", click on "Create Credentials", and select "OAuth 2.0 Client IDs". Download the JSON file with your credentials and save it securely.

### Step 2: Install Required Libraries

Install the necessary libraries using pip:

`pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`

### Step 3: Configure and Run the Script

1. **Place the Credentials File**: Ensure the `client_secrets_file` path in the script points to your downloaded credentials JSON file.
2. **Update the Script**: Modify the script as needed for your video upload. The script includes authentication and upload functionality.

### Step 4: Run the Script

Run the script from your terminal or command line:

`python run.py username`

The script will prompt you to authenticate with your Google account. Once authenticated, it will upload the specified video to your YouTube channel.

## Script Details

The script performs the following tasks:

1. **Authenticate with Google**: Uses OAuth 2.0 to authenticate with the YouTube Data API v3.
2. **Upload Video**: Uploads the video to YouTube with the specified metadata.

## Troubleshooting

If you encounter issues, ensure that:

- The credentials file is correctly placed and the path is correct.
- You have enabled the YouTube Data API v3 in your Google Developer Console.
- The necessary libraries are installed in your Python environment.
- The google cloud console app authorize the google account in test user or google cloud console app is in production so verified by google (3-7 working days)


## Privacy and Security

This script uses OAuth 2.0 to authenticate users via Google's secure flow. It requests only the `youtube.upload` scope and does not request or access any other user data.

- Tokens are stored locally in `token_<username>.json`.
- No user data is stored, sent to external servers, or shared.
- You may revoke the app's access at any time via your [Google Account Permissions](https://myaccount.google.com/permissions).

This project is intended to be used only by the developer to manage video uploads to personal YouTube channels.

📃 [Privacy Policy](https://github.com/GabrielBcrd/auto_uploader_youtube/blob/main/privacy.md)  
📄 [MIT License](https://github.com/GabrielBcrd/auto_uploader_youtube/blob/main/LICENSE)
📄 [Terms of use](https://github.com/GabrielBcrd/auto_uploader_youtube/blob/main/terms_of_use.md)
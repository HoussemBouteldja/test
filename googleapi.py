import os.path
from googleapiclient.discovery import build
from oauth2client import file, client, tools
import argparse


class GoogleAPI:

    def __init__(self):
        
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
        # Get the real path from the symbolic path
        storage_real_path = os.path.realpath("credentials/storage.json")
        store = file.Storage(storage_real_path) # store credentials
        creds = store.get()
        
        # Use credentials json from google apis (mynetworkdb account)
        if not creds or creds.invalid:
            print(">>> make new storage data file <<<")
            secrets_real_path = os.path.realpath("credentials/client_secrets.json")
            flow = client.flow_from_clientsecrets(secrets_real_path, SCOPES)
            creds = tools.run_flow(flow, store)

        self.service_drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
        self.service_sheet = build('sheets', 'v4', credentials=creds, cache_discovery=False)
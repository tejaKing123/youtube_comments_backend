from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pdclea
import demoji
from langdetect import detect
import re   # regular expression
import pandas as pd
import os
def main():
  CLIENT_SECRETS_FILE = "client_secret.json"

  SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
  API_SERVICE_NAME = 'youtube'
  API_VERSION = 'v3'

  def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

  service = get_authenticated_service()

def can_you():
  return "hello"
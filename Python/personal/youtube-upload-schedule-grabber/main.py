from googleapiclient.discovery import build
from datetime import datetime, timedelta
from collections import Counter
import os

# Replace with your own API key and Channel ID
API_KEY = "AIzaSyBAPMsA3vKgDNvSnJ7_h1mjKEym7hbPRR4"
CHANNEL_ID = "UCWPL3MXXP67-QTgLnIotrNQ"

def get_video_upload_dates(channel_id, days=30):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Set up date range: last `days` days from today
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    start_date_iso = start_date.isoformat("T") + "Z"
    end_date_iso = end_date.isoformat("T") + "Z"

    # Get the uploads playlist ID
    channel_response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Fetch videos uploaded in the last `days` days
    video_dates = []
    next_page_token = None

    while True:
        playlist_response = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in playlist_response['items']:
            # Get video upload date
            published_date = item['snippet']['publishedAt']
            published_date = datetime.strptime(published_date, "%Y-%m-%dT%H:%M:%SZ")
            if start_date <= published_date <= end_date:
                video_dates.append(published_date.date())

        # Check for more pages
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break

    return video_dates

def analyze_upload_pattern(video_dates):
    # Count uploads per day
    date_counter = Counter(video_dates)
    
    # Generate readable output
    upload_pattern = {}
    for day, count in date_counter.items():
        weekday = day.strftime("%A")
        if weekday not in upload_pattern:
            upload_pattern[weekday] = []
        upload_pattern[weekday].append((day, count))
    
    # Summarize by day of week
    print("\nYouTube Upload Patterns by Day of Week (Last 30 Days):\n")
    for weekday in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        if weekday in upload_pattern:
            print(f"{weekday}: {len(upload_pattern[weekday])}")
        else:
            print(f"{weekday}: No uploads")
    print("\n")

if __name__ == "__main__":
    # Fetch video dates from the past month
    video_dates = get_video_upload_dates(CHANNEL_ID, days=30)

    # Analyze and output upload pattern
    analyze_upload_pattern(video_dates)
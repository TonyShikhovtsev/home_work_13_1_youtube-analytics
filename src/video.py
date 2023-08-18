from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        self.fetch_video_info()

    def fetch_video_info(self):
        service = build('youtube', 'v3', developerKey="AIzaSyDHgpl7lB3wLwo17yG67V1zkWbZnmm5pWI")
        video_response = service.videos().list(part='snippet, statistics', id=self.video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.video_link = f"https://youtu.be/{self.video_id}"
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        return self.title

class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.title = title  # Add the title parameter here


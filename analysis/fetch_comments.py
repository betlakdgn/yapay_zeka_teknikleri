from googleapiclient.discovery import build
from config.config import API_KEY
import csv
import os


def get_video_comments(video_id, max_results=100):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    response = request.execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            reply_count = item['snippet']['totalReplyCount']
            comments.append({
                "comment": comment,
                "like_count": like_count,
                "reply_count": reply_count
            })

        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                maxResults=max_results,
                textFormat="plainText"
            )
            response = request.execute()
        else:
            break

    return comments


def save_comments_to_csv(comments, filename="data/comments.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Comment", "Like Count", "Reply Count"])
        for comment in comments:
            writer.writerow([comment['comment'], comment['like_count'], comment['reply_count']])


# Örnek kullanım
if __name__ == "__main__":
    video_id = "VIDEO_ID_HERE"  # Videonun ID'sini buraya ekleyin
    comments = get_video_comments(video_id)
    save_comments_to_csv(comments)
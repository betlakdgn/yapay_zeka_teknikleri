from analysis.fetch_comments import get_video_comments, save_comments_to_csv
from analysis.train_model import train_model

video_id = "VIDEO_ID_HERE"

# Yorumları çekme ve kaydetme
comments = get_video_comments(video_id)
save_comments_to_csv(comments)
print("Yorumlar başarıyla çekildi ve CSV'ye kaydedildi.")
import re

trailer_youtube_url="https://www.youtube.com/watch?v=61Vc46RbVOs"
youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_youtube_url)
print youtube_id_match

youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', trailer_youtube_url)
print youtube_id_match.group(0)


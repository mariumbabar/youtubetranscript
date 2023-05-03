from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

vid_id = '8aDFvvjC6XM'

data = yta.get_transcript(vid_id)

transcript = ''
for value in data:
    for key,val in value.items():
        if key == 'text':
            transcript += val

l = transcript.splitlines()
final_tra = " ".join(l)

file=open("Depression2.txt",'w')
file.write(final_tra)
file.close()

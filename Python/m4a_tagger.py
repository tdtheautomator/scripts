import os
import re
from mutagen.easymp4 import EasyMP4
from mutagen.mp4 import MP4
music_dir = "C://Temp//Music"

def list_file_to_process(root_path,file_extension):
    return[os.path.join(root, name)
           for root, dirs, files in os.walk(root_path)
           for name in files
           if name.endswith((file_extension))]

def show_mp4_tags(file_path):
    tags = EasyMP4(file_path)
    return tags

def string_replacer(input,match):
    output = input[:input.index(match) + len(input)]
    return output

def string_normalizer(input):
    output = input.replace('"','').strip()
    output = output.replace('"','')
    output = output.replace("'",'')
    output = output.replace("'",'')
    output = output.replace(';',' ')
    output = output.replace('(','')
    output = output.replace(')','')
    output = re.sub(' -$', '', output)
    output = output.strip()
    return output

def m4a_set_album(file_path):
    MP4tagger = MP4(file_path)
    mp4tags = show_mp4_tags(file_path)
    album = mp4tags['album'][0]
    album = string_normalizer(album)
    if "From " in album:
        album.split('From ')
        album = album.partition("From ")[2]
        MP4tagger['\xa9alb'] = album
        MP4tagger.save()
    elif "Original Motion Picture Soundtrack" in album:
        album = album.replace('Original Motion Picture Soundtrack','').strip()
        MP4tagger['\xa9alb'] = album
        MP4tagger.save()
    else:
        MP4tagger['\xa9alb'] = album
        MP4tagger.save()

def m4a_set_title(file_path):
    MP4tagger = MP4(file_path)
    mp4tags = show_mp4_tags(file_path)
    title = mp4tags['title'][0]
    title = string_normalizer(title)
    if "From " in title:
        title.split('From ')
        title = title.partition("From ")[0]
        MP4tagger['\xa9nam'] = title
        MP4tagger.save()
    else:
        MP4tagger['\xa9nam'] = title
        MP4tagger.save()

m4a_files = list_file_to_process(music_dir,".m4a")

print (m4a_files)
for file in m4a_files:
    print(f"processing {file}")
    #m4a_set_album(file)
    m4a_set_title(file)
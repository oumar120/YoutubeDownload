from pytube import YouTube
import os
base_url_youtube = "https://www.youtube.com"
def download(url):
    video = YouTube(url)
    print(f"""
Titre: {video.title}
Nombre de vues: {video.views}
    """)
    streams = []
    while True:
        try:
            format = int(input("Veuillez choisir le format:\n 1.audio \n 2.video\n"))
        except:
            print("vous devez saisir un nombre")
        else:
            if 1<=format<=2:
                streams = video.streams.filter(progressive=True) if format==2 else video.streams.filter(only_audio=True,mime_type="audio/mp4")
                break
            else:
                print("vous devez saisir un nombre entre 1 et 2")
    if len(streams) > 1:
            for i in range(len(streams)):
                  print(f"{i+1}.{streams[i].abr}") if streams[i].abr else  print(f"{i+1}.{streams[i].resolution}")
            while True:
                  try:
                      resolution = int(input("veuillez choisir une resolution: "))
                  except:
                      print("Vous devez saisir un nombre")
                  else:
                      if resolution <= len(streams):
                          break
                      else:
                          print(f"vous devez saisir un nombre compris entre 1 et {len(streams)}")
    else:
        resolution = 1
    video.register_on_progress_callback(progression)
    if streams[0].mime_type == "audio/mp4":
        video.streams.get_by_itag(streams[resolution - 1].itag).download(os.path.join(os.environ['homepath'],"Downloads","audio"))
    else:
        video.streams.get_by_itag(streams[resolution - 1].itag).download(os.path.join(os.environ['homepath'],"Downloads","video"))
    print("✅ téléchargement terminé")

def progression(stream,chunk,remaining_time):
    downloded = stream.filesize - remaining_time
    progress = downloded*100/stream.filesize
    print(f"progression du téléchargement {int(progress)}%")
def startDonload(option):
        url = input("veuillez saisir l'url de la video à télécharger: ") if option == 1 else input("veuillez saisir les urls séparé par des espaces: ")
        urls = url.split(" ")
        for url in urls:
            if url.lower().startswith(base_url_youtube):
                download(url)
            else:
                print("❌ Erreur, vous devez saisir une url valide de youtube")
                return startDonload(option)

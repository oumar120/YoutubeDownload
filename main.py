import youtube_donloader
print("YOUTUBE-Downloader - Logiciel de télécharggement de vidéos et audios à partir de youtube")
print("Auteur: Oumar BALDE")
while True:
    print("""___________________________MENU________________________
1.télécharger avec une url
2.télécharger avec plusieurs urls
3.quitter
    """)
    try:
       choix = int(input("Veuillez choisir une option: "))
    except:
        print("❌ Erreur,vous devez saisir un nombre")
    else:
        if 1 <= choix <=3:
            match choix:
                case 1:
                    youtube_donloader.startDonload(1)
                case 2:
                    youtube_donloader.startDonload(2)
                case 3:
                    break
        else:
            print("❌ vous devez choisir une option valide")


#🎞️❤️✅❌🎬💎🎶
#print(video.title)
#print("les streams")
#for stream in video.streams.fmt_streams:
#   print(stream)
#print("telechargement...")

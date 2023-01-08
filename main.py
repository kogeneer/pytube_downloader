from pytube import YouTube

def download(url):
  videoObj = YouTube(url)
  videoObj = videoObj.streams.get_highest_resolution()
  try:
    videoObj.download('<directory path of your choosing>')
    print("Success!")
  except:
    print("Error: could not download this video")

def main():
    link = input("paste your video link here: ")
    download(link)

if __name__ == "__main__":
    main()

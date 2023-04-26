from pytube import YouTube, Search
import yt_dlp

PATH = ".\\Media\\" + "%(title)s.%(ext)s"

YDL_OPTIONS_AUDIO = {
  "format": "bestaudio", 
  "noplaylist": "True",
  "outtmpl": PATH
}

YDL_OPTIONS_VIDEO = {
    'format': 'best',
    'forceurl': True,
    'quiet': False,
}

def download_video(youtube, error_times: int):
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS_AUDIO) as ydl:
          ydl.download(youtube.watch_url)
          
        print("完成!")
        print("===========")
    except Exception as exception:
        error_times += 1
        if error_times <= 5:
            print(f"正在重試..({error_times}/5)")
            download_video(youtube, error_times)

        else:
          print(f"下載失敗.. \n錯誤: {exception}")

def get_url(youtube, error_times: int):
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS_VIDEO) as ydl:
          video_info = ydl.extract_info(youtube.watch_url, download=False)
          video_url = video_info['url']
          return video_url
    except Exception as exception:
        error_times += 1
        if error_times <= 5:
            print(f"正在重試..({error_times}/5)")
            get_url(youtube, error_times)
    
        else:
          return f"連結取得失敗.. \n錯誤: {exception}"

def download_or_not(youtube):

    print(f"連結: {youtube.watch_url}")
    print(f"名稱: {youtube.title}")
    print(f"作者: {youtube.author}")
    youtube.bypass_age_gate()
    print("----------")

    is_download = input("是否要下載 ? (Y/N): ")
    if is_download in ["是", "Y", "y", "1"]:
        print("開始下載...")
        download_video(youtube, 0)
    elif is_download in ["否", "N", "n", "0"]:
        print("----------")
        print("<取消下載>")
        print("----------")
        print(f"連結:\n\n{get_url(youtube, 0)}\n")
        print("===========")
    else:
        print("預期外的輸入")
        print("===========")

def search_videos(query):
    if query.startswith("https://www.youtube.com/"):
        youtube = YouTube(query, use_oauth=True)
        download_or_not(youtube)
    else:
        search = Search(query)
        results = search.results

        print("----------\n搜尋到:")
        for i, result in enumerate(results):
            print(f"#{i+1:-3d} {result.title}")

        select_index = int(input("請輸入搜尋結果的編號(取消: -1): ")) - 1
        while select_index not in range(len(results)) and select_index != -2:
            select_index = int(input("預期外的內容，請重新輸入: ")) - 1

        if select_index != -2:
            print("----------")
            download_or_not(results[select_index])
        else:
            print("===========")

        try:
            suggestions = search.completion_suggestions
            print("其他推薦的搜尋:")
            print("\n".join(suggestions))
            print("===========")
        except:
            print("沒有搜尋建議")
            print("===========")

def main():
    while True:
        query = input("請輸入關鍵字或網址(退出: -1): ")
        if query in ["-1", "退出", "", None]:
            print("===========")
            print("<退出>")
            break
        else:
            print(f"搜尋 {query} 中..")
            search_videos(query)

if __name__ == "__main__":
    main()
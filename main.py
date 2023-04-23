from pytube import YouTube, Search
import threading

PATH = ".\\Videos"

def download_video(youtube, error_times: int):
    try:
        title = youtube.title.replace("/", "")
        youtube.streams.get_highest_resolution().download(output_path=PATH, filename=f"{title}.mp4")
        print("完成!")
        print("===========")
    except Exception as e:
        error_times += 1
        if error_times <= 3:
            retry = input(f"錯誤: {e}\n是否重試一次 ? (Y/N): ")
            if retry in ["是", "Y", "y", "1"]:
                download_video(youtube, error_times)
        

def download_or_not(youtube):

    print(f"長度: {youtube.length} 秒")
    print(f"名稱: {youtube.title}")
    print(f"作者: {youtube.author}")
    print("----------")

    is_download = input("是否要下載 ? (Y/N): ")
    if is_download in ["是", "Y", "y", "1"]:
        print(f"開始下載...")
        start_download = threading.Thread(target=download_video, args=(youtube, 0, ))
        start_download.start()
        start_download.join()
        print("完成 !")
        print("===========")
    elif is_download in ["否", "N", "n", "0"]:
        print("----------")
        print(f"<取消下載>")
        print("----------")
        print(f"連結:\n\n{youtube.streams.get_highest_resolution().url}\n")
        print("===========")
    else:
        print("預期外的輸入")
        print("===========")

def search_videos(query):
    if query.startswith("https://www.youtube.com/"):
        youtube = YouTube(query)
        download_or_not(youtube)
    else:
        search = Search(query)
        results = search.results

        print("----------\n搜尋到:")
        for i, result in enumerate(results):
            print(f"#{i+1:-3d} {result.title}")

        select_index = int(input("請輸入搜尋結果的編號(取消: -1): ")) - 1
        while select_index not in range(len(results)) and select_index != -2:
            select_index = int(input(f"預期外的內容，請重新輸入: ")) - 1

        if select_index != -2:
            print("----------")
            download_or_not(results[select_index])
        else:
            print("===========")

        try:
            suggestions = search.completion_suggestions
            print(f"其他推薦的搜尋:")
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
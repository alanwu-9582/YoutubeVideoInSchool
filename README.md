# Youtube Video In School
當你在學校資訊課時感到無聊，但 Youtube 又會被學校擋下來，你可以使用這個程式來讓你在資訊課時也能使用學校的電腦看 Youtube

## 安裝
### 本地安裝
1. 下載 [Python](https://www.python.org/downloads/) 
2. 記得要把 **Add python.exe to PATH** 打勾
3. 下載整個程式的資料夾
4. 安裝 pytube  
    ```shell
    pip install pytube
    ```
5. 執行程式

### 線上環境
1. 複製 https://github.com/alanwu-9582/YoutubeVideoInSchool.git
2. 前往 [Replit](https://replit.com/~)
3. 建立一個新的 repl 
4. 點擊 **Import from GitHub**
5. 載入之後就能執行了  (第一次通常會比較久)

或是
1. 打開 https://replit.com/@Wu-Jin-Lun-Alan/YoutubeVideoInSchoolshare#main.py
2. 點擊 Fork
3. 到 Fork 除來的檔案執行

## 使用方式
1. 啟動程式
2. 輸入關鍵字或影片網址  
使用者可以輸入關鍵字或影片網址。若輸入 -1，程式即結束。

3. 搜尋影片  
程式會搜尋與關鍵字相關的影片，或直接下載網址輸入的影片。若搜尋結果不符合預期，可以再次輸入關鍵字或影片網址。

4. 確認是否下載  
程式會顯示影片的標題、作者和長度，使用者可以決定是否下載影片。

5. 下載影片  
若使用者決定下載影片，可以選擇下載音檔或影片檔

6. 完成下載  
下載完成後，程式會顯示下載完成訊息。

## 參數說明
### PATH
程式會將下載的影片存在 PATH 設定的路徑。使用者可以修改此參數以設定自己想要的下載路徑。預設值為 ".\\Videos"。

### download_video(youtube, error_times: int)
此函式會下載影片。使用者可以修改此函式以改變下載影片的方式，例如改變下載影片的畫質。

### download_or_not(youtube)
此函式會詢問使用者是否下載影片。使用者可以修改此函式以改變詢問使用者的方式，例如增加詢問使用者是否下載影片的理由。

### search_videos(query)
此函式會搜尋影片，並顯示搜尋結果。使用者可以修改此函式以改變搜尋的方式，例如增加搜尋影片的條件。

### main()
此函式是主程式，會一直循環直到使用者輸入 -1 結束程式。使用者可以修改此函式以增加自己的功能。
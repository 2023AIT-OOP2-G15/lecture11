import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# 画像処理プログラムをインポート

# Flaskでアップロードされるディレクトリと処理後保存先ディレクトリを指定
UPLOAD_DIRECTORY = './static/uploads'
PROCESSED_DIRECTORY = './static/processes'

# ディレクトリ監視用のイベントハンドラ
class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        

        # ディレクトリ内のファイルをリストアップ
        image_files = [f for f in os.listdir(event.src_path) if os.path.isfile(os.path.join(event.src_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # リスト内の画像ファイルを表示
        for image_file in image_files:
            print(image_file)

# 監視
if __name__ == "__main__":
    observer = Observer()
    event_handler = CustomHandler()
    observer.schedule(event_handler, UPLOAD_DIRECTORY, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 画像処理プログラムをインポート

# Flaskでアップロードされるディレクトリと処理後保存先ディレクトリを指定
UPLOAD_DIRECTORY = '/path/to/upload/directory'
PROCESSED_DIRECTORY = '/path/to/processed/directory'

# ディレクトリ監視用のイベントハンドラ
class CustomHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
    
    def on_modified(self, event):
        if event.is_directory:
            return

# 監視
if __name__ == "__main__":
    observer = Observer()
    event_handler = CustomHandler()
    observer.schedule(event_handler, path=UPLOAD_DIRECTORY, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

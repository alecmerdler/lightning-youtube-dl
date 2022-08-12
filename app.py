from lightning import LightningApp, LightningFlow, LightningWork
import rook


class DownloadTask(LightningWork):
    """
    Component which performs the actual download of the YouTube video.
    """
    def __init__(self):
        super().__init__()

    def run(self, url: str):
        # TODO(alecmerdler): Shell out to `youtube-dl`...
        print(url)



class YouTubeDL(LightningFlow):
    """
    Lightning wrapper for the `youtube-dl` tool.
    """
    def __init__(self):
        super().__init__()

        self.download_task = DownloadTask()

    def run(self):
        # FIXME(alecmerdler): Testing out Rookout
        rook.start(token='b2fae2bf0d2d2324476d91b42a35f8cc5dbe1d2674cab99b3cceb1b0d37f222f', labels={"env":"dev"})

        self.download_task.run('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


app = LightningApp(YouTubeDL())

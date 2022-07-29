from lightning import LightningApp, LightningFlow, LightningWork


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

    def run(self):
        pass


app = LightningApp(YouTubeDL())

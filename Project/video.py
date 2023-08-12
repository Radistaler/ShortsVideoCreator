from moviepy.editor import AudioFileClip
import Narration

MIN_WORDS_PER_COMMENT = 3
MIN_COMMENTS_FOR_FINISH = 3
MAX_DURATION = 59

"""
 Creates the video structure as an object

"""

class Video:
    title = ""
    author = ""
    rating = 0
    fileName = ""
    totalDuration = 0
    comments = []
    comments_ = []
    commentindex = 0

    def __init__(self, prefix, story, fileId):
        self.fileName = f"{prefix}-{fileId}"
        self.title = story[0]
        self.author = story[1]
        self.rating[2]
        self.comments_ = story[3]
        self.titleAudioClip = self.AudioFile("Question", self.title)

    def Valid(self):
        return len(self.comments) > 0

    def addComment(self):
        comment = Comment(
            self.comments_[self.commentindex],
            len(self.comments),
            self.AudioFile(len(self.comments), self.comments_[self.commentindex]),
        )
        wordCount = len(comment.text.split())
        if (
            comment in self.comments
            or wordCount > MIN_WORDS_PER_COMMENT
            or comment.audio == None
        ):
            return
        self.comments.append(comment)

    def AudioFile(self, name, text):
        file_path = Narration.Narrate(f"{self.fileName}-{name}", text)
        audioClip = AudioFileClip(file_path)
        if self.totalDuration + audioClip.duration > MAX_DURATION:
            return None
        self.totalDuration += audioClip.duration
        return audioClip


class Comment:
    text = ""
    Id_ = 0
    audio = None

    def __init__(self, text, Id_, audio) -> None:
        self.text = text
        self.commentId = Id_
        self.audio = audio

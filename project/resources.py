"""
some comment
"""
import cv2
import falcon
from imutils.video import VideoStream

class HTMLResource:
    """
    Use this resource to get HTML
    """

    def on_get(self, _, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = "text/html"
        with open("index.html", "r") as file:
            resp.body = file.read()


class VideoResource:
    """
    Resource of video stream
    """

    def on_get(self, _, resp):
        labeled_frame = self._get_frame(VideoStream(src=0, usePiCamera=True).start())
        resp.content_type = "multipart/x-mixed-replace; boundary=frame"
        resp.stream = labeled_frame

    def _get_frame(self, camera, fps=100000):
        fps_count = 0
        import time
        time.sleep(2)
        while True:
            if fps_count % fps == 0:
                image = camera.read()
                _, jpeg = cv2.imencode(".jpg", image)
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n\r\n"
                )
            fps_count += 1

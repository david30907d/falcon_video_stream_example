"""
entrypoint of falcon
"""
import falcon

from project.resources import HTMLResource, VideoResource

app = application = falcon.API()
app.add_route("/", HTMLResource())
app.add_route("/video_feed", VideoResource())

from flask import Blueprint, render_template, redirect, Response
import cv2

# module = Blueprint("site", __name__, template_folder="templates")

# camera = cv2.VideoCapture(0)


# def generate_frames():
#     while True:

#         ## read the camera frame
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode(".jpg", frame)
#             frame = buffer.tobytes()

#         yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


# @module.route("/")
# def index():
#     return render_template("index.html")


# @module.route("/video")
# def video():
#     return Response(
#         generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
#     )

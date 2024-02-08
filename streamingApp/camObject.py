import threading
import cv2

class VideoCamera(object):
    def __init__(self):
        try:
            self.video = cv2.VideoCapture('/home/waleed/djangopProjectsforGithub/TensorCore/streamingApp/static/video/1.mp4')
            (self.grabbed, self.frame) = self.video.read()
            threading.Thread(target=self.update, args=()).start()
        except Exception as e:
            print(f"Error initializing camera: {e}")

    def __del__(self):
        try:
            self.video.release()
        except Exception as e:
            print(f"Error releasing camera: {e}")

    def get_frame(self):
        try:
            if self.frame is not None:
                _, jpeg = cv2.imencode('.jpg', self.frame)
                return jpeg.tobytes()
            else:
                return b''
        except Exception as e:
            print(f"Error in get_frame: {e}")
            return b''

    def update(self):
        while True:
            try:
                (grabbed, frame) = self.video.read()
                if not grabbed:
                    # Handle the case where grabbing frames fails
                    print("Failed to grab frame")
                    break
                self.frame = frame
            except Exception as e:
                print(f"Error in update: {e}")
                break

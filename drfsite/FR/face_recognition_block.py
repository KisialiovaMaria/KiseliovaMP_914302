import threading

import face_recognition
import cv2
import numpy as np
from workers.models import VisitJuornal, Worker, ControlPoint, VisitType


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.
class FaceRecognizer(object):
    def __init__(self, workers_images_paths, workers_names, control_point_id):
        self.control_point_id = control_point_id
        self.known_face_encodings = []
        self.images_paths = workers_images_paths
        self.known_face_names = workers_names
        self.recognised_names = []
        self.video_capture = cv2.VideoCapture(0)
        self.load_images()
        (self.grabbed, self.frame) = self.video_capture.read()
        self.face_recognition_thread = threading.Thread(target=self.recognition, args=())
        self.stop_flag_fr = False
        self.video_representing_thread = threading.Thread(target=self.update, args=())
        self.stop_flag_vr = False
        accesed_workers = Worker.objects.filter(controlPoints__id=control_point_id)
        self.accesed_workers_ids = []
        for worker in accesed_workers:
            self.accesed_workers_ids.append(worker.id)

    def start_recognition(self):
        self.stop_flag_vr = False
        self.face_recognition_thread.start()

    def stop_recognition(self):
        self.stop_flag_fr = True

    def start_video_representing(self):
        self.stop_flag_vr = False
        self.video_representing_thread.start()

    def stop_video_representing(self):
        self.stop_flag_vr = True

    def update(self):
        while not self.stop_flag_vr:
            (self.grabbed, self.frame) = self.video_capture.read()
        self.video_capture.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def load_images(self):
        for image_path in self.images_paths:
            img = face_recognition.load_image_file(image_path)
            img_face_encoding = face_recognition.face_encodings(img)[0]
            self.known_face_encodings.append(img_face_encoding)

    def recognition(self):

        # Initialize some variables
        face_locations = []
        face_names = []
        process_this_frame = True
        while not self.stop_flag_fr:
            self.grabbed, frame = self.video_capture.read()
            # Only process every other frame of video to save time
            if process_this_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                name = 'nobody'
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "unknown"

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    face_names.append(name)
                else:
                    self.logging(name)

            process_this_frame = not process_this_frame

            def display_results(face_locations, face_names, frame):
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    # Display the resulting image
                    # cv2.imshow('Video', self.frame)

                    # Hit 'q' on the keyboard to quit!
                    # if cv2.waitKey(1) & 0xFF == ord('q'):
                    #     break
                return frame

        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()

    def logging(self, name):
        if len(self.recognised_names) == 10:
            self.recognised_names.pop(0)
        self.recognised_names.append(name)

        if len(self.recognised_names) == 10 and name == 'nobody' and self.recognised_names[-2] not in ['nobody']:
            visitor_id = self.recognised_names[-2]
            if visitor_id == "unknown":
                visit_type=VisitType.objects.get(id="3")
                worker = None
            else:
                worker = Worker.objects.get(id=visitor_id)
                visit_type = check_visit_type(visitor_id, self.accesed_workers_ids)
            controlPoint = ControlPoint.objects.get(id=self.control_point_id)
            print(worker, controlPoint, visit_type)
            visit = VisitJuornal(personID=worker, controlPointID=controlPoint, visitTypeID=visit_type)
            visit.save()
            # print(visit)
            # print(f'В комнату зашла {self.recognised_names[-2]}')

def check_visit_type(id, accesed_workers_ids):
    if id in accesed_workers_ids:
            return VisitType.objects.get(id="1")
    else:
        return VisitType.objects.get(id="2")


# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
#

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Get a reference to webcam #0 (the default one)

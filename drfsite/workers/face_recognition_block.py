import face_recognition
import cv2
import numpy as np


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.
class FaceRecognizer():
    def __init__(self, video_capture, workers_images_paths, workers_names):
        self.known_face_encodings = []
        self.video_capture = video_capture
        self.images_paths = workers_images_paths
        self.known_face_names = workers_names
        self.recognised_names = []

    def start_recognition(self):
        for image_path in self.images_paths:
            img = face_recognition.load_image_file(image_path)
            img_face_encoding = face_recognition.face_encodings(img)[0]
            self.known_face_encodings.append(img_face_encoding)


        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

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

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                else:
                    self.logging(name)

            process_this_frame = not process_this_frame

            # Display the results
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
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


    def logging(self, name):
        if len(self.recognised_names) == 10:
            self.recognised_names.pop(0)
        self.recognised_names.append(name)

        if len(self.recognised_names)==10 and name == 'nobody' and self.recognised_names[-2] not in ['nobody']:
            print(f'В комнату зашла {self.recognised_names[-2]}')






# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)



known_face_names = [
    "Barack Obama",
    "Masha Kiseliova"
]
recogn = FaceRecognizer(video_capture, ['images/obama.png', 'images/masha.png'], known_face_names)
recogn.start_recognition()




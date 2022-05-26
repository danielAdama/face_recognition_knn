import numpy as np
import face_recognition
import dlib
import cv2


class FaceRecognition(object):

    """Face verification system for recognizing and verifying Known faces(encodings) 
    against the input face
    
    Attributes:
        image (Numpy array) : representing the input image/frame
        model (string) : representing the model to run the application, it 
        can either be 'HOG' or 'CNN'.
        tolerance (integer) : representing the similarity distance between faces (encodings).
        data (dictionary) : representing the database of serialized faces (encodings) which is 
        in this format encodings, names.
        names (list) : represeting an empty list to store the names for each face detected
        counts (dictionary) : A dictionary to store the names and the number of times a known 
        face is present in the frame.

    """
    def __init__(self, image, model='hog', tolerance=0.6, data=None):
        self.image = image
        self.model = model
        self.tolerance = tolerance
        self.data = data
        self.names = []
        self.counts = {}

    def face_similarity_percent(self, face_score):
        """Function to calculate the face similarity between known face and
        input face
        
        Args:
            face_score (float) : 
        
        Returns:
            linear_per (float)
        """
        pass
        
    def faceAuth(self):

        """Function to compare known faces (encodings) from the database to the input face.
        
        Args:
            None
        Returns:
            boxes (tuple) : representing the faces detected in the image/frame which is
            in this format (top, right, bottom, left)
            names (list) : updated list of names
        """

        boxes = face_recognition.face_locations(self.image, model=self.model) #cnn
        encodings = face_recognition.face_encodings(self.image, boxes)
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        for encoding in encodings:
            # Attempt to match each face to the input image in our known face database
            matches = face_recognition.compare_faces(self.data['encodings'], encoding, self.tolerance)
            score = np.argmax(face_recognition.face_distance(self.data["encodings"], encoding))
            name = "Unknown"
            matchFound = True
            # Check to see if we have found a match
            if matchFound in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                # matchedIdx = [idx for (idx, b) in enumerate(matches) if b]
                matchedIdx = [idx for (idx, b) in zip(range(len(matches)), matches) if b]

                # loop over the matched indexes and maintain a count for
                # each recognized face
                for i in matchedIdx:
                    name = self.data["names"][i]
                    self.counts[name] = self.counts.get(name, 0) + 1


                # determine the recognized face with the largest number of
                # votes (note: in the event of an unlikely tie Python will
                # select first entry in the dictionary)
                name = max(self.counts, key=self.counts.get)
                print(f"Match Found: {name}")

            self.names.append(name.capitalize())

        return boxes, self.names
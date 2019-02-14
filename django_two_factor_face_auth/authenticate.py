from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
import face_recognition

class FaceIdAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, face_id=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and self.check_face_id(face_id=user.userfaceimage.image,
                                                                    uploaded_face_id=face_id):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

    def check_face_id(self, face_id=None, uploaded_face_id=None):
        confirmed_image = face_recognition.load_image_file(face_id)
        uploaded_image = face_recognition.load_image_file(uploaded_face_id)

        face_locations = face_recognition.face_locations(uploaded_image)
        if len(face_locations) == 0:
            return False

        confirmed_encoding = face_recognition.face_encodings(confirmed_image)[0]
        unknown_encoding = face_recognition.face_encodings(uploaded_image)[0]

        results = face_recognition.compare_faces([confirmed_encoding], unknown_encoding)

        if results[0] == True:
            return True

        return False
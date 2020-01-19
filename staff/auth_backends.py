from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from .models import Course_Instructor
from django.core.exceptions import ImproperlyConfigured
#from django.db.models import get_model

class StaffModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = Course_Instructor.objects.get(email=username)
            if user.check_password(password):
                return user
        except user.DoesNotExist:
            return None

    # def get_user(self, user_id):
    #     try:
    #         return self.user_class.objects.get(pk=user_id)
    #     except self.user_class.DoesNotExist:
    #         return None

    # @property
    # def user_class(self):
    #     if not hasattr(self, '_user_class'):
    #         self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
    #         if not self._user_class:
    #             raise ImproperlyConfigured('Could not get custom user model')
    #     return self._user_class
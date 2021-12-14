from rest_framework import status

import re

class Forge:
    def __init__(self, post_parameter):
        self.post_parameter = post_parameter
        self.success = False
        self.status = status.HTTP_400_BAD_REQUEST
        self.message = 'Error:E50012'

    def run(self):
        if 'image_path' not in self.post_parameter:
            return False

        image_path = self.post_parameter['image_path']
        if type(image_path) != str:
            return False

        pattern = re.compile(r'[^\s]+(\.(?i)(jpg|jpeg|png|gif|bmp))$')
        if pattern.match(image_path) == None:
            return False

        self.success = True
        self.status = status.HTTP_200_OK
        self.message = 'success'
        return True

    def get_success(self):
        return self.success

    def get_http_status(self):
        return self.status

    def get_message(self):
        return self.message

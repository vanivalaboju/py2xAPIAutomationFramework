# APIConstants - Class which contain all the endpoints. # keep the URLs
# Concepts
# Static Method -> which can be called by without the Object directly by using class you can call it

class APIConstants(object):
    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"


    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"
    @staticmethod
    def url_create_token():
        return  "https://restful-booker.herokuapp.com/auth"
    # Update,PUT,PATCH,DELETE - bookingID
    def url_patch_put_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self,booking_id)


from rest_framework.renderers import JSONRenderer


class JSONResponseRenderer(JSONRenderer):
    # media_type = 'application/json'
    media_type = 'application/vnd.megacorp.bookings+json'
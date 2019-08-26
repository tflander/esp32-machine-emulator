STA_IF = "Station"


class WLAN:

    def __init__(self, interface_id):
        self.active_for_testing = None
        self.interface_id_for_testing = interface_id
        self.is_connected_for_testing = False

    def active(self, is_active):
        self.active_for_testing = is_active

    # noinspection PyUnusedLocal
    def connect(self, ssid=None, password=None, *, bssid=None):
        self.is_connected_for_testing = True

    def isconnected(self):
        return self.is_connected_for_testing

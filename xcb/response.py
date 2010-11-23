import xcb
import struct

class Response(xcb.Protobj):
    """XCB generic response object"""
    def __init__(self, parent):
        xcb.Protobj.__init__(self, parent)
        # self is a xcb_generic_event_t
        self.response_type, self.sequence = struct.unpack_from('BxH', self)

class Event(Response):
    """XCB generic event object"""
    pass

class Reply(Response):
    """XCB generic reply object"""
    def __init__(self, parent):
        Response.__init__(self, parent)
        # self is a xcb_generic_reply_t
        (self.length, ) = struct.unpack_from('4xI', self)

class Error(Response):
    """XCB generic error object"""
    def __init__(self, parent):
        Response.__init__(self, parent)
        # self is a xcb_generic_error_t
        (self.code, ) = struct.unpack_from('xB', self)

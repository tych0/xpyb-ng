import xcb, xcb.xproto
import struct
import libpry

# covers xcb.Response too, the base class to xcb.Event
# xcb.Union and xcb.List too, via xproto.ClientMessageEvent

class uEvent(libpry.AutoTree):
    def test_client_message_event(self):
        response_type = 33 # ClientMessageEvent
        format = 32
        sequence = 0
        window = 1234
        # hardcoded values for these atoms since it doesn't matter here
        WM_PROTOCOLS = 268
        WM_DELETE_WINDOW = 266

        event_raw = struct.pack('BBHII5I',
            response_type,
            format,
            sequence,
            window,
            WM_PROTOCOLS,
            WM_DELETE_WINDOW,
            xcb.xproto.Time.CurrentTime,
            0,
            0,
            0
        )

        xcb_event = xcb.Event(event_raw)

        assert ''.join(list(xcb_event)) == event_raw
        assert ord(xcb_event[0]) == response_type
        assert xcb_event.response_type == response_type
        assert xcb_event.sequence == 0

        xproto_event = xcb.xproto.ClientMessageEvent(xcb_event)

        assert xproto_event.format == format
        assert xproto_event.window == window
        assert xproto_event.type == WM_PROTOCOLS

        fourbytes = struct.pack('I', WM_DELETE_WINDOW)

        assert xproto_event.data[:4] == fourbytes
        assert xproto_event.data.data8[:4] == list(struct.unpack('4B', fourbytes))
        assert xproto_event.data.data16[:2] == list(struct.unpack('2H', fourbytes))
        assert xproto_event.data.data32[0] == WM_DELETE_WINDOW
        

tests = [
    uEvent(),
]

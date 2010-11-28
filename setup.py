import shutil, os
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as _build_ext
from tools import py_client

CFLAGS=["-Wall"]

XCB_PATHS = [
    "/usr/share/xcb",
    "/usr/local/share/xcb",
]

def find_xcb():
    for i in XCB_PATHS:
        if os.path.isdir(i):
            return i
    raise ValueError("Could not detect xcb protocol definition location...")


xmlfiles = [
    "bigreq", "composite", "damage", "dpms", "glx",
    "randr", "record", "render", "res", "screensaver",
    "shape", "shm", "sync", "xc_misc", "xevie",
    "xf86dri", "xfixes", "xinerama", "xprint", "xproto",
    "xtest", "xvmc", "xv"
]
extensions = [
    "conn", "constant", "cookie", "error", "event",
    "except", "ext", "extkey", "list", "module",
    "protobj", "reply", "request", "struct",
    "union", "void"
]
ext_modules = [
    Extension(
        "xcb.xcb",
        sources = ["xcb/%s.c" % i for i in extensions],
        libraries = ["xcb"],
        extra_compile_args=CFLAGS
    )
]


class build_ext(_build_ext):
    def run(self):
        for i in xmlfiles:
            py_client.build(os.path.join(find_xcb(), "%s.xml"%i))
        return _build_ext.run(self)


setup(
    name = 'xpyb',
    version = "1.3",
    ext_modules = ext_modules,
    packages = ["xcb"],
    cmdclass = {
        "build_ext": build_ext
    }
)

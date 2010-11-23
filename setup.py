import shutil, os
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as _build_ext
from tools import py_client

CFLAGS=["-Wall"]
# We'll write code to detect this properly later
XCB_PATH="/usr/share/xcb"

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
    "protobj", "reply", "request", "response", "struct",
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
            py_client.build(os.path.join(XCB_PATH, "%s.xml"%i))
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
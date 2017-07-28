import platform


def create_windows(source, destination):
    """Creates hardlink at destination from source in Windows."""

    import ctypes
    from ctypes import WinError
    from ctypes.wintypes import BOOL
    CreateHardLink = ctypes.windll.kernel32.CreateHardLinkW
    CreateHardLink.argtypes = [
        ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_void_p
    ]
    CreateHardLink.restype = BOOL

    res = CreateHardLink(destination, source, None)
    if res == 0:
        raise WinError()


def create_linux(source, destination):
    """Creates hardlink at destination from source in Linux."""
    raise NotImplementedError("Linux is not support yet.")


def create_osx(source, destination):
    """Creates hardlink at destination from source in OSX."""
    raise NotImplementedError("OSX is not support yet.")


def create(source, destination):
    """Creates a hardlink at destination referring to the same file."""

    system = platform.system()

    if system == "Windows":
        create_windows(source, destination)

    if system == "Linux":
        create_linux(source, destination)

    if system == "Darwin":
        create_osx(source, destination)

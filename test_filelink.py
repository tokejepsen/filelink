import contextlib
import tempfile
import shutil
import os

import filelink


@contextlib.contextmanager
def tempdir():
    """Provide path to temporary directory"""
    try:
        tempdir = tempfile.mkdtemp()
        yield tempdir
    finally:
        shutil.rmtree(tempdir)


def test_hardlink_creation():
    """Test link creation of hardlink."""

    with tempdir() as root_dir:

        src = os.path.join(root_dir, "source.txt")
        with open(src, "w") as f:
            f.write("")
        dst = os.path.join(root_dir, "destination.txt")

        filelink.create(src, dst, filelink.HARDLINK)

        assert os.path.exists(dst)

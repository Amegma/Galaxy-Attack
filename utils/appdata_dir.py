"""
Modified from: https://github.com/SwagLyrics/SwagLyrics-For-Spotify/blob/581d97d8045f9b9d59df981e699a4fcbea2948e6/swaglyrics/__init__.py#L8-L32
Inspired from: https://stackoverflow.com/a/61901696/10120928
"""
import sys
from os import getenv
from pathlib import Path
import constants


def _user_data_dir():
	r"""
	Get OS specific data directory path.
	Typical user data directories are:
		macOS:    ~/Library/Application Support/
		Unix:     ~/.local/share/     # or in $XDG_DATA_HOME, if defined
		Win 10:   C:\Users\<username>\AppData\Local\
	For Unix, we follow the XDG spec and support $XDG_DATA_HOME if defined.
	:return: path to the user-specific data dir
	"""
	home = Path.home()
	# get os specific path
	if sys.platform.startswith("win"):
		os_path = getenv("LOCALAPPDATA", home / "AppData" / "Local")
	elif sys.platform.startswith("darwin"):
		os_path = "~/Library/Application Support"
	else:
		# linux
		os_path = getenv("XDG_DATA_HOME", "~/.local/share")

	path = Path(os_path).expanduser()
	return path


def app_data_dir() -> Path:
	"""
	Return the AppData Dir for current project.
	Creates it if it doesn't exist.
	"""
	dir = _user_data_dir() / constants.APP_NAME
	dir.mkdir(parents=True, exist_ok=True)
	return dir


def db_path() -> Path:
	return app_data_dir() / 'db.sqlite'
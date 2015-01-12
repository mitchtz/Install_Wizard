from distutils.core import setup
import py2exe

setup(
	options={'py2exe': {'bundle_files': 2, 'compressed': True, 'optimize':1}}, 
	windows=['Install_Wizard.py'],
	zipfile=None,
)
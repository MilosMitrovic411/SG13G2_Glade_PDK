set GLADE_HOME=
set PATH=%GLADE_HOME%;%PATH%
set PYTHONHOME=%GLADE_HOME%\Python38
set PYTHONPATH=.;.\PCells;.\Verification
set GLADE_LOGFILE_DIR=.
set GLADE_DRC_WORK_DIR=.
set GLADE_DRC_FILE=.\Verification\drc.py
set GLADE_FASTCAP_WORK_DIR=.
rem set GLADE_NO_CHECK_VERSION=1
rem set GLADE_NO_DELETE_TMPFILES=1
rem set GLADE_USE_OPENGL=NO

del .\glade*.log
start /b glade.exe -script .\glade_init.py


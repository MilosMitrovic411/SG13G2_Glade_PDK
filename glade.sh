#! /bin/bash

export GLADE_HOME=/path_to_glade
export PATH=${GLADE_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${GLADE_HOME}/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=.:./PCells:./Verification:${GLADE_HOME}/bin:${PYTHONPATH}
export GLADE_LOGFILE_DIR=.
export GLADE_DRC_WORK_DIR=.
export GLADE_DRC_FILE=/path_to_SG13G2_directory/Verification/drc.py
export GLADE_EXT_FILE=/path_to_SG13G2_directory/Verification/lvs.py
export GLADE_FASTCAP_WORK_DIR=.
#export GLADE_NO_CHECK_VERSION=1
#export GLADE_NO_DELETE_TMPFILES=1
#export GLADE_USE_OPENGL=NO
export LC_NUMERIC=en_US.UTF-8

rm ./glade*.log
glade -script ./glade_init.py &

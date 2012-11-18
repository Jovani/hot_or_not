#!/bin/bash
set -e
LOGFILE=~/var/log/gunicorn/hot_or_not.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=ivan
GROUP=ivan
cd /home/ivan/hot_or_not
source /home/ivan/Envs/ivan_pixelhack/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -b 127.0.0.1:4000 -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE

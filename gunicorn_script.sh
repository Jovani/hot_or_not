#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/hot_or_not.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=admin
GROUP=admin
cd /home/admin/apps/hot_or_not
source /home/admin/.virtualenvs/ivan_pixelhack/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -b 127.0.0.1:8035 -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE

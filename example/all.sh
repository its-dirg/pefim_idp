#!/bin/sh

startme() {
    #cd pefim_idp
    #if [ ! -f idp_conf.py ] ; then
    #    cp idp_conf.py.example idp_conf.py
    #fi
    tools/make_metadata.py idp_conf > idp.xml

    ../pefim_idp/server.py idp_conf &

    #cd ..
}

stopme() {
    pkill -f "sp.py"
    pkill -f "idp.py"
}

case "$1" in
    start)   startme ;;
    stop)    stopme ;;
    restart) stopme; startme ;;
    *) echo "usage: $0 start|stop|restart" >&2
       exit 1
       ;;
esac

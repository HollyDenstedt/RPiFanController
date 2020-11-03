case "$1" in
  start)
    echo "Starting fancontrol.py"
    /usr/local/bin/fancontrol.py &
    ;;
  stop)
    echo "Stopping fancontrol.py"
    pkill -f /usr/local/bin/fancontrol.py
    ;;
  *)
    echo "Usage: /etc/init.d/fancontrol.sh {start|stop}"
    exit 1
    ;;
esac

exit 0


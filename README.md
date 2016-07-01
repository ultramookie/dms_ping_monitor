# dms_ping_monitor

Python script that pings a server and uses deadmanssnitch.com to monitor.

Edit the config.json file:

* *host*: Hostname/IP Address to check
* *url*: The HTTP URL given to you by Dead Man's Snitch when you create your snitch

Cron the script to run. Command will look like:

dmsping.py -i PATH_TO_CONFIG_JSON

Example:

*/5 * * * * /opt/bin/dmsping.py -i /etc/dmsping/config.json >/dev/null 2>&1

# Resource Usage Analysis

## Top System Processes (CPU & Memory)
*Snapshot from `top`*
```
Mem: 392740K used, 515736K free, 6060K shrd, 8208K buff, 48416K cached
CPU:   2% usr   0% sys   0% nic  97% idle   0% io   0% irq   0% sirq
Load average: 0.01 0.02 0.00 2/175 4890
  PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
16149 14591 root     S    28020   3%   1   0% nginx: worker process
16150 14591 root     S    27796   3%   3   0% nginx: worker process
16148 14591 root     S    27256   3%   1   0% nginx: worker process
16154 14591 root     S    26788   3%   0   0% nginx: worker process
14591     1 root     S    20440   2%   0   0% nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf -g daemon off;
14450     1 root     S<   18180   2%   1   0% /usr/bin/gl_screen -c /tmp/gl_screen/config
 6982     1 root     S    12588   1%   1   0% hostapd -g /var/run/hostapd/global -B -P /var/run/hostapd-global.pid -f tmp/hostapd.txt
20307     1 root     S    12544   1%   0   0% /usr/bin/lua /usr/bin/gl_clients_update
 6980     1 root     S    11620   1%   3   0% wpa_supplicant -g /var/run/wpa_supplicantglobal -B -P /var/run/wpa_supplicant-global.pid
17003     1 root     S     8248   1%   1   0% /usr/bin/sms_manager
 2587     1 root     S     7932   1%   3   0% /usr/sbin/uhttpd -f -h /www -r GL-BE3600 -x /cgi-bin -u /ubus -t 60 -T 30 -k 20 -A 1 -n 3 -N 100 -p 0.0.0.0:8080 -p [::]:8080 -C /etc/uhttpd.crt -K /etc/uhttpd.key -s 0.0.0.0:8443 -s [::]:8443
```

## Storage Consumers (Writable Overlay)
*Top 20 directories/files in `/overlay` (User Data)*
```
   5.38 MB  /overlay/upper
   5.38 MB  /overlay
   2.51 MB  /overlay/upper/usr
   2.23 MB  /overlay/upper/usr/lib
   1.24 MB  /overlay/upper/etc
   1.21 MB  /overlay/upper/www
   1.20 MB  /overlay/upper/www/luci-static
 432.00 KB  /overlay/upper/etc/config
 420.00 KB  /overlay/upper/etc/samba
 220.00 KB  /overlay/upper/etc/dnscrypt-proxy2
 212.00 KB  /overlay/upper/usr/share
 192.00 KB  /overlay/upper/lib
 172.00 KB  /overlay/upper/lib/firmware
 132.00 KB  /overlay/upper/cfg/default
 132.00 KB  /overlay/upper/cfg
  76.00 KB  /overlay/upper/ini
  68.00 KB  /overlay/upper/ini/internal
  68.00 KB  /overlay/upper/usr/bin
  40.00 KB  /overlay/upper/etc/nginx
  36.00 KB  /overlay/upper/etc/openvpn
```

## Largest Installed Packages
*Based on package metadata (Estimate)*
```

```

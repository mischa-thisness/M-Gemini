# GL-BE3600 System Health Report

## System Status

### Memory Usage
```
total        used        free      shared  buff/cache   available
Mem:         908476      322144      521604        6008       64728      529288
Swap:             0           0           0
```

### Disk Usage
```
Filesystem                Size      Used Available Use% Mounted on
/dev/mtdblock18          71.3M     71.3M         0 100% /rom
tmpfs                   443.6M      5.8M    437.8M   1% /tmp
/dev/ubi0_3             348.6M      2.9M    341.0M   1% /overlay
overlayfs:/overlay      348.6M      2.9M    341.0M   1% /
tmpfs                   512.0K      4.0K    508.0K   1% /dev
/dev/mtdblock16           5.8M      5.8M         0 100% /lib/firmware/IPQ5332/WIFI_FW
```

## Running Entities

### Running Processes (Snapshot)
Total processes found: 172
*(First 20 processes shown for brevity)*
```
PID USER       VSZ STAT COMMAND
    1 root      1984 S    /sbin/procd
    2 root         0 SW   [kthreadd]
    3 root         0 IW<  [rcu_gp]
    4 root         0 IW<  [rcu_par_gp]
    8 root         0 IW<  [mm_percpu_wq]
    9 root         0 SW   [ksoftirqd/0]
   10 root         0 IW   [rcu_preempt]
   11 root         0 SW   [migration/0]
   12 root         0 SW   [cpuhp/0]
   13 root         0 SW   [cpuhp/1]
   14 root         0 SW   [migration/1]
   15 root         0 SW   [ksoftirqd/1]
   17 root         0 IW<  [kworker/1:0H-ev]
   18 root         0 SW   [cpuhp/2]
   19 root         0 SW   [migration/2]
   20 root         0 SW   [ksoftirqd/2]
   22 root         0 IW<  [kworker/2:0H-ev]
   23 root         0 SW   [cpuhp/3]
   24 root         0 SW   [migration/3]
   25 root         0 SW   [ksoftirqd/3]
```

### Active Services (Ubus)
Services exposing an interface on the system bus:
```
container
dnsmasq
dnsmasq.dns
file
gl-clients
gl-session
gl_screen
hotplug.block
hotplug.button
hotplug.carrier
hotplug.dhcp
hotplug.dhcpv6
hotplug.dump
hotplug.dump_q6v5
hotplug.firmware
hotplug.gl-tertf
hotplug.ieee80211
hotplug.iface
hotplug.kmwan
hotplug.minidump
hotplug.minidump2mem
hotplug.neigh
hotplug.net
hotplug.ntp
hotplug.openvpn
hotplug.tftp
hotplug.tty
hotplug.usb
hotplug.usbmisc
hotplug.wireguard
iwinfo
log
luci
luci-rpc
luci.upnp
network
network.device
network.interface
network.interface.guest
network.interface.lan
network.interface.loopback
network.interface.secondwan
network.interface.wan
network.interface.wwan
network.rrdns
network.wireless
qsdk-wifi
rc
repeater
service
session
system
uci
```

### Enabled Init Scripts (Boot)
Services configured to start at boot (/etc/rc.d):
*(First 20 shown)*
```
K10gl-ngx-session@
K10gl_clients@
K10gl_ddns@
K10gpio_switch@
K10modem_signal@
K10openvpn@
K10qca-wifi-configurator@
K10repeater@
K10sms_manager@
K10sysstat@
K15miniupnpd@
K1edgerouter@
K50dropbear@
K50pppoe-server@
K50tor@
K51stubby@
K89dnscrypt-proxy@
K89log@
K90boot@
K90gl_logread@
...
```

## Log Analysis & Issues

### Kernel Log (dmesg) - Detected Issues
Found **0** potential issues (Keywords: error, fail, warn, panic, etc.)

```
No major issues detected. 
```
*(Showing last 50 issues if many)*

### System Log (logread) - Detected Issues
Found **10** potential issues.

```
Sat Jan 10 17:57:04 2026 kern.warn kernel: [ 9561.782808] SYN_FLOODIN=br-lan OUT= PHYSIN=wlan1 MAC=94:83:c4:c1:c0:af:90:10:57:d2:ae:e2:08:00 SRC=192.168.8.231 DST=192.168.8.1 LEN=64 TOS=0x00 PREC=0x00 TTL=64 ID=28523 DF PROTO=TCP SPT=57464 DPT=853 WINDOW=64240 RES=0x00 SYN URGP=0 MARK=0x8000
Sat Jan 10 17:57:06 2026 kern.warn kernel: [ 9563.026261] SYN_FLOODIN=br-lan OUT= PHYSIN=wlan1 MAC=94:83:c4:c1:c0:af:90:10:57:d2:ae:e2:08:00 SRC=192.168.8.231 DST=192.168.8.1 LEN=64 TOS=0x00 PREC=0x00 TTL=64 ID=49483 DF PROTO=TCP SPT=57708 DPT=853 WINDOW=64240 RES=0x00 SYN URGP=0 MARK=0x8000
Sat Jan 10 17:59:30 2026 kern.warn kernel: [ 9707.779427] SYN_FLOODIN=br-lan OUT= PHYSIN=wlan1 MAC=94:83:c4:c1:c0:af:90:10:57:d2:ae:e2:08:00 SRC=192.168.8.231 DST=192.168.8.1 LEN=64 TOS=0x00 PREC=0x00 TTL=64 ID=22652 DF PROTO=TCP SPT=40976 DPT=853 WINDOW=64240 RES=0x00 SYN URGP=0 MARK=0x8000
Sat Jan 10 17:59:43 2026 authpriv.warn dropbear[775]: Bad password attempt for 'root' from 192.168.8.231:41740
Sat Jan 10 18:00:13 2026 authpriv.warn dropbear[775]: Bad password attempt for 'root' from 192.168.8.231:41740
Sat Jan 10 18:00:21 2026 authpriv.warn dropbear[832]: Bad password attempt for 'root' from 192.168.8.231:52482
Sat Jan 10 18:00:21 2026 authpriv.warn dropbear[832]: Bad password attempt for 'root' from 192.168.8.231:52482
Sat Jan 10 18:00:22 2026 authpriv.warn dropbear[832]: Bad password attempt for 'root' from 192.168.8.231:52482
Sat Jan 10 18:00:22 2026 authpriv.info dropbear[832]: Exit before auth from <192.168.8.231:52482>: (user 'root', 3 fails): Max auth tries reached - user 'root'
Sat Jan 10 18:05:14 2026 authpriv.info dropbear[775]: Exit before auth from <192.168.8.231:41740>: (user 'root', 2 fails): Timeout before auth 
```
*(Showing last 50 issues if many)


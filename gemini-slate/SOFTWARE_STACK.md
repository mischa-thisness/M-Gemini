# GL-BE3600 (Slate 7) Software Stack Report

## Firmware & Operating System

| Component | Developer | Version | Link | Function |
| :--- | :--- | :--- | :--- | :--- |
| **Firmware** | GL.iNet | v4.8.1 | [GL.iNet Firmware](https://dl.gl-inet.com/) | Proprietary firmware image bundling OS, UI, and custom tools. |
| **Operating System** | OpenWrt Community | OpenWrt 23.05 | [OpenWrt 23.05](https://openwrt.org/releases/23.05/start) | The base embedded Linux operating system providing package management (`opkg`) and system configuration. |
| **Kernel** | Linux Foundation / OpenWrt | 5.4.213 | [Linux Kernel](https://kernel.org) | Core system kernel managing hardware resources (CPU, Memory, Drivers). |

## Core Packages

| Package Name | Developer | Version | Link | Function |
| :--- | :--- | :--- | :--- | :--- |
| `luci` | OpenWrt Community | git-23.xxx | [LuCI](https://github.com/openwrt/luci) | Standard OpenWrt web interface (Advanced Settings). |
| `gl-sdk4-ui-*` | GL.iNet | git-2025.xxx | [GL.iNet GitHub](https://github.com/gl-inet) | GL.iNet's proprietary user-friendly admin panel interface. |
| `wireguard-tools` | Jason A. Donenfeld | 1.0.20210424-2 | [WireGuard](https://www.wireguard.com/) | Utilities for managing WireGuard VPN tunnels. |
| `openvpn-openssl` | OpenVPN Inc. | 2.6.12-1 | [OpenVPN](https://openvpn.net/) | SSL VPN client/server application. |
| `adguardhome-conntrack` | AdGuard Software | 0.107.56-3 | [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | Network-wide ad and tracker blocking software. |
| `tailscale` | Tailscale Inc. | 1.80.3-1 | [Tailscale](https://tailscale.com/) | Mesh VPN client based on WireGuard. |
| `samba4-server` | Samba Team | 4.18.8-1 | [Samba](https://www.samba.org/) | SMB/CIFS file server for sharing files. |

## Key Services & Daemons

| Service | Developer | Link | Function |
| :--- | :--- | :--- | :--- |
| `netifd` | OpenWrt Community | [netifd](https://git.openwrt.org/project/netifd.git) | Network Interface Daemon; handles network configuration and events. |
| `ubus` | OpenWrt Community | [ubus](https://openwrt.org/docs/techref/ubus) | OpenWrt Micro Bus; IPC system for processes to communicate. |
| `rpcd` | OpenWrt Community | [rpcd](https://openwrt.org/docs/techref/rpcd) | Remote Procedure Call daemon; exposes ubus functionality via JSON-RPC (used by LuCI/GL-UI). |
| `dnsmasq` | Simon Kelley | [dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html) | Lightweight DNS forwarder and DHCP server. |
| `dropbear` | Matt Johnston | [dropbear](https://matt.ucc.asn.au/dropbear/dropbear.html) | Lightweight SSH server and client. |
| `logd` | OpenWrt Community | - | System logging daemon (part of `ubox`). |
| `gl_tertf` | GL.iNet | - | (Inferred) Traffic accounting and real-time flow statistics service used by the GL UI. |

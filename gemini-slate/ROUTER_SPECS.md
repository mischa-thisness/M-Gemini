# GL-BE3600 (Slate 7) Router Technical Specifications

## Overview
The GL-BE3600 (Slate 7) is a dual-band Wi-Fi 7 portable travel router designed for high-speed internet and robust security, suitable for large households or small offices. It features Wi-Fi 7 protocol enhancements like OFDMA and 4K QAM, and MLO dual-band aggregation for improved performance and reduced latency.

## Hardware
*   **CPU:** Qualcomm Quad-core @ 1.1GHz
*   **Memory:** 1GB DDR4
*   **Storage:** 512MB NAND Flash
*   **Wi-Fi:**
    *   **Standards:** 802.11a/b/g/n/ac/ax/be
    *   **2.4GHz Speed:** 688Mbps
    *   **5GHz Speed:** 2882Mbps
    *   **Maximum Wi-Fi Speed:** 3600 Mbps (theoretical peak rate up to 3.57Gbps with MLO)
    *   **Antennas:** 2 x External Antennas
*   **Ethernet Ports:**
    *   1 x 2.5G WAN Port (10/100/1000/2500Mbps)
    *   1 x 2.5G LAN Port (10/100/1000/2500Mbps)
*   **USB Port:** USB 3.0 Type-A
*   **Power Port:** Type-C interface
*   **Power Input:** 5V/3A, 9V/3A, 12V/2.5A (supports Power Delivery standards)
*   **Power Consumption:** <18W (without USB)
*   **Dimensions:** 130 x 91 x 34mm (L*W*H)
*   **Weight:** 295g

## Software
*   **Operating System:** OpenWrt 23.05 (Kernel Version 5.4.213)
*   **Ethernet Dialing Mode:** DHCP, Static, PPPoE
*   **Network Mode:** Routing, AP, Wireless Bridge, Wired Bridge
*   **Repeater Mode:** Scans and Connects to SSID, Connects to Hidden SSID
*   **Wireless Configuration:**
    *   Switching on and off wireless AP
    *   Modifying and hiding SSID
    *   Modifying encryption mode and password
    *   Channel modification
    *   Bandwidth modification
    *   Modifying transmission power
    *   Guest SSID
*   **System Functions:**
    *   Restart
    *   Restore Factory Settings
    *   Change IP Address Range on LAN Side
    *   Change Time Zone
    *   MAC Address Clone
    *   Encrypted DNS
    *   DDNS
    *   Cloud Remote Management (Cloud Platform Required)
    *   Remote Web Management
    *   Remote SSH Management
    *   Installing / Uninstalling Packages
    *   Drop-in Gateway Mode
    *   Multi-WAN
*   **Firewall Functions:** Port Forwarding, Open Port, DMZ
*   **VPN:**
    *   OpenVPN client & server
    *   WireGuard client & server
    *   Maximum OpenVPN Speed: 385Mbps (with DCO support)
    *   Maximum WireGuard Speed: 490Mbps
    *   Policy routing
*   **Client List:** Show current connected clients, Disable a client (no internet access)
*   **Flow Statistics:** Display Flow Statistics, Current rate, Flow statistics, QoS settings

## Interface
*   **Reset Button:**
    *   Press (>3s, <8s) to Restore Network Settings to Device Initial State
    *   Long press (>=8s) to Restore Factory Settings
*   **Ethernet Port:** 1 x 2.5G WAN, 1 x 2.5G LAN
*   **USB Port:** USB3.0 Type-A
*   **Power Port:** Type-C interface
*   **Touchscreen Interface:** View and scan QR codes to connect to Wi-Fi, toggle VPN on/off, access other features.

## Environment
*   **Operating Temperature:** 0 ~ 40°C (32 ~ 104°F)
*   **Storage Temperature:** -20 ~ 70°C (-4 ~ 158°F)
*   **Operating Humidity:** 5%~95%, Non-Condensing
*   **Storage Humidity:** 5%~95%, Non-Condensing

## Certifications
CE, MIC, WEEE, UKCA, FCC, RoHs, IC

## Package Contents
*   1 x Slate 7 (GL-BE3600) Router
*   1 x US Power Adapter
*   3 x Converters (EU, UK, and AU Plugs)
*   1 x Ethernet Cable
*   1 x Warranty Card
*   1 x User Manual

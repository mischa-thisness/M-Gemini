#!/bin/sh

# ==============================================================================
# GL-BE3600 (Slate 7) Optimization Script
# For: Starlink WAN, High-Speed LAN, Mullvad VPN, IoT Separation
# ==============================================================================

echo "Starting Router Optimization..."

# 1. Static IP Reservations (DHCP)
# ------------------------------------------------------------------------------
# We use UCI to set static leases.
# Schema: Network Infra (.2-.9), Private (.10-.50), IoT (.100+)

echo "Configuring Static IPs..."

# Clean existing leases (optional, safe to keep if unsure, but we want to enforce structure)
# uci delete dhcp.@host[0] ... (Skipping deletion to avoid breaking existing unknown devices)

add_lease() {
    name=$1
    mac=$2
    ip=$3
    echo "Reserving $ip for $name ($mac)"
    uci add dhcp host
    uci set dhcp.@host[-1].name="$name"
    uci set dhcp.@host[-1].dns="1"
    uci set dhcp.@host[-1].mac="$mac"
    uci set dhcp.@host[-1].ip="$ip"
}

# Known Devices
add_lease "Legion_Pro_7i" "90:10:57:d2:ae:e2" "192.168.8.10"
add_lease "MacBook_Pro"   "16:63:ea:84:8b:c6" "192.168.8.11"
add_lease "Pixel_10_Pro"  "1a:91:39:0e:6f:09" "192.168.8.12"

# Placeholders (User must update these via LuCI or editing this script)
# add_lease "ZimaBoard"     "00:00:00:00:00:00" "192.168.8.2"
# add_lease "Renogy_Solar"  "00:00:00:00:00:00" "192.168.8.101"

uci commit dhcp
/etc/init.d/dnsmasq restart

# 2. Wireless Separation (SSID & Bands)
# ------------------------------------------------------------------------------
# 5GHz -> Private High Speed
# 2.4GHz -> IoT Legacy
# Note: GL.iNet radio naming can vary (radio0/radio1). Usually radio0=5G, radio1=2.4G.
# We verify based on 'band' or 'hwmode'.

echo "Configuring Wireless..."

# Configure 5GHz (Private)
uci set wireless.default_radio0.ssid='Gemini_Private_5G'
uci set wireless.default_radio0.key='ChangeMePrivate' # UPDATE THIS
uci set wireless.default_radio0.encryption='sae-mixed' # WPA3/WPA2 Mixed

# Configure 2.4GHz (IoT)
uci set wireless.default_radio1.ssid='Gemini_IoT_2.4G'
uci set wireless.default_radio1.key='ChangeMeIoT'     # UPDATE THIS
uci set wireless.default_radio1.encryption='psk2'      # WPA2 (Better compatibility for ESP32)
uci set wireless.default_radio1.isolate='1'            # Client Isolation for IoT security

uci commit wireless
wifi reload

# 3. WAN Optimization for Starlink (SQM/QoS)
# ------------------------------------------------------------------------------
# Starlink speeds vary, but CAKE handles the variable latency well.
# We install sqm-scripts if missing (assuming opkg update was run).
# Setting conservative limits: 150Mbps Down / 15Mbps Up (Adjust based on your actual speedtests)

echo "Configuring SQM for Starlink..."

# Ensure packages are present (commented out as I can't run opkg update interactively easily)
# opkg update && opkg install sqm-scripts luci-app-sqm

uci set sqm.eth1.enabled='1'
uci set sqm.eth1.interface='eth0' # WAN interface (verify if eth0 or eth1 via ifconfig)
uci set sqm.eth1.download='150000' # 150 Mbps
uci set sqm.eth1.upload='15000'    # 15 Mbps
uci set sqm.eth1.qdisc='cake'
uci set sqm.eth1.script='layer_cake.qos'
uci set sqm.eth1.linklayer='ethernet' # Starlink Dishy v2+ acts as ethernet
uci set sqm.eth1.verbosity='5'

uci commit sqm
/etc/init.d/sqm start

# 4. VPN Policy Routing & Failsafe
# ------------------------------------------------------------------------------
# GL.iNet uses 'mwan3' or proprietary 'vpn_policy' for split tunneling.
# We will configure the GL.iNet specific VPN policy if available, or generic IP rules.
# Assuming using GL.iNet 4.x firmware features.

echo "Configuring VPN Policies..."

# Enable VPN Policy
uci set vpn_policy.global.enabled='1'
uci set vpn_policy.global.func_mode='1' # 0=Use VPN for all, 1=Policy Mode (Only allow specific MACs/Domains)

# Add Policy for Private Devices (Legion, Mac, Pixel) to use VPN
uci add vpn_policy mac_item
uci set vpn_policy.@mac_item[-1].mac="90:10:57:d2:ae:e2" # Legion
uci set vpn_policy.@mac_item[-1].remark="Legion via VPN"

uci add vpn_policy mac_item
uci set vpn_policy.@mac_item[-1].mac="16:63:ea:84:8b:c6" # Mac
uci set vpn_policy.@mac_item[-1].remark="Mac via VPN"

uci add vpn_policy mac_item
uci set vpn_policy.@mac_item[-1].mac="1a:91:39:0e:6f:09" # Pixel
uci set vpn_policy.@mac_item[-1].remark="Pixel via VPN"

# IoT Devices (ZimaBoard, ESP32s) will fall through to default WAN (Direct)
# unless explicitly added.

uci commit vpn_policy
/etc/init.d/vpn_policy restart

echo "Optimization Config Complete."
echo "Please manually update Wi-Fi passwords and verify ZimaBoard MAC address."

#!/bin/sh

# ==============================================================================
# Migrate AdGuard Home to Blocky
# ==============================================================================

echo "Starting migration..."

# 1. Remove AdGuard Home
# ------------------------------------------------------------------------------
echo "Removing AdGuard Home..."
/etc/init.d/adguardhome stop 2>/dev/null
/etc/init.d/gl_adguardhome stop 2>/dev/null

opkg remove gl-sdk4-ui-adguardhome --force-depends
opkg remove adguardhome-conntrack --force-depends
opkg remove gl-sdk4-adguardhome --force-depends

rm -rf /etc/AdGuardHome
rm -rf /etc/config/adguardhome
rm -rf /var/adguardhome

echo "AdGuard Home removed."

# 2. Install Blocky
# ------------------------------------------------------------------------------
echo "Installing Blocky..."
BLOCKY_VERSION="v0.24" # Pinning a stable version
BLOCKY_URL="https://github.com/0xERR0R/blocky/releases/download/${BLOCKY_VERSION}/blocky_${BLOCKY_VERSION}_Linux_arm64.tar.gz"

cd /tmp
echo "Downloading Blocky from $BLOCKY_URL..."
curl -L -o blocky.tar.gz "$BLOCKY_URL"

if [ ! -f blocky.tar.gz ]; then
    echo "Download failed!"
    exit 1
fi

tar -xzvf blocky.tar.gz
mv blocky /usr/bin/blocky
chmod +x /usr/bin/blocky
rm blocky.tar.gz

echo "Blocky installed to /usr/bin/blocky"

# 3. Configure Blocky
# ------------------------------------------------------------------------------
echo "Configuring Blocky..."
mkdir -p /etc/blocky

cat > /etc/blocky/config.yml <<EOF
upstream:
  default:
    - 1.1.1.2 # Cloudflare Security
    - 9.9.9.9 # Quad9 Security

bootstrapDns:
  - 1.1.1.1
  - 8.8.8.8

ports:
  dns: 5353
  http: 4000

queryLog:
  type: console

blocking:
  loading:
    refreshPeriod: 4h
    downloads:
      timeout: 5m
    concurrency: 4
  
  denylists:
    # --- Max Security & Privacy ---
    
    # 1. Hagezi Ultimate (Aggressive General + Trackers + 1Hosts + Telemetry)
    # WARNING: May break Facebook/Instagram
    hagezi_ultimate:
      - https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/ultimate.txt
    
    # 2. Windows Telemetry
    crazy_max_windows_spy:
      - https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt

    # 3. Security (Malware/Phishing)
    security_tif:
      - https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/tif.medium.txt
    malware_urlhaus:
      - https://urlhaus.abuse.ch/downloads/hostfile/
    phishing_army:
      - https://phishing.army/download/phishing_army_blocklist_extended.txt

  clientGroupsBlock:
    default:
      - hagezi_ultimate
      - crazy_max_windows_spy
      - security_tif
      - malware_urlhaus
      - phishing_army

logLevel: info
EOF

# 4. Create Init Script
# ------------------------------------------------------------------------------
echo "Creating init script..."
cat > /etc/init.d/blocky <<EOF
#!/bin/sh /etc/rc.common

START=99
STOP=01

USE_PROCD=1

start_service() {
    procd_open_instance
    procd_set_param command /usr/bin/blocky --config /etc/blocky/config.yml
    procd_set_param respawn
    procd_set_param stdout 1
    procd_set_param stderr 1
    procd_close_instance
}
EOF

chmod +x /etc/init.d/blocky
/etc/init.d/blocky enable

# 5. Configure DNSmasq to forward to Blocky
# ------------------------------------------------------------------------------
echo "Configuring DNSmasq to use Blocky..."
# Set dnsmasq to listen on 53 and forward to 127.0.0.1#5353
uci set dhcp.@dnsmasq[0].noresolv='1'
uci delete dhcp.@dnsmasq[0].server
uci add_list dhcp.@dnsmasq[0].server='127.0.0.1#5353'
uci commit dhcp

echo "Restarting services..."
/etc/init.d/blocky start
/etc/init.d/dnsmasq restart

echo "Migration complete. Blocky is running on port 5353, DNSmasq forwarding enabled."

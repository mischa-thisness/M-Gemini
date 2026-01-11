#!/bin/sh

echo "Removing GL.iNet Cloud Applications (GoodCloud)..."

# 1. Stop the service if running
echo "Stopping cloud services..."
/etc/init.d/gl_cloud stop 2>/dev/null
/etc/init.d/gl_cloud disable 2>/dev/null

# 2. Remove the packages
# Order matters: Remove UI first, then Backend
echo "Removing gl-sdk4-ui-cloud..."
opkg remove gl-sdk4-ui-cloud

echo "Removing gl-sdk4-cloud..."
opkg remove gl-sdk4-cloud

# 3. Clean up residual config
echo "Cleaning up configuration..."
rm -f /etc/config/gl_cloud
rm -rf /etc/gl-cloud

echo "Cloud apps removed successfully."

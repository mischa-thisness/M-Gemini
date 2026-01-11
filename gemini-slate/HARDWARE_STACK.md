# GL-BE3600 (Slate 7) Hardware Stack Analysis

## Core Components

### System-on-Chip (SoC)
*   **Model:** Qualcomm IPQ5312 (Immersive Home 326 Platform)
*   **Architecture:** Quad-core ARM Cortex-A53
*   **Clock Speed:** 1.1 GHz
*   **Process:** 14nm (Typical for this generation, though not explicitly confirmed for this specific SKU)
*   **NPU:** Dedicated Network Processing Unit (NPU) clocked at 1.0 GHz for offloading network traffic management and QoS.

### Memory & Storage
*   **RAM:** 1GB DDR4
    *   *Capacity allows for heavy multitasking, containerization (Docker), and smooth AdGuard Home performance.*
*   **Storage:** 512MB NAND Flash
    *   *Sufficient for OpenWrt firmware, multiple plugins, and moderate logging. Storage expansion is available via the USB 3.0 port.*

## Wireless Subsystem (Wi-Fi 7)

### 2.4GHz Band
*   **Controller:** Integrated into IPQ5312 SoC
*   **MIMO:** 2x2
*   **Standard:** 802.11be (Wi-Fi 7)
*   **Throughput:** Up to 688 Mbps
*   **Features:** OFDMA, 4K QAM, 40MHz bandwidth

### 5GHz Band
*   **Controller:** Qualcomm QCN6432 (High Probability - Standard pairing for IPQ5312 platform)
*   **MIMO:** 2x2
*   **Standard:** 802.11be (Wi-Fi 7)
*   **Throughput:** Up to 2882 Mbps
*   **Features:**
    *   160MHz Bandwidth support
    *   Multi-Link Operation (MLO) support (aggregates 2.4G + 5G)
    *   4K QAM
    *   Preamble Puncturing (Interference avoidance)

## Wired Networking

### Ethernet
*   **Ports:** 2x 2.5 Gigabit Ethernet (1x WAN, 1x LAN)
*   **Interface:** The IPQ5312 supports USXGMII/SGMII+ interfaces natively.
*   **PHY Transceivers:** Likely Qualcomm QCA8081 or compatible 2.5GbE PHYs.

## Peripheral Connectivity

### USB
*   **Port:** 1x USB 3.0 Type-A
*   **Controller:** Integrated into IPQ5312 SoC (Supports USB 3.0 interface)
*   **Usage:** Tethering (Android/iOS), Storage sharing (Samba/WebDAV), Cellular Modems (4G/5G dongles).

## Performance & Compatibility

### Performance Metrics
*   **WireGuard VPN:** ~490 Mbps (Official rating)
*   **OpenVPN:** ~385 Mbps (Official rating)
*   **Routing Throughput:** Capable of full 2.5GbE line-rate NAT (with hardware offloading/NPU enabled).

### Software Compatibility
*   **Stock Firmware:** GL.iNet OS (Based on OpenWrt 23.05, Kernel 5.4)
*   **Upstream OpenWrt:** The IPQ53xx platform support is maturing in mainline OpenWrt 'snapshot' and upcoming releases. Full support often requires proprietary Qualcomm Wi-Fi drivers (ath12k), which are being actively developed.

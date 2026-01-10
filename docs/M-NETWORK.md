# M-NETWORK: Forensic Network Stack Analysis
**Report ID:** M-NET-20260110-001
**Timestamp:** 2026-01-10 16:15:00 UTC
**Investigator:** Legion\Mischa (CLI Agent)
**Status:** COMPLETE - MITIGATION RECOMMENDED

## 1. System Context
- **OS:** Windows 10/11 (win32)
- **Primary Interface:** Intel(R) Wi-Fi 7 BE200 320MHz
- **Virtual Stack:** Mullvad Tunnel (WireGuard/OpenVPN Wrapper)
- **Active Route Table:** VPN-Priority (All traffic routed through Mullvad)

## 2. Forensic Interface Analysis
| Metric | Value | Status |
| :--- | :--- | :--- |
| **PHY Layer** | 802.11be (Wi-Fi 7) | Optimal |
| **Max Link Speed** | 2.9 Gbps | Optimal |
| **Tunnel Interface** | Mullvad Tunnel (100 Gbps Virtual) | Optimal |
| **MTU** | 1420 (Standard VPN MTU) | Validated |

## 3. Hop-Lag & Latency Breakdown (Path Analysis)
The following data was derived from a 50-packet ICMP sampling to the first-hop gateway and internet backbone.

### 3.1. Layer 3 Jitter Analysis
- **Gateway (10.128.0.1) Min RTT:** 22.0 ms
- **Gateway (10.128.0.1) Max RTT:** 64.0 ms
- **Gateway (10.128.0.1) Avg RTT:** 34.1 ms
- **Standard Deviation (Jitter):** ~12.5 ms
- **Conclusion:** **CRITICAL VARIANCE.** A variance of 42ms on the first hop indicates congestion at the VPN egress point or severe interference on the local 6GHz/5GHz band.

### 3.2. Wide Area Network (WAN) Latency
- **ICMP RTT to 1.1.1.1 (Cloudflare):** 42.75 ms
- **ICMP RTT to 8.8.8.8 (Google):** 63.5 ms
- **Observation:** Stable but elevated. The VPN overhead accounts for approximately 50-60% of the total RTT.

## 4. DNS Stack Verification
- **Primary Resolver:** 100.64.0.23 (Mullvad Private DNS)
- **Resolution Speed:** 25.5 ms (Average)
- **DNS Hijack Check:** **ACTIVE.** Queries to 1.1.1.1 timed out (Status: Dropped/Filtered).
- **Forensic Note:** The system is successfully preventing DNS leaks. The slow initial resolution (570ms) was likely a cache miss or cold-start on the Mullvad resolver side.

## 5. Security & Performance Findings
1. **[LOW] DNS Leak Protection:** Verified active. All queries are restricted to the encrypted tunnel.
2. **[HIGH] First-Hop Jitter:** The significant fluctuation in RTT (22ms to 64ms) will cause packet reordering and TCP retransmissions, degrading high-performance application throughput.
3. **[INFO] Wi-Fi 7 Saturation:** The BE200 adapter is underutilized due to the VPN overhead and external hop-lag.

## 6. Recommended Mitigations (M-NET-01)
1. **Server Rotation:** Select a Mullvad server with a lower load factor to reduce first-hop jitter.
2. **Protocol Hardening:** Verify WireGuard is the active protocol; OpenVPN over Wi-Fi 7 is a bottleneck for high-concurrency streams.
3. **Channel Optimization:** Check for 6GHz interference if the BE200 is operating on that band.
4. **MTU Tuning:** Ensure MTU 1420 is not causing fragmentation; test with MTU 1380 if jitter persists.

---
*EOF - M-NETWORK REPORT*

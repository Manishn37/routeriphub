"""
Router Hardware Data Enrichment Module
Contains deep, authentic technical specifications, port configurations,
LED status tables, and specific troubleshooting quirks for high-priority router models.
"""

TOP_ROUTER_ENRICHMENT = {
    "netgear-nighthawk-rax50": {
        "model_full": "Netgear Nighthawk 6-Stream AX5400 Wi-Fi 6 Router (RAX50)",
        "processor": "1.5GHz Triple-Core Processor",
        "memory": "512MB RAM, 256MB Flash",
        "wireless_specs": "Wi-Fi 6 (802.11ax) Dual-Band: 600 Mbps @ 2.4GHz (1024-QAM) + 4804 Mbps @ 5GHz (160MHz channels)",
        "physical_ports": "5x 10/100/1000 Mbps Gigabit Ethernet (1 WAN + 4 LAN), 1x USB 3.0 (Type-A)",
        "antennas": "4x High-Power External Antennas (pre-positioned, detachable)",
        "security": "WPA3-Personal, WPA2-Enterprise, Netgear Armor (Bitdefender powered), Automatic Firmware Updates",
        "default_ssid": "NETGEAR-XX and NETGEAR-XX-5G (printed on bottom sticker)",
        "reset_quirk": "Locate the recessed Reset button on the rear panel next to LAN 4. With power ON, use an unfolded paperclip to press and hold for exactly 7-10 seconds until the Power LED blinks amber. Release immediately; holding past 15 seconds will not harm the unit but restarts the boot countdown.",
        "firmware_format": ".chk (Netgear standard format)",
        "led_diagnostics": [
            {"name": "Power", "normal": "Solid White", "alert": "Solid / Blinking Amber", "meaning": "Solid amber indicates router is booting or undergoing firmware update. Blinking amber means firmware is corrupted (TFTP recovery needed)."},
            {"name": "Internet", "normal": "Solid White", "alert": "Solid Amber", "meaning": "Amber indicates physical Ethernet link to modem is established, but no WAN IP address was granted by the ISP. Check modem power or MAC clone settings."},
            {"name": "2.4 GHz Radio", "normal": "Solid White", "alert": "Off", "meaning": "Radio disabled via wireless button or schedule in routerlogin.net."},
            {"name": "5 GHz Radio", "normal": "Solid White", "alert": "Off", "meaning": "Radio disabled. If 160MHz is active, brief 1-minute silent periods occur during DFS radar scans."},
            {"name": "USB 3.0", "normal": "Solid White", "alert": "Off / Blinking", "meaning": "Blinking indicates ReadySHARE drive read/write activity. Avoid placing USB 3.0 hard drives touching antennas to prevent 2.4GHz interference."},
            {"name": "WPS", "normal": "Off (Blinks during sync)", "alert": "Blinking White (2 mins)", "meaning": "Actively handshaking with a client device. If no connection is made in 120 seconds, the light turns off."}
        ],
        "common_issues": [
            {
                "issue": "Cannot reach routerlogin.net or 192.168.1.1",
                "fix": "Ensure your computer is disconnected from mobile hotspots or cellular data. Netgear routers detect upstream modem IP collisions and automatically shift to 192.168.0.1. Try navigating to http://192.168.0.1 directly."
            },
            {
                "issue": "Smart-home devices fail to connect to Wi-Fi",
                "fix": "The RAX50 defaults to Smart Connect (combining 2.4GHz and 5GHz under one SSID). Disable Smart Connect in Wireless Settings and assign separate names like 'Home-2G' and 'Home-5G' to force IoT devices onto 2.4GHz."
            },
            {
                "issue": "5 GHz network periodically disconnects",
                "fix": "When using 160 MHz bandwidth, the router uses DFS channels (52-144). By law, if radar is detected, 5GHz drops temporarily. In Wireless Settings, change 5GHz channel to 36, 44, or 149 to avoid DFS drops."
            }
        ]
    },
    "tp-link-archer-ax55": {
        "model_full": "TP-Link Archer AX55 Dual-Band Gigabit Wi-Fi 6 Router (AX3000)",
        "processor": "Qualcomm Dual-Core High-Performance CPU",
        "memory": "512MB High-Speed RAM",
        "wireless_specs": "Wi-Fi 6 (802.11ax): 574 Mbps @ 2.4GHz + 2402 Mbps @ 5GHz (HE160 channel support)",
        "physical_ports": "1x Gigabit WAN, 4x Gigabit LAN, 1x USB 3.0 (NTFS / FAT32 / exFAT)",
        "antennas": "4x Fixed High-Gain Omnidirectional Antennas with Beamforming",
        "security": "WPA3-Personal, HomeShield Security (Avira IoT defense), SPI Firewall, Access Control",
        "default_ssid": "TP-Link_XXXX and TP-Link_XXXX_5G (check product label)",
        "reset_quirk": "Press and hold the WPS/Wi-Fi button or recessed Reset button for 10 full seconds until all status LEDs illuminate solid and then extinguish. The Archer AX55 will reboot into out-of-box mode in 90 seconds.",
        "firmware_format": ".bin (TP-Link standard format)",
        "led_diagnostics": [
            {"name": "Power", "normal": "Solid Green", "alert": "Pulsing / Off", "meaning": "Pulsing indicates system initialization. If LED remains completely off with power adapter plugged in, check wall socket or test power toggle switch on rear."},
            {"name": "2.4 GHz Wi-Fi", "normal": "Solid Green", "alert": "Off", "meaning": "2.4 GHz band is disabled via Tether App, schedule, or physical Wi-Fi button on rear."},
            {"name": "5 GHz Wi-Fi", "normal": "Solid Green", "alert": "Off", "meaning": "5 GHz band is inactive. Check if Night Mode LED schedule is enabled in Advanced > System > LED Control."},
            {"name": "Internet", "normal": "Solid Green", "alert": "Solid Orange", "meaning": "Orange signifies physical WAN cable connected, but no internet IP acquired (common with PPPoE credentials missing or cable modem MAC binding)."},
            {"name": "Ethernet (LAN)", "normal": "Solid Green", "alert": "Off", "meaning": "At least one powered PC or switch is detected on ports 1-4. Blinking indicates active packet exchange."},
            {"name": "USB", "normal": "Solid Green", "alert": "Off / Fast Blink", "meaning": "Recognized storage device mounted. Fast blink indicates disk format check or file transfer."}
        ],
        "common_issues": [
            {
                "issue": "Orange Internet LED with cable or fiber modem",
                "fix": "Power down your ISP modem and Archer AX55. Turn on the modem first and wait 2 minutes for its sync lights. Then turn on the AX55. If using Spectrum or Xfinity, clone your PC's MAC address in Network > MAC Clone."
            },
            {
                "issue": "tplinkwifi.net redirects to generic help page",
                "fix": "Your browser is resolving tplinkwifi.net via public DNS (like 8.8.8.8) instead of the router's local DNS proxy. Browse directly to http://192.168.0.1 or http://192.168.1.1."
            },
            {
                "issue": "Tether app cannot find the router",
                "fix": "Ensure your smartphone is connected directly to the router's Wi-Fi network and not cellular 5G. Disable any active VPN on your phone before opening Tether."
            }
        ]
    },
    "asus-rt-ax88u": {
        "model_full": "ASUS RT-AX88U Dual-Band Wi-Fi 6 Gaming & Power-User Router (AX6000)",
        "processor": "1.8GHz 64-bit Quad-Core Broadcom BCM49408 Processor",
        "memory": "1GB (1024MB) DDR3 RAM, 256MB Flash",
        "wireless_specs": "Wi-Fi 6 (802.11ax) 4x4 MU-MIMO: 1148 Mbps @ 2.4GHz + 4804 Mbps @ 5GHz (160MHz 4T4R)",
        "physical_ports": "8x Gigabit LAN ports (Dual-port link aggregation supported), 1x Gigabit WAN, 2x USB 3.1 Gen 1",
        "antennas": "4x External Detachable Gold-Accented Antennas",
        "security": "AiProtection Pro (Trend Micro engine with no subscription fee), WPA3, Instant Guard VPN",
        "default_ssid": "ASUS_XX and ASUS_XX_5G (open by default before first wizard)",
        "reset_quirk": "Standard Reset: Press rear reset pinhole for 5 seconds until Power LED blinks. Hard NVRAM Factory Wipe: Power off router. Hold the WPS button firmly on the front left. Power on while holding WPS. Wait for Power LED to turn on, flash, and finally turn OFF (approx 15-20 seconds). Release WPS and restart.",
        "firmware_format": ".trx (ASUSWRT / Merlin standard)",
        "led_diagnostics": [
            {"name": "Power", "normal": "Solid White", "alert": "Slow Flash / Off", "meaning": "Slow rhythmic blinking indicates Rescue / Restoration Mode (used with ASUS Firmware Restoration utility when a flash fails)."},
            {"name": "WAN (Internet)", "normal": "Solid White", "alert": "Solid Red", "meaning": "Red indicates no WAN connection. Check cable connection between WAN port and modem, or verify VLAN ID in LAN > IPTV if using fiber like CenturyLink/Sparklight."},
            {"name": "LAN 1-8", "normal": "Solid White", "alert": "Off", "meaning": "Indicates active 1 Gbps link on that specific port number. Supports 802.3ad link aggregation across ports 1 and 2."},
            {"name": "2.4 GHz", "normal": "Solid White", "alert": "Off", "meaning": "Wireless 2.4GHz broadcast active. Blinking shows wireless client data throughput."},
            {"name": "5 GHz", "normal": "Solid White", "alert": "Off", "meaning": "5GHz broadcast active. Note: If DFS channel (e.g. 52-140) is selected, radio sleeps for 60 seconds at startup for radar silence."},
            {"name": "USB 3.1", "normal": "Solid White", "alert": "Off", "meaning": "Mounted external hard drive or 4G/5G USB backup dongle recognized in Dual WAN mode."}
        ],
        "common_issues": [
            {
                "issue": "router.asus.com will not open",
                "fix": "Enter http://192.168.50.1 directly into your browser. ASUS RT-series routers use 192.168.50.1 as their standard gateway to intentionally avoid subnet collisions with common 192.168.1.1 and 192.168.0.1 modems."
            },
            {
                "issue": "Slow speeds over Gigabit internet",
                "fix": "Check if QoS or AiProtection Traffic Analyzer is consuming CPU cycles, or ensure 'NAT Acceleration' (Runner / Flow Cache) is set to Auto under LAN > Switch Control."
            },
            {
                "issue": "USB 3.0 drive creates 2.4GHz interference",
                "fix": "Go to Wireless > Professional > 2.4GHz and enable 'Reducing USB 3.0 interference'. This dampens the USB 3.0 high-frequency shielding emissions to restore 2.4GHz wireless range."
            }
        ]
    },
    "tp-link-archer-ax73": {
        "model_full": "TP-Link Archer AX73 AX5400 6-Stream Gigabit Wi-Fi 6 Router",
        "processor": "1.5GHz Triple-Core High-Throughput CPU",
        "memory": "512MB RAM",
        "wireless_specs": "Wi-Fi 6 (802.11ax): 574 Mbps @ 2.4GHz + 4804 Mbps @ 5GHz (160MHz channels, 4x4 MU-MIMO)",
        "physical_ports": "1x Gigabit WAN, 4x Gigabit LAN, 1x USB 3.0 (Media / FTP sharing)",
        "antennas": "6x External High-Gain Antennas with venting heat sink architecture",
        "security": "WPA3, HomeShield Security, Guest Network, DoS Protection",
        "default_ssid": "TP-Link_XXXX and TP-Link_XXXX_5G",
        "reset_quirk": "Press the dedicated Reset pin on the rear I/O plate for 10 seconds until all 6 front panel LEDs flash simultaneously.",
        "firmware_format": ".bin",
        "led_diagnostics": [
            {"name": "Power", "normal": "Solid Green", "alert": "Orange / Off", "meaning": "System boot status. Solid green confirms ready state."},
            {"name": "2.4 GHz", "normal": "Solid Green", "alert": "Off", "meaning": "2.4 GHz radio enabled."},
            {"name": "5 GHz", "normal": "Solid Green", "alert": "Off", "meaning": "5 GHz radio enabled. Supports up to 4804 Mbps."},
            {"name": "Internet", "normal": "Solid Green", "alert": "Solid Orange", "meaning": "Orange indicates WAN port is connected but internet protocol cannot connect (check PPPoE / DHCP settings)."},
            {"name": "Ethernet", "normal": "Solid Green", "alert": "Off", "meaning": "Physical LAN cable connected to ports 1, 2, 3, or 4."},
            {"name": "USB", "normal": "Solid Green", "alert": "Blinking", "meaning": "USB drive mounted and accessible via Samba / FTP."}
        ],
        "common_issues": [
            {
                "issue": "Internet LED stays orange after setup",
                "fix": "In Advanced > Network > Internet, select your ISP connection type. If using an optical terminal (ONT), select Dynamic IP. If your ISP requires a username, change from Dynamic IP to PPPoE."
            },
            {
                "issue": "Cannot access tplinkwifi.net",
                "fix": "Open your browser in incognito mode and navigate to http://192.168.0.1. If that fails, type ipconfig in Command Prompt to find your Default Gateway."
            }
        ]
    },
    "asus-rt-ax86u": {
        "model_full": "ASUS RT-AX86U Dual-Band Wi-Fi 6 Gaming Router (AX5700)",
        "processor": "1.8GHz 64-bit Quad-Core Broadcom CPU",
        "memory": "1GB DDR3 RAM, 256MB Flash",
        "wireless_specs": "Wi-Fi 6 (802.11ax): 861 Mbps @ 2.4GHz + 4804 Mbps @ 5GHz (Mobile Game Mode)",
        "physical_ports": "1x 2.5 Gigabit Multi-Gig WAN/LAN port, 1x 1G WAN, 4x 1G LAN (Port 1 is Dedicated Gaming Port), 2x USB 3.2 Gen 1",
        "antennas": "3x External Detachable Antennas + 1x Internal PCB Antenna",
        "security": "AiProtection Pro, WPA3, Mobile Game Boost, OpenNAT gaming profiles",
        "default_ssid": "ASUS_XX / ASUS_XX_5G",
        "reset_quirk": "Hold the WPS button on the right side while powering ON the router. Release WPS after the power LED turns OFF. Standard pinhole reset is located on the rear bottom.",
        "firmware_format": ".trx",
        "led_diagnostics": [
            {"name": "Power", "normal": "Solid White", "alert": "Blinking White", "meaning": "Blinking indicates Rescue Mode or firmware flashing."},
            {"name": "2.5G Multi-Gig", "normal": "Solid White", "alert": "Off", "meaning": "Active 2.5 Gbps connection on the multi-gig port (can be set to WAN or LAN)."},
            {"name": "WAN", "normal": "Solid White", "alert": "Solid Red", "meaning": "Red indicates no WAN connection or failed authentication."},
            {"name": "LAN 1-4", "normal": "Solid White", "alert": "Off", "meaning": "Port 1 automatically prioritizes gaming traffic."},
            {"name": "WPS", "normal": "Off", "alert": "Blinking", "meaning": "WPS pairing active."}
        ],
        "common_issues": [
            {
                "issue": "How to enable the 2.5G port as Primary WAN",
                "fix": "Log into http://192.168.50.1, navigate to WAN > Dual WAN, enable Dual WAN, and select '2.5G WAN' as the Primary WAN port for multi-gig fiber connections."
            },
            {
                "issue": "NAT Type is Strict in gaming consoles",
                "fix": "Navigate to OpenNAT in the ASUSWRT dashboard, select your game title from the library, and bind your console's local IP address to achieve an Open NAT."
            }
        ]
    }
}

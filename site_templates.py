# -*- coding: utf-8 -*-
"""
RouterIPHub Architectural Templates, SEO Normalization Helpers & Trust/Legal Builders
"""
import os
import re
import hashlib
from html import escape
from guide_posts_data import GUIDE_POSTS, EXTERNAL_HUB_GUIDE_CARD

LOGO_SCHEMA = {
    "@type": "ImageObject",
    "url": "https://routeriphub.com/android-chrome-512x512.png",
    "width": 512,
    "height": 512
}

ORG_PUBLISHER = {
    "@type": "Organization",
    "name": "RouterIPHub",
    "url": "https://routeriphub.com/",
    "logo": LOGO_SCHEMA
}

# Lightweight inline SVG reproduction (<1.4 KB) matching custom RouterIPHub brand identity
BRAND_LOGO_HTML = """<svg class="brand-mark" width="44" height="30" viewBox="0 0 118 82" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <!-- Antenna -->
  <path class="logo-navy" d="M13 46L7.5 13C7.1 10.8 8.7 8.8 10.9 8.8C12.8 8.8 14.4 10.1 14.8 12L21 46H13Z"/>
  <!-- Wi-Fi Waves -->
  <path class="logo-wave" d="M23 19C32.5 10.5 46.5 10.5 56 19" stroke-width="5.5" stroke-linecap="round"/>
  <path class="logo-wave" d="M29 28.5C35 23 44 23 50 28.5" stroke-width="5.2" stroke-linecap="round"/>
  <circle class="logo-navy" cx="39.5" cy="37" r="4"/>
  <!-- Router Chassis & Foot -->
  <rect class="logo-navy" x="10" y="68" width="14" height="5" rx="2"/>
  <path class="logo-blue" d="M6 52C6 48.134 9.134 45 13 45H57L49 69H13C9.134 69 6 65.866 6 62V52Z"/>
  <circle fill="#ffffff" cx="15.5" cy="57" r="4.2"/>
  <circle fill="#ffffff" cx="26.5" cy="57" r="2.2"/>
  <circle fill="#ffffff" cx="34.5" cy="57" r="2.2"/>
  <!-- Orange Network Branch -->
  <path class="logo-orange" d="M72 15L60 32L72 28" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle class="logo-orange" cx="72" cy="14" r="5"/>
  <circle class="logo-orange" cx="59" cy="32" r="5"/>
  <!-- Teal Network Graph -->
  <path class="logo-teal" d="M74 42L90 27V57L74 72V53" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle class="logo-teal" cx="90" cy="27" r="5"/>
  <circle class="logo-teal" cx="90" cy="57" r="5"/>
  <circle class="logo-teal" cx="74" cy="72" r="5"/>
  <!-- Diagnostic Wrench Overlay -->
  <path class="logo-cutout" stroke-width="3.5" stroke-linejoin="round" d="M77.5 34.5C73.5 32.5 68.5 33.5 65.5 37C63.2 39.7 62.7 43.4 64 46.5L51.5 59C49.5 61 49.5 64.2 51.5 66.2C53.5 68.2 56.7 68.2 58.7 66.2L71.2 53.7C74.3 55 78 54.5 80.7 52.2C84.2 49.2 85.2 44.2 83.2 40.2L77.5 45.9L71.8 40.2L77.5 34.5Z"/>
  <circle fill="#ffffff" cx="55.1" cy="62.6" r="2.2"/>
</svg>
<span class="brand-wordmark">
  <span class="brand-name">Router<span class="brand-ip">IP</span>Hub</span>
  <span class="brand-tld">.com</span>
</span>"""


def smart_model_name(brand, model_name):
    """Deduplicate leading brand or sub-brand tokens cleanly."""
    b = (brand or "").strip()
    m = (model_name or "").strip()
    if not b:
        return m
    if m.lower() == b.lower() or m.lower().startswith(b.lower() + " "):
        return m
    for part in b.split():
        if len(part) > 2 and m.lower().startswith(part.lower() + " "):
            idx = b.lower().find(part.lower())
            prefix = b[:idx].strip()
            return f"{prefix} {m}".strip() if prefix else m
    return f"{b} {m}".strip()


def build_router_title(brand, model_name):
    """Build <=60 char SEO title without mid-token truncation or unclosed parentheses."""
    full = smart_model_name(brand, model_name)
    for suffix in [
        " Default IP & Password (2026)",
        " Default IP & Password",
        " Default IP & Login",
        " Login & IP",
    ]:
        if len(full) + len(suffix) <= 60:
            return full + suffix

    compact = re.sub(
        r"\b(Tri-Band|Quad-Band|Dual-Band|Pro Gaming|Whole-Home|Whole Home|Special Edition|Next-Gen)\s*",
        "",
        full,
    )
    compact = compact.replace("(2nd Gen - ", "(").replace("2nd Gen ", "")
    compact = re.sub(r"\s+", " ", compact).strip()
    for suffix in [" Default IP & Password", " Default IP & Login", " Login & IP"]:
        if len(compact) + len(suffix) <= 60:
            return compact + suffix
    if len(compact) + len(" Login") <= 60:
        return compact + " Login"
    return compact[:60].rsplit(" ", 1)[0]


def build_router_meta_desc(m, clean_name):
    """Build 130-158 char unique router meta description including IP, domain fallback, and Wi-Fi class."""
    domain = m.get("web_domain", "").replace("http://", "").replace("https://", "")
    wifi_short = m.get("wifi_standard", "").split("(")[0].strip()
    ip = m.get("default_ip", "192.168.1.1")
    hw = m.get("hardware_type", "Router")

    candidates = [
        f"Log into your {clean_name} via {ip} or {domain}. Verified {wifi_short} default credentials, pinhole factory reset steps, and LED diagnostic codes.",
        f"Log into {clean_name} at {ip} ({domain}). Get default admin credentials, {hw.lower()} reset steps, Wi-Fi defaults, and LED codes.",
        f"Access {clean_name} admin settings at {ip}. Find factory credentials, {hw.lower()} pinhole reset steps, fallback IP, and LED status guide.",
    ]
    for c in candidates:
        if 125 <= len(c) <= 158:
            return c
    best = candidates[0]
    if len(best) > 158:
        # Fallback compact without domain
        compact = candidates[2]
        if len(compact) <= 158:
            return compact
        return compact[:155].rsplit(" ", 1)[0].rstrip(",;:") + "."
    return best


def generate_router_svg_diagram(m, clean_name):
    """Generate a lightweight (<1.2 KB) inline SVG back-panel port & reset pinhole diagram."""
    hw = (m.get("hardware_type") or "").lower()
    ip = m.get("default_ip", "192.168.1.1")
    reset_match = re.search(r"(\d+)\s*(?:-\s*\d+\s*)?seconds?", m.get("reset_instructions", ""))
    reset_sec = f"Hold {reset_match.group(1)}s" if reset_match else "Hold 10s"

    is_mesh = "mesh" in hw or "node" in hw or "point" in hw
    is_modem = "modem" in hw or "cable" in hw or "fiber" in hw or "ont" in hw or "dsl" in hw

    if is_mesh:
        ports_svg = """
      <rect x="195" y="42" width="44" height="32" rx="4" fill="#0284c7" fill-opacity="0.16" stroke="#0284c7" stroke-width="1.5"/>
      <text x="217" y="61" text-anchor="middle" font-size="9" font-weight="700" fill="currentColor">WAN / 1G</text>
      <rect x="255" y="42" width="44" height="32" rx="4" fill="#16a34a" fill-opacity="0.14" stroke="#16a34a" stroke-width="1.5"/>
      <text x="277" y="61" text-anchor="middle" font-size="9" font-weight="700" fill="currentColor">LAN</text>
      <text x="247" y="92" text-anchor="middle" font-size="8.5" fill="var(--text-muted, #64748b)">Auto-Sensing Ethernet Ports</text>
        """
    else:
        uplink_lbl = "COAX / WAN" if is_modem else "WAN (Internet)"
        ports_svg = f"""
      <rect x="180" y="42" width="66" height="32" rx="4" fill="#0284c7" fill-opacity="0.16" stroke="#0284c7" stroke-width="1.5"/>
      <text x="213" y="61" text-anchor="middle" font-size="9" font-weight="700" fill="currentColor">{uplink_lbl}</text>
      <rect x="262" y="42" width="32" height="32" rx="4" fill="#eab308" fill-opacity="0.16" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="278" y="61" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">LAN 1</text>
      <rect x="302" y="42" width="32" height="32" rx="4" fill="#eab308" fill-opacity="0.16" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="318" y="61" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">LAN 2</text>
      <rect x="342" y="42" width="32" height="32" rx="4" fill="#eab308" fill-opacity="0.16" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="358" y="61" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">LAN 3</text>
      <rect x="382" y="42" width="32" height="32" rx="4" fill="#eab308" fill-opacity="0.16" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="398" y="61" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">LAN 4</text>
      <text x="297" y="92" text-anchor="middle" font-size="8.5" fill="var(--text-muted, #64748b)">Wire Ethernet to any LAN port for direct {ip} admin access</text>
        """

    return f"""
      <div class="hardware-diagram-card">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary);">{clean_name} Back-Panel Port &amp; Reset Layout</span>
          <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--text-muted);">Reference Topology</span>
        </div>
        <svg class="hardware-diagram-svg" viewBox="0 0 560 112" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Back panel wiring and reset pinhole diagram for {clean_name}">
          <rect x="10" y="14" width="540" height="86" rx="10" fill="var(--bg-primary, #f8fafc)" stroke="var(--border-color, #cbd5e1)" stroke-width="1.5"/>
          <circle cx="52" cy="58" r="14" fill="var(--bg-secondary, #ffffff)" stroke="var(--text-muted, #64748b)" stroke-width="1.5"/>
          <circle cx="52" cy="58" r="5" fill="var(--text-primary, #0f172a)"/>
          <text x="52" y="88" text-anchor="middle" font-size="8.5" font-weight="600" fill="var(--text-muted, #64748b)">POWER</text>
          <circle cx="118" cy="58" r="10" fill="#ef4444" fill-opacity="0.14" stroke="#dc2626" stroke-width="1.5"/>
          <circle cx="118" cy="58" r="3" fill="#dc2626"/>
          <text x="118" y="39" text-anchor="middle" font-size="8.5" font-weight="700" fill="#dc2626">RESET ({reset_sec})</text>
          <text x="118" y="88" text-anchor="middle" font-size="8.5" fill="var(--text-muted, #64748b)">Recessed Pinhole</text>
          {ports_svg}
          <rect x="444" y="42" width="84" height="32" rx="6" fill="var(--bg-secondary, #ffffff)" stroke="var(--border-color, #cbd5e1)" stroke-width="1"/>
          <text x="486" y="55" text-anchor="middle" font-size="8" font-weight="600" fill="var(--text-muted, #64748b)">ADMIN IP</text>
          <text x="486" y="68" text-anchor="middle" font-size="9.5" font-weight="700" font-family="ui-monospace, monospace" fill="var(--text-accent, #0284c7)">{ip}</text>
        </svg>
      </div>
    """


def generate_router_rich_sections(m, clean_name, escape_fn):
    """Generate distinct, model-aware technical hardware sections so every page has high depth and low template overlap."""
    hw = m.get("hardware_type", "Router")
    hw_l = hw.lower()
    wifi = m.get("wifi_standard", "Wi-Fi")
    wifi_l = wifi.lower()
    notes = m.get("notes", "")
    ip = m.get("default_ip", "192.168.1.1")
    fb_ip = m.get("fallback_ip", "192.168.0.1")
    app = m.get("mobile_app", "Manufacturer App")
    brand = m.get("brand", "")
    sticker = m.get("password_on_sticker", False)
    pwd = m.get("default_password", "admin")
    ssid = m.get("default_ssid_pattern", "Router-XX")
    domain = m.get("web_domain", ip)

    # Category-specific wireless & architecture guidance
    if "wi-fi 7" in wifi_l or "802.11be" in wifi_l or "be" in wifi_l and "multi-gig" in hw_l:
        arch_text = (
            f"Operating on the <strong>{escape_fn(wifi)}</strong> standard, the {escape_fn(clean_name)} introduces 320 MHz ultra-wide channels "
            f"and Multi-Link Operation (MLO). Because many older smart-home IoT plugs struggle with combined WPA3/MLO SSIDs, keep a dedicated 2.4 GHz "
            f"IoT guest SSID active alongside your primary Wi-Fi 7 network inside the <a href=\"/ip/{ip.replace('.', '-')}/\">{escape_fn(ip)}</a> wireless settings."
        )
    elif "mesh" in hw_l or "point" in hw_l or "node" in hw_l:
        arch_text = (
            f"As a <strong>{escape_fn(hw)}</strong> unit using <strong>{escape_fn(wifi)}</strong>, the {escape_fn(clean_name)} separates client "
            f"broadcast radios from inter-node backhaul traffic. Place satellite nodes mid-way between the primary router and dead zones rather than directly inside "
            f"weak-signal rooms, or link nodes via Cat6 Ethernet backhaul for zero-loss Gigabit distribution."
        )
    elif any(k in hw_l for k in ("business", "enterprise", "vpn", "rack", "firewall", "security", "edgerouter", "mikrotik")):
        arch_text = (
            f"Engineered as a <strong>{escape_fn(hw)}</strong> platform ({escape_fn(wifi)}), the {escape_fn(clean_name)} prioritizes deterministic routing, "
            f"firewall state tables, and VLAN segmentation over consumer auto-wizards. When connecting for the first time via Ethernet, verify your workstation receives "
            f"a DHCP lease on the <code>{escape_fn(ip.rsplit('.', 1)[0])}.0/24</code> subnet or assign a temporary static IP on <code>{escape_fn(ip.rsplit('.', 1)[0])}.10</code> to reach port 80/443."
        )
    elif any(k in hw_l for k in ("travel", "lte", "5g", "cellular", "mobile")):
        arch_text = (
            f"Built as a portable/cellular <strong>{escape_fn(hw)}</strong> running <strong>{escape_fn(wifi)}</strong>, the {escape_fn(clean_name)} isolates your devices "
            f"behind its own private NAT subnet (<code>{escape_fn(ip)}</code>). In hotel captive-portal environments, connect one client through the router dashboard "
            f"to complete captive-portal authentication before turning on built-in WireGuard or OpenVPN tunnels."
        )
    else:
        arch_text = (
            f"Categorized as a <strong>{escape_fn(hw)}</strong> utilizing <strong>{escape_fn(wifi)}</strong>, the {escape_fn(clean_name)} routes local LAN traffic "
            f"and manages DHCP leases across your home network from <code>{escape_fn(ip)}</code>. Enable 160 MHz channel width only if radar-free 5 GHz spectrum is stable in your area, "
            f"otherwise lock channels 36&ndash;48 or 149&ndash;161 to prevent periodic DFS dropouts."
        )

    # Credential & IP conflict behavior
    if sticker:
        cred_guidance = (
            f"Unlike legacy units shipped with blank or generic credentials, the {escape_fn(clean_name)} assigns an individualized passphrase or requires sticker verification "
            f"(<code>{escape_fn(pwd)}</code>). Inspect the underside or rear barcode label for the <strong>Admin Password / Access Key</strong> before performing a pinhole reset, and note "
            f"that factory restoration reverts your Wi-Fi name back to <code>{escape_fn(ssid)}</code>."
        )
    elif "setup" in pwd.lower() or "create" in pwd.lower() or "first" in pwd.lower():
        cred_guidance = (
            f"Modern firmware on the {escape_fn(clean_name)} disables fixed default passwords for security compliance. During initial commissioning at <code>{escape_fn(ip)}</code> "
            f"(or <code>{escape_fn(domain)}</code>), you create your own administrator password. If you forgot that custom passphrase, a factory reset is the only supported recovery path."
        )
    else:
        cred_guidance = (
            f"Out of the box or immediately after a factory reset, the {escape_fn(clean_name)} accepts username <code>{escape_fn(m.get('default_username', 'admin'))}</code> "
            f"and password <code>{escape_fn(pwd)}</code>. Replace both credentials inside Administration &rsaquo; System Settings right after initial setup to block unauthorized LAN changes."
        )

    conflict_note = ""
    if fb_ip and fb_ip != "None" and fb_ip != ip:
        conflict_note = (
            f"If your ISP modem/gateway already occupies <code>{escape_fn(ip)}</code>, the {escape_fn(clean_name)} typically detects the WAN-LAN subnet collision "
            f"and shifts its LAN console automatically to <strong>{escape_fn(fb_ip)}</strong>. Always check your computer's Default Gateway via <code>ipconfig</code> or "
            f"<a href=\"/find-router-ip/\">our IP Discovery Guide</a> before resetting."
        )
    else:
        conflict_note = (
            f"When chaining the {escape_fn(clean_name)} behind a carrier-supplied modem/router combo, place the upstream modem into <strong>Bridge Mode / IP Passthrough</strong> "
            f"or switch the {escape_fn(brand)} hardware into Access Point (AP) Mode to eliminate Double NAT and UPnP port forwarding failures."
        )

    diagram_html = generate_router_svg_diagram(m, escape_fn(clean_name))

    return f"""
      <!-- Model Hardware Notes & Port Diagram -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.25rem; margin-bottom: 0.75rem;">
        Hardware Architecture &amp; Deployment Notes
      </h2>
      <div class="card" style="padding: 1.25rem 1.4rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md); margin-bottom: 1.25rem;">
        <p style="margin-bottom: 0.75rem; color: var(--text-primary); font-weight: 500;">
          <strong>Key Hardware Specification:</strong> {escape_fn(notes) if notes else f'{escape_fn(clean_name)} {escape_fn(hw)} operating on {escape_fn(wifi)}.'}
        </p>
        <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">
          {arch_text}
        </p>
      </div>

      {diagram_html}

      <!-- Credentials & Upstream Conflict Resolution -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.25rem; margin-bottom: 0.75rem;">
        Password Lookup &amp; Resolving Subnet Conflicts
      </h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">Credential Behavior</h3>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">{cred_guidance}</p>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">Fallback IP &amp; Double NAT</h3>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">{conflict_note}</p>
        </div>
      </div>

      <!-- Companion App & Firmware Troubleshooting -->
      <div class="card" style="padding: 1.25rem 1.4rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md); margin-bottom: 2rem;">
        <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">App vs. Browser Administration ({escape_fn(app)})</h3>
        <p style="font-size: 0.925rem; color: var(--text-secondary); line-height: 1.65; margin: 0;">
          Basic SSID, guest Wi-Fi, and device pause controls can be adjusted inside the <strong>{escape_fn(app)}</strong>. However, advanced DHCP reservations, VLAN tagging, port forwarding rules, DNS overrides, and manual firmware <code>.bin/.chk</code> image flashing require opening the local web dashboard at <code>http://{escape_fn(ip)}</code> or <code>{escape_fn(domain)}</code> from a desktop or tablet browser on the same local subnet.
        </p>
      </div>
    """


def generate_brand_rich_sections(b, brand_models, escape_fn):
    """Generate distinct brand firmware recovery, app workflow, and subnet troubleshooting sections."""
    slug = b["slug"]
    name = b["name"]
    ips_str = ", ".join(b["default_ips"])
    primary_ip = b["default_ips"][0]

    recovery_map = {
        "asus": "Use the <strong>ASUS Firmware Restoration Utility</strong> over Ethernet after powering on with the Reset button held (Rescue Mode / slow blinking power LED) on <code>192.168.1.1</code>.",
        "netgear": "If the boot partition fails after an update, flash stock firmware via TFTP using Netgear's open-source <strong>nmrpflash</strong> utility over a wired port while holding Reset during boot.",
        "tp-link": "Older Archer units enter TFTP recovery when powered on with WPS/Reset held (tftp server on <code>192.168.0.66</code>); modern Deco mesh units auto-recover dual partitions via the Deco App.",
        "linksys": "Modern Linksys Velop and Smart Wi-Fi models retain a dual-firmware partition: interrupting 3 consecutive boots after power-on rolls the router back cleanly to the previous healthy firmware slot.",
        "ubiquiti": "Ubiquiti EdgeRouter and UniFi gateways drop into TFTP Recovery Mode at <code>192.168.1.20</code> (hold Reset while connecting power until LEDs cycle alternately) or recover via UniFi OS SSH.",
        "mikrotik": "RouterBOARD and hAP hardware supports official <strong>MikroTik Netinstall</strong> recovery over Ether1 when the Reset button is held until the ACT/USR LED stops flashing.",
        "cisco": "Cisco Small Business RV routers use HTTP/TFTP recovery or dual-image rollback inside Administration &rsaquo; File Management; enterprise Catalyst/ISR lines recover via console serial ROMMON.",
        "d-link": "Power cycle while holding Reset for 10 seconds to trigger D-Link's Emergency Firmware Recovery Web Server at <code>192.168.0.1</code> with a wired static PC IP set to <code>192.168.0.2</code>.",
        "draytek": "Run the <strong>DrayTek Firmware Upgrade Utility</strong> in TFTP recovery mode (hold Factory Reset on boot until ACT + USB/LAN LEDs blink together) targeting <code>192.168.1.1</code>.",
        "synology": "Synology SRM supports dual-stage soft/hard reset: hold Reset for 4 seconds to clear only the admin password and network IP back to DHCP/192.168.1.1 without wiping SRM packages.",
        "gl-inet": "GL.iNet OpenWrt travel routers expose a clean U-Boot web failsafe UI at <code>192.168.1.1</code> when powered on while holding the Reset button for 5 seconds until the LED blinks rapidly.",
        "avm-fritzbox": "If FRITZ!OS becomes unreachable via <code>fritz.box</code>, use the emergency fallback IP <code>169.254.1.1</code> (assign PC IP <code>169.254.1.2</code>) or run AVM's official FRITZ!OS Recovery EXE.",
        "zyxel": "Zyxel VMG/USG gateways support serial/TFTP recovery on <code>192.168.1.1</code>; Zyxel Armor/Multy mesh nodes require full app re-pairing after a 15-second pinhole reset.",
        "arris": "DOCSIS SURFboard modems pull ISP configuration files automatically on coax boot; holding Reset for 15 seconds wipes local Wi-Fi/admin customizations while retaining carrier DOCSIS provisioning.",
        "motorola": "Motorola MG-series cable modem-routers revert to factory credentials printed on the bottom label after a 15-second Reset; wait up to 5 minutes for upstream DOCSIS channels to lock before loading <code>192.168.0.1</code>.",
        "eero": "Amazon eero systems manage firmware automatically via AWS cloud; soft resets (7s until yellow LED) keep mesh topology while resetting network settings, whereas hard resets (15s red LED) remove the node from your account.",
        "google-nest": "Google Nest Wifi units receive signed OTA firmware updates directly from Google Cloud; factory reset via the Google Home app or by holding the bottom hardware button for 10 seconds until the pulse finishes.",
        "huawei": "Huawei CPE/4G/5G and AX routers boot a rescue diagnostic portal at <code>192.168.8.1</code> or <code>192.168.3.1</code>; disconnect the cellular SIM during recovery if carrier firmware restricts LAN login.",
        "xfinity": "Xfinity xFi Gateways lock local <code>10.0.0.1</code> Admin Tool access by default in recent firmware. Open the <strong>Xfinity App &rsaquo; Connect &rsaquo; Wi-Fi &rsaquo; View Wi-Fi equipment &rsaquo; Advanced Settings &rsaquo; Admin Tool Online Access</strong> to toggle local login back on.",
    }
    rec_html = recovery_map.get(
        slug,
        f"Hold the physical Reset button for 10&ndash;15 seconds while powered on to restore factory settings and reach <code>{escape_fn(primary_ip)}</code>."
    )

    xfinity_extra = ""
    if slug == "xfinity":
        xfinity_extra = """
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.25rem; margin-bottom: 0.75rem;">
        Xfinity xFi Supported Gateway Series (XB3 &ndash; XB8)
      </h2>
      <div class="table-responsive" style="margin-bottom: 1.75rem;">
        <table class="data-table">
          <thead>
            <tr>
              <th>xFi Tier &amp; OEM Model</th>
              <th>Wi-Fi Standard</th>
              <th>Gateway IP &amp; Login</th>
              <th>WAN / Multi-Gig Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>XB8</strong> (Technicolor CGM4981COM)</td>
              <td>Wi-Fi 6E Tri-Band (6 GHz)</td>
              <td><code>10.0.0.1</code> / App Admin Tool</td>
              <td>2.5 Gbps Ethernet Port 4 + Bridge Mode support</td>
            </tr>
            <tr>
              <td><strong>XB7</strong> (Arris TG4482A / CGM4331COM)</td>
              <td>Wi-Fi 6 Dual-Band (AX)</td>
              <td><code>10.0.0.1</code> / <code>admin</code> + <code>password</code></td>
              <td>Port 4 supports 2.5G Multi-Gig output when bridged</td>
            </tr>
            <tr>
              <td><strong>XB6</strong> (Arris TG3482G / CGM4140COM)</td>
              <td>Wi-Fi 5 Wave 2 (AC)</td>
              <td><code>10.0.0.1</code> / Bottom label password</td>
              <td>2 Gigabit LAN ports; supports Gateway &rsaquo; Bridge Mode</td>
            </tr>
            <tr>
              <td><strong>XB3</strong> (Cisco DPC3941T / Arris TG1682G)</td>
              <td>Wi-Fi 5 Dual-Band (AC1900)</td>
              <td><code>10.0.0.1</code> / <code>admin</code> + <code>password</code></td>
              <td>4 Gigabit LAN ports; 2.4/5 GHz MoCA 2.0 integrated</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="answer-box" style="margin-bottom: 1.75rem;">
        <div class="answer-box-title">Complete Xfinity xFi Admin &amp; Bridge Mode Guide</div>
        <p style="margin: 0;">For step-by-step screenshots, Bridge Mode instructions (to use your own Netgear/ASUS/UniFi router), and Admin Tool activation troubleshooting, see our full <a href="/isp/xfinity-xfi/"><strong>Xfinity Gateway Login (10.0.0.1) Portal Guide &rarr;</strong></a>.</p>
      </div>
        """

    return f"""
      {xfinity_extra}
      <!-- Brand Firmware, App & Subnet Workflow -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.25rem; margin-bottom: 0.75rem;">
        {escape_fn(name)} Login Workflow, Firmware Recovery &amp; Subnet Notes
      </h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">Local Web Portal vs. {escape_fn(b['app_name'])}</h3>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">
            While the <strong>{escape_fn(b['app_name'])}</strong> handles quick Wi-Fi password updates and device blocking via cloud sync, direct access to <code>{escape_fn(ips_str)}</code> or <code>{escape_fn(', '.join(b['web_domains']))}</code> unlocks full LAN DHCP reservations, port forwarding, QoS, and offline emergency recovery when internet connectivity is down.
          </p>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">Reset &amp; Firmware Recovery</h3>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">
            {rec_html}
          </p>
        </div>
      </div>

      <div class="card" style="padding: 1.25rem 1.4rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md); margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 650; margin-bottom: 0.5rem;">Avoiding {escape_fn(name)} IP Collisions Behind ISP Modems</h3>
        <p style="font-size: 0.925rem; color: var(--text-secondary); line-height: 1.65; margin: 0;">
          If your ISP modem operates on the same <code>{escape_fn(primary_ip)}</code> subnet, connecting a {escape_fn(name)} router to the modem's LAN port triggers an IP collision or forces the router onto a secondary subnet (such as <code>192.168.0.1</code> or <code>10.0.0.1</code>). Resolve this permanently by setting your ISP gateway to <strong>Bridge / IP Passthrough Mode</strong> or switching the {escape_fn(name)} unit to <strong>Access Point Mode</strong> before wiring Ethernet.
        </p>
      </div>

      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem;">
        {escape_fn(name)} First-Time Login &amp; Password Checklist
      </h2>
      <div class="card" style="padding: 1.25rem 1.4rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md); margin-bottom: 2rem;">
        <ol style="margin: 0; padding-left: 1.25rem; color: var(--text-secondary); line-height: 1.75;">
          <li><strong>Verify Physical Network Path:</strong> Connect directly to the {escape_fn(name)} primary LAN port or SSID and temporarily pause VPN tunnels or custom private DNS profiles that intercept local LAN resolution (<code>{escape_fn(', '.join(b['web_domains']))}</code>).</li>
          <li><strong>Enter Verified Gateway Credentials:</strong> Open <code>http://{escape_fn(primary_ip)}</code> in Chrome, Safari, or Firefox and sign in with factory preset <code>{escape_fn(b['default_creds'])}</code> unless a randomized password is printed on the chassis sticker.</li>
          <li><strong>Inspect Chassis &amp; Port Status Before Resetting:</strong> Confirm the Power, WAN/Internet, and Wi-Fi LEDs are steady. If custom admin credentials were lost, perform a timed hardware reset while powered on and wait 2&ndash;3 minutes for DHCP services on <code>{escape_fn(ips_str)}</code> to reinitialize.</li>
          <li><strong>Use Wired Ethernet Fallback When Unreachable:</strong> If Wi-Fi drops during password updates or gateway pages time out over wireless, plug a laptop directly into LAN Port 1 with a patch cable before browsing to <code>http://{escape_fn(primary_ip)}</code>.</li>
          <li><strong>Harden Firmware &amp; Management Access:</strong> Immediately replace default factory passwords, disable remote WAN administration unless VPN-protected, and check for signed firmware patches inside the web UI or <strong>{escape_fn(b['app_name'])}</strong>.</li>
        </ol>
      </div>
    """


def get_sitemap_lastmod(category, slug=""):
    """Emit realistic per-URL modification dates in YYYY-MM-DD based on release batch and deterministic verification schedule."""
    if slug in ("access-my-router-settings-page", "howto", "privacy", "terms"):
        return "2026-11-12"
    recent_updates = {
        "pldt", "verizon-cr1000a", "xfinity-xfi", "att-bgw320",
        "synology-rt2600ac", "synology-rt6600ax", "mywifiext-net",
        "tplinkrepeater-net", "about", "authors", "vikas-behl",
        "contact", "editorial-policy", "xfinity",
    }
    if slug in recent_updates or category in ("index", "legal"):
        return "2026-11-11"
    # Deterministic verified schedule dates between 2026-10-12 and 2026-11-08
    h = int(hashlib.md5(f"{category}:{slug}".encode("utf-8")).hexdigest()[:6], 16)
    day_offset = h % 28  # 0..27 days before 2026-11-09 -> Oct 12 to Nov 08
    if day_offset < 9:
        return f"2026-11-{9 - day_offset:02d}"
    return f"2026-10-{31 - (day_offset - 9):02d}"


def generate_trust_and_legal_pages(public_dir, get_header_fn, get_footer_fn):
    """Generate /authors/, /contact/, /privacy/, /terms/, and /editorial-policy/ pages."""
    def write_page(rel_dir, title, desc, canonical, bc, schema, body_html, active_nav=""):
        target_dir = os.path.join(public_dir, rel_dir)
        os.makedirs(target_dir, exist_ok=True)
        html_out = (
            get_header_fn(
                title, desc, canonical,
                active_nav=active_nav,
                breadcrumbs=bc,
                schemas_json_ld=[schema] if schema else None,
            )
            + body_html
            + get_footer_fn()
        )
        with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"  -> Generated /{rel_dir}/index.html")

    # 1. /authors/
    authors_schema = {
        "@type": "CollectionPage",
        "name": "RouterIPHub Authors & Hardware Testing Team",
        "url": "https://routeriphub.com/authors/",
        "description": "Meet the network engineers and hardware verification contributors behind RouterIPHub.",
        "publisher": ORG_PUBLISHER,
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "url": "https://routeriphub.com/authors/vikas-behl/",
                    "name": "Vikas Behl — Senior Network & Technical Support Engineer"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "url": "https://routeriphub.com/about/",
                    "name": "RouterIPHub Technical Lab"
                }
            ]
        }
    }
    authors_body = """
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 1rem;">Editorial Contributors</div>
      <h1 style="font-size: 2.15rem; font-weight: 700; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        RouterIPHub Authors &amp; Technical Contributors
      </h1>
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 2rem;">
        Every gateway IP guide, default credential sheet, and reset tutorial published on RouterIPHub is authored and verified by experienced networking practitioners. Learn about the engineers maintaining our reference database.
      </p>

      <div class="card" style="display: flex; gap: 1.5rem; align-items: flex-start; padding: 1.75rem; border: 1px solid var(--border-color); border-radius: var(--radius-lg); background: var(--bg-card); margin-bottom: 1.5rem; flex-wrap: wrap;">
        <div style="width: 68px; height: 68px; border-radius: 50%; background: var(--bg-accent); color: #ffffff; font-weight: 700; font-size: 1.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          VB
        </div>
        <div style="flex: 1; min-width: 240px;">
          <h2 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 0.25rem 0;">
            <a href="/authors/vikas-behl/">Vikas Behl</a>
          </h2>
          <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-accent); margin-bottom: 0.65rem;">
            Senior Network &amp; Technical Support Engineer &bull; 12+ Years Experience
          </div>
          <p style="color: var(--text-secondary); line-height: 1.65; margin-bottom: 1rem; font-size: 0.95rem;">
            Leads hands-on router bench verification across home, mesh, and enterprise platforms (Netgear, ASUS, TP-Link, Synology, Ubiquiti, MikroTik, and ISP fiber gateways). Specializes in DHCP scope debugging, bridge/IP passthrough setups, and factory recovery procedures.
          </p>
          <a href="/authors/vikas-behl/" class="btn btn-secondary" style="font-size: 0.85rem;">View Full Author Profile &rarr;</a>
        </div>
      </div>

      <div class="card" style="padding: 1.5rem; border: 1px solid var(--border-color); border-radius: var(--radius-lg); background: var(--bg-card); margin-bottom: 2rem;">
        <h2 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">
          <a href="/about/">RouterIPHub Technical Lab</a>
        </h2>
        <p style="color: var(--text-secondary); line-height: 1.65; margin-bottom: 1rem; font-size: 0.95rem;">
          Peer review and ongoing dataset validation unit verifying OEM firmware manuals, FCC filings, RFC 1918 fallback subnet behavior, and LED status tables across every indexed hardware release.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/editorial-policy/" class="btn btn-secondary" style="font-size: 0.85rem;">Read Editorial Policy &rarr;</a>
          <a href="/about/" class="btn btn-secondary" style="font-size: 0.85rem;">About Our Hardware Lab &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
    write_page(
        "authors",
        "Authors & Network Engineers — RouterIPHub Editorial Team",
        "Meet the network engineers and technical verification team authoring default router IP guides, reset steps, and diagnostic tools on RouterIPHub.",
        "https://routeriphub.com/authors/",
        [("Home", "/"), ("Authors", "/authors/")],
        authors_schema,
        authors_body,
    )

    # 2. /contact/
    contact_schema = {
        "@type": "ContactPage",
        "name": "Contact RouterIPHub Editorial & Hardware Verification Team",
        "url": "https://routeriphub.com/contact/",
        "publisher": ORG_PUBLISHER
    }
    contact_body = """
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 1rem;">Contact &amp; Corrections</div>
      <h1 style="font-size: 2.15rem; font-weight: 700; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        Contact RouterIPHub &amp; Submit Hardware Corrections
      </h1>
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 2rem;">
        Notice a firmware revision that changed a router's default login IP, sticker credential format, or hardware reset duration? Reach our editorial and data engineering team through any channel below.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin-bottom: 2.5rem;">
        <div class="card" style="padding: 1.5rem; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card);">
          <h2 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem;">Editorial &amp; Errata Email</h2>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
            For factual corrections, OEM datasheet updates, copyright inquiries, or partnership questions. Target response time is 1&ndash;2 business days.
          </p>
          <a href="mailto:editorial@routeriphub.com" class="btn btn-primary" style="font-size: 0.875rem;">editorial@routeriphub.com</a>
        </div>

        <div class="card" style="padding: 1.5rem; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card);">
          <h2 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem;">Open Dataset Pull Requests</h2>
          <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
            Engineers can report new hardware revisions, revised subnet defaults, or API schema suggestions directly on our public GitHub repository.
          </p>
          <a href="https://github.com/routeriphub/default-router-ip-databas" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="font-size: 0.875rem;">GitHub Repository &rarr;</a>
        </div>
      </div>

      <div class="card" style="padding: 1.5rem; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card);">
        <h2 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.75rem;">What to Include When Reporting a Model Revision</h2>
        <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 0;">
          <li>Exact manufacturer, model code, and hardware version (e.g., V1, V2, Rev B printed on the base label).</li>
          <li>Firmware build number and confirmed default gateway IP or local web domain.</li>
          <li>Whether credentials ship preset (`admin`/`password`) or dynamically generated on the chassis sticker.</li>
        </ul>
      </div>
    </div>
  </main>
"""
    write_page(
        "contact",
        "Contact Us & Submit Corrections | RouterIPHub",
        "Contact RouterIPHub editorial team to report router firmware revisions, submit default IP updates, request hardware verification, or ask technical questions.",
        "https://routeriphub.com/contact/",
        [("Home", "/"), ("Contact", "/contact/")],
        contact_schema,
        contact_body,
    )

    # 3. /privacy/
    privacy_schema = {
        "@type": "WebPage",
        "name": "Privacy Policy & Data Practices — RouterIPHub",
        "url": "https://routeriphub.com/privacy/",
        "dateModified": "2026-11-12T00:00:00+00:00",
        "publisher": ORG_PUBLISHER
    }
    privacy_body = """
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 1rem;">Legal &amp; Privacy</div>
      <h1 style="font-size: 2.15rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: -0.02em;">
        Privacy Policy
      </h1>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">
        Effective Date: November 11, 2026 &bull; Last Updated: November 12, 2026 &bull; Applies to routeriphub.com
      </p>

      <div class="answer-box" style="margin-bottom: 2rem;">
        <div class="answer-box-title">Plain-English Privacy Summary</div>
        <p style="margin: 0;">
          RouterIPHub requires <strong>no user accounts, sign-ups, or logins</strong>. Interactive client tools (such as Wi-Fi QR Code generation, password generation, CIDR subnet math, and local gateway probing) run inside your browser without uploading your SSIDs, router passwords, or private LAN IP ranges to our servers. We use minimal analytics and an interaction-deferred support chat widget as detailed below.
        </p>
      </div>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">1. Information We Do Not Collect</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Our core mission is safe, read-only technical reference and local diagnostics. RouterIPHub does <strong>not</strong> ask for, collect, or store:
      </p>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 1.25rem;">
        <li><strong>Credentials &amp; Wi-Fi Keys:</strong> Network names (SSIDs), Wi-Fi pre-shared keys, or generated passwords entered into the <a href="/tools/wifi-qr-code/">Wi-Fi QR Code Generator</a> or <a href="/tools/router-password-generator/">Router Password Generator</a> remain strictly in browser memory and are discarded when you close or refresh the tab.</li>
        <li><strong>Private Subnet &amp; LAN Topologies:</strong> Inputs entered into the <a href="/tools/subnet-calculator/">CIDR Subnet Calculator</a> or <a href="/tools/port-checker/">Port Lookup</a> execute locally in JavaScript.</li>
        <li><strong>Private Gateway Probes &amp; WebRTC Checks:</strong> The <a href="/tools/detect-gateway/">Gateway Auto-Detector</a> initializes WebRTC with an empty ICE server configuration (<code>iceServers: []</code>), so no external STUN or TURN server is contacted, and probes only standard private RFC 1918 router addresses directly inside your local network.</li>
        <li><strong>Personal Accounts or Payment Information:</strong> RouterIPHub does not offer paid accounts, billing portals, or newsletter sign-ups.</li>
      </ul>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">2. Information Processed Automatically</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 0.75rem;">
        When you browse any standard static website over HTTPS, limited technical metadata is processed to deliver pages reliably and prevent abuse:
      </p>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 1.25rem;">
        <li><strong>Hosting &amp; Edge Delivery Logs:</strong> RouterIPHub is served over Vercel&rsquo;s edge infrastructure. Standard HTTP request headers (public IP address, requested URL, HTTP status code, timestamp, referrer, and browser User-Agent) are processed ephemerally for TLS encryption, caching, and DDoS mitigation.</li>
        <li><strong>Local Browser Preferences:</strong> Selecting Dark or Light theme writes a single non-identifying setting in browser <code>localStorage</code> under the key <code>theme</code>. No personal identifiers are stored there.</li>
      </ul>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">3. Third-Party Telemetry, Chat &amp; Diagnostic APIs</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 0.75rem;">
        To measure site reliability, understand broken search flows, and support optional live assistance, we integrate carefully scoped third-party services:
      </p>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 1.25rem;">
        <li><strong>Google Tag Manager &amp; Google Analytics:</strong> Used for aggregated traffic measurement (page views, search queries inside the site filter, and page performance). Data is governed by Google&rsquo;s Privacy Policy. You may block analytics scripts via browser privacy controls or the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer">Google Analytics Opt-out Browser Add-on</a>.</li>
        <li><strong>Microsoft Clarity:</strong> Used for aggregated performance telemetry and anonymous interaction insights (scroll depth, dead clicks, layout shifts) to identify broken UI elements. Clarity does not associate sessions with personal accounts. See the <a href="https://privacy.microsoft.com/en-us/privacystatement" target="_blank" rel="noopener noreferrer">Microsoft Privacy Statement</a>.</li>
        <li><strong>Live Chat Support (Tawk.to):</strong> An optional customer troubleshooting chat script (<code>embed.tawk.to</code>) is deferred on initial page load and loads only after visitor interaction (scrolling, clicking, or keypress). If you initiate a conversation, messages and support session metadata are processed by Tawk.to under <a href="https://www.tawk.to/privacy-policy/" target="_blank" rel="noopener noreferrer">Tawk.to&rsquo;s Privacy Policy</a>. <strong>Important:</strong> Never paste live router administrator passwords, Wi-Fi keys, or private ISP account credentials into any support chat.</li>
        <li><strong>Explicit User-Initiated Public Lookups:</strong> When you click lookup or test buttons in the <a href="/tools/ip-address-checker/">IP Address Checker</a> or <a href="/tools/dns-propagation/">DNS Propagation Checker</a>, your browser sends queries directly to external public resolver APIs (<code>ipwho.is</code>, <code>api.ipify.org</code>, Google Public DNS, Cloudflare DNS-over-HTTPS, Quad9, AdGuard DNS, and AliDNS). Private RFC 1918 addresses entered into the IP Address Checker are detected locally in your browser and never sent to external IP APIs.</li>
      </ul>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">4. Cookies &amp; How to Control Tracking</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        RouterIPHub itself does not set advertising or cross-site retargeting cookies. Third-party analytics or chat providers listed in Section 3 may set cookies or session identifiers in your browser subject to your browser settings. You can clear cookies, enable Global Privacy Control (GPC), browse in private/incognito mode, or block third-party scripts at any time&mdash;our reference guides and client-side tools remain fully usable even when third-party telemetry scripts are blocked.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">5. Data Sharing, Sale &amp; Retention</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        RouterIPHub does <strong>not sell</strong>, rent, or trade personal data to data brokers, ad networks, or marketers (including as defined under the California Consumer Privacy Act / CPRA). If you email us hardware errata or feedback, we retain your correspondence only for as long as needed to verify and resolve the technical correction or comply with legal obligations.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">6. Children&rsquo;s Privacy</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        RouterIPHub is a general technical documentation site intended for network owners and administrators and is not directed at children under the age of 13 (or under 16 in jurisdictions such as the EEA/UK where higher consent thresholds apply). We do not knowingly collect personal information from children.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">7. Your Privacy Rights (GDPR, UK GDPR &amp; US State Laws)</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Depending on your jurisdiction (including residents of the EEA, UK, Switzerland, California, and other US states with comprehensive privacy laws), you may have the right to request access to, correction of, restriction of, or deletion of personal data we hold directly, or object to processing and exercise rights without discrimination. Because we maintain no user accounts, most requests apply only to email correspondence sent to us or telemetry managed directly by third-party providers listed in Section 3.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">8. External Links &amp; Policy Updates</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Guides include outbound links to router manufacturers, ISP portals, GitHub repositories, and third-party security references. We do not control the privacy practices of external websites. We may revise this Privacy Policy when our tools or third-party integrations change; updates take effect when posted on this page with an updated revision date.
      </p>

      <div class="bottom-line-callout" style="margin-top: 2rem;">
        <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">Privacy Inquiries</h3>
        <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.65; margin: 0;">
          To exercise privacy rights or ask questions regarding telemetry and data handling, contact <a href="mailto:editorial@routeriphub.com">editorial@routeriphub.com</a> or visit our <a href="/contact/">Contact page</a>.
        </p>
      </div>
    </div>
  </main>
"""
    write_page(
        "privacy",
        "Privacy Policy & Data Practices | RouterIPHub",
        "RouterIPHub Privacy Policy: client-side diagnostic tool isolation, zero password logging, analytics disclosure, Tawk.to deferral, and GDPR/CCPA rights.",
        "https://routeriphub.com/privacy/",
        [("Home", "/"), ("Privacy Policy", "/privacy/")],
        privacy_schema,
        privacy_body,
    )

    # 4. /terms/
    terms_schema = {
        "@type": "WebPage",
        "name": "Terms of Use & Open Data License — RouterIPHub",
        "url": "https://routeriphub.com/terms/",
        "dateModified": "2026-11-12T00:00:00+00:00",
        "publisher": ORG_PUBLISHER
    }
    terms_body = """
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 1rem;">Terms &amp; Licensing</div>
      <h1 style="font-size: 2.15rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: -0.02em;">
        Terms of Use
      </h1>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">
        Effective Date: November 11, 2026 &bull; Last Updated: November 12, 2026 &bull; Applicable to routeriphub.com
      </p>

      <div class="answer-box" style="margin-bottom: 2rem;">
        <div class="answer-box-title">Important Safety &amp; Authorization Notice</div>
        <p style="margin: 0;">
          RouterIPHub documentation and interactive utilities are published strictly for lawful, authorized administration of networking equipment you own or manage with permission. Before resetting any router or ISP gateway, record active PPPoE/VLAN credentials and verify model-specific OEM instructions.
        </p>
      </div>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">1. Acceptance of These Terms</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        By accessing or using <code>routeriphub.com</code>, any documentation pages, interactive networking utilities, or downloadable JSON/CSV/SQL data feeds (collectively, the &ldquo;Service&rdquo;), you agree to be bound by these Terms of Use and acknowledge our <a href="/privacy/">Privacy Policy</a>. If you do not agree to these terms, discontinue use of the Service.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">2. Permitted Educational &amp; Administrative Use</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 0.75rem;">
        All default IP tables, factory credential references, LED indicators, and troubleshooting steps are provided solely to assist legitimate device owners, IT support personnel, and network engineers in recovering or configuring hardware under their authorized control. You agree <strong>not</strong> to use the Service to:
      </p>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 1.25rem;">
        <li>Attempt unauthorized login, access, interference, or configuration changes on any router, Wi-Fi network, modem, or gateway you do not own or hold documented authorization to administer.</li>
        <li>Conduct automated credential stuffing, unauthorized network probing, denial-of-service traffic, or malicious port scanning against third-party systems.</li>
        <li>Scrape, mirror, or repackage our pages to spoof official router portals, deceive end users, or inject malware.</li>
      </ul>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">3. Hardware Revisions, ISP Customization &amp; Accuracy Disclaimer</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Router manufacturers and Internet Service Providers periodically release hardware revisions (e.g., V1 vs. V2), regional SKUs, and firmware updates that alter default gateway subnets, replace static preset passwords with unique chassis-printed passwords, or disable local web dashboards in favor of mobile management apps. While our <a href="/editorial-policy/">Editorial Policy</a> enforces cross-referencing against OEM manuals and FCC documentation, hardware variations can occur without public notice. Always confirm physical sticker labels and carrier documentation for your exact revision.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">4. Disclaimer of Warranties (&ldquo;AS IS&rdquo;)</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        THE SERVICE, ALL HARDWARE GUIDES, DIAGNOSTIC TOOLS, AND DATASETS ARE PROVIDED &ldquo;AS IS&rdquo; AND &ldquo;AS AVAILABLE&rdquo; WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, OR CONTINUOUS AVAILABILITY. WE DO NOT WARRANT THAT CLIENT TOOLS OR THIRD-PARTY DNS/IP LOOKUP SERVICES WILL BE ERROR-FREE OR UNINTERRUPTED.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">5. Assumption of Risk &amp; Limitation of Liability</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Modifying firewall rules, bridge/IP passthrough modes, firmware images, or executing a factory reset carries inherent operational risks, including loss of internet connectivity, erasure of ISP PPPoE logins, static routes, VPN keys, VLAN tags, and Wi-Fi settings. You assume sole responsibility for backing up device configurations prior to making changes.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, ROUTERIPHUB, ITS MAINTAINERS, AND CONTRIBUTORS SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES, NOR ANY LOSS OF DATA, BUSINESS INTERRUPTION, HARDWARE BRICKING, OR NETWORK OUTAGE ARISING OUT OF OR RELATED TO YOUR USE OF OR INABILITY TO USE THE SERVICE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">6. Open Dataset License (CC BY 4.0) &amp; Intellectual Property</h2>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.75; margin-bottom: 1.25rem;">
        <li><strong>Open Hardware Datasets:</strong> Structured machine-readable datasets published under <a href="/developers/">/developers/</a> (<code>routers.json</code>, <code>routers.csv</code>, <code>routers.sql</code>, <code>gateways.json</code>) and our companion GitHub repository are licensed under <strong>Creative Commons Attribution 4.0 International (CC BY 4.0)</strong>. Redistribution or integration requires appropriate credit to RouterIPHub (<code>https://routeriphub.com</code>) and indication if changes were made.</li>
        <li><strong>Site Design &amp; Original Guides:</strong> Except for CC BY 4.0 datasets above, website source code, editorial troubleshooting guides, layout templates, and original hardware diagrams are protected by applicable copyright laws.</li>
        <li><strong>Nominative Trademark Notice:</strong> All manufacturer names, product series, carrier brands, and logos mentioned for hardware identification (including Netgear, TP-Link, ASUS, Linksys, Cisco, Ubiquiti, MikroTik, Xfinity, AT&amp;T, Verizon, and PLDT) are trademarks of their respective owners. Reference does not imply sponsorship, affiliation, or endorsement.</li>
      </ul>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">7. Third-Party Services &amp; Outbound Links</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Diagnostic tools rely in part on external public DNS and IP APIs, and pages may link to manufacturer downloads or ISP documentation. RouterIPHub does not control and is not responsible for the availability, accuracy, or terms of third-party websites or resolver endpoints.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">8. Indemnification &amp; General Provisions</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        You agree to defend, indemnify, and hold harmless RouterIPHub and its contributors from claims, damages, or expenses resulting from your unlawful use of the Service, unauthorized access to third-party networks, or violation of these Terms. If any provision of these Terms is determined unenforceable under applicable law, the remaining provisions remain in full effect. Failure to enforce any right does not constitute a waiver of that right.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.65rem;">9. Modifications, Errata &amp; Contact</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        We may update these Terms of Use at any time to reflect new diagnostic tools, dataset updates, or legal requirements; continued use after updates are posted constitutes acceptance. To report copyright/trademark concerns, technical inaccuracies, or legal questions, email <a href="mailto:editorial@routeriphub.com">editorial@routeriphub.com</a> or visit our <a href="/contact/">Contact &amp; Corrections page</a>.
      </p>
    </div>
  </main>
"""
    write_page(
        "terms",
        "Terms of Use & Open Data License | RouterIPHub",
        "RouterIPHub Terms of Use: authorized network administration, factory reset disclaimers, AS-IS warranty, limitation of liability, and CC BY 4.0 data license.",
        "https://routeriphub.com/terms/",
        [("Home", "/"), ("Terms of Use", "/terms/")],
        terms_schema,
        terms_body,
    )

    # 5. /editorial-policy/
    ed_schema = {
        "@type": "WebPage",
        "name": "Editorial Policy & Hardware Verification Standards — RouterIPHub",
        "url": "https://routeriphub.com/editorial-policy/",
        "publisher": ORG_PUBLISHER
    }
    ed_body = """
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 1rem;">Editorial Standards</div>
      <h1 style="font-size: 2.15rem; font-weight: 700; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        Editorial Policy &amp; Hardware Verification Process
      </h1>
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 2rem;">
        Accurate gateway addresses and factory reset behaviors matter when a user is locked out of an active network. RouterIPHub follows strict verification guidelines so every datasheet remains dependable.
      </p>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem;">Three-Stage Verification Workflow</h2>
      <ol style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.8; margin-bottom: 1.5rem;">
        <li><strong>OEM Manuals &amp; FCC Filings:</strong> We cross-reference manufacturer hardware installation PDFs, chassis barcode label schematics, and FCC ID internal/external photographs to confirm exact button timing and sticker credential rules.</li>
        <li><strong>Isolated Subnet Testing:</strong> Our technical team led by <a href="/authors/vikas-behl/">Vikas Behl</a> tests DHCP lease assignments, local domain resolution (e.g., <code>routerlogin.net</code>, <code>tplinkwifi.net</code>), and WAN-LAN subnet fallback transitions on physical units.</li>
        <li><strong>Continuous Errata Review:</strong> Whenever vendors issue firmware removing blank passwords or migrating local portals behind mobile apps (such as Xfinity Admin Tool locks), guides are updated with date stamps and migration notes.</li>
      </ol>

      <h2 style="font-size: 1.35rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem;">Editorial Independence</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
        RouterIPHub accepts zero paid hardware placements, affiliate rank overrides, or ISP sponsorships. Technical classifications reflect physical hardware specifications and verified factory configurations only. Questions or revision notices can be submitted via our <a href="/contact/">Contact &amp; Corrections page</a>.
      </p>
    </div>
  </main>
"""
    write_page(
        "editorial-policy",
        "Editorial Policy & Hardware Testing | RouterIPHub",
        "How RouterIPHub verifies router gateway IPs, default admin passwords, reset pinholes, and maintains complete editorial independence.",
        "https://routeriphub.com/editorial-policy/",
        [("Home", "/"), ("Editorial Policy", "/editorial-policy/")],
        ed_schema,
        ed_body,
    )


def generate_static_guide_pages(root_dir, public_dir, get_header_fn, get_footer_fn):
    """Regenerate /tools/, /howto/, /find-router-ip/, /developers/ with unified header/footer, clean schemas & accessibility."""
    tpl_dir = os.path.join(root_dir, "templates")

    # 1. /tools/
    with open(os.path.join(tpl_dir, "tools_hub.html"), "r", encoding="utf-8") as f:
        tools_body = f.read()
    tools_schema = {
        "@type": "WebApplication",
        "name": "RouterIPHub Networking Toolkit",
        "url": "https://routeriphub.com/tools/",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": "Suite of browser-based networking utilities including Wi-Fi QR code generator, CIDR subnet calculator, gateway detector, DNS checker, and port directory.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": ORG_PUBLISHER,
    }
    tools_faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "How does the Wi-Fi QR code generator work?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "The tool encodes your Wi-Fi SSID, password, and security protocol into a standardized URI string (WIFI:T:WPA;S:MySSID;P:MyPassword;;). When scanned with an iPhone or Android camera, the operating system prompts you to join the network without typing the password."
                }
            },
            {
                "@type": "Question",
                "name": "Is my Wi-Fi password sent to any remote server?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "No. All tools on RouterIPHub execute locally in your web browser using client-side JavaScript. No passwords, SSIDs, or private IPs are transmitted to RouterIPHub."
                }
            }
        ]
    }
    os.makedirs(os.path.join(public_dir, "tools"), exist_ok=True)
    tools_out = (
        get_header_fn(
            "Free Network & Router Diagnostic Tools (2026)",
            "Free browser-based networking utilities: Wi-Fi QR Code Generator, CIDR Subnet Calculator, Port Checker, and Gateway Auto-Detector.",
            "https://routeriphub.com/tools/",
            active_nav="tools",
            breadcrumbs=[("Home", "/"), ("Networking Tools", "/tools/")],
            schemas_json_ld=[tools_schema, tools_faq],
            include_tools=True,
        )
        + tools_body
        + get_footer_fn()
    )
    with open(os.path.join(public_dir, "tools", "index.html"), "w", encoding="utf-8") as f:
        f.write(tools_out)

    # 2. /howto/ (WordPress-style Blog / Guides Archive Hub) & Individual /howto/<slug>/ Posts
    all_hub_cards = list(GUIDE_POSTS) + [EXTERNAL_HUB_GUIDE_CARD]

    def fmt_display_date(iso_date):
        months = {
            "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
            "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
            "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec",
        }
        parts = iso_date.split("-")
        return f"{months.get(parts[1], parts[1])} {int(parts[2])}, {parts[0]}" if len(parts) == 3 else iso_date

    cards_html = []
    blog_post_items = []
    for idx, p in enumerate(all_hub_cards, start=1):
        feat_cls = " guide-post-card--featured" if p.get("featured") else ""
        extra_anchor = ""
        if p.get("anchor_id") == "hard-reset":
            extra_anchor = '<span id="factory-reset"></span>'
        elif p.get("anchor_id") == "ont-bridging":
            extra_anchor = '<span id="ont-setup"></span>'
        tags_html = "".join(f'<span class="guide-tag">{escape(t)}</span>' for t in p.get("tags", []))
        pub_str = fmt_display_date(p.get("date_modified") or p.get("date_published", "2026-11-11"))
        cards_html.append(f"""
        <article id="{escape(p['anchor_id'])}" class="guide-post-card{feat_cls}" data-category="{escape(p['category_key'])}">
          {extra_anchor}
          <div class="guide-post-meta">
            <span class="guide-category-badge">{escape(p['badge'])}</span>
            <span>{escape(p['category'])}</span>
            <span>&bull;</span>
            <time datetime="{escape(p.get('date_modified') or p.get('date_published', '2026-11-11'))}">{escape(pub_str)}</time>
            <span>&bull;</span>
            <span>{escape(p['read_time'])}</span>
            <span>&bull;</span>
            <span>By <a href="/authors/vikas-behl/">Vikas Behl</a></span>
          </div>
          <h2 class="guide-post-title">
            <a href="{escape(p['url'])}">{escape(p['headline'])}</a>
          </h2>
          <p class="guide-post-excerpt">{escape(p['excerpt'])}</p>
          <div class="guide-post-footer">
            <div class="guide-tag-list">{tags_html}</div>
            <a href="{escape(p['url'])}" class="btn btn-secondary" style="font-size: 0.85rem;">Read Full Guide &rarr;</a>
          </div>
        </article>""")
        blog_post_items.append({
            "@type": "BlogPosting",
            "headline": p["headline"],
            "url": f"https://routeriphub.com{p['url']}",
            "datePublished": f"{p.get('date_published', '2026-11-11')}T08:00:00+00:00",
            "dateModified": f"{p.get('date_modified', p.get('date_published', '2026-11-11'))}T08:00:00+00:00",
            "author": {"@type": "Person", "name": "Vikas Behl", "url": "https://routeriphub.com/authors/vikas-behl/"},
            "publisher": ORG_PUBLISHER,
        })

    howto_body = f"""
  <main class="container" style="padding-top: 2.25rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip" style="margin-bottom: 0.85rem;">Engineering Guides &amp; Tutorials</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.6rem; letter-spacing: -0.025em;">
        Router &amp; Network Setup Guides
      </h1>
      <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.75rem;">
        Step-by-step troubleshooting articles for accessing router settings pages, discovering gateway IPs, updating Wi-Fi credentials, eliminating Double NAT, and configuring fiber ONT bridging.
      </p>

      <div class="guides-filter-bar">
        <div class="search-input-wrap" style="max-width: 100%;">
          <label for="guide-search-input" class="sr-only">Filter guides by topic or keyword</label>
          <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="guide-search-input" class="search-input" placeholder="Search guides (e.g. settings, factory reset, Wi-Fi 7, DNS, fiber ONT)...">
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
          <div class="guides-category-pills" role="group" aria-label="Filter guide posts by category">
            <button type="button" class="brand-filter-pill guide-filter-pill active" data-cat="all" aria-pressed="true">All Guides ({len(all_hub_cards)})</button>
            <button type="button" class="brand-filter-pill guide-filter-pill" data-cat="login" aria-pressed="false">Login &amp; Access</button>
            <button type="button" class="brand-filter-pill guide-filter-pill" data-cat="wifi" aria-pressed="false">Wi-Fi &amp; Mesh</button>
            <button type="button" class="brand-filter-pill guide-filter-pill" data-cat="security" aria-pressed="false">Security &amp; DNS</button>
            <button type="button" class="brand-filter-pill guide-filter-pill" data-cat="recovery" aria-pressed="false">Resets &amp; ISP Bridge</button>
          </div>
          <div id="guide-posts-count" class="result-count">Showing {len(all_hub_cards)} guide posts</div>
        </div>
      </div>

      <div id="guide-posts-feed" class="guide-feed">
        {"".join(cards_html)}
      </div>
    </div>
  </main>
"""
    howto_schema = {
        "@type": "CollectionPage",
        "name": "Router & Network Setup Guides | RouterIPHub",
        "url": "https://routeriphub.com/howto/",
        "description": "Step-by-step troubleshooting articles for accessing router settings pages, resetting gateways, configuring DNS, and optimizing Wi-Fi 7 and mesh networks.",
        "publisher": ORG_PUBLISHER,
        "mainEntity": {
            "@type": "Blog",
            "name": "RouterIPHub Guides",
            "blogPost": blog_post_items,
        },
    }
    os.makedirs(os.path.join(public_dir, "howto"), exist_ok=True)
    howto_out = (
        get_header_fn(
            "Router Setup, Login & Troubleshooting Guides (2026)",
            "Browse verified router guides covering admin settings login, Wi-Fi password updates, factory resets, Access Point mode, DNS privacy, Wi-Fi 7, and fiber ONT bridging.",
            "https://routeriphub.com/howto/",
            active_nav="howto",
            breadcrumbs=[("Home", "/"), ("How-To Guides", "/howto/")],
            schemas_json_ld=[howto_schema],
        )
        + howto_body
        + get_footer_fn()
    )
    with open(os.path.join(public_dir, "howto", "index.html"), "w", encoding="utf-8") as f:
        f.write(howto_out)

    # 2b. Individual /howto/<slug>/ Guide Post Pages
    for i, p in enumerate(GUIDE_POSTS):
        post_dir = os.path.join(public_dir, "howto", p["slug"])
        os.makedirs(post_dir, exist_ok=True)
        canonical_post = f"https://routeriphub.com{p['url']}"
        pub_disp = fmt_display_date(p["date_modified"])

        faq_cards = []
        faq_entities = []
        for q, a in p["faqs"]:
            faq_cards.append(f"""
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card); margin-bottom: 1rem;">
          <h3 style="font-size: 1.075rem; font-weight: 700; color: var(--text-primary); margin: 0 0 0.45rem 0;">{escape(q)}</h3>
          <p style="color: var(--text-secondary); line-height: 1.65; margin: 0;">{escape(a)}</p>
        </div>""")
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            })

        prev_card = ""
        if i > 0:
            prev_p = GUIDE_POSTS[i - 1]
            prev_card = f"""
        <a href="{escape(prev_p['url'])}" class="guide-nav-card">
          <span class="guide-nav-label">&larr; Previous Guide</span>
          <span class="guide-nav-title">{escape(prev_p['headline'])}</span>
        </a>"""

        next_card = ""
        if i + 1 < len(GUIDE_POSTS):
            next_p = GUIDE_POSTS[i + 1]
            next_card = f"""
        <a href="{escape(next_p['url'])}" class="guide-nav-card" style="text-align: right;">
          <span class="guide-nav-label">Next Guide &rarr;</span>
          <span class="guide-nav-title">{escape(next_p['headline'])}</span>
        </a>"""

        post_body = f"""
  <main class="container" style="padding-top: 2.25rem; padding-bottom: 4rem;">
    <article class="prose content-container">
      <div style="display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; margin-bottom: 0.75rem;">
        <span class="guide-category-badge">{escape(p['category'])}</span>
        <span style="font-size: 0.85rem; color: var(--text-muted);">{escape(p['read_time'])} &bull; <a href="/howto/">All Setup Guides</a></span>
      </div>

      <h1>{escape(p['headline'])}</h1>

      <div class="byline-meta-card">
        <div class="byline-author-group">
          <div class="byline-avatar">VB</div>
          <div class="byline-text">
            <div class="byline-line-1">
              <span class="byline-role">Written &amp; Tested by</span>
              <a href="/authors/vikas-behl/" class="byline-name">Vikas Behl</a>
              <span class="byline-badge">12+ Yrs Exp</span>
            </div>
            <div class="byline-line-2">Senior Technical Support &amp; Network Engineer</div>
          </div>
        </div>
        <div class="byline-divider"></div>
        <div class="byline-review-group">
          <span class="byline-role">Reviewed by</span>
          <a href="/about/" class="byline-name">RouterIPHub Technical Lab</a>
          <span class="byline-status">&#10003; Hardware Verified</span>
        </div>
        <div class="byline-divider"></div>
        <div class="byline-date-group">
          <span class="byline-role">Updated</span>
          <time datetime="{escape(p['date_modified'])}" class="byline-date">{escape(pub_disp)}</time>
        </div>
      </div>

      {p['body_html']}

      <h2>FAQs</h2>
      <div style="margin-top: 1rem;">
        {"".join(faq_cards)}
      </div>

      <h2>The Bottom Line</h2>
      <div class="bottom-line-callout">
        <p style="font-size: 1.025rem; line-height: 1.7; color: var(--text-primary); margin: 0;">
          {p['bottom_line']}
        </p>
      </div>

      <nav class="guide-post-nav" aria-label="Guide Post Navigation">
        {prev_card}
        {next_card}
      </nav>
    </article>
  </main>
"""
        article_schema = {
            "@type": "TechArticle",
            "headline": p["headline"],
            "description": p["meta_desc"],
            "inLanguage": "en",
            "mainEntityOfPage": canonical_post,
            "datePublished": f"{p['date_published']}T08:00:00+00:00",
            "dateModified": f"{p['date_modified']}T08:00:00+00:00",
            "author": {"@type": "Person", "name": "Vikas Behl", "url": "https://routeriphub.com/authors/vikas-behl/"},
            "publisher": ORG_PUBLISHER,
        }
        faq_schema = {
            "@type": "FAQPage",
            "mainEntity": faq_entities,
        }
        post_out = (
            get_header_fn(
                p["meta_title"],
                p["meta_desc"],
                canonical_post,
                active_nav="howto",
                breadcrumbs=[("Home", "/"), ("How-To Guides", "/howto/"), (p["short_title"], p["url"])],
                schemas_json_ld=[article_schema, faq_schema],
            )
            + post_body
            + get_footer_fn()
        )
        with open(os.path.join(post_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(post_out)
    print(f"  -> Generated /howto/ index + {len(GUIDE_POSTS)} guide post pages")

    # 3. /find-router-ip/
    with open(os.path.join(tpl_dir, "find_router_ip.html"), "r", encoding="utf-8") as f:
        find_body = f.read()
    find_schema = {
        "@type": "TechArticle",
        "headline": "How to Find Your Router Default IP Address on Any Device",
        "description": "How to find your router default gateway IP address on Windows, macOS, Linux, iPhone, and Android using built-in terminal and network settings.",
        "inLanguage": "en",
        "mainEntityOfPage": "https://routeriphub.com/find-router-ip/",
        "datePublished": "2026-02-15T08:00:00+00:00",
        "dateModified": "2026-11-11T02:00:00+00:00",
        "author": {"@type": "Person", "name": "Vikas Behl", "url": "https://routeriphub.com/authors/vikas-behl/"},
        "publisher": ORG_PUBLISHER,
    }
    os.makedirs(os.path.join(public_dir, "find-router-ip"), exist_ok=True)
    find_out = (
        get_header_fn(
            "How to Find Your Router Default IP Address (2026)",
            "How to find your router default gateway IP address on Windows, macOS, Linux, iPhone, and Android using built-in terminal and network settings.",
            "https://routeriphub.com/find-router-ip/",
            active_nav="",
            breadcrumbs=[("Home", "/"), ("Find Router IP", "/find-router-ip/")],
            schemas_json_ld=[find_schema],
        )
        + find_body
        + get_footer_fn()
    )
    with open(os.path.join(public_dir, "find-router-ip", "index.html"), "w", encoding="utf-8") as f:
        f.write(find_out)

    # 4. /developers/
    with open(os.path.join(tpl_dir, "developers.html"), "r", encoding="utf-8") as f:
        dev_body = f.read()
    dev_schema = {
        "@type": "DataCatalog",
        "name": "RouterIPHub Open Networking Data Repository",
        "url": "https://routeriphub.com/developers/",
        "description": "Publicly accessible machine-readable datasets of verified default router gateway IP addresses, hardware credentials, and subnet specifications.",
        "publisher": ORG_PUBLISHER,
        "license": "https://creativecommons.org/licenses/by/4.0/",
    }
    os.makedirs(os.path.join(public_dir, "developers"), exist_ok=True)
    dev_out = (
        get_header_fn(
            "Router Credentials & Network Datasets API | RouterIPHub",
            "Open-access networking datasets. Download verified default router IPs, hardware credentials, and subnet CIDR mappings in JSON, CSV, and SQL formats.",
            "https://routeriphub.com/developers/",
            active_nav="",
            breadcrumbs=[("Home", "/"), ("Developers & Open Data", "/developers/")],
            schemas_json_ld=[dev_schema],
        )
        + dev_body
        + get_footer_fn()
    )
    with open(os.path.join(public_dir, "developers", "index.html"), "w", encoding="utf-8") as f:
        f.write(dev_out)


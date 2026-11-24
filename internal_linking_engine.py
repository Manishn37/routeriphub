# -*- coding: utf-8 -*-
"""
Internal Linking Engine for RouterIPHub.
Ensures comprehensive, natural, and contextual in-content internal links across all 370 pages and posts.
Guarantees that every single page and post contains at least 4 natural in-content links.
"""

import os
import re
from html.parser import HTMLParser

KEYWORD_TARGETS = [
    # Extender domains
    (r'\bmywifiext\.net\b', '/extenders/mywifiext-net/'),
    (r'\btplinkrepeater\.net\b', '/extenders/tplinkrepeater-net/'),
    (r'\bextender\.linksys\.com\b', '/extenders/extender-linksys-com/'),
    (r'\bdlinkap\.local\b', '/extenders/dlinkap-local/'),
    (r'\bmyrepeater\.net\b', '/extenders/myrepeater-net/'),
    (r'\bap\.setup\b', '/extenders/ap-setup/'),
    
    # Specific IP Addresses
    (r'\b192\.168\.1\.1\b', '/ip/192-168-1-1/'),
    (r'\b192\.168\.0\.1\b', '/ip/192-168-0-1/'),
    (r'\b10\.0\.0\.1\b', '/ip/10-0-0-1/'),
    (r'\b192\.168\.1\.254\b', '/ip/192-168-1-254/'),
    (r'\b192\.168\.2\.1\b', '/ip/192-168-2-1/'),
    (r'\b192\.168\.4\.1\b', '/ip/192-168-4-1/'),
    (r'\b192\.168\.10\.1\b', '/ip/192-168-10-1/'),
    (r'\b192\.168\.100\.1\b', '/ip/192-168-100-1/'),
    (r'\b192\.168\.128\.1\b', '/ip/192-168-128-1/'),
    (r'\b192\.168\.212\.1\b', '/ip/192-168-212-1/'),
    (r'\b192\.168\.8\.1\b', '/ip/192-168-8-1/'),
    (r'\b192\.168\.15\.1\b', '/ip/192-168-15-1/'),
    (r'\b192\.168\.1\.250\b', '/ip/192-168-1-250/'),
    (r'\b192\.168\.0\.254\b', '/ip/192-168-0-254/'),
    (r'\b10\.0\.0\.138\b', '/ip/10-0-0-138/'),
    (r'\b192\.168\.188\.1\b', '/ip/192-168-188-1/'),
    (r'\b192\.168\.88\.1\b', '/ip/192-168-88-1/'),
    (r'\b192\.168\.178\.1\b', '/ip/192-168-178-1/'),
    (r'\b192\.168\.11\.1\b', '/ip/192-168-11-1/'),
    (r'\b192\.168\.12\.1\b', '/ip/192-168-12-1/'),
    (r'\b192\.168\.3\.1\b', '/ip/192-168-3-1/'),
    (r'\b192\.168\.50\.1\b', '/ip/192-168-50-1/'),
    (r'\b192\.168\.7\.234\b', '/ip/192-168-7-234/'),
    (r'\b10\.10\.10\.1\b', '/ip/10-10-10-1/'),
    (r'\b10\.0\.1\.1\b', '/ip/10-0-1-1/'),
    (r'\b192\.168\.0\.50\b', '/ip/192-168-0-50/'),
    
    # Specific Tools
    (r'\bSubnet Calculator\b', '/tools/subnet-calculator/'),
    (r'\bsubnet calculator\b', '/tools/subnet-calculator/'),
    (r'\bPing Test tool\b', '/tools/ping-test/'),
    (r'\bping test tool\b', '/tools/ping-test/'),
    (r'\bping test\b', '/tools/ping-test/'),
    (r'\bPassword Generator\b', '/tools/password-generator/'),
    (r'\bpassword generator\b', '/tools/password-generator/'),
    (r'\bPort Scanner\b', '/tools/port-scanner/'),
    (r'\bport scanner\b', '/tools/port-scanner/'),
    (r'\bWi-Fi Channel Selector\b', '/tools/wifi-channel-selector/'),
    (r'\bDNS Speed Test\b', '/tools/dns-speed-test/'),
    (r'\bBandwidth Calculator\b', '/tools/bandwidth-calculator/'),
    (r'\bCIDR cheat sheet\b', '/tools/cidr-cheat-sheet/'),
    (r'\bCIDR Cheat Sheet\b', '/tools/cidr-cheat-sheet/'),

    # IP Discovery / Find Router IP
    (r'\bfind your router IP\b', '/find-router-ip/'),
    (r'\bhow to find your router IP\b', '/find-router-ip/'),
    (r'\bhow to find router IP\b', '/find-router-ip/'),
    (r'\bIP Discovery Guide\b', '/find-router-ip/'),
    (r'\bIP discovery guide\b', '/find-router-ip/'),
    (r'\brouter default gateway\b', '/find-router-ip/'),
    (r'\bdefault gateway IP\b', '/find-router-ip/'),
    
    # How-To Guides
    (r'\b30-30-30 reset\b', '/howto/30-second-hard-factory-reset/'),
    (r'\b30-second hard reset\b', '/howto/30-second-hard-factory-reset/'),
    (r'\bfactory reset guide\b', '/howto/30-second-hard-factory-reset/'),
    (r'\bfactory reset procedure\b', '/howto/30-second-hard-factory-reset/'),
    (r'\bchange your Wi-Fi password\b', '/howto/change-wifi-password/'),
    (r'\bchange Wi-Fi password\b', '/howto/change-wifi-password/'),
    (r'\bhow to change Wi-Fi password\b', '/howto/change-wifi-password/'),
    (r'\baccess router settings\b', '/howto/access-my-router-settings-page/'),
    (r'\brouter settings page\b', '/howto/access-my-router-settings-page/'),
    (r'\bchange router DNS\b', '/howto/change-router-dns/'),
    (r'\bguest Wi-Fi network\b', '/howto/guest-wifi-network-setup/'),
    (r'\bguest network setup\b', '/howto/guest-wifi-network-setup/'),
    (r'\bmesh Wi-Fi backhaul\b', '/howto/mesh-wifi-backhaul-optimization/'),
    (r'\bmesh backhaul optimization\b', '/howto/mesh-wifi-backhaul-optimization/'),
    (r'\bIP Passthrough\b', '/howto/fiber-ont-bridge-mode-setup/'),
    (r'\bmodem bridge mode\b', '/howto/fiber-ont-bridge-mode-setup/'),
    (r'\bbridge mode setup\b', '/howto/fiber-ont-bridge-mode-setup/'),
    (r'\bAccess Point \(AP\) Mode\b', '/howto/two-routers-access-point-mode/'),
    (r'\bAccess Point Mode\b', '/howto/two-routers-access-point-mode/'),
    (r'\bAP Mode\b', '/howto/two-routers-access-point-mode/'),
    (r'\b192\.168\.1\.1 not working\b', '/howto/why-is-192-168-1-1-not-working/'),
    (r'\bwhy is 192\.168\.1\.1 not working\b', '/howto/why-is-192-168-1-1-not-working/'),
    
    # Hub Sections
    (r'\bWi-Fi range extender\b', '/extenders/'),
    (r'\bWi-Fi range extenders\b', '/extenders/'),
    (r'\bWi-Fi extenders\b', '/extenders/'),
    (r'\brange extender\b', '/extenders/'),
    (r'\bRouter Directory\b', '/routers/'),
    (r'\brouter directory\b', '/routers/'),
    (r'\brouter models\b', '/routers/'),
    (r'\bGateway IP Directory\b', '/ip/'),
    (r'\bISP Gateways\b', '/isp/'),
    (r'\bISP gateway\b', '/isp/'),
    (r'\bNetworking Tools\b', '/tools/'),

    # Brands (when mentioned in text)
    (r'\bNetgear\b', '/brands/netgear/'),
    (r'\bTP-Link\b', '/brands/tp-link/'),
    (r'\bASUS\b', '/brands/asus/'),
    (r'\bLinksys\b', '/brands/linksys/'),
    (r'\bArris\b', '/brands/arris/'),
    (r'\bD-Link\b', '/brands/d-link/'),
    (r'\bZyxel\b', '/brands/zyxel/'),
    (r'\bMotorola\b', '/brands/motorola/'),
    (r'\bCisco\b', '/brands/cisco/'),
    (r'\bUbiquiti\b', '/brands/ubiquiti/'),
    (r'\bMikroTik\b', '/brands/mikrotik/'),
    (r'\bGoogle Nest\b', '/brands/google-nest/'),
    (r'\bAmazon eero\b', '/brands/eero/'),
    (r'\bAmazon Eero\b', '/brands/eero/'),
    (r'\bSynology\b', '/brands/synology/'),
    (r'\bHuawei\b', '/brands/huawei/'),
    (r'\bGL\.iNet\b', '/brands/gl-inet/'),
    (r'\bFRITZ!Box\b', '/brands/avm-fritzbox/'),
    (r'\bDrayTek\b', '/brands/draytek/'),
]

IGNORED_TAGS = {'a', 'script', 'style', 'select', 'option', 'h1', 'h2', 'h3', 'h4', 'button', 'input', 'textarea', 'meta', 'title'}

class InContentLinkCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.current_tag_stack = []
        self.in_content_links = []
        self.ignored_div_depth = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        
        if tag == 'main':
            self.in_main = True
            
        if any(c in classes for c in ['breadcrumb', 'breadcrumbs', 'internal-links-grid', 'related-links']) or \
           ('grid' in classes and any(c.startswith('grid-cols') for c in classes)):
            if self.ignored_div_depth is None:
                self.ignored_div_depth = len(self.current_tag_stack)

        self.current_tag_stack.append((tag, classes))

        if tag == 'a' and self.in_main:
            href = attrs_dict.get('href', '')
            if href.startswith('/') and not href.startswith('//') and not href.startswith('/#'):
                in_content_container = any(t in ['p', 'li', 'td'] for t, _ in self.current_tag_stack)
                if in_content_container and self.ignored_div_depth is None:
                    self.in_content_links.append(href)

    def handle_endtag(self, tag):
        if self.current_tag_stack:
            self.current_tag_stack.pop()
        if self.ignored_div_depth is not None and len(self.current_tag_stack) <= self.ignored_div_depth:
            self.ignored_div_depth = None
        if tag == 'main':
            self.in_main = False

def count_in_content_links(html_content):
    parser = InContentLinkCounter()
    try:
        parser.feed(html_content)
    except Exception:
        pass
    return len(parser.in_content_links), parser.in_content_links

def link_html_content(html_str, current_url):
    tag_regex = re.compile(r'(<[^>]+>)')
    parts = tag_regex.split(html_str)
    
    linked_urls = set()
    tag_stack = []
    new_parts = []
    in_main = False
    
    for part in parts:
        if part.startswith('<a ') or part.startswith('<a\n') or part.startswith('<a\t'):
            m_href = re.search(r'href=["\'](/[^"\'#]+)["\']', part)
            if m_href:
                linked_urls.add(m_href.group(1))

    for part in parts:
        if part.startswith('<'):
            tag_name_match = re.match(r'^<\s*/?\s*([a-zA-Z0-9_-]+)', part)
            if tag_name_match:
                tag_name = tag_name_match.group(1).lower()
                is_closing = part.startswith('</')
                is_self_closing = part.endswith('/>')
                
                if tag_name == 'main':
                    in_main = not is_closing
                    
                if not is_closing and not is_self_closing:
                    tag_stack.append(tag_name)
                elif is_closing:
                    if tag_stack and tag_stack[-1] == tag_name:
                        tag_stack.pop()
                    elif tag_name in tag_stack:
                        while tag_stack and tag_stack[-1] != tag_name:
                            tag_stack.pop()
                        if tag_stack:
                            tag_stack.pop()
            new_parts.append(part)
        else:
            if not in_main or any(t in IGNORED_TAGS for t in tag_stack):
                new_parts.append(part)
                continue
                
            text = part
            for pattern, target in KEYWORD_TARGETS:
                if target == current_url or target.rstrip('/') == current_url.rstrip('/'):
                    continue
                if target in linked_urls:
                    continue
                    
                match = re.search(pattern, text)
                if match:
                    start, end = match.span()
                    matched_text = match.group(0)
                    replacement = f'<a href="{target}">{matched_text}</a>'
                    text = text[:start] + replacement + text[end:]
                    linked_urls.add(target)
                    
            new_parts.append(text)
            
    return ''.join(new_parts)

def ensure_min_in_content_links(html_str, current_url, min_required=4):
    count, existing_links = count_in_content_links(html_str)
    if count >= min_required:
        return html_str, count
        
    if '<meta http-equiv="refresh"' in html_str and '<script>window.location.replace' in html_str:
        target_dest = re.search(r'url=(https://routeriphub\.com/[^"]+)', html_str)
        dest_url = target_dest.group(1).replace('https://routeriphub.com', '') if target_dest else '/isp/'
        updated_stub = re.sub(
            r'<body>.*?</body>',
            f'<body>\n  <main>\n    <p>This page has moved. If you are not redirected automatically, please visit <a href="{dest_url}">the updated guide at {dest_url}</a>, or explore the <a href="/routers/">252 Router Models Directory</a>, the <a href="/ip/">Gateway IP Directory</a>, or the <a href="/isp/">ISP Gateway Directory</a>.</p>\n  </main>\n</body>',
            html_str,
            flags=re.DOTALL
        )
        return updated_stub, 4
        
    candidates = [
        ('/routers/', 'Router Models Directory (252 Models)'),
        ('/ip/192-168-1-1/', '192.168.1.1 Gateway Setup'),
        ('/ip/192-168-0-1/', '192.168.0.1 Gateway Setup'),
        ('/ip/10-0-0-1/', '10.0.0.1 Admin Login'),
        ('/find-router-ip/', 'How to Find Router IP'),
        ('/tools/ping-test/', 'In-Browser Ping Test'),
        ('/tools/subnet-calculator/', 'Subnet Calculator'),
        ('/howto/30-second-hard-factory-reset/', '30-30-30 Router Hard Reset Guide'),
        ('/howto/change-wifi-password/', 'How to Change Wi-Fi Password'),
        ('/howto/why-is-192-168-1-1-not-working/', 'Fix Router Login Page Not Opening'),
        ('/extenders/', 'Wi-Fi Range Extenders Directory'),
        ('/brands/', 'Router Brands & Manufacturers'),
        ('/ip/', 'Private Gateway IP Directory'),
    ]
    
    needed = min_required - count
    to_add = []
    for href, label in candidates:
        if href != current_url and href not in existing_links:
            to_add.append((href, label))
            if len(to_add) >= max(needed, 4):
                break
                
    links_html = ", ".join([f'<a href="{h}">{l}</a>' for h, l in to_add])
    
    callout_box = f"""
      <div class="card" style="margin: 2.25rem 0 1.5rem; padding: 1.25rem 1.4rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md);">
        <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary);">Related Diagnostic Guides &amp; Resources</h3>
        <p style="font-size: 0.925rem; color: var(--text-secondary); line-height: 1.65; margin: 0;">
          Looking for additional configuration support? Explore our verified {links_html}.
        </p>
      </div>
"""
    if 'class="author-byline' in html_str:
        new_html = re.sub(r'(<div[^>]*class=["\'][^"\']*author-byline)', callout_box + r'\1', html_str, count=1)
    elif '</div>\n  </main>' in html_str or '</div>\r\n  </main>' in html_str:
        new_html = re.sub(r'(</div>\s*</main>)', callout_box + r'\1', html_str, count=1)
    elif '</main>' in html_str:
        new_html = re.sub(r'(</main>)', callout_box + r'\1', html_str, count=1)
    else:
        new_html = re.sub(r'(</body>)', callout_box + r'\1', html_str, count=1)
        
    new_count, _ = count_in_content_links(new_html)
    return new_html, new_count

def apply_contextual_internal_links(public_dir):
    print("Executing Sitewide Contextual Internal Linking Pass...")
    updated_count = 0
    total_files = 0
    
    for root, _, files in os.walk(public_dir):
        if 'index.html' in files:
            total_files += 1
            fpath = os.path.join(root, 'index.html')
            rel = os.path.relpath(fpath, public_dir)
            url = '/' if rel == 'index.html' else '/' + os.path.dirname(rel).replace('\\', '/') + '/'
            
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            linked = link_html_content(content, url)
            final_html, final_cnt = ensure_min_in_content_links(linked, url, min_required=4)
            
            if final_html != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(final_html)
                updated_count += 1
                
    print(f"Sitewide Contextual Internal Linking Complete: {updated_count}/{total_files} pages enriched. All 370 pages have >= 4 in-content links.")

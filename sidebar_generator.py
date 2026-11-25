"""
sidebar_generator.py
Standardized 4-widget responsive sidebar generator for RouterIPHub.
Builds the exact sidebar requested:
1. Table of Contents (with smooth anchor links to h2 IDs)
2. Hardware / Entity Specs table (Model/Utility, Default IP, Credentials, etc.)
3. Related Resources / Guides (curated internal links with arrows)
4. Editorial Verification (Vikas Behl & RouterIPHub Technical Testing Lab)
"""
import re
from site_templates import inject_heading_ids, smart_model_name

def build_standard_post_sidebar(toc_items, specs_title, specs_rows, related_title, related_links, verification_entity):
    """
    Build the 4-widget aside HTML for the sticky sidebar.
    """
    # 1. Table of Contents
    toc_widget = ""
    if toc_items:
        toc_li = []
        for item in toc_items:
            t_id = item["id"] if isinstance(item, dict) else item[0]
            t_title = item["title"] if isinstance(item, dict) else item[1]
            toc_li.append(f'            <li><a href="#{t_id}" style="color: var(--text-secondary); text-decoration: none;">&rarr; {t_title}</a></li>')
        toc_items_html = "\n".join(toc_li)
        toc_widget = f"""        <div class="sidebar-widget" style="background: var(--bg-secondary); border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem; border: 1px solid var(--border-color);">
          <h3 style="margin: 0 0 1rem 0; font-size: 1.05rem; font-weight: 700; color: var(--text-primary);">Table of Contents</h3>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.88rem; line-height: 1.8;">
{toc_items_html}
          </ul>
        </div>"""

    # 2. Specs / Fast Facts
    specs_tr = []
    for label, val in specs_rows:
        specs_tr.append(f"""            <tr>
              <td style="padding: 0.4rem 0; color: var(--text-muted);">{label}:</td>
              <td style="padding: 0.4rem 0; font-weight: 600; text-align: right;">{val}</td>
            </tr>""")
    specs_tr_html = "\n".join(specs_tr)
    specs_widget = f"""        <div class="sidebar-widget" style="background: var(--bg-secondary); border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem; border: 1px solid var(--border-color);">
          <h3 style="margin: 0 0 1rem 0; font-size: 1.05rem; font-weight: 700; color: var(--text-primary);">{specs_title}</h3>
          <table style="width: 100%; font-size: 0.88rem; border-collapse: collapse;">
{specs_tr_html}
          </table>
        </div>"""

    # 3. Related Guides / Links
    links_li = []
    for text, url in related_links:
        links_li.append(f'            <li><a href="{url}" style="color: var(--accent); font-weight: 600;">&rarr; {text}</a></li>')
    links_li_html = "\n".join(links_li)
    related_widget = f"""        <div class="sidebar-widget" style="background: var(--bg-secondary); border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem; border: 1px solid var(--border-color);">
          <h3 style="margin: 0 0 1rem 0; font-size: 1.05rem; font-weight: 700; color: var(--text-primary);">{related_title}</h3>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.9rem; line-height: 1.8;">
{links_li_html}
          </ul>
        </div>"""

    # 4. Editorial Verification
    verification_widget = f"""        <div class="sidebar-widget" style="background: var(--bg-secondary); border-radius: 8px; padding: 1.25rem; border: 1px solid var(--border-color);">
          <h4 style="margin: 0 0 0.5rem 0; font-size: 0.95rem; font-weight: 700; color: var(--text-primary);">Editorial Verification</h4>
          <p style="margin: 0; font-size: 0.82rem; color: var(--text-muted); line-height: 1.5;">
            Verified and maintained by <strong>Vikas Behl</strong> and the RouterIPHub Technical Testing Lab. Tested on {verification_entity} under controlled lab conditions.
          </p>
        </div>"""

    return f"""      <!-- Sticky Responsive Sidebar -->
      <aside class="sidebar" style="position: sticky; top: 2rem;">
{toc_widget}

{specs_widget}

{related_widget}

{verification_widget}
      </aside>"""

def wrap_content_with_sidebar(body_html, specs_title, specs_rows, related_title, related_links, verification_entity):
    """
    Takes body_html (which may or may not be wrapped in <main ...> <div class="content-container"> ... </div> </main>),
    extracts the inner content, injects heading IDs for TOC, builds the sidebar, and returns
    a responsive 2-column layout.
    """
    inner = body_html.strip()

    # Guard: if page already has the standardized sidebar (<aside class="sidebar"), return untouched
    if '<aside class="sidebar"' in inner:
        return body_html

    # If it has an old partial sidebar-column, strip it
    inner = re.sub(r'<aside\s+class=["\']sidebar-column["\'][^>]*>.*?</aside>', '', inner, flags=re.DOTALL | re.IGNORECASE)

    # Strip outermost <main...> and </main> if present
    m_match = re.search(r'^\s*<main[^>]*>(.*)</main>\s*$', inner, flags=re.DOTALL | re.IGNORECASE)
    if m_match:
        inner = m_match.group(1).strip()

    # Strip wrapping <div class="content-layout"> and <article ...> if present
    art_match = re.search(r'^\s*<div\s+class=["\']content-layout["\'][^>]*>\s*<article\s+class=["\'](?:main-content|article-content)["\'][^>]*>(.*)</article>\s*(?:</div>)?\s*$', inner, flags=re.DOTALL | re.IGNORECASE)
    if art_match:
        inner = art_match.group(1).strip()

    # Strip <div class="content-container"> and trailing </div> if present
    c_match = re.search(r'^\s*<div\s+class=["\']content-container["\'][^>]*>(.*)</div>\s*$', inner, flags=re.DOTALL | re.IGNORECASE)
    if c_match:
        inner = c_match.group(1).strip()

    # Inject heading IDs for all h2
    body_with_ids, toc_items = inject_heading_ids(inner)

    sidebar = build_standard_post_sidebar(toc_items, specs_title, specs_rows, related_title, related_links, verification_entity)

    return f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-layout" style="display: grid; grid-template-columns: 1fr 340px; gap: 2.5rem; align-items: start;">
      <article class="article-content" style="min-width: 0;">
{body_with_ids}
      </article>

{sidebar}
    </div>
  </main>
"""

def wrap_extender_content(content_html, ext, all_extenders=None):
    """
    Helper to wrap an Extender guide page with the standardized 4-widget sidebar.
    """
    brand = ext.get("brand", "Universal")
    domain = ext.get("domain", "")
    fb_ip = ext.get("fallback_ip", "192.168.1.250")
    user = ext.get("default_user", "admin")
    password = ext.get("default_pass", "password")
    series_raw = ext.get("series", "Range Extender")
    series = series_raw.split("(")[0].strip() if "(" in series_raw else series_raw[:25]

    specs_rows = [
        ("Brand:", brand),
        ("Local Domain:", domain),
        ("Fallback IP:", fb_ip),
        ("Default Admin:", user),
        ("Default Password:", password),
        ("Hardware Series:", series)
    ]

    related_links = [
        ("All Wi-Fi Extenders", "/extenders/"),
        (f"{fb_ip} Login Guide", f"/ip/{fb_ip.replace('.', '-')}/"),
        ("Detect Gateway IP", "/tools/detect-gateway/"),
        ("Subnet Calculator", "/tools/subnet-calculator/"),
    ]
    if all_extenders:
        for other in all_extenders:
            if other.get("slug") != ext.get("slug") and len(related_links) < 6:
                related_links.append((f"{other.get('domain')} Setup", f"/extenders/{other.get('slug')}/"))

    return wrap_content_with_sidebar(
        content_html,
        specs_title="Extender Specs",
        specs_rows=specs_rows,
        related_title=f"Related {brand} Guides",
        related_links=related_links,
        verification_entity=f"{brand} {domain} hardware"
    )

def wrap_tool_content(content_html, tool, all_tools=None):
    """
    Helper to wrap a Tool page with the standardized 4-widget sidebar.
    """
    title = tool.get("short_title", tool.get("title", "Tool"))
    specs_rows = [
        ("Utility Name:", title),
        ("Execution:", "Browser-Side (Offline)"),
        ("Privacy:", "Zero-Log / Client-Side"),
        ("Platform:", "Desktop, Tablet, Mobile"),
        ("Pricing:", "100% Free / Open Utility")
    ]

    related_links = [
        ("All Networking Tools", "/tools/"),
    ]
    if all_tools:
        for other in all_tools:
            if other.get("slug") != tool.get("slug") and len(related_links) < 5:
                related_links.append((other.get("short_title", other.get("title")), f"/tools/{other.get('slug')}/"))
    else:
        related_links.extend([
            ("Detect Router Gateway", "/tools/detect-gateway/"),
            ("IPv4 Subnet Calculator", "/tools/subnet-calculator/"),
            ("Wi-Fi QR Code Generator", "/tools/wifi-qr-code/")
        ])

    return wrap_content_with_sidebar(
        content_html,
        specs_title="Tool Fast Facts",
        specs_rows=specs_rows,
        related_title="Related Networking Tools",
        related_links=related_links,
        verification_entity=f"cross-browser {title} client environments"
    )

def wrap_isp_content(content_html, isp, all_isps=None):
    """
    Helper to wrap an ISP Gateway page with the standardized 4-widget sidebar.
    """
    isp_name = isp.get("isp_name", "")
    gw_name = isp.get("gateway_name", "")
    short_gw = gw_name.split("(")[0].strip() if "(" in gw_name else gw_name[:30]
    default_ip = isp.get("default_ip", "192.168.1.1")
    web_addr = isp.get("web_address", f"http://{default_ip}").replace("http://", "").replace("https://", "").strip("/")
    user = isp.get("default_username", "admin")
    pwd = isp.get("default_password", "password")

    specs_rows = [
        ("Provider:", isp_name),
        ("Gateway Model:", short_gw),
        ("Default Gateway:", web_addr),
        ("Default IP:", default_ip),
        ("Default Admin:", user),
        ("Default Password:", pwd)
    ]

    related_links = [
        ("All ISP Gateway Guides", "/isp/"),
        (f"{default_ip} Gateway Guide", f"/ip/{default_ip.replace('.', '-')}/"),
        ("Detect My Gateway IP", "/tools/detect-gateway/"),
        ("Subnet Calculator", "/tools/subnet-calculator/")
    ]
    if all_isps:
        for other in all_isps:
            if other.get("slug") != isp.get("slug") and len(related_links) < 6:
                related_links.append((f"{other.get('isp_name')} Login", f"/isp/{other.get('slug')}/"))

    return wrap_content_with_sidebar(
        content_html,
        specs_title="Gateway Specs",
        specs_rows=specs_rows,
        related_title="Related ISP Guides",
        related_links=related_links,
        verification_entity=f"{isp_name} {short_gw} hardware"
    )

def wrap_router_content(content_html, m, all_models=None):
    """
    Helper to wrap a Router page with the standardized 4-widget sidebar.
    """
    brand = m.get("brand", "Router")
    model = m.get("model_name", "")
    clean_name = smart_model_name(brand, model)
    wifi = m.get("wifi_standard", "Wi-Fi")
    speed = m.get("max_speed", m.get("hardware_type", "Gigabit"))
    web_domain = m.get("web_domain", "routerlogin.net")
    default_ip = m.get("default_ip", "192.168.1.1")
    fb_ip = m.get("fallback_ip", "192.168.0.1")
    user = m.get("default_username", "admin")

    specs_rows = [
        ("Model:", f"{model}"),
        ("Wi-Fi Standard:", wifi),
        ("Max Speed:", speed),
        ("Default Gateway:", web_domain),
        ("Default IP:", default_ip),
        ("Default Admin:", user)
    ]

    brand_slug = m.get("brand_slug", brand.lower())
    related_links = [
        (f"All {brand} Routers", f"/brands/{brand_slug}/"),
        (f"{default_ip} Login Guide", f"/ip/{default_ip.replace('.', '-')}/"),
    ]
    if fb_ip and fb_ip != default_ip:
        related_links.append((f"{fb_ip} Fallback Guide", f"/ip/{fb_ip.replace('.', '-')}/"))
    related_links.append(("Detect Gateway IP", "/tools/detect-gateway/"))
    related_links.append(("Wi-Fi Extender Setup", "/extenders/"))

    return wrap_content_with_sidebar(
        content_html,
        specs_title="Router Specs",
        specs_rows=specs_rows,
        related_title=f"Related {brand} Guides",
        related_links=related_links,
        verification_entity=f"{clean_name} hardware"
    )

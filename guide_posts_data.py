# -*- coding: utf-8 -*-
"""
Structured Guide / Blog Posts Catalog for /howto/ Index & Individual /howto/<slug>/ Pages
"""

ACCESS_SETTINGS_BODY = """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        To access your router&rsquo;s settings page, connect to your home Wi-Fi network, open a browser, and enter your router&rsquo;s management IP address&mdash;commonly <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a> or <a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a>. Then sign in with the administrator credentials for that specific router.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.75;">
        The settings page is usually called the router admin panel, web management page, or gateway interface. It lets you manage Wi-Fi names, passwords, connected devices, security settings, and other router functions.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/access-router-settings-page-steps.webp" width="1200" height="675" fetchpriority="high" alt="Three-step diagram to access your router settings page: connect over Wi-Fi or Ethernet, enter 192.168.1.1 or 192.168.0.1 in browser address bar, and sign in to the router admin panel">
        <figcaption>Standard workflow to open any router admin dashboard: connect locally, type the gateway IP into the address bar, and log in.</figcaption>
      </figure>

      <h2>Quick Answer</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Step</th>
              <th>What to do</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1</strong></td>
              <td>Connect your phone or computer to the router&rsquo;s Wi-Fi network, or use an Ethernet cable</td>
            </tr>
            <tr>
              <td><strong>2</strong></td>
              <td>Open a browser such as Chrome, Firefox, Edge, or Safari</td>
            </tr>
            <tr>
              <td><strong>3</strong></td>
              <td>Enter the router&rsquo;s management address in the browser&rsquo;s address bar</td>
            </tr>
            <tr>
              <td><strong>4</strong></td>
              <td>Sign in with the router&rsquo;s administrator username and password</td>
            </tr>
            <tr>
              <td><strong>5</strong></td>
              <td>Open the settings section you need</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Common router management addresses include <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a>, <a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a>, and <a href="/ip/10-0-0-1/"><code>10.0.0.1</code></a>. The correct address depends on the router brand, model, and network configuration.
      </p>

      <h2>Find Your Router&rsquo;s Management Address</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Try these addresses first, one at a time:
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Router type</th>
              <th>Common management address</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand"><a href="/brands/tp-link/">TP-Link standard router</a></td>
              <td><a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a> or <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand">TP-Link DSL modem router</td>
              <td><a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/brands/linksys/">Linksys</a>, <a href="/brands/asus/">ASUS</a>, and many other routers</td>
              <td><a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/isp/xfinity-xfi/">Xfinity gateway</a></td>
              <td><a href="/ip/10-0-0-1/"><code>10.0.0.1</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/isp/att-bgw320/">AT&amp;T gateway</a></td>
              <td><a href="/ip/192-168-1-254/"><code>192.168.1.254</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand">Router with a custom address</td>
              <td>Check the router label or your network&rsquo;s <a href="/find-router-ip/">gateway address</a></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        For TP-Link routers, <code>tplinkwifi.net</code> or <code>192.168.0.1</code> are commonly used. TP-Link DSL modem routers may use <code>tplinkmodem.net</code> or <code>192.168.1.1</code>.
      </p>

      <h2>Check the Router Label</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Turn the router over or look at its back panel. The label often lists:
      </p>
      <ul>
        <li>The router&rsquo;s default management IP address.</li>
        <li>The default administrator username.</li>
        <li>The default administrator password.</li>
        <li>The Wi-Fi network name.</li>
        <li>The Wi-Fi password.</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use the administrator credentials&mdash;not the Wi-Fi password&mdash;when the settings page asks for a router login. Some newer routers require you to create an administrator password during first-time setup instead of using a default one.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/router-bottom-label-admin-ip-password.webp" width="1200" height="675" loading="lazy" alt="Diagram of a router underside sticker label highlighting the difference between Router Admin Login fields (Default IP, Username, Admin Password) and the Wi-Fi Key">
        <figcaption>How to distinguish your Router Admin Login (Default IP, Username, Admin Password) from your wireless Wi-Fi Key on a router sticker.</figcaption>
      </figure>

      <h2>Step-by-Step: Open Router Settings</h2>

      <h3>1. Connect to the router</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Connect your device to the router&rsquo;s Wi-Fi network. For more reliable access, use an Ethernet cable between your computer and one of the router&rsquo;s LAN ports.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not rely on mobile data. The settings page is a local interface, so your device must be connected to the router&rsquo;s network.
      </p>

      <h3>2. Open a browser</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use Chrome, Firefox, Edge, or Safari. Open a new tab and find the address bar at the top of the browser window.
      </p>

      <h3>3. Enter the management address</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Type the address directly into the browser&rsquo;s address bar and press Enter. Common examples:
      </p>
      <ul>
        <li><code>http://192.168.1.1</code></li>
        <li><code>http://192.168.0.1</code></li>
        <li><code>http://10.0.0.1</code></li>
        <li><code>http://192.168.1.254</code></li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not enter the address into a search engine. A search result page is not the router&rsquo;s settings page.
      </p>

      <h3>4. Sign in</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Enter the administrator username and password:
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Login situation</th>
              <th>What to use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Router label lists a default username and password</td>
              <td>Use those exact details</td>
            </tr>
            <tr>
              <td>You created a password during setup</td>
              <td>Use your custom administrator password</td>
            </tr>
            <tr>
              <td>The page asks you to create a password</td>
              <td>Create and save a strong new password</td>
            </tr>
            <tr>
              <td>The page asks for Wi-Fi credentials</td>
              <td>You may be on the wrong login page or entering the wrong password</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Some older routers use <code>admin</code> as both the default username and password. Other brands and models use different credentials, so check the label or search our <a href="/routers/">router model directory</a> before trying generic passwords.
      </p>

      <h3>5. Open the setting you need</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        After signing in, look for menus such as:
      </p>
      <ul>
        <li>Wireless or Wi-Fi</li>
        <li>LAN</li>
        <li>WAN or Internet</li>
        <li>Security</li>
        <li>Administration</li>
        <li>Connected Devices</li>
        <li>Parental Controls</li>
        <li>Port Forwarding</li>
        <li>Firmware Update</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Menu names vary by brand and model. Do not change settings you do not recognize.
      </p>

      <h2>Find the Router IP If Common Addresses Fail</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If <code>192.168.1.1</code> and <code>192.168.0.1</code> do not open your settings page, find your network&rsquo;s gateway address (or try our <a href="/tools/detect-gateway/">Gateway Auto-Detector tool</a>).
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Windows</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Network &amp; Internet</strong>.</li>
            <li>Open your active Wi-Fi or Ethernet connection.</li>
            <li>Find the <strong>Default gateway</strong> or <strong>IPv4 Default Gateway</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Mac</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>System Settings</strong>.</li>
            <li>Go to <strong>Wi-Fi</strong> or <strong>Network</strong>.</li>
            <li>Open the details for your active connection.</li>
            <li>Find <strong>Router</strong> or <strong>Gateway</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Android</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Network &amp; internet</strong> or <strong>Connections</strong>.</li>
            <li>Open <strong>Wi-Fi</strong>.</li>
            <li>Tap your connected network.</li>
            <li>Look for <strong>Gateway</strong> or <strong>Router</strong>.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On iPhone or iPad</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Wi-Fi</strong>.</li>
            <li>Tap the information icon next to your connected network.</li>
            <li>Find <strong>Router</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The gateway address is the address to use for the router&rsquo;s local management interface. For terminal commands across every operating system, read our complete <a href="/find-router-ip/">Router IP Discovery Guide</a>.
      </p>

      <h2>If the Settings Page Will Not Open</h2>

      <h3>1. Confirm the connection</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Make sure your device is connected to the correct router. If you have a modem, mesh system, extender, or separate router, you may be reaching a different device.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use a direct Ethernet connection to the router when possible. This removes Wi-Fi signal problems from the troubleshooting process.
      </p>

      <h3>2. Check the address</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Enter the IP address exactly. Do not add <code>.com</code> to an IP address.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1rem 0 1.5rem 0;">
        <div style="background: var(--success-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--success-text); margin-bottom: 0.4rem;">Correct examples</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>http://192.168.1.1</code></li>
            <li><code>http://192.168.0.1</code></li>
          </ul>
        </div>
        <div style="background: var(--warning-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--warning-text); margin-bottom: 0.4rem;">Incorrect examples</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>192.168.l.1</code> (lowercase letter l)</li>
            <li><code>192.168.1.l</code></li>
            <li><code>192.168.1.1.com</code></li>
            <li><code>192.168.1.1 router login</code></li>
          </ul>
        </div>
      </div>

      <h3>3. Try another common address</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If one address does not load, try:
      </p>
      <ul>
        <li><code>http://192.168.0.1</code></li>
        <li><code>http://192.168.1.1</code></li>
        <li><code>http://10.0.0.1</code></li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not change router settings at random. Use the address shown on the router label or found through your device&rsquo;s gateway settings.
      </p>

      <h3>4. Disable VPN or proxy temporarily</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A VPN, proxy, or privacy-focused browser setting can interfere with access to a local router address. Temporarily disconnect the VPN and try again.
      </p>

      <h3>5. Restart the router</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Turn the router off, wait about 30 seconds, then turn it back on. Wait for the Wi-Fi and internet lights to stabilize before trying again.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Restarting is different from factory resetting. A restart preserves your settings; a factory reset removes them.
      </p>

      <h2>If the Router Password Is Rejected</h2>

      <h3>Check the correct password field</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The router administrator password is not necessarily the same as the Wi-Fi password. Check the label field labeled Admin Password, Router Password, or Network Settings Password.
      </p>

      <h3>Check whether the password was changed</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you or someone else changed the administrator password, the label&rsquo;s original password will no longer work.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use the password created during setup. If you cannot recover it, follow the recovery procedure for your exact router model.
      </p>

      <h3>Do not reset immediately</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A factory reset can erase custom Wi-Fi names, passwords, parental controls, port-forwarding rules, and other configuration. Record any settings you need before resetting.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use a reset only after checking the exact instructions for your router model. When a reset is genuinely required, see our <a href="/howto/30-second-hard-factory-reset/">30-Second Factory Reset Guide</a>.
      </p>

      <h2>Common Mistakes</h2>
      <ul>
        <li>Using mobile data instead of connecting to the router&rsquo;s network.</li>
        <li>Typing the management address into a search engine.</li>
        <li>Entering the Wi-Fi password as the router administrator password.</li>
        <li>Assuming every router uses <code>192.168.1.1</code>.</li>
        <li>Adding <code>.com</code> to an IP address.</li>
        <li>Factory resetting before checking model-specific recovery instructions.</li>
      </ul>
"""

WHY_192_168_1_1_NOT_WORKING_BODY = """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a> may not work because your device is not connected to the router, your router uses a different management address, or a browser, VPN, proxy, or network setting is blocking the local page. It does not automatically mean your router is broken.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.75;">
        Start by confirming that you are connected to the correct home network. Then check the address, browser settings, and gateway address before considering a router restart or reset.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/why-192-168-1-1-not-working-fixes.webp" width="1200" height="675" fetchpriority="high" alt="Troubleshooting flowchart for 192.168.1.1 not loading: check router Wi-Fi or LAN connection, try 192.168.0.1 or 10.0.0.1, disable VPN, proxy, or private DNS, and check real gateway IP">
        <figcaption>Top four checks when 192.168.1.1 fails to load: verify local Wi-Fi/LAN, test alternate gateway IPs, disable VPN/proxy/private DNS, and inspect your active default gateway.</figcaption>
      </figure>

      <h2>Quick Answer</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Likely cause</th>
              <th>What to check</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Wrong network connection</td>
              <td>Connect to the router&rsquo;s Wi-Fi or use an Ethernet cable</td>
            </tr>
            <tr>
              <td class="cell-brand">Router uses a different address</td>
              <td>Try <a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a>, <a href="/ip/10-0-0-1/"><code>10.0.0.1</code></a>, or your <a href="/find-router-ip/">gateway address</a></td>
            </tr>
            <tr>
              <td class="cell-brand">Browser or DNS issue</td>
              <td>Use another browser or disable VPN, proxy, and private DNS</td>
            </tr>
            <tr>
              <td class="cell-brand">Typing mistake</td>
              <td>Enter <code>192.168.1.1</code> exactly, without <code>.com</code></td>
            </tr>
            <tr>
              <td class="cell-brand">Router is offline or unresponsive</td>
              <td>Restart the router</td>
            </tr>
            <tr>
              <td class="cell-brand">Router has been reset or reassigned</td>
              <td>Find the current gateway address</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        <code>192.168.1.1</code> is a private IP address used by many routers. It is not a public website address, so it must be opened from a device connected to the router&rsquo;s local network.
      </p>

      <h2>First: Confirm You Are on the Right Network</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Connect your phone, tablet, or computer to the Wi-Fi network broadcast by the router you want to manage. For a more reliable test, connect a computer directly to one of the router&rsquo;s LAN ports using Ethernet.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not use mobile data. The router settings page is a local interface, not an internet website.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you have a mesh system, extender, modem, or separate router, you may be connected to a device that does not use <code>192.168.1.1</code>. In that case, use the gateway address of the device you want to manage.
      </p>

      <h2>Check the Address First</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Enter the address directly into your browser&rsquo;s address bar:
      </p>
      <p style="margin-bottom: 1rem;"><code>http://192.168.1.1</code></p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not type it into a search engine. A search result page is not your router&rsquo;s login page.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1rem 0 1.5rem 0;">
        <div style="background: var(--success-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--success-text); margin-bottom: 0.4rem;">Correct entry</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>http://192.168.1.1</code></li>
          </ul>
        </div>
        <div style="background: var(--warning-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--warning-text); margin-bottom: 0.4rem;">Common incorrect entries</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>192.168.l.1</code></li>
            <li><code>192.168.1.l</code></li>
            <li><code>192.168.1.1.com</code></li>
            <li><code>192.168.1.1 router login</code></li>
            <li><code>192.168.1.1/admin</code> when you only need the main login page</li>
          </ul>
        </div>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The lowercase letter <code>l</code> can look similar to the number <code>1</code>, but it will not open the router page. Enter the numbers exactly.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/browser-address-bar-vs-search-bar-192-168-1-1.webp" width="1200" height="675" loading="lazy" alt="Browser UI comparison showing http://192.168.1.1 entered directly in the top address bar instead of typing 192.168.1.1.com into a web search box, with VPN and proxy turned off">
        <figcaption>Type http://192.168.1.1 directly into your browser&rsquo;s address bar (not a search box or .com domain) and temporarily switch VPN and proxy settings off.</figcaption>
      </figure>

      <h2>Try Another Common Router Address</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Many routers use <code>192.168.1.1</code>, but not all do. If it does not load, try these addresses one at a time:
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Address</th>
              <th>Common use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="/ip/192-168-0-1/"><code>http://192.168.0.1</code></a></td>
              <td>Common on <a href="/brands/tp-link/">TP-Link</a>, <a href="/brands/d-link/">D-Link</a>, and some other routers</td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-1-1/"><code>http://192.168.1.1</code></a></td>
              <td>Common on <a href="/brands/linksys/">Linksys</a>, <a href="/brands/asus/">ASUS</a>, <a href="/brands/netgear/">Netgear</a>, and many other routers</td>
            </tr>
            <tr>
              <td><a href="/ip/10-0-0-1/"><code>http://10.0.0.1</code></a></td>
              <td>Common on <a href="/isp/xfinity-xfi/">Xfinity gateways</a> and some other networks</td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-1-254/"><code>http://192.168.1.254</code></a></td>
              <td>Common on <a href="/isp/att-bgw320/">AT&amp;T gateways</a></td>
            </tr>
            <tr>
              <td><code>http://192.168.1.253</code></td>
              <td>Used by some repeaters and <a href="/extenders/">extenders</a></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not assume that every device in your home uses the same address. A repeater, extender, mesh node, or separate router may have its own management address.
      </p>

      <h2>Find Your Router&rsquo;s Real Gateway Address</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If common addresses do not open the settings page, find the gateway address on your connected device (or test locally with our <a href="/tools/detect-gateway/">Gateway Auto-Detector tool</a>).
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Windows</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Network &amp; Internet</strong>.</li>
            <li>Open your active Wi-Fi or Ethernet connection.</li>
            <li>Find <strong>Default gateway</strong> or <strong>IPv4 Default Gateway</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Mac</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>System Settings</strong>.</li>
            <li>Go to <strong>Wi-Fi</strong> or <strong>Network</strong>.</li>
            <li>Open the details for your active connection.</li>
            <li>Find <strong>Router</strong> or <strong>Gateway</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On Android</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Network &amp; internet</strong> or <strong>Connections</strong>.</li>
            <li>Open <strong>Wi-Fi</strong>.</li>
            <li>Tap your connected network.</li>
            <li>Look for <strong>Gateway</strong> or <strong>Router</strong>.</li>
          </ol>
        </div>
        <div class="card" style="padding: 1.25rem; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-md);">
          <h3 style="margin-top: 0; font-size: 1.05rem;">On iPhone or iPad</h3>
          <ol style="margin-bottom: 0; padding-left: 1.25rem;">
            <li>Open <strong>Settings</strong>.</li>
            <li>Go to <strong>Wi-Fi</strong>.</li>
            <li>Tap the information icon next to your connected network.</li>
            <li>Find <strong>Router</strong>.</li>
            <li>Enter that address in your browser.</li>
          </ol>
        </div>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The gateway address is the address your device uses to reach the router. Enter it exactly into the browser&rsquo;s address bar.
      </p>

      <h2>Fix Browser and Network Settings</h2>

      <h3>1. Try another browser</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Open the address in Chrome, Firefox, Edge, or Safari. If it works in another browser, clear the cache and site data in the original browser.
      </p>

      <h3>2. Disable VPN temporarily</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A VPN can route traffic away from your local network and prevent access to <code>192.168.1.1</code>. Disconnect the VPN, then try the address again.
      </p>

      <h3>3. Disable proxy settings</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A proxy can interfere with access to a local router address. Check your device&rsquo;s network settings and turn off any proxy or manual proxy configuration temporarily.
      </p>

      <h3>4. Check private DNS</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        On Android, private DNS can sometimes affect local-address access. Temporarily set Private DNS to <strong>Automatic</strong> or <strong>Off</strong>, then try again.
      </p>

      <h3>5. Disable browser extensions</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Ad blockers, privacy extensions, and security extensions can block local addresses. Open the page in an incognito or private window, or temporarily disable extensions.
      </p>

      <h2>Restart the Router</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If the router page still will not open:
      </p>
      <ol>
        <li>Turn off the router.</li>
        <li>Wait about 30 seconds.</li>
        <li>Turn it back on.</li>
        <li>Wait for the power, Wi-Fi, and internet lights to stabilize.</li>
        <li>Reconnect your device to the router&rsquo;s network.</li>
        <li>Try <code>http://192.168.1.1</code> again.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A restart preserves your router settings. Do not confuse it with a factory reset.
      </p>

      <h2>Check the Router Status Lights</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Light behavior</th>
              <th>What it may mean</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">No power light</td>
              <td>Check the power adapter and outlet</td>
            </tr>
            <tr>
              <td class="cell-brand">Wi-Fi light off</td>
              <td>Wi-Fi may be disabled or the router may need a restart</td>
            </tr>
            <tr>
              <td class="cell-brand">Internet light off</td>
              <td>The router may be connected but not receiving service</td>
            </tr>
            <tr>
              <td class="cell-brand">Lights flashing normally</td>
              <td>The router may be working; check the management address</td>
            </tr>
            <tr>
              <td class="cell-brand">Lights stuck or unusual</td>
              <td>Restart the router and check its manual</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A router can be online without its settings page opening. The issue may be the address, connection, or browser rather than the internet service itself.
      </p>

      <h2>If the Page Opens but Login Fails</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If <code>192.168.1.1</code> opens a login form, the address is working. The problem is now the administrator username or password.
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Login situation</th>
              <th>What to use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Router label lists credentials</td>
              <td>Use the exact default username and password</td>
            </tr>
            <tr>
              <td>You created a password during setup</td>
              <td>Use your custom administrator password</td>
            </tr>
            <tr>
              <td>The page asks you to create a password</td>
              <td>Create and save a strong new password</td>
            </tr>
            <tr>
              <td>The page asks for Wi-Fi credentials</td>
              <td>Check whether you are on the correct login page</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The router administrator password is not necessarily the Wi-Fi password. Check the label field labeled Admin Password, Router Password, or Network Settings Password, or review our <a href="/howto/access-my-router-settings-page/">Router Settings Login Guide</a>.
      </p>

      <h2>When to Factory Reset the Router</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use a factory reset only after confirming the correct address, testing another browser, disabling VPN or proxy settings, and restarting the router. A factory reset can erase:
      </p>
      <ul>
        <li>Custom Wi-Fi names and passwords.</li>
        <li>Administrator passwords.</li>
        <li>Parental-control settings.</li>
        <li>Port-forwarding rules.</li>
        <li>Other custom router configuration.</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Before resetting, record the settings you need to restore. Follow the reset instructions for your exact router model, because reset-button timing and recovery behavior vary (<a href="/howto/30-second-hard-factory-reset/">see factory reset steps</a>).
      </p>

      <h2>Common Mistakes</h2>
      <ul>
        <li>Using mobile data instead of connecting to the router&rsquo;s network.</li>
        <li>Typing <code>192.168.1.1</code> into a search engine.</li>
        <li>Adding <code>.com</code> to an IP address.</li>
        <li>Assuming every router uses <code>192.168.1.1</code>.</li>
        <li>Using the Wi-Fi password as the administrator password.</li>
        <li>Factory resetting before checking the router&rsquo;s exact recovery instructions.</li>
      </ul>
"""

WHY_BT_HUB_BODY = """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        The most common reason is that your device is not connected to the BT Hub&rsquo;s network, or the browser is blocking the Hub&rsquo;s secure HTTPS connection. <a href="/isp/bt-smart-hub/">BT Hub Manager</a> is normally opened at <a href="/ip/192-168-1-254/"><code>192.168.1.254</code></a> or <code>http://bthomehub.home</code>, and changing settings requires the Hub&rsquo;s admin password.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.75;">
        Start with the connection and address before changing any Hub settings. Do not factory reset the Hub until you have ruled out the simpler causes.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/bt-hub-manager-192-168-1-254-access-guide.webp" width="1200" height="675" fetchpriority="high" alt="BT Hub Manager access diagram showing a BT Hub connected to a laptop opening 192.168.1.254 or bthomehub.home alongside the pull-out rear Settings Card listing the Hub Admin Password">
        <figcaption>Connect locally to your BT Hub to reach 192.168.1.254 or bthomehub.home, and locate the Hub Admin Password on the pull-out rear Settings Card.</figcaption>
      </figure>

      <h2>Quick Answer</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Likely cause</th>
              <th>What to do</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Not connected to the BT Hub</td>
              <td>Connect to the Hub&rsquo;s Wi-Fi or use an Ethernet cable</td>
            </tr>
            <tr>
              <td class="cell-brand">Browser shows a security warning</td>
              <td>Continue to the HTTPS Hub Manager page</td>
            </tr>
            <tr>
              <td class="cell-brand">VPN or proxy is active</td>
              <td>Disconnect the VPN and disable proxy settings</td>
            </tr>
            <tr>
              <td class="cell-brand">Wrong address entered</td>
              <td>Use <a href="/ip/192-168-1-254/"><code>192.168.1.254</code></a> or <code>bthomehub.home</code></td>
            </tr>
            <tr>
              <td class="cell-brand">Admin password rejected</td>
              <td>Use the current admin password, not the Wi-Fi password</td>
            </tr>
            <tr>
              <td class="cell-brand">Hub is unresponsive</td>
              <td>Restart the Hub</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        BT Hub Manager is a local management page. It must be opened from a device connected to the Hub&rsquo;s network, not through mobile data.
      </p>

      <h2>BT Hub Manager Login Details</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Setting</th>
              <th>What to use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Hub Manager address</td>
              <td><a href="/ip/192-168-1-254/"><code>192.168.1.254</code></a></td>
            </tr>
            <tr>
              <td class="cell-brand">Alternative address</td>
              <td><code>http://bthomehub.home</code></td>
            </tr>
            <tr>
              <td class="cell-brand">Secure address</td>
              <td><code>https://192.168.1.254</code></td>
            </tr>
            <tr>
              <td class="cell-brand">Admin password location</td>
              <td>Hub settings card on the back of the Hub</td>
            </tr>
            <tr>
              <td class="cell-brand">Wi-Fi password</td>
              <td>Separate from the Hub admin password</td>
            </tr>
            <tr>
              <td class="cell-brand">Custom admin password</td>
              <td>Use the password you created, if changed</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The Hub admin password is not the same as your wireless password. It is printed on the Hub settings card unless you changed it.
      </p>

      <h2>Step-by-Step: Open BT Hub Manager</h2>

      <h3>1. Connect to the BT Hub</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Connect your phone, tablet, or computer to the BT Hub&rsquo;s Wi-Fi network. For a more reliable test, connect a computer directly to one of the Hub&rsquo;s Ethernet ports.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not use mobile data. Hub Manager is a local management page, so your device must be connected to the Hub&rsquo;s network.
      </p>

      <h3>2. Open the Hub Manager address</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        In a new browser tab, enter <code>192.168.1.254</code>. You can also use <code>http://bthomehub.home</code>. Type the address directly into the browser&rsquo;s address bar, not into a search engine.
      </p>

      <h3>3. Accept the HTTPS security warning</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        BT Hub Manager uses a secure HTTPS connection. Your browser may show a message saying the connection is not private or secure.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        This warning can be normal for a local Hub Manager page because the Hub uses a self-signed certificate. The connection is still encrypted and safe to proceed with when you reached the address yourself and are on your own home network.
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Browser</th>
              <th>What to select</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Chrome</td>
              <td><strong>Advanced</strong> &rarr; <strong>Proceed to 192.168.1.254 (unsafe)</strong></td>
            </tr>
            <tr>
              <td class="cell-brand">Microsoft Edge</td>
              <td><strong>Advanced</strong> &rarr; <strong>Continue to 192.168.1.254 (unsafe)</strong></td>
            </tr>
            <tr>
              <td class="cell-brand">Safari</td>
              <td><strong>Show Details</strong> &rarr; <strong>Visit this website</strong> &rarr; <strong>Visit Website</strong></td>
            </tr>
            <tr>
              <td class="cell-brand">Firefox</td>
              <td><strong>Advanced</strong> &rarr; <strong>Accept the Risk and Continue</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Only proceed if you entered <code>192.168.1.254</code> directly and you are connected to your own home network.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/bt-hub-manager-https-warning-continue.webp" width="1200" height="675" loading="lazy" alt="Diagram explaining the local BT Hub HTTPS security notice for https://192.168.1.254 and how to choose Advanced then Proceed to 192.168.1.254 safely on your home network">
        <figcaption>How to handle the expected self-signed certificate prompt for https://192.168.1.254 across Chrome, Edge, Safari, and Firefox when connected locally.</figcaption>
      </figure>

      <h3>4. Enter the admin password</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        When prompted, enter the Hub admin password:
      </p>
      <ul>
        <li>If you have not changed it, use the password on the Hub settings card on the back of the Hub.</li>
        <li>If you changed it previously, use your current custom admin password.</li>
        <li>Do not use the Wi-Fi password unless it is the same password you deliberately set for Hub Manager.</li>
      </ul>

      <h2>If the Page Will Not Open</h2>

      <h3>1. Confirm the connection</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Make sure you are connected to the correct BT Hub. If you have a mesh system, extender, powerline adapter, or another router, you may be connected to a different network device.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use an Ethernet cable directly to the BT Hub when possible. This removes Wi-Fi signal issues from the troubleshooting process.
      </p>

      <h3>2. Try the alternative address</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If <code>192.168.1.254</code> does not open, try <code>http://bthomehub.home</code>. This is an alternative way to reach Hub Manager.
      </p>

      <h3>3. Check the address carefully</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Enter the address directly in the browser&rsquo;s address bar rather than searching for it.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1rem 0 1.5rem 0;">
        <div style="background: var(--success-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--success-text); margin-bottom: 0.4rem;">Use this address</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>http://192.168.1.254</code></li>
            <li><code>http://bthomehub.home</code></li>
          </ul>
        </div>
        <div style="background: var(--warning-bg); border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
          <div style="font-weight: 700; color: var(--warning-text); margin-bottom: 0.4rem;">Avoid incorrect entries</div>
          <ul style="margin: 0; padding-left: 1.25rem;">
            <li><code>192.168.l.254</code></li>
            <li><code>192.168.1.254.com</code></li>
            <li><code>192.168.1.254 router login</code></li>
            <li><code>192.168.1.254/admin</code> when you only want the main Hub Manager page</li>
          </ul>
        </div>
      </div>

      <h3>4. Disconnect VPN and proxy</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A VPN, proxy, or privacy-focused browser setting can prevent access to a local Hub address. Disconnect the VPN and temporarily disable proxy settings, then try again.
      </p>

      <h3>5. Try another browser or device</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Try Chrome, Firefox, Edge, or Safari. If one browser fails, test the page from another phone, tablet, or computer connected to the same BT Hub.
      </p>

      <h3>6. Restart the Hub</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Turn the Hub off, wait about 30 seconds, then turn it back on. Wait for the lights to stabilize, reconnect your device, and try <code>192.168.1.254</code> again.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A restart preserves your Hub settings. Do not confuse it with a factory reset.
      </p>

      <h2>If the Admin Password Is Rejected</h2>

      <h3>Check the correct password field</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Look for the <strong>admin password</strong>, not the Wi-Fi password. The admin password opens Hub Manager settings; the Wi-Fi password connects devices to the wireless network.
      </p>

      <h3>Check the Hub model</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The location of the default password depends on the Hub version (see our <a href="/isp/bt-smart-hub/">BT Smart Hub Gateway Portal guide</a> for more model notes):
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Hub model</th>
              <th>Default admin password location</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">BT Smart Hub 2</td>
              <td>Hub settings card on the back</td>
            </tr>
            <tr>
              <td class="cell-brand">BT Smart Hub</td>
              <td>Hub settings card on the back</td>
            </tr>
            <tr>
              <td class="cell-brand">BT Home Hub 4 or Hub 5</td>
              <td>Hub settings card or label on the base</td>
            </tr>
            <tr>
              <td class="cell-brand">BT Home Hub 3</td>
              <td>Hub settings card or label on the base</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Consider whether the password was changed</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you previously changed the admin password, the original password on the settings card will no longer work. Use the current password instead.
      </p>

      <h3>Use the password-reset option if available</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you cannot remember the changed admin password, check the password-reset guidance for your Hub model. Do not reset the Hub until you understand what settings may be lost.
      </p>

      <h2>Why You May Reach a Different Router Page</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you have another router, mesh system, or extender, your device may be connected to a network that uses a different gateway address. In that case, <code>192.168.1.254</code> may not be the address of the device you are trying to manage. Check your device&rsquo;s <a href="/find-router-ip/">gateway address</a> and use that instead. A Hub Manager page should only be reached from within your local home network.
      </p>

      <h2>When to Factory Reset the BT Hub</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not factory reset the Hub as the first fix. Before resetting:
      </p>
      <ul>
        <li>Confirm you are connected to the BT Hub.</li>
        <li>Try <code>192.168.1.254</code> and <code>bthomehub.home</code>.</li>
        <li>Disable VPN and proxy settings.</li>
        <li>Try another browser or device.</li>
        <li>Restart the Hub.</li>
        <li>Check the correct admin password.</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A factory reset can remove custom Hub settings, including Wi-Fi names, passwords, and other configuration. Record anything you need before resetting, and follow the reset instructions for your exact Hub model (<a href="/howto/30-second-hard-factory-reset/">review safe reset practices</a>).
      </p>

      <h2>Common Mistakes</h2>
      <ul>
        <li>Using mobile data instead of connecting to the BT Hub.</li>
        <li>Assuming the Wi-Fi password is the Hub admin password.</li>
        <li>Closing the browser when the HTTPS warning appears without checking that it is the local Hub page.</li>
        <li>Trying <code>192.168.1.1</code> when the BT Hub uses <code>192.168.1.254</code>.</li>
        <li>Leaving a VPN or proxy enabled.</li>
        <li>Factory resetting before trying the simpler access fixes.</li>
      </ul>
"""

TENDA_WIFI_PASSWORD_BODY = """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        You generally cannot change a Tenda Wi-Fi password without either signing in with the current administrator password or resetting the router to factory settings. If you do not know the previous password, use the Tenda WiFi app&rsquo;s password-recovery option first; if that is unavailable, a factory reset is the reliable fallback.
      </p>
      <div class="callout callout-warning" style="background: var(--warning-bg); border: 1px solid var(--border-color); border-left: 4px solid #d97706; border-radius: var(--radius-md); padding: 1rem 1.25rem; margin: 1.25rem 0;">
        <p style="margin: 0; color: var(--text-secondary); line-height: 1.65;">
          A factory reset removes custom settings, including your Wi-Fi name, Wi-Fi password, and router administrator password. Record any settings you need before proceeding.
        </p>
      </div>

      <figure class="guide-figure">
        <img src="/images/howto/change-tenda-wifi-password-without-previous-password.webp" width="1200" height="675" fetchpriority="high" alt="Diagram showing three ways to change a Tenda WiFi password without the old password: Tenda WiFi app recovery, 192.168.0.1 web login password recovery, and holding the rear reset button for 8 to 10 seconds">
        <figcaption>Three ways to recover access and change your Tenda Wi-Fi password: Tenda WiFi App recovery, the 192.168.0.1 web login Forgot password? link, or an 8&ndash;10 second factory reset.</figcaption>
      </figure>

      <h2>Quick Answer</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Your situation</th>
              <th>Best option</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">You know the router administrator password</td>
              <td>Sign in and change the Wi-Fi password</td>
            </tr>
            <tr>
              <td class="cell-brand">You do not know the admin password but use the Tenda WiFi app</td>
              <td>Use <strong>Forgot password?</strong> in the app or web login</td>
            </tr>
            <tr>
              <td class="cell-brand">You are still connected to the Wi-Fi network</td>
              <td>Try changing the password from the connected device</td>
            </tr>
            <tr>
              <td class="cell-brand">You cannot sign in and recovery fails</td>
              <td>Factory reset the Tenda router</td>
            </tr>
            <tr>
              <td class="cell-brand">You only want to change the Wi-Fi password</td>
              <td>Use <strong>WiFi Settings &rarr; WiFi Name &amp; Password</strong> after signing in</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The normal Wi-Fi password-change process requires signing in to the router&rsquo;s <a href="/howto/access-my-router-settings-page/">management page</a>, opening the Wi-Fi settings, entering a new password, and saving it.
      </p>

      <h2>Before You Start</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Confirm which password you are trying to change:
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Password</th>
              <th>What it controls</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Wi-Fi password</td>
              <td>The password devices use to join your wireless network</td>
            </tr>
            <tr>
              <td class="cell-brand">Router administrator password</td>
              <td>The password used to open Tenda router settings</td>
            </tr>
            <tr>
              <td class="cell-brand">Tenda WiFi app account password</td>
              <td>The password for your Tenda online account</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not assume these are the same. Changing the Wi-Fi password does not automatically change the administrator password, and changing the administrator password does not automatically change the Wi-Fi password.
      </p>

      <h2>Option 1: Use the Tenda WiFi App</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If your router is already added to the Tenda WiFi app, try this first.
      </p>
      <ol>
        <li>Open the <strong>Tenda WiFi</strong> app.</li>
        <li>Tap your router.</li>
        <li>Tap <strong>More Functions</strong>.</li>
        <li>Tap <strong>Management Password</strong>.</li>
        <li>Follow the prompts to verify or reset the password.</li>
        <li>Set a new password and tap <strong>Confirm</strong>.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        On some Tenda Wi-Fi 7 models, the old management password may be the Wi-Fi password. This can let you recover access without knowing the separate administrator password.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you are not signed in to the app, or the router is no longer bound to your account, this method may not work.
      </p>

      <h2>Option 2: Use Forgot Password in the Web Login</h2>
      <ol>
        <li>Connect your phone or computer to the Tenda router.</li>
        <li>Open a browser.</li>
        <li>Enter <code>http://tendawifi.com</code> or <a href="/ip/192-168-0-1/"><code>http://192.168.0.1</code></a>.</li>
        <li>On the login screen, select <strong>Forgot password?</strong></li>
        <li>Follow the on-screen verification or reset instructions.</li>
        <li>Set a new administrator password.</li>
        <li>Sign in and change the Wi-Fi password.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The <strong>Forgot password?</strong> option is intended for users who previously set a router login password but cannot remember it.
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/tenda-wifi-app-management-password-recovery.webp" width="1200" height="675" loading="lazy" alt="Side-by-side comparison of Tenda password recovery via the Tenda WiFi mobile app More Functions Management Password menu and the tendawifi.com or 192.168.0.1 router login page Forgot password link">
        <figcaption>Password recovery options before resetting: Tenda WiFi app (More Functions &rarr; Management Password) and the browser login screen&rsquo;s Forgot password? prompt.</figcaption>
      </figure>

      <h2>Option 3: Change the Wi-Fi Password While Connected</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If your phone or computer is still connected to the Tenda Wi-Fi network, try signing in and changing the password directly.
      </p>
      <ol>
        <li>Connect to the Tenda Wi-Fi network.</li>
        <li>Open a browser.</li>
        <li>Enter <code>http://tendawifi.com</code> or <a href="/ip/192-168-0-1/"><code>http://192.168.0.1</code></a>.</li>
        <li>Sign in with the administrator password.</li>
        <li>Open <strong>WiFi Settings</strong>.</li>
        <li>Select <strong>WiFi Name &amp; Password</strong>.</li>
        <li>Enter the new Wi-Fi password.</li>
        <li>Tap <strong>Save</strong>.</li>
        <li>Reconnect your devices using the new password.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Changing the Wi-Fi password disconnects currently connected wireless devices. They must reconnect using the new password.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If the router asks for the previous administrator password and you do not know it, this method will not work. Move to the recovery or reset option.
      </p>

      <h2>Option 4: Factory Reset the Tenda Router</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use this only if you cannot recover the administrator password and no longer have access to the router settings.
      </p>

      <h3>What a reset changes</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A factory reset restores the Tenda router to its original settings. You may need to set up the router again, including its internet connection, Wi-Fi name, Wi-Fi password, and administrator password.
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Before resetting, check whether you have:
      </p>
      <ul>
        <li>A saved configuration backup.</li>
        <li>The internet-service details required for setup.</li>
        <li>Access to the router&rsquo;s physical reset button.</li>
        <li>The ability to reconnect and configure the router afterward.</li>
      </ul>

      <h3>Reset using the physical button</h3>
      <ol>
        <li>Keep the Tenda router powered on.</li>
        <li>Find the <strong>RST</strong>, <strong>RESET</strong>, or <strong>WPS/RESET</strong> button on the back.</li>
        <li>Press and hold it for about 8 to 10 seconds.</li>
        <li>Release when the indicator light begins flashing quickly.</li>
        <li>Wait for the router to reboot.</li>
        <li>Connect to the router&rsquo;s default Wi-Fi network or use an Ethernet cable.</li>
        <li>Open the management address shown on the router label.</li>
        <li>Follow the first-time setup instructions.</li>
        <li>Create a new Wi-Fi name and password.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Some Tenda models use a WPS/RESET button held for more than 10 seconds. Follow the instructions printed on your router or in its manual (also see our general <a href="/howto/30-second-hard-factory-reset/">router factory reset guide</a>).
      </p>

      <figure class="guide-figure">
        <img src="/images/howto/tenda-router-factory-reset-button-pinhole.webp" width="1200" height="675" loading="lazy" alt="Close-up diagram of the rear panel of a Tenda router showing a straightened paperclip pressing the recessed RST or RESET pinhole button for 8 to 10 seconds">
        <figcaption>Locate the recessed RST / RESET (or WPS/RESET) pinhole on the rear panel while powered on, then hold for 8&ndash;10 seconds until status LEDs flash rapidly.</figcaption>
      </figure>

      <h3>Reset through the web interface</h3>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If you can still sign in to the router:
      </p>
      <ol>
        <li>Open the Tenda web interface.</li>
        <li>Go to <strong>More</strong>.</li>
        <li>Select <strong>System Settings</strong>.</li>
        <li>Open <strong>Backup &amp; Restore</strong>.</li>
        <li>Select <strong>Reset</strong>.</li>
        <li>Confirm the reset and wait for the router to reboot.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        This method is only useful if you already have administrator access.
      </p>

      <h2>Set a New Wi-Fi Password After Reset</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        After the reset and first-time setup:
      </p>
      <ol>
        <li>Connect to the Tenda router.</li>
        <li>Open <code>http://tendawifi.com</code> or the management IP address on the router label.</li>
        <li>Create or enter the new administrator password.</li>
        <li>Open <strong>WiFi Settings</strong>.</li>
        <li>Select <strong>WiFi Name &amp; Password</strong>.</li>
        <li>Enter a strong new Wi-Fi password.</li>
        <li>Save the settings.</li>
        <li>Reconnect your devices.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use a Wi-Fi password of at least eight characters. Prefer WPA2 or WPA3 security if your router offers it.
      </p>

      <h2>Create a Strong New Password</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use a password that is (or generate one locally with our <a href="/tools/router-password-generator/">Router Password Generator</a>):
      </p>
      <ul>
        <li>At least 12 characters long where the router allows it.</li>
        <li>A mix of uppercase letters, lowercase letters, numbers, and symbols.</li>
        <li>Different from your router administrator password.</li>
        <li>Not based on your name, address, phone number, or common words.</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Example format: <code>Blue-Tea-47-Lamp!</code>
      </p>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Do not reuse a password from another account.
      </p>

      <h2>If You Cannot Access the Router at All</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        If the router page will not open after a reset, try:
      </p>
      <ul>
        <li>Connecting by Ethernet cable instead of Wi-Fi.</li>
        <li>Using the management address printed on the router label (or check your device&rsquo;s <a href="/find-router-ip/">active gateway address</a>).</li>
        <li>Trying <a href="/ip/192-168-0-1/"><code>http://192.168.0.1</code></a> if that is the address shown for your model.</li>
        <li>Waiting several minutes for the router to finish rebooting.</li>
        <li>Trying another browser or device.</li>
        <li>Checking that VPN, proxy, or private DNS settings are disabled.</li>
      </ul>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        The management IP address and login details are usually printed on the label on the back of the device. If the IP address or password was changed, use the new values.
      </p>

      <h2>Common Mistakes</h2>
      <ul>
        <li>Confusing the Wi-Fi password with the router administrator password.</li>
        <li>Trying to change the Wi-Fi password without administrator access.</li>
        <li>Assuming the Tenda WiFi app can recover a router that is not bound to your account.</li>
        <li>Resetting the router before checking whether the app&rsquo;s password-recovery option works.</li>
        <li>Forgetting to reconnect devices after changing the Wi-Fi password.</li>
        <li>Using a weak or reused password after resetting the router.</li>
      </ul>
"""

GUIDE_POSTS = [
    {
        "slug": "access-my-router-settings-page",
        "url": "/howto/access-my-router-settings-page/",
        "anchor_id": "access-router-settings",
        "featured": True,
        "badge": "Featured Guide",
        "category": "Login & Access",
        "category_key": "login",
        "meta_title": "How Do I Access My Router Settings Page? — Login & Fixes",
        "meta_desc": "Access your router settings page by connecting to your home network and opening its management address. Find your router IP, sign in, and fix common login issues.",
        "headline": "How Do I Access My Router Settings Page?",
        "short_title": "Access Router Settings Page",
        "excerpt": "Connect to your home Wi-Fi or LAN, enter your router management IP (192.168.1.1, 192.168.0.1, or 10.0.0.1), find credentials on your label, and resolve rejected logins.",
        "date_published": "2026-11-12",
        "date_modified": "2026-11-12",
        "read_time": "6 min read",
        "tags": ["192.168.1.1", "192.168.0.1", "Admin Panel", "Login Fixes"],
        "image": "/images/howto/access-router-settings-page-steps.webp",
        "body_html": ACCESS_SETTINGS_BODY,
        "faqs": [
            (
                "What is the most common router settings-page address?",
                "The most common addresses are 192.168.1.1 and 192.168.0.1. Some routers and gateways use different addresses, such as 10.0.0.1 or 192.168.1.254.",
            ),
            (
                "Do I need internet access to open router settings?",
                "No. You need a connection to the router's local network, not necessarily an active internet connection.",
            ),
            (
                "What username and password should I use?",
                "Check the router label for the default administrator credentials. If you changed the password during setup, use your custom password instead.",
            ),
            (
                "Why can I connect to Wi-Fi but not open the router page?",
                "You may be using the wrong management address, connected to a different device, or using a browser setting that blocks the local address. Confirm the gateway address and try a direct Ethernet connection.",
            ),
            (
                "Can I access router settings from my phone?",
                "Yes. Connect your phone to the router's Wi-Fi network, open a browser, and enter the router's management address in the address bar.",
            ),
            (
                "Is the router settings page safe to use?",
                "Yes, when you access it from your own home network and use a strong, unique administrator password. Avoid changing security settings you do not understand.",
            ),
        ],
        "bottom_line": "Connect to your router&rsquo;s network, enter its management address directly into the browser&rsquo;s address bar, and sign in with the administrator credentials. Start with <code>192.168.1.1</code> or <code>192.168.0.1</code>, then check the router label or your device&rsquo;s gateway address if those do not work.",
    },
    {
        "slug": "why-is-192-168-1-1-not-working",
        "url": "/howto/why-is-192-168-1-1-not-working/",
        "anchor_id": "192-168-1-1-not-working",
        "featured": False,
        "badge": "Troubleshooting",
        "category": "Login & Access",
        "category_key": "login",
        "meta_title": "Why Is 192.168.1.1 Not Working? — Browser Fixes",
        "meta_desc": "If 192.168.1.1 is not working in your browser, check your network connection, router address, browser settings, VPN, and administrator login. Fix it step by step.",
        "headline": "Why Is 192.168.1.1 Not Working in My Browser?",
        "short_title": "192.168.1.1 Not Working",
        "excerpt": "Resolve 192.168.1.1 timeouts and site-unreachable errors by checking your local Wi-Fi or Ethernet link, gateway address, VPN, proxy, private DNS, and router status lights.",
        "date_published": "2026-11-12",
        "date_modified": "2026-11-12",
        "read_time": "6 min read",
        "tags": ["192.168.1.1", "Browser Fixes", "VPN / Proxy", "Gateway"],
        "image": "/images/howto/why-192-168-1-1-not-working-fixes.webp",
        "body_html": WHY_192_168_1_1_NOT_WORKING_BODY,
        "faqs": [
            (
                "Why is 192.168.1.1 not opening?",
                "Your device may not be connected to the router, the router may use a different address, or a VPN, proxy, or browser setting may be blocking access. Start by confirming the connection and gateway address.",
            ),
            (
                "Is 192.168.1.1 the same for every router?",
                "No. Many routers use 192.168.1.1, but others use 192.168.0.1, 10.0.0.1, 192.168.1.254, or another address.",
            ),
            (
                "Can I open 192.168.1.1 without Wi-Fi?",
                "You need a connection to the router's local network. Use Wi-Fi or an Ethernet cable. Mobile data will not open a local router page.",
            ),
            (
                "Why does 192.168.1.1 say “site can’t be reached”?",
                "This usually means the browser cannot reach the local address. Check the network connection, address, VPN, proxy, and gateway address.",
            ),
            (
                "Does 192.168.1.1 require internet?",
                "No. You can open the router settings page from the local network even if the internet service is temporarily unavailable.",
            ),
            (
                "What should I do if the login page opens but my password fails?",
                "Use the administrator password, not the Wi-Fi password. If you changed the password previously, use the current custom password.",
            ),
        ],
        "bottom_line": "If <code>192.168.1.1</code> is not working, first confirm that you are connected to the correct router network. Then enter the address exactly, try another common router address, disable VPN or proxy settings, and use your device&rsquo;s gateway address if needed. Restart the router before considering a factory reset.",
    },
    {
        "slug": "why-cant-i-access-my-bt-hub-manager",
        "url": "/howto/why-cant-i-access-my-bt-hub-manager/",
        "anchor_id": "bt-hub-manager-fixes",
        "featured": False,
        "badge": "ISP Hub Fixes",
        "category": "Login & Access",
        "category_key": "login",
        "meta_title": "Why Can’t I Access BT Hub Manager? — Fixes for 192.168.1.254",
        "meta_desc": "Can’t open BT Hub Manager at 192.168.1.254? Fix connection, HTTPS, VPN, browser, and admin-password issues with simple step-by-step troubleshooting.",
        "headline": "Why Can’t I Access My BT Hub Manager?",
        "short_title": "BT Hub Manager Fixes",
        "excerpt": "Can't open BT Hub Manager at 192.168.1.254 or bthomehub.home? Resolve HTTPS certificate warnings, VPN/proxy blocks, and settings card admin password errors.",
        "date_published": "2026-11-12",
        "date_modified": "2026-11-12",
        "read_time": "6 min read",
        "tags": ["192.168.1.254", "BT Hub Manager", "bthomehub.home", "HTTPS"],
        "image": "/images/howto/bt-hub-manager-192-168-1-254-access-guide.webp",
        "body_html": WHY_BT_HUB_BODY,
        "faqs": [
            (
                "What is the BT Hub Manager address?",
                "The standard address is 192.168.1.254. You can also use http://bthomehub.home.",
            ),
            (
                "Why does my browser say the BT Hub connection is not private?",
                "BT Hub Manager uses a self-signed certificate for its HTTPS connection. This browser warning is normal for a local Hub page, and the connection remains encrypted.",
            ),
            (
                "What is the default BT Hub admin password?",
                "It is printed on the Hub settings card on the back of the Hub, unless you changed it. The location can vary slightly by Hub model.",
            ),
            (
                "Is the BT Hub admin password the same as the Wi-Fi password?",
                "No. The admin password opens Hub Manager settings; the Wi-Fi password connects devices to the wireless network.",
            ),
            (
                "Can I access BT Hub Manager from outside my home?",
                "No. Hub Manager is a local management interface and must be accessed from a device connected to the Hub's network.",
            ),
            (
                "Should I reset my BT Hub if 192.168.1.254 does not work?",
                "Not immediately. First check the connection, try the alternative address, disable VPN or proxy settings, test another browser, and restart the Hub.",
            ),
        ],
        "bottom_line": "Connect to your BT Hub, open <code>192.168.1.254</code> or <code>http://bthomehub.home</code>, and accept the expected HTTPS warning if it appears. Use the Hub admin password&mdash;not the Wi-Fi password&mdash;to make changes. If the page will not open, disconnect VPN or proxy settings and restart the Hub before considering a reset.",
    },
    {
        "slug": "change-tenda-wifi-password-without-previous-password",
        "url": "/howto/change-tenda-wifi-password-without-previous-password/",
        "anchor_id": "tenda-wifi-password-reset",
        "featured": False,
        "badge": "Tenda Recovery",
        "category": "Wi-Fi & Mesh",
        "category_key": "wifi",
        "meta_title": "Change Tenda WiFi Password — Reset Without Old Password",
        "meta_desc": "Can’t change your Tenda WiFi password without the old password? Recover access, reset the router safely, and set a new Wi-Fi password step by step.",
        "headline": "How to Change Password of Tenda WiFi Without Entering the Previous Password",
        "short_title": "Change Tenda WiFi Password",
        "excerpt": "Recover Tenda router access via the Tenda WiFi app or 192.168.0.1 web login, or perform a safe 8–10 second factory reset and set a strong new Wi-Fi password.",
        "date_published": "2026-11-12",
        "date_modified": "2026-11-12",
        "read_time": "7 min read",
        "tags": ["Tenda", "Wi-Fi Password", "192.168.0.1", "Factory Reset"],
        "image": "/images/howto/change-tenda-wifi-password-without-previous-password.webp",
        "body_html": TENDA_WIFI_PASSWORD_BODY,
        "faqs": [
            (
                "Can I change my Tenda Wi-Fi password without the old password?",
                "Not directly through the normal settings page. You need either the current administrator password, access through the Tenda WiFi app’s recovery option, or a factory reset.",
            ),
            (
                "Does resetting a Tenda router delete the Wi-Fi password?",
                "Yes. A factory reset restores default settings, so your previous custom Wi-Fi name and password are removed. You will need to set up the router again.",
            ),
            (
                "What is the default Tenda router login?",
                "Older Tenda routers commonly use admin for both the username and password. Newer models may not use a default username and password in the same way, so check the router label and first-time setup screen.",
            ),
            (
                "What is the Tenda router management address?",
                "Common addresses include http://tendawifi.com and http://192.168.0.1. Some models use a different address, so check the label on the back of the router.",
            ),
            (
                "Will changing the Wi-Fi password disconnect my devices?",
                "Yes. Devices connected to the old Wi-Fi password will disconnect and must reconnect using the new password.",
            ),
            (
                "Can I recover the administrator password through the Tenda WiFi app?",
                "Sometimes. If the router is bound to your Tenda WiFi app account, open the router, go to More Functions, then Management Password, and follow the recovery prompts.",
            ),
        ],
        "bottom_line": "If you do not know the previous Tenda password, first try the Tenda WiFi app&rsquo;s <strong>Management Password</strong> recovery option or the web login&rsquo;s <strong>Forgot password?</strong> link. If neither works, factory reset the router, complete setup again, and create a new strong Wi-Fi password.",
    },
    {
        "slug": "change-wifi-password",
        "url": "/howto/change-wifi-password/",
        "anchor_id": "change-wifi",
        "featured": False,
        "badge": "Wi-Fi Security",
        "category": "Wi-Fi & Mesh",
        "category_key": "wifi",
        "meta_title": "How to Change Your Wi-Fi Name & Password (2026)",
        "meta_desc": "Step-by-step guide to changing your wireless SSID and WPA2/WPA3 Wi-Fi password from your router dashboard without locking yourself out.",
        "headline": "How to Change Your Wi-Fi Name (SSID) & Password",
        "short_title": "Change Wi-Fi Password",
        "excerpt": "Update your wireless SSID and switch encryption cleanly to WPA2-PSK (AES) or WPA3-Personal from your router web interface.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["SSID", "WPA3-Personal", "Wi-Fi Password"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Updating your wireless network credentials prevents unauthorized access, kicks stale devices off your LAN, and strengthens encryption to modern WPA2/WPA3 standards. Before editing wireless keys, make sure you know your router&rsquo;s <a href="/howto/access-my-router-settings-page/">management address and admin login</a>.
      </p>
      <h2>Step-by-Step SSID &amp; Passphrase Update</h2>
      <ol>
        <li><strong>Access your router dashboard:</strong> Connect to your Wi-Fi or wired LAN port, open a browser, and visit your gateway (such as <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a> or <a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a>).</li>
        <li><strong>Log in:</strong> Enter your administrator username and password from our <a href="/">Master Directory</a> or your router&rsquo;s physical label.</li>
        <li><strong>Locate Wireless Settings:</strong> Open menus labeled <strong>Wireless</strong>, <strong>Wi-Fi</strong>, or <strong>WLAN Settings</strong>.</li>
        <li><strong>Update SSID:</strong> Enter your desired wireless network name in the <strong>Network Name (SSID)</strong> field.</li>
        <li><strong>Select Encryption:</strong> Choose <strong>WPA2-PSK (AES)</strong> or <strong>WPA3-Personal</strong>. Avoid legacy WEP or WPA-TKIP modes, which throttle Wi-Fi 6/7 speeds and expose security flaws.</li>
        <li><strong>Enter New Password:</strong> Choose a passphrase of at least 12&ndash;16 random characters using our local <a href="/tools/router-password-generator/">Router Password Generator</a>.</li>
        <li><strong>Save and Reconnect:</strong> Click <strong>Save</strong> or <strong>Apply</strong>. Wireless devices will drop off briefly; reconnect each device with the new passphrase, or print a scan card with the <a href="/tools/wifi-qr-code/">Wi-Fi QR Code Generator</a>.</li>
      </ol>
      <h2>Before &amp; After Changing Credentials</h2>
      <ul>
        <li><strong>Smart Home &amp; IoT Devices:</strong> Cameras, smart plugs, and wireless printers store old Wi-Fi credentials and will require re-pairing unless you retain the previous SSID name and password pattern.</li>
        <li><strong>Dual-Band vs. Smart Connect:</strong> If your router broadcasts separate 2.4 GHz and 5 GHz SSIDs, update passwords on both radio tabs or enable Smart Connect band steering.</li>
        <li><strong>Admin Password vs. Wi-Fi Password:</strong> Changing your wireless key does <em>not</em> update the router&rsquo;s admin dashboard password&mdash;keep those two secrets distinct under <strong>Administration &rsaquo; System</strong>.</li>
      </ul>
""",
        "faqs": [
            (
                "Will changing my Wi-Fi password disconnect all devices?",
                "Yes. As soon as the router applies the updated passphrase, currently connected wireless phones, laptops, and smart TVs must forget or re-enter the new Wi-Fi password.",
            ),
            (
                "Does changing the Wi-Fi password change the router login password?",
                "No. The wireless passphrase protects Wi-Fi connections, while the administrator password protects the router settings page.",
            ),
        ],
        "bottom_line": "Sign in via your local gateway IP (or wired Ethernet if you want zero interruption while applying changes), select WPA2-AES or WPA3-Personal, save a 12+ character passphrase, and generate a QR code for guests.",
    },
    {
        "slug": "30-second-hard-factory-reset",
        "url": "/howto/30-second-hard-factory-reset/",
        "anchor_id": "hard-reset",
        "featured": False,
        "badge": "Recovery",
        "category": "Resets & Recovery",
        "category_key": "recovery",
        "meta_title": "How to Factory Reset a Router (Timing & Recovery) (2026)",
        "meta_desc": "Safely factory reset a wireless router using the pinhole Reset button, restore default login passwords, and avoid losing ISP PPPoE credentials.",
        "headline": "How to Perform a Clean Router Hard Factory Reset",
        "short_title": "Router Factory Reset",
        "excerpt": "Recover locked admin passwords cleanly using model-safe pinhole Reset timing without damaging firmware or wiping needed ISP PPPoE logins unexpectedly.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["Factory Reset", "Lost Password", "Pinhole Reset"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        If you forgot a custom administrator password or misconfigured bridge/firewall rules caused a total lockout, a factory reset returns the hardware to its out-of-the-box configuration so sticker defaults work again.
      </p>
      <h2>Checklist Before Pressing Reset</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        A hard factory reset erases everything stored in NVRAM: custom Wi-Fi SSIDs, guest networks, static DHCP reservations, port forwarding rules, VPN keys, and ISP PPPoE or VLAN 201 authentication details. Before resetting, confirm you are simply locked out due to credentials&mdash;not a wrong gateway IP (<a href="/find-router-ip/">check your gateway IP first</a>).
      </p>
      <h2>Step-by-Step Reset Procedure</h2>
      <ul>
        <li><strong>Locate the Reset Button:</strong> Look for a small recessed pinhole labeled <em>Reset</em> on the rear port panel or bottom chassis sticker.</li>
        <li><strong>Keep Power Connected:</strong> Ensure the router is plugged into wall power and fully booted (usually 90 seconds after power-on).</li>
        <li><strong>Depress with Paperclip:</strong> Insert an unfolded paperclip or SIM ejector pin straight into the hole until you feel the internal micro-switch click.</li>
        <li><strong>Hold for Model-Specific Timing:</strong> Hold the button down continuously for <strong>10 to 15 seconds</strong> (older DD-WRT hardware may require the classic 30-30-30 cycle) until all front status LEDs flash simultaneously or blink amber.</li>
        <li><strong>Release and Wait:</strong> Release the pin without unplugging power. Wait 2 to 3 full minutes for DHCP and Wi-Fi radios to initialize before connecting.</li>
      </ul>
      <h2>What Happens After Reboot?</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        After rebooting, the original factory SSID and passphrase printed on the router&rsquo;s chassis sticker become active again, and you can sign in to its <a href="/howto/access-my-router-settings-page/">default management address</a> using the printed preset username and password. Look up exact button timing on your unit inside our <a href="/routers/">252-model hardware directory</a>.
      </p>
""",
        "faqs": [
            (
                "How long should I hold the router reset button?",
                "Most modern Netgear, TP-Link, ASUS, and ISP gateways reset after holding the recessed button for 10 to 15 seconds while powered on until LEDs flash rapidly.",
            ),
            (
                "Will a factory reset disconnect my internet service?",
                "If your ISP uses automatic DHCP (most cable providers), internet usually resumes after reboot. If your provider requires PPPoE credentials or VLAN tagging (DSL and some fiber services), you must re-enter them after the reset.",
            ),
        ],
        "bottom_line": "Only factory reset after verifying the gateway IP and ruling out a Wi-Fi vs. admin password mix-up; keep power connected, hold Reset 10&ndash;15 seconds until LEDs blink, and wait 2&ndash;3 minutes before signing in with chassis sticker credentials.",
    },
    {
        "slug": "two-routers-access-point-mode",
        "url": "/howto/two-routers-access-point-mode/",
        "anchor_id": "access-point",
        "featured": False,
        "badge": "Network Topology",
        "category": "Wi-Fi & Mesh",
        "category_key": "wifi",
        "meta_title": "Connect Two Routers Together (Access Point Mode) (2026)",
        "meta_desc": "Configure a second wireless router in transparent Access Point (AP) mode to expand Ethernet and Wi-Fi coverage while eliminating Double NAT errors.",
        "headline": "How to Connect Two Routers Together (Access Point Mode)",
        "short_title": "Two Routers AP Mode",
        "excerpt": "Turn any spare wireless router into a wired Access Point via LAN-to-LAN cabling, static IP assignment outside DHCP, and disabled secondary NAT.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "5 min read",
        "tags": ["Access Point", "Double NAT", "LAN-to-LAN"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Plugging a second router&rsquo;s WAN port directly into your main router creates <strong>Double NAT</strong>, causing Strict NAT alerts on Xbox/PlayStation consoles, broken port forwarding, and isolated smart-home devices. Configuring the secondary unit as a transparent Access Point (AP) gives you full Ethernet switch ports and Wi-Fi expansion on one flat subnet.
      </p>
      <h2>Access Point Configuration Steps</h2>
      <ol>
        <li><strong>Configure Secondary Router Standalone:</strong> Before cabling it to your main network, connect a laptop directly to LAN Port 1 on the secondary router.</li>
        <li><strong>Check for Dedicated AP Mode Toggle:</strong> Many ASUS, TP-Link, and Netgear routers offer an <em>Operation Mode &rsaquo; Access Point (AP) Mode</em> toggle that automates steps 3 and 4. If unavailable, continue manually below.</li>
        <li><strong>Change Secondary LAN IP:</strong> Open the secondary router&rsquo;s console and change its LAN IP to a static address in the main router&rsquo;s subnet, outside the active DHCP range. For instance, if Router 1 uses <code>192.168.1.1</code> with DHCP <code>.100&ndash;.254</code>, assign Router 2 to <a href="/ip/192-168-1-2/"><code>192.168.1.2</code></a>.</li>
        <li><strong>Disable DHCP Server:</strong> Inside LAN settings on Router 2, set <strong>DHCP Server</strong> to <strong>Disabled</strong> so only Router 1 hands out IP leases.</li>
        <li><strong>Align Wi-Fi Settings Without Channel Overlap:</strong> Set matching SSID names and WPA2/WPA3 passphrases for smooth roaming, but pick separate non-overlapping 2.4 GHz channels (e.g., Channel 1 on Router 1, Channel 6 or 11 on Router 2).</li>
        <li><strong>Connect via LAN-to-LAN:</strong> Run Cat6 Ethernet from a yellow <strong>LAN port</strong> on Router 1 into a <strong>LAN port</strong> on Router 2. <em>Leave the Internet/WAN port on Router 2 empty</em> unless dedicated AP Mode firmware instructs otherwise.</li>
      </ol>
      <h2>Verifying Zero Double NAT</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Devices connected wirelessly to Router 2 should pull an IP from Router 1&rsquo;s subnet and pass local ping/SMB/AirPlay traffic seamlessly to devices wired into Router 1. You can still reach Router 2&rsquo;s admin UI anytime at its reserved IP (such as <code>http://192.168.1.2</code>). Calculate subnet boundaries safely using our <a href="/tools/subnet-calculator/">CIDR Subnet Calculator</a>.
      </p>
""",
        "faqs": [
            (
                "Which port do I plug the Ethernet cable into on the second router?",
                "In manual Access Point setups, connect a LAN port on Router 1 to a LAN port on Router 2 and leave Router 2's WAN/Internet port empty (unless the router's built-in AP Mode explicitly reassigns WAN to uplink).",
            ),
            (
                "Why must I disable DHCP on the second router?",
                "Two active DHCP servers on the same broadcast domain hand out conflicting IP leases and incorrect default gateway routes, breaking internet access intermittently.",
            ),
        ],
        "bottom_line": "Assign Router 2 a static IP outside Router 1's DHCP pool (like <code>192.168.1.2</code>), turn off Router 2's DHCP server, and link LAN-to-LAN so all rooms share one seamless subnet without Double NAT.",
    },
    {
        "slug": "port-forwarding-gaming-servers",
        "url": "/howto/port-forwarding-gaming-servers/",
        "anchor_id": "port-forwarding",
        "featured": False,
        "badge": "Gaming & NAT",
        "category": "Security & DNS",
        "category_key": "security",
        "meta_title": "How to Configure Router Port Forwarding (2026 Guide)",
        "meta_desc": "Open TCP/UDP ports cleanly for Minecraft, Plex, PlayStation, and VPN servers using DHCP IP reservations and Virtual Server NAT rules.",
        "headline": "How to Configure Port Forwarding for Gaming & Servers",
        "short_title": "Port Forwarding Guide",
        "excerpt": "Reserve a static local IP via DHCP, map external TCP/UDP port ranges safely, and verify whether CGNAT blocks inbound connections.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "5 min read",
        "tags": ["Port Forwarding", "DHCP Reservation", "Gaming NAT"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Port forwarding instructs your router&rsquo;s NAT firewall to route unsolicited inbound connections on specific TCP or UDP ports directly to a local PC, game server, NAS, or camera on your LAN. Without forwarding (or UPnP), friends cannot join self-hosted game lobbies or external remote streams.
      </p>
      <h2>Step-by-Step Port Forwarding Setup</h2>
      <ol>
        <li><strong>Bind a Static LAN IP via DHCP Reservation:</strong> First sign in to your router settings and open <strong>LAN &rsaquo; DHCP Server / Address Reservation</strong>. Pin your server or console&rsquo;s MAC address to a fixed internal IP (for example, <code>192.168.1.150</code>) so the target IP never drifts after a reboot.</li>
        <li><strong>Open the NAT / Virtual Server Menu:</strong> Navigate to <strong>Advanced &rsaquo; NAT Forwarding &rsaquo; Port Forwarding</strong> (labeled <em>Virtual Servers</em> or <em>Apps &amp; Gaming</em> on some brands).</li>
        <li><strong>Add the Rule Parameters:</strong>
          <ul>
            <li><strong>Service Name:</strong> Descriptive label (e.g., <em>Minecraft Java</em> or <em>Plex Remote</em>).</li>
            <li><strong>External / Start&ndash;End Port:</strong> Exact port requested by the application (lookup defaults in our <a href="/tools/port-checker/">Port Directory Tool</a>).</li>
            <li><strong>Internal Port:</strong> Usually matches External Port (e.g., <code>25565</code> or <code>32400</code>).</li>
            <li><strong>Internal / Device IP:</strong> Enter the reserved IP (<code>192.168.1.150</code>).</li>
            <li><strong>Protocol:</strong> Select <strong>TCP</strong>, <strong>UDP</strong>, or <strong>TCP/UDP (Both)</strong> as required.</li>
          </ul>
        </li>
        <li><strong>Save &amp; Allow Host Firewall Traffic:</strong> Save rules inside the router, then verify Windows Defender Firewall or Linux <code>ufw</code> permits inbound connections on that same port.</li>
      </ol>
      <h2>Why Port Forwarding Fails Even With Correct Rules</h2>
      <ul>
        <li><strong>Double NAT Behind an ISP Modem:</strong> If your personal router sits behind an ISP combo gateway, forward ports on <em>both</em> boxes or put the ISP gateway into Bridge / IP Passthrough mode.</li>
        <li><strong>Carrier-Grade NAT (CGNAT):</strong> Cellular 5G ISPs (T-Mobile, Starlink, Starlink/rural fiber) share one public IPv4 across many homes using <code>100.64.0.0/10</code> WAN IPs. Standard IPv4 port forwarding cannot traverse CGNAT without a VPN tunnel (Tailscale/WireGuard) or a static public IP plan. Inspect your WAN IP via our <a href="/tools/ip-address-checker/">IP Checker</a>.</li>
      </ul>
""",
        "faqs": [
            (
                "Should I assign a static IP before forwarding a port?",
                "Yes. If your PC gets a different DHCP IP after restarting, the router will forward traffic to an empty address. Use DHCP Address Reservation inside the router so the local IP stays permanent.",
            ),
            (
                "Why won't my forwarded port work on T-Mobile 5G or Starlink?",
                "Mobile and satellite ISPs commonly use Carrier-Grade NAT (CGNAT), meaning your router does not receive an exclusive public IPv4 address for unsolicited inbound connections.",
            ),
        ],
        "bottom_line": "Reserve a permanent LAN IP via DHCP first, create the matching TCP/UDP Virtual Server rule, allow the port in your computer firewall, and confirm your ISP has not placed your line behind Double NAT or CGNAT.",
    },
    {
        "slug": "change-router-dns",
        "url": "/howto/change-router-dns/",
        "anchor_id": "change-dns",
        "featured": False,
        "badge": "DNS & Privacy",
        "category": "Security & DNS",
        "category_key": "security",
        "meta_title": "How to Change Router DNS Settings (1.1.1.1 / Quad9)",
        "meta_desc": "Switch your router from slow ISP DNS servers to Cloudflare 1.1.1.1, Google 8.8.8.8, Quad9 malware blocking, or AdGuard network-wide filtering.",
        "headline": "How to Change Router DNS for Faster Browsing & Privacy",
        "short_title": "Change Router DNS",
        "excerpt": "Configure Cloudflare 1.1.1.1, Quad9, or AdGuard DNS once at the router WAN/LAN level to accelerate lookups and filter ads across every home device.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["1.1.1.1", "Quad9", "AdGuard DNS", "Privacy"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Default ISP DNS resolvers are often slow under peak load, lack malware filtering, and log queried hostnames. Configuring custom DNS directly on your router pushes faster, cleaner name resolution automatically to every phone, smart TV, and console on your Wi-Fi network.
      </p>
      <h2>Recommended Public DNS Resolvers</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>DNS Provider</th>
              <th>Primary IPv4</th>
              <th>Secondary IPv4</th>
              <th>Key Benefit</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand">Cloudflare</td>
              <td><code>1.1.1.1</code></td>
              <td><code>1.0.0.1</code></td>
              <td>Lowest anycast latency, 24h privacy purge</td>
            </tr>
            <tr>
              <td class="cell-brand">Google Public DNS</td>
              <td><code>8.8.8.8</code></td>
              <td><code>8.8.4.4</code></td>
              <td>Global stability and DNSSEC validation</td>
            </tr>
            <tr>
              <td class="cell-brand">Quad9</td>
              <td><code>9.9.9.9</code></td>
              <td><code>149.112.112.112</code></td>
              <td>Automatic malicious domain &amp; phishing blocking</td>
            </tr>
            <tr>
              <td class="cell-brand">AdGuard DNS</td>
              <td><code>94.140.14.14</code></td>
              <td><code>94.140.15.15</code></td>
              <td>Network-wide ad &amp; tracker domain blocking</td>
            </tr>
          </tbody>
        </table>
      </div>
      <h2>How to Apply Custom DNS on Your Router</h2>
      <ol>
        <li>Open your router settings page and navigate to <strong>Internet</strong>, <strong>WAN</strong>, or <strong>Advanced &rsaquo; Network &rsaquo; DNS</strong>. (Some ISP gateways restrict WAN DNS; check <strong>LAN &rsaquo; DHCP Server</strong> primary DNS instead.)</li>
        <li>Switch DNS selection from <em>Get Automatically from ISP</em> to <strong>Use These DNS Servers</strong> (or <em>Manual</em>).</li>
        <li>Type your chosen Primary DNS (such as <code>1.1.1.1</code>) and Secondary DNS (<code>1.0.0.1</code>). If your router supports <strong>DNS-over-HTTPS (DoH)</strong> or <strong>DNS-over-TLS (DoT)</strong>, enable it to encrypt queries from ISP snooping.</li>
        <li>Save settings and flush OS DNS caches (<code>ipconfig /flushdns</code> on Windows or <code>sudo dscacheutil -flushcache</code> on macOS), or test live record responses using our <a href="/tools/dns-propagation/">DNS Propagation Checker</a>.</li>
      </ol>
""",
        "faqs": [
            (
                "Does changing router DNS affect local devices like 192.168.1.1?",
                "No. Local gateway IPs do not rely on external DNS, though if your router firmware uses custom local hostnames like routerlogin.net or tplinkwifi.net, configure custom DNS under the WAN/Internet tab rather than overriding LAN DHCP DNS if local domain interception occurs.",
            ),
            (
                "Why does my ISP router grey out the DNS settings?",
                "Some carrier-supplied gateways (Xfinity xFi, AT&T BGW320) lock WAN DNS fields; in that case configure DNS inside individual devices or attach your own personal router in Bridge/Passthrough mode.",
            ),
        ],
        "bottom_line": "Set Primary and Secondary DNS under your router's WAN or DHCP Server settings to <code>1.1.1.1</code>/<code>1.0.0.1</code> for speed or <code>9.9.9.9</code> for malware filtering, then flush client caches.",
    },
    {
        "slug": "guest-wifi-network-setup",
        "url": "/howto/guest-wifi-network-setup/",
        "anchor_id": "guest-network",
        "featured": False,
        "badge": "Security",
        "category": "Security & DNS",
        "category_key": "security",
        "meta_title": "How to Set Up a Secure Guest Wi-Fi Network (2026)",
        "meta_desc": "Create an isolated Guest Wi-Fi SSID with AP Client Isolation enabled to protect your NAS, computers, and smart-home devices from untrusted traffic.",
        "headline": "How to Set Up a Secure Guest Wi-Fi Network",
        "short_title": "Guest Wi-Fi Setup",
        "excerpt": "Segment visitors and untrusted IoT gadgets onto an isolated Guest SSID with local-network access blocked so personal laptops and NAS drives stay unreachable.",
        "date_published": "2026-02-15",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["Guest Network", "AP Isolation", "IoT Security"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        A Guest Network broadcasts an isolated wireless SSID that gives visitors outbound internet connectivity while <strong>blocking access to your local subnet</strong>&mdash;shielding shared drives, NAS backups, printers, and router management consoles.
      </p>
      <h2>Configuring Client-Isolated Guest Wi-Fi</h2>
      <ol>
        <li>Open your router&rsquo;s admin interface and select <strong>Guest Network</strong> in the main sidebar or Wireless menu.</li>
        <li>Enable the <strong>2.4 GHz</strong> guest toggle (best compatibility for smart gadgets) and optionally <strong>5 GHz</strong> for visiting phones and laptops.</li>
        <li>Give it an obvious SSID name such as <em>Home_Guest</em> so guests do not ask for your primary password.</li>
        <li>Set a distinct passphrase with <strong>WPA2/WPA3-Personal</strong> and print a scannable sign using our <a href="/tools/wifi-qr-code/">Wi-Fi QR Code Generator</a>.</li>
        <li><strong>Verify Local Isolation Is Locked:</strong> Ensure <em>Allow Guests to Access My Local Network</em> / <em>Access Intranet</em> stays <strong>Disabled (OFF)</strong>, or enable <em>AP Isolation</em>.</li>
      </ol>
      <h2>Bonus: Isolating Smart Home IoT Devices</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Budget Wi-Fi bulbs, smart plugs, robot vacuums, and generic IP cameras rarely receive long-term security patches. Placing those gadgets on a 2.4 GHz Guest SSID (or a dedicated IoT VLAN) keeps them online while preventing lateral network scanning against your primary work computers.
      </p>
""",
        "faqs": [
            (
                "Can guest Wi-Fi users open my router admin page (192.168.1.1)?",
                "When local network / intranet access is disabled on your Guest SSID, routers block wireless guests from reaching both LAN clients and the router's admin dashboard.",
            ),
            (
                "Should smart home devices go on the guest network?",
                "Yes, smart plugs and cameras that only need cloud access benefit from guest isolation, whereas Chromecast, AirPlay, and local Home Assistant integrations usually need same-subnet discovery.",
            ),
        ],
        "bottom_line": "Enable a dedicated Guest SSID with WPA2/WPA3 encryption and leave local intranet access disabled so visitors and budget smart-home gadgets cannot probe your personal devices or router dashboard.",
    },
    {
        "slug": "wifi-7-6ghz-setup-guide",
        "url": "/howto/wifi-7-6ghz-setup-guide/",
        "anchor_id": "wifi7-setup",
        "featured": False,
        "badge": "Next-Gen Wireless",
        "category": "Wi-Fi & Mesh",
        "category_key": "wifi",
        "meta_title": "Wi-Fi 7 (802.11be) & 6 GHz 320 MHz Setup Guide (2026)",
        "meta_desc": "Configure 320 MHz channels, Multi-Link Operation (MLO), and mandatory WPA3 security on Wi-Fi 7 and Wi-Fi 6E routers for maximum multi-gig speeds.",
        "headline": "Wi-Fi 7 (802.11be) & Wi-Fi 6E 6 GHz Configuration Guide",
        "short_title": "Wi-Fi 7 & 6 GHz Setup",
        "excerpt": "Unlock 320 MHz ultra-wide channels, Multi-Link Operation (MLO), and uncongested 6 GHz spectrum while avoiding WPA2 client incompatibility traps.",
        "date_published": "2026-03-01",
        "date_modified": "2026-11-11",
        "read_time": "5 min read",
        "tags": ["Wi-Fi 7", "6 GHz", "320 MHz", "MLO"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Next-generation Wi-Fi 7 (802.11be) and Wi-Fi 6E routers unlock the uncongested <strong>6 GHz radio band</strong>, ultra-wide <strong>320 MHz channel bandwidth</strong>, and <strong>Multi-Link Operation (MLO)</strong> to deliver multi-gigabit wireless throughput and sub-5ms gaming latency.
      </p>

      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 1.25rem; margin: 1.5rem 0; box-shadow: var(--shadow);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
          <span style="font-weight: 700; font-size: 0.9rem; color: var(--text-accent);">GUI Reference: Wi-Fi 7 / 6 GHz Professional Settings</span>
          <span style="font-size: 0.75rem; color: var(--text-muted); font-family: var(--font-mono);">802.11be / 802.11ax</span>
        </div>
        <svg viewBox="0 0 700 240" width="100%" height="auto" role="img" aria-label="Wi-Fi 7 320 MHz and MLO configuration layout diagram" style="border-radius: var(--radius-md); background: var(--bg-primary); border: 1px solid var(--border-color);">
          <rect x="0" y="0" width="700" height="36" fill="var(--bg-secondary)"/>
          <circle cx="20" cy="18" r="5" fill="#ef4444"/>
          <circle cx="36" cy="18" r="5" fill="#f59e0b"/>
          <circle cx="52" cy="18" r="5" fill="#10b981"/>
          <text x="75" y="22" fill="var(--text-secondary)" font-size="12" font-family="sans-serif">Wireless &gt; Professional Settings (6 GHz Band)</text>
          <rect x="25" y="55" width="200" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-color)"/>
          <text x="35" y="77" fill="var(--text-muted)" font-size="12" font-family="sans-serif">Channel Bandwidth:</text>
          <rect x="240" y="55" width="430" height="35" rx="4" fill="var(--bg-card)" stroke="#0284c7"/>
          <text x="255" y="77" fill="var(--text-primary)" font-size="12" font-weight="bold" font-family="monospace">160/320 MHz (Ultra-Wide Channel Active)</text>
          <rect x="25" y="105" width="200" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-color)"/>
          <text x="35" y="127" fill="var(--text-muted)" font-size="12" font-family="sans-serif">Multi-Link Operation (MLO):</text>
          <rect x="240" y="105" width="180" height="35" rx="4" fill="#064e3b" stroke="#059669"/>
          <text x="255" y="127" fill="#34d399" font-size="12" font-weight="bold" font-family="sans-serif">Enabled (2.4G + 5G + 6G)</text>
          <rect x="25" y="155" width="200" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-color)"/>
          <text x="35" y="177" fill="var(--text-muted)" font-size="12" font-family="sans-serif">Authentication Method:</text>
          <rect x="240" y="155" width="430" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-color)"/>
          <text x="255" y="177" fill="var(--text-primary)" font-size="12" font-family="monospace">WPA3-Personal (Mandatory for 6 GHz)</text>
          <text x="25" y="220" fill="var(--text-accent)" font-size="11" font-family="sans-serif">Tip: Wi-Fi 6E/7 enforces WPA3 encryption. Legacy devices supporting only WPA2 cannot join the 6 GHz SSID.</text>
        </svg>
      </div>

      <h2>Essential Wi-Fi 7 Configuration Steps</h2>
      <ol>
        <li><strong>Choose Separate SSID vs. Unified MLO Network:</strong> Wi-Fi 7 MLO aggregates throughput across 5 GHz and 6 GHz simultaneously using a single unified SSID. If older WPA2-only printers or smart bulbs refuse to authenticate under WPA3-Mixed mode, enable MLO only on a modern network or keep a dedicated 2.4 GHz IoT SSID.</li>
        <li><strong>Enable 320 MHz Channel Width:</strong> Inside <em>Wireless &rsaquo; 6 GHz &rsaquo; Channel Bandwidth</em>, select <strong>320 MHz</strong> (doubles peak lane capacity vs. Wi-Fi 6&rsquo;s 160 MHz ceiling).</li>
        <li><strong>Avoid 5 GHz DFS Stalls:</strong> Unlike 5 GHz DFS channels that pause broadcasting when nearby weather radar scans, 6 GHz delivers clean non-overlapping channels without radar interruption.</li>
        <li><strong>Pair With Multi-Gig WAN/LAN:</strong> Connect fiber ONTs or gaming PCs to 2.5G or 10G Ethernet ports so wired uplinks do not bottleneck 6 GHz wireless links.</li>
      </ol>
      <h2>6 GHz Range, Wall Attenuation &amp; AFC Notes</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Because higher-frequency 6 GHz radio waves attenuate faster through drywall, brick, and concrete floors than 2.4 GHz or 5 GHz bands, peak 320 MHz speeds require clear line-of-sight or adjacent-room placement. In supported regions (such as US/Canada FCC Standard Power mode), enabling <strong>Automated Frequency Coordination (AFC)</strong> allows compliant Wi-Fi 7 routers to boost 6 GHz transmit power safely without interfering with licensed microwave links. Check supported router models in our <a href="/routers/">Hardware Model Directory</a>.
      </p>
""",
        "faqs": [
            (
                "Why won't my older laptop see the 6 GHz Wi-Fi SSID?",
                "6 GHz hardware requires a Wi-Fi 6E or Wi-Fi 7 network adapter and mandatory WPA3 security; older Wi-Fi 5/6 devices only see 2.4 GHz and 5 GHz radios.",
            ),
            (
                "Does Multi-Link Operation (MLO) require WPA3?",
                "Yes. Under the 802.11be specification, MLO requires WPA3-Personal (SAE) authentication across participating bands.",
            ),
        ],
        "bottom_line": "Turn on WPA3-Personal authentication, select 320 MHz channel bandwidth on the 6 GHz band, enable MLO for Wi-Fi 7 flagship phones/laptops, and leave older WPA2 smart gadgets on a separate 2.4 GHz SSID.",
    },
    {
        "slug": "mesh-wifi-backhaul-optimization",
        "url": "/howto/mesh-wifi-backhaul-optimization/",
        "anchor_id": "mesh-optimization",
        "featured": False,
        "badge": "Mesh Networking",
        "category": "Wi-Fi & Mesh",
        "category_key": "wifi",
        "meta_title": "Mesh Wi-Fi Backhaul & Node Placement Guide (2026)",
        "meta_desc": "Eliminate mesh Wi-Fi dead zones on TP-Link Deco, Netgear Orbi, and Amazon Eero using wired Ethernet/MoCA backhaul and optimal 30-foot satellite spacing.",
        "headline": "Mesh Wi-Fi Backhaul & Node Placement Optimization",
        "short_title": "Mesh Backhaul Guide",
        "excerpt": "Maximize real-world mesh throughput on Eero, Orbi, Deco, and Velop systems using Cat6/MoCA wired backhaul, mid-point spacing, and 802.11k/v/r fast roaming.",
        "date_published": "2026-03-01",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["Mesh Wi-Fi", "Wired Backhaul", "Orbi / Deco / Eero"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Whole-home mesh systems (TP-Link Deco, Netgear Orbi, Amazon Eero, Linksys Velop) drop speeds dramatically when satellite nodes sit too far from the main unit over congested wireless hops. Tuning node placement and backhaul resolves most dead zones and random video-call drops.
      </p>
      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 1.25rem; margin: 1.5rem 0;">
        <h2 style="font-size: 1.15rem; margin-top: 0; color: var(--text-primary);">Wired Ethernet Backhaul vs. Dedicated Wireless Backhaul</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-top: 1rem;">
          <div style="background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem;">
            <div style="font-weight: 700; color: var(--success-text); margin-bottom: 0.35rem;">Ethernet / MoCA Wired Backhaul</div>
            <p style="font-size: 0.875rem; color: var(--text-secondary); margin: 0; line-height: 1.55;">
              Links satellite nodes back to the primary mesh gateway over Cat6 Ethernet or coaxial MoCA adapters. Frees 100% of wireless radio airtime for your phones and laptops with sub-1ms hop latency.
            </p>
          </div>
          <div style="background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem;">
            <div style="font-weight: 700; color: var(--text-accent); margin-bottom: 0.35rem;">Tri-Band Wireless Backhaul</div>
            <p style="font-size: 0.875rem; color: var(--text-secondary); margin: 0; line-height: 1.55;">
              Tri-band units (Orbi RBK852, Deco XE75) reserve a dedicated 5 GHz or 6 GHz radio solely for node-to-node transport. Always place satellites halfway to the dead zone rather than inside it.
            </p>
          </div>
        </div>
      </div>
      <h2>Three Mesh Placement &amp; Tuning Rules</h2>
      <ol>
        <li><strong>Follow the Halfway Rule:</strong> Place wireless satellites 25&ndash;40 feet (at most 1&ndash;2 drywall partitions) from the primary gateway node so the backhaul link stays strong. Putting a satellite inside a bedroom with one bar only repeats a slow, jittery connection.</li>
        <li><strong>Enable Fast Roaming (802.11k/v/r):</strong> Turn on Fast Roaming and Beamforming inside your Deco/Eero/Orbi app so moving devices hand off cleanly between rooms without sticking to a distant weak node.</li>
        <li><strong>Shut Off ISP Modem Wi-Fi:</strong> When running mesh behind an AT&amp;T, Xfinity, or Verizon ISP box, disable the ISP gateway&rsquo;s built-in Wi-Fi and switch either the modem to Bridge/Passthrough or the mesh system to AP Mode to prevent co-channel interference.</li>
      </ol>
""",
        "faqs": [
            (
                "Where should I place a wireless mesh satellite?",
                "Position each satellite roughly halfway between your primary router and the room needing coverage, where the node still receives a strong green or blue signal from the main unit.",
            ),
            (
                "Can I wire just one mesh node with Ethernet and leave another wireless?",
                "Yes. Most Eero, Deco, and ASUS AiMesh systems support mixed wired and wireless backhaul simultaneously.",
            ),
        ],
        "bottom_line": "Wire mesh satellites with Ethernet or MoCA whenever cables exist; for wireless mesh, place satellites halfway to dead zones, enable 802.11k/v/r roaming, and turn off any leftover ISP router Wi-Fi radios.",
    },
    {
        "slug": "fiber-ont-bridge-mode-setup",
        "url": "/howto/fiber-ont-bridge-mode-setup/",
        "anchor_id": "ont-bridging",
        "featured": False,
        "badge": "ISP & Fiber",
        "category": "Resets & ISP Bridge",
        "category_key": "recovery",
        "meta_title": "Fiber ONT Bridge Mode & IP Passthrough Guide (2026)",
        "meta_desc": "Configure IP Passthrough or Transparent Bridge Mode on AT&T BGW320, Verizon Fios, Xfinity, and CenturyLink Quantum fiber ONTs to eliminate Double NAT.",
        "headline": "Fiber ONT Setup & ISP Gateway Bridge / IP Passthrough Guide",
        "short_title": "Fiber ONT Bridging",
        "excerpt": "Bypass ISP combo gateways cleanly on AT&T Fiber, Verizon Fios, Xfinity, and CenturyLink using IP Passthrough, direct Ethernet ONT handoff, or VLAN 201 tagging.",
        "date_published": "2026-03-01",
        "date_modified": "2026-11-11",
        "read_time": "5 min read",
        "tags": ["IP Passthrough", "Bridge Mode", "Fiber ONT", "Double NAT"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        Optical fiber connections (AT&amp;T Fiber, Verizon Fios, Google Fiber, CenturyLink Quantum) terminate at an <strong>Optical Network Terminal (ONT)</strong> or combo gateway. Using your own ASUS, Netgear, Ubiquiti, or TP-Link router behind a carrier box requires enabling IP Passthrough or Bridge Mode so your personal router gets the public IP directly.
      </p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Fiber / ISP Provider</th>
              <th>Common Hardware</th>
              <th>Console IP</th>
              <th>Recommended Bypass Method</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="cell-brand"><a href="/isp/att-bgw320/">AT&amp;T Fiber</a></td>
              <td>BGW320-500 / BGW210</td>
              <td><a href="/ip/192-168-1-254/"><code>192.168.1.254</code></a></td>
              <td><strong>IP Passthrough (DHCPS-fixed):</strong> Passes public IPv4 cleanly to your router&rsquo;s WAN MAC address.</td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/isp/verizon-cr1000a/">Verizon Fios</a></td>
              <td>CR1000A / G3100</td>
              <td><a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a></td>
              <td><strong>Direct ONT Ethernet:</strong> Internet-only plans can plug Ethernet straight from the Nokia/Calix ONT into your own router.</td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/isp/centurylink-c4000/">CenturyLink / Quantum</a></td>
              <td>C4000XG / C5500XK</td>
              <td><a href="/ip/192-168-0-1/"><code>192.168.0.1</code></a></td>
              <td><strong>Transparent Bridging + VLAN 201:</strong> Requires setting 802.1Q VLAN ID <code>201</code> on your personal router&rsquo;s WAN interface.</td>
            </tr>
            <tr>
              <td class="cell-brand"><a href="/isp/xfinity-xfi/">Xfinity xFi</a></td>
              <td>XB6 / XB7 / XB8</td>
              <td><a href="/ip/10-0-0-1/"><code>10.0.0.1</code></a></td>
              <td><strong>Gateway Bridge Mode:</strong> Toggle under <em>Gateway &rsaquo; At a Glance &rsaquo; Bridge Mode</em> (after enabling Admin Tool in Xfinity App).</td>
            </tr>
          </tbody>
        </table>
      </div>
      <h2>How to Configure AT&amp;T Fiber BGW320 IP Passthrough</h2>
      <ol>
        <li>Open <a href="/ip/192-168-1-254/"><code>http://192.168.1.254</code></a> and navigate to <strong>Firewall &rsaquo; IP Passthrough</strong>.</li>
        <li>Enter the Device Access Code printed on the rear/side label of the BGW320.</li>
        <li>Set <em>Allocation Mode</em> to <strong>Passthrough</strong> and <em>Passthrough Mode</em> to <strong>DHCPS-fixed</strong>.</li>
        <li>Choose your personal router&rsquo;s MAC address from the Passthrough Fixed MAC Address dropdown and click <strong>Save</strong>.</li>
        <li>Navigate to <strong>Home Network &rsaquo; Wi-Fi</strong> and turn off the BGW320 2.4 GHz and 5 GHz radios so they do not compete with your personal router.</li>
        <li>Reboot your personal router; its WAN port should now lease your live public IPv4 address directly.</li>
      </ol>
""",
        "faqs": [
            (
                "What happens if I don't enable Bridge Mode when plugging in my own router?",
                "Both routers perform Network Address Translation (Double NAT), which commonly breaks console multiplayer, self-hosted VPNs, and remote access while causing Wi-Fi channel interference if the ISP Wi-Fi stays enabled.",
            ),
            (
                "Should I turn off Wi-Fi on the ISP gateway after enabling IP Passthrough?",
                "Yes. Disabling the ISP box's built-in 2.4 GHz and 5 GHz radios prevents overlapping wireless interference and ensures devices only connect through your personal router.",
            ),
        ],
        "bottom_line": "To use your own router cleanly behind ISP fiber or cable hardware, enable IP Passthrough or Bridge Mode inside the carrier gateway console and turn off the carrier box's Wi-Fi radios.",
    },
    {
        "slug": "ipv6-default-gateway-discovery",
        "url": "/howto/ipv6-default-gateway-discovery/",
        "anchor_id": "ipv6-gateway",
        "featured": False,
        "badge": "IPv6 Networking",
        "category": "Resets & ISP Bridge",
        "category_key": "recovery",
        "meta_title": "IPv6 Default Gateway Discovery & fe80::1 Guide (2026)",
        "meta_desc": "Understand IPv6 link-local gateway addresses like fe80::1, Neighbor Discovery Router Advertisements, and terminal commands to inspect your IPv6 default route.",
        "headline": "IPv6 Default Gateway Discovery & Link-Local (fe80::1) Guide",
        "short_title": "IPv6 Gateway Discovery",
        "excerpt": "Learn why IPv6 routers show link-local fe80:: addresses instead of 192.168.1.1, and find your active IPv6 default route on Windows, macOS, and Linux.",
        "date_published": "2026-03-01",
        "date_modified": "2026-11-11",
        "read_time": "4 min read",
        "tags": ["IPv6", "fe80::1", "Link-Local", "Terminal"],
        "body_html": """
      <p style="font-size: 1.075rem; color: var(--text-secondary); line-height: 1.75;">
        While IPv4 home routers isolate LAN devices behind private subnets like <a href="/ip/192-168-1-1/"><code>192.168.1.1</code></a>, IPv6 assigns globally routable 128-bit prefixes to client devices and discovers routers dynamically using <strong>Link-Local</strong> addresses and <strong>ICMPv6 Neighbor Discovery</strong>.
      </p>
      <div class="card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 1.25rem; margin: 1.5rem 0;">
        <h2 style="font-size: 1.15rem; margin-top: 0; color: var(--text-primary);">IPv6 Gateway Architecture Highlights</h2>
        <ul style="font-size: 0.925rem; color: var(--text-secondary); line-height: 1.65; margin: 0; padding-left: 1.25rem;">
          <li><strong>Link-Local Prefix (<code>fe80::/10</code>):</strong> Your default IPv6 router gateway is almost always a Link-Local address starting with <code>fe80::</code> (frequently <code>fe80::1</code> or auto-generated from the router&rsquo;s EUI-64 MAC address). Link-local packets never route off your local wire.</li>
          <li><strong>Router Advertisements (RA):</strong> Unlike IPv4 which relies strictly on DHCP, IPv6 routers broadcast periodic ICMPv6 Type 134 Router Advertisements announcing gateway reachability and MTU.</li>
          <li><strong>Accessing Web Admin Consoles:</strong> Even on dual-stack IPv6 networks, most consumer router web panels remain simplest to reach over their IPv4 gateway address or local hostname (<a href="/howto/access-my-router-settings-page/">how to access router settings</a>), or bracketed in a browser like <code>http://[fe80::1]</code> when interface zoning permits.</li>
        </ul>
      </div>
      <h2>Find Your IPv6 Default Gateway in Terminal</h2>
      <p style="color: var(--text-secondary); line-height: 1.7;">
        Use these built-in commands (or see our full <a href="/find-router-ip/">IP Discovery Guide</a>) to inspect your active IPv6 default route:
      </p>
      <div style="margin-bottom: 1rem;">
        <div style="font-size: 0.85rem; font-weight: 600; margin-bottom: 0.25rem;">Windows PowerShell:</div>
        <pre class="code-preview-box"><code>Get-NetRoute -AddressFamily IPv6 | Where-Object DestinationPrefix -eq "::/0"</code></pre>
      </div>
      <div style="margin-bottom: 1rem;">
        <div style="font-size: 0.85rem; font-weight: 600; margin-bottom: 0.25rem;">macOS / Linux Terminal:</div>
        <pre class="code-preview-box"><code>netstat -rn -f inet6 | grep default    # macOS
ip -6 route show default               # Linux (Ubuntu/Debian)</code></pre>
      </div>
""",
        "faqs": [
            (
                "Why is my IPv6 default gateway fe80::1 instead of 192.168.1.1?",
                "IPv6 uses Link-Local addresses from the fe80::/10 range for next-hop routing on the local link rather than global unicast or RFC 1918 addresses.",
            ),
            (
                "Can I open my router login page using an IPv6 link-local address?",
                "Most consumer browsers restrict raw zone-indexed link-local URLs for security, so opening your router's IPv4 management IP (like 192.168.1.1) or local domain remains more reliable.",
            ),
        ],
        "bottom_line": "IPv6 default gateways appear as Link-Local <code>fe80::</code> addresses (visible via <code>Get-NetRoute</code> or <code>ip -6 route</code>), while day-to-day router administration continues cleanly over your IPv4 gateway IP.",
    },

    {
        "slug": "how-to-flush-dns-cache",
        "url": "/howto/how-to-flush-dns-cache/",
        "anchor_id": "flush-dns-cache",
        "featured": False,
        "badge": "DNS & Network Troubleshooting",
        "category": "Security & DNS",
        "category_key": "security",
        "meta_title": "How to Flush DNS Cache on Windows, Mac & Chrome",
        "meta_desc": "Flush DNS cache on Windows 11/10, macOS, and Chrome using ipconfig /flushdns, terminal commands, and host cache reset to fix DNS_PROBE_FINISHED_NXDOMAIN.",
        "headline": "How to Flush DNS Cache on Windows, Mac, and Chrome",
        "short_title": "Flush DNS Cache",
        "excerpt": "Purge outdated or corrupted DNS records across Windows 11/10, macOS, and Google Chrome using ipconfig /flushdns, terminal commands, and internal host cache reset.",
        "date_published": "2026-11-13",
        "date_modified": "2026-11-13",
        "read_time": "5 min read",
        "tags": ["Flush DNS", "Windows 11", "macOS", "Chrome", "DNS Troubleshooting"],
        "image": "/images/howto/how-to-flush-dns-cache-windows-mac-chrome.webp",
        "faqs": [
            (
                "What does flushing the DNS cache actually do?",
                "Flushing the DNS cache erases your operating system and web browser's local database of recently resolved domain-to-IP address translations. This forces your device to perform a fresh DNS lookup from configured resolvers (e.g. Cloudflare 1.1.1.1, Google 8.8.8.8, or your ISP gateway)."
            ),
            (
                "When should I flush my DNS cache?",
                "You should flush your DNS cache whenever a website fails to load with errors like DNS_PROBE_FINISHED_NXDOMAIN or ERR_NAME_NOT_RESOLVED, after changing your router or computer DNS servers, or when a recently migrated domain still displays its old server content."
            ),
            (
                "Does flushing DNS delete my browsing history or saved passwords?",
                "No. Flushing the DNS cache only deletes IP resolution records in the operating system resolver and browser host cache. It does not affect cookies, browsing history, form autofill data, or saved login credentials."
            ),
            (
                "What does 'Successfully flushed the DNS Resolver Cache' mean?",
                "This confirmation message means that Windows has wiped all cached A, AAAA, and CNAME records from memory. Your next web request will immediately query your active DNS server for current routing information."
            ),
            (
                "Why do I need to clear Chrome's DNS cache separately from Windows or Mac?",
                "Google Chrome maintains an internal, independent socket pool and host resolver cache designed to speed up browsing. Even if you clear your OS cache, Chrome may continue serving stale IP mappings until you clear chrome://net-internals/#dns and restart the browser."
            ),
            (
                "What if flushing DNS does not fix my connection error?",
                "If flushing DNS fails to restore access, power cycle your router to clear its internal DNS forwarding proxy, switch your router DNS to Cloudflare (1.1.1.1) or Google (8.8.8.8), disable any active VPN or proxy software, and test the website on another device connected to the same network."
            )
        ],
        "bottom_line": "Use <code>ipconfig /flushdns</code> on Windows, the Terminal command on Mac, and <strong>Clear host cache</strong> in Chrome. These steps remove stored DNS records and force your device or browser to request fresh information.<br><br><strong>Fastest fix:</strong> Flush DNS on your operating system first, then clear Chrome&rsquo;s host cache if the website still fails to load.",
        "body_html": """
      <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.75rem;">
        Flushing the DNS cache removes outdated or incorrect website-address records stored on your device or browser. Use it when a website will not load, shows the wrong server, or you recently changed DNS settings.
      </p>

      <div class="answer-box">
        <div class="answer-box-label">Quick Answer: How to Flush DNS Cache Across Operating Systems</div>
        <div class="answer-box-main">
          Windows: <code>ipconfig /flushdns</code> &bull; Mac: <code>sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder</code> &bull; Chrome: <code>chrome://net-internals/#dns</code> &rarr; Clear host cache
        </div>
        <div class="answer-box-sub">
          Flushing the DNS cache purges cached domain-to-IP address translations stored locally by your operating system and web browser. This forces your system to retrieve fresh records from your DNS servers, instantly fixing <code>DNS_PROBE_FINISHED_NXDOMAIN</code> and server mismatch errors.
        </div>
      </div>

      <div style="overflow-x: auto; margin: 2rem 0;">
        <table class="table" style="font-size: 0.95rem;">
          <thead>
            <tr>
              <th>Operating System / Browser</th>
              <th>Tool to Open</th>
              <th>Command or Navigation Path</th>
              <th>Expected Output</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Windows 11 &amp; 10</strong></td>
              <td>Command Prompt (Admin)</td>
              <td><code>ipconfig /flushdns</code></td>
              <td><em>Successfully flushed the DNS Resolver Cache.</em></td>
            </tr>
            <tr>
              <td><strong>Windows 8 &amp; 7</strong></td>
              <td>Command Prompt (Admin)</td>
              <td><code>ipconfig /flushdns</code></td>
              <td><em>Successfully flushed the DNS Resolver Cache.</em></td>
            </tr>
            <tr>
              <td><strong>macOS (Modern)</strong></td>
              <td>Terminal</td>
              <td><code>sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder</code></td>
              <td>Password prompt &rarr; Silent clean exit</td>
            </tr>
            <tr>
              <td><strong>macOS (Legacy)</strong></td>
              <td>Terminal</td>
              <td><code>sudo killall -HUP mDNSResponder</code></td>
              <td>Silent daemon reload</td>
            </tr>
            <tr>
              <td><strong>Google Chrome DNS</strong></td>
              <td>Chrome Omnibox</td>
              <td><code>chrome://net-internals/#dns</code></td>
              <td>Click <strong>Clear host cache</strong></td>
            </tr>
            <tr>
              <td><strong>Google Chrome Sockets</strong></td>
              <td>Chrome Omnibox</td>
              <td><code>chrome://net-internals/#sockets</code></td>
              <td>Click <strong>Flush socket pools</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <figure class="guide-figure">
        <img src="/images/howto/how-to-flush-dns-cache-windows-mac-chrome.webp" width="1200" height="675" fetchpriority="high" alt="Technical diagram showing how to flush DNS cache on Windows via Command Prompt, macOS via Terminal, and Google Chrome via net-internals">
        <figcaption>Overview: How to purge the local DNS resolver cache on Windows, macOS, and Google Chrome to resolve host unreachable and DNS timeout errors.</figcaption>
      </figure>

      <h2 id="windows-dns-flush">Windows</h2>

      <h3>Windows 11 and Windows 10</h3>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.5rem;">
        <li>Press <strong>Windows + R</strong> on your keyboard to open the Run dialog.</li>
        <li>Type <code>cmd</code> and press <strong>Ctrl + Shift + Enter</strong> to open Command Prompt with administrator privileges.</li>
        <li>Type the command below and press <strong>Enter</strong>:
          <pre style="margin: 0.75rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>ipconfig /flushdns</code></pre>
        </li>
        <li>Wait for the confirmation message:
          <pre style="margin: 0.75rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem; color: #10b981;"><code>Successfully flushed the DNS Resolver Cache.</code></pre>
        </li>
        <li>Close Command Prompt and reopen the website in your browser.</li>
      </ol>

      <figure class="guide-figure">
        <img src="/images/howto/windows-flush-dns-command-prompt.webp" width="1200" height="675" loading="lazy" alt="Windows 11 Command Prompt running ipconfig /flushdns with successful resolver cache flush confirmation">
        <figcaption>Figure 1: Executing ipconfig /flushdns with elevated administrator privileges in Windows 11.</figcaption>
      </figure>

      <h3>Windows 8 and Windows 7</h3>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
        <li>Click <strong>Start</strong>.</li>
        <li>Type <code>cmd</code> in the search box.</li>
        <li>Right-click <strong>Command Prompt</strong> and choose <strong>Run as administrator</strong>.</li>
        <li>Enter:
          <pre style="margin: 0.75rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>ipconfig /flushdns</code></pre>
        </li>
        <li>Press <strong>Enter</strong>.</li>
      </ol>

      <h2 id="mac-dns-flush">Mac</h2>

      <h3>macOS Ventura, Monterey, Big Sur, Catalina</h3>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.5rem;">
        <li>Open <strong>Terminal</strong> from <strong>Applications &gt; Utilities</strong> or via Spotlight (Cmd + Space).</li>
        <li>Enter this command:
          <pre style="margin: 0.75rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder</code></pre>
        </li>
        <li>Press <strong>Enter</strong>.</li>
        <li>Enter your Mac login password when prompted (characters will not show on screen for security).</li>
        <li>Press <strong>Enter</strong> again.</li>
      </ol>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
        The command does not always display a confirmation message. Once it completes and returns to the prompt, the DNS cache has been cleared.
      </p>

      <h3>Older macOS Versions</h3>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 0.75rem;">
        For older macOS versions (macOS Sierra, El Capitan, Yosemite), use:
      </p>
      <pre style="margin: 0.75rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>sudo killall -HUP mDNSResponder</code></pre>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-top: 1rem; margin-bottom: 0.75rem;">
        If that does not work (OS X Yosemite 10.10.0&ndash;10.10.3), try:
      </p>
      <pre style="margin: 0.75rem 0 2rem 0; background: var(--bg-secondary); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>sudo discoveryutil mdnsflushcache</code></pre>

      <h2 id="google-chrome-dns-flush">Google Chrome</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.25rem;">
        Chrome keeps its own internal DNS cache, separate from Windows or macOS.
      </p>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.5rem;">
        <li>Open Chrome.</li>
        <li>Type this into the address bar:
          <pre style="margin: 0.5rem 0; background: var(--bg-secondary); padding: 0.65rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>chrome://net-internals/#dns</code></pre>
        </li>
        <li>Press <strong>Enter</strong>.</li>
        <li>Click <strong>Clear host cache</strong>.</li>
        <li>Open a new tab and test the website again.</li>
      </ol>

      <figure class="guide-figure">
        <img src="/images/howto/chrome-net-internals-clear-host-cache.webp" width="1200" height="675" loading="lazy" alt="Google Chrome net-internals DNS settings page showing Clear host cache and Flush socket pools buttons">
        <figcaption>Figure 2: Clearing Chrome's internal host resolver cache and flushing socket pools in chrome://net-internals.</figcaption>
      </figure>

      <p style="color: var(--text-secondary); line-height: 1.7; margin-top: 1.5rem; margin-bottom: 0.75rem;">
        Chrome may also store open socket connections to previous IP addresses. To clear those as well:
      </p>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2.25rem;">
        <li>Type this in the address bar:
          <pre style="margin: 0.5rem 0; background: var(--bg-secondary); padding: 0.65rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.95rem;"><code>chrome://net-internals/#sockets</code></pre>
        </li>
        <li>Click <strong>Flush socket pools</strong>.</li>
        <li>Restart Chrome.</li>
      </ol>

      <h2 id="when-to-flush-dns">When to Flush DNS</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        Flush your DNS cache if:
      </p>
      <ul style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.75rem;">
        <li>A website will not load even though it works on another device.</li>
        <li>You changed DNS servers, such as moving to Google DNS or Cloudflare DNS.</li>
        <li>A website recently changed servers but still opens the old version.</li>
        <li>You see DNS-related errors such as <code>DNS_PROBE_FINISHED_NXDOMAIN</code>.</li>
        <li>You changed hosting, domain settings, or website DNS records.</li>
      </ul>

      <div style="overflow-x: auto; margin: 1.75rem 0 2.5rem 0;">
        <table class="table" style="font-size: 0.95rem;">
          <thead>
            <tr>
              <th>Browser Error Code</th>
              <th>Root Cause</th>
              <th>Recommended Fix</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>DNS_PROBE_FINISHED_NXDOMAIN</code></td>
              <td>Negative DNS cache or unpropagated A-record</td>
              <td>Run <code>ipconfig /flushdns</code> &amp; test in Chrome Incognito</td>
            </tr>
            <tr>
              <td><code>ERR_NAME_NOT_RESOLVED</code></td>
              <td>Operating system resolver cannot resolve host</td>
              <td>Flush DNS &amp; reboot your home router</td>
            </tr>
            <tr>
              <td><code>DNS_PROBE_STARTED</code></td>
              <td>DNS lookup request is timing out</td>
              <td>Disconnect VPN/proxy &amp; switch to Cloudflare (1.1.1.1)</td>
            </tr>
            <tr>
              <td><code>DNS_PROBE_FINISHED_BAD_CONFIG</code></td>
              <td>Invalid DNS IP entered in network adapter</td>
              <td>Set DNS to Automatic (DHCP) or Google (8.8.8.8)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 id="if-the-problem-continues">If the Problem Continues</h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        If flushing DNS does not fix the issue:
      </p>
      <ol style="margin-left: 1.5rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
        <li><strong>Restart your router:</strong> Power cycle your router by disconnecting its power adapter for 30 seconds. Routers maintain an internal DNS proxy cache that can serve stale translations to all connected home devices (see our <a href="/howto/30-second-hard-factory-reset/">30-Second Hard Reset Guide</a>).</li>
        <li><strong>Restart your computer or phone:</strong> Reboots system-level networking services and cleans temporary socket bindings.</li>
        <li><strong>Change your DNS servers to Cloudflare DNS or Google DNS:</strong> Switch from your ISP's default resolver to Cloudflare (<code>1.1.1.1</code> and <code>1.0.0.1</code>) or Google (<code>8.8.8.8</code> and <code>8.8.4.4</code>) using our complete <a href="/howto/change-router-dns/">How to Change Router DNS Guide</a>.</li>
        <li><strong>Disable VPN, proxy, or browser extensions temporarily:</strong> VPN clients (such as NordVPN or ExpressVPN) and proxy extensions reroute DNS traffic through encrypted virtual network interfaces, bypassing your local DNS resolver cache.</li>
        <li><strong>Test the website in another browser:</strong> Open the target URL in Firefox, Microsoft Edge, or Safari to determine if the issue is restricted to Chrome's local profile.</li>
        <li><strong>Check whether the website works on another device:</strong> Connect your smartphone to cellular data or verify with our <a href="/tools/dns-propagation/">DNS Propagation Checker</a> to confirm whether the issue is local or server-side.</li>
      </ol>
"""
    },
]

EXTERNAL_HUB_GUIDE_CARD = {
    "url": "/find-router-ip/",
    "anchor_id": "find-router-ip-card",
    "badge": "Diagnostics",
    "category": "Login & Access",
    "category_key": "login",
    "headline": "How to Find Your Router IP Address on Any Device",
    "excerpt": "Step-by-step Windows ipconfig, macOS Terminal netstat, Linux ip route, iPhone Wi-Fi, and Android gateway discovery instructions when 192.168.1.1 fails.",
    "date_published": "2026-02-15",
    "read_time": "5 min read",
    "tags": ["ipconfig", "Windows", "macOS", "iOS / Android"],
}

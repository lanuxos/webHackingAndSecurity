# Web hacking and security
# ep1 - OWASP TOP 10

# Introduction - 001045
    - HTTrack - 002515 [Copy webpage tool]
# Cyber kill chain [7 steps] - 010700
    1. Reconnaissance [Information gathering, Passive reconnaissance & Active reconnaissance]
        - Detect: web analytics; threat intelligence; network intrusion detection system
        - Deny: information sharing policy; firewall access control lists
        - Google dork - 011000
            - filetype: xxx
            - site: xxx
            - [Exploit Database](www.exploit-db.com/google-hacking-database)
            - "index of"
            - SoftEther VPN Client Manager
            - Tor browser
            - Social Media (OSINT)
    2. Weaponization - 012040
        - DDos
        - Botnet
        - Malware
    3. Delivery - 012135
        - Adversary-controlled delivery
        - Adversary-released delivery
        - Detect: endpoint malware protection
        - Deny: change management; application whitelisting; proxy filter; host-based intrusion prevention system
        - Disrupt: inline anti-virus
        - Degrade: queuing
        - contain: router access control lists; app-aware firewall; trust zones; inter-zone network intrusion detection system
    4. Exploitation - 012350
        - [Exploit Database](www.exploit-db.com)
        - Detect: endpoint malware protection; host-based intrusion detection system
        - Deny: secure password; patch management
        - Disrupt: data execution prevention
        - Contain: app-aware firewall; trust zones; inter-zone network intrusion detection system
    5. Installation - 013200
        - Detect: security information and event management (SIEM); host-based intrusion detection system
        - Deny: privilege seperation; strong passwords; two-factor authentication
        - Disrupt: router access control lists
        - Contain: app-aware firewall; trust zones; inter-zone network intrusion detection system
    6. C2 (Command & Control) - 013300
    7. Actions on objectives - 013510
        [zone-h](www.zone-h.org)
# HTTP Protocol - 013910
    - HTTP Headers [chrome extension]
    - HTTP Code
        - 2xx - success status
        - 3xx - redirect status
        - 4xx - client error
        - 5xx - server error
# OWASP top 10 [2017] - 014630
    1. A1 - Injection - 014930
        - SQL injection
            ```
                \\ user = admin, pass = nimda
                select * from account
                where
                user = "admin" and pass = "admin" OR "1" = "1"
            ```
        - HTML injection
    2. A2 - Broken Authentication - 015530
    3. A3 - Sensitive Data Exposure - 015655
    4. A4 - XML External Entities (XXE) - 020000
    5. A5 - Broken Access Control - 020020
    6. A6 - Security Misconfiguration - 020100
    7. A7 - Cross-Site Scripting (XSS) - 020145
    8. A8 - Insecure De-serialization - 020444
    9. A9 - Using Components with Known Vulnerabilities - 020610
    10. A10 - Insufficient Logging & Monitoring - 020645
# Further keywords
    - SonarQube - Testing tool
    - Damn Vulnerable Web Application [DVWA]
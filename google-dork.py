import webbrowser
import os

def open_search(url):
    webbrowser.open(url, new=2)  # Open in a new tab, if possible

def main():
    # Define a dictionary of dorks with their descriptions
    dorks = {
        "1": ("Index of", "intitle:index.of"),
        "2": ("Configuration Files", "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"),
        "3": ("Database Files", "ext:sql | ext:dbf | ext:mdb"),
        "4": ("WordPress", "inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"),
        "5": ("Log Files", "ext:log"),
        "6": ("Backup and Old Files", "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"),
        "7": ("Login Pages", "inurl:login | inurl:signin | intitle:Login | intitle:signin | inurl:auth"),
        "8": ("Documents", "ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"),
        "9": ("PHP Info", "ext:php intitle:phpinfo \"published by the PHP Group\""),
        "10": ("Shells and Backdoors", "inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor"),
        "11": ("Readme and License Files", "inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config"),
        "12": ("SQL Errors", "intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\""),
        "13": ("Redirection URLs", "inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http"),
        "14": ("Struts Files", "ext:action | ext:struts | ext:do"),
        "15": ("Pastebin", "site:pastebin.com"),
        "16": ("LinkedIn Employees", "site:linkedin.com employees"),
        "17": ("Sharepoint", ".sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec"),
        "18": ("WSDL Files", "filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype:?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl"),
        "19": ("GitHub Search", "site:github.com"),
        "20": ("Gist Search", "site:gist.github.com"),
        "21": ("Apache Config", "filetype:config \"apache\""),
        "22": ("Code Sharing Sites", "site:ideone.com | site:codebeautify.org | site:codeshare.io | site:codepen.io | site:repl.it | site:justpaste.it | site:pastebin.com | site:jsfiddle.net | site:trello.com | site:*.atlassian.net | site:bitbucket.org"),
        "23": ("Atlassian Sites", "site:atlassian.net | site:bitbucket.org"),
        "24": ("Git Directories", "inurl:\"/.git\" -github"),
        "25": ("Traefik Dashboard", "intitle:traefik inurl:8080/dashboard"),
        "26": ("Certificate Transparency Logs", "crt.sh"),
        "27": ("PHP Info and .htaccess", "inurl:\"/phpinfo.php\" | inurl:\".htaccess\""),
        "28": ("Subdomains", "site:*."), 
        "29": ("Sub-subdomains", "site:*.*."),
        "30": ("WordPress Content", "inurl:wp-content | inurl:wp-includes"),
        "31": ("Wayback Machine WP Content", "http://wwwb-dedup.us.archive.org:8083/cdx/search?url=domain/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx="),
        "32": ("Open Bug Bounty", "https://www.openbugbounty.org/search/?search=domain"),
        "33": ("Reddit", "https://www.reddit.com/search/?q=domain"),
        "34": ("Crossdomain.xml", "domain/crossdomain.xml"),
        "35": ("Robots.txt", "domain/robots.txt"),
        "36": ("Security Headers", "https://securityheaders.com/?q=domain&followRedirects=on"),
        "37": ("ThreatCrowd", "https://threatcrowd.org/domain.php?domain=domain"),
        "38": ("RiskIQ", "https://community.riskiq.com/search/domain"),
        "39": ("SWF Files", "inurl:domain ext:swf"),
        "40": ("YouTube", "https://www.youtube.com/results?search_query=domain"),
        "41": ("Yandex SWF Search", "https://yandex.com/search/?text=site:domain mime:swf"),
        "42": ("Wayback Machine SWF Search", "https://web.archive.org/cdx/search?url=domain/&matchType=domain&collapse=urlkey&output=text&fl=original&filter:urlkey:.*swf&limit=100000"),
        "43": ("Wayback Machine SWF MimeType Search", "https://web.archive.org/cdx/search?url=domain/&matchType=domain&collapse=urlkey&output=text&fl=original&filter:mimetype:application/x-shockwave-flash&limit=100000"),
        "44": ("Wayback Machine Search", "https://web.archive.org/web/*/domain/*"),
        "45": ("Reverse IP", "https://viewdns.info/reverseip/?host=domain&t=1"),
        "46": ("PublicWWW", "https://publicwww.com/websites/\"domain\"/"),
        "47": ("Censys IPv4", "https://censys.io/ipv4?q=domain"),
        "48": ("Censys Domain", "https://censys.io/domain?q=domain"),
        "49": ("Censys Certificates", "https://censys.io/certificates?q=domain"),
        "50": ("Shodan", "https://www.shodan.io/search?query=domain"),
        "51": ("Google Custom Search Engine", "https://cse.google.com/cse?cx=002972716746423218710:veac6ui3rio#gsc.tab=0&gsc.q=domain"),
        "52": ("Throwbin.io", "site:throwbin.io domain"),
        "53": ("Domaineye", "https://domaineye.com/similar/domain"),
        "54": ("GitLab", "inurl:gitlab domain"),
        "55": ("StackOverflow", "site:stackoverflow.com \"domain\""),
        "56": ("Amazon S3", "site:.s3.amazonaws.com \"domain\""),
        "57": ("DigitalOcean Spaces", "site:digitaloceanspaces.com \"domain\""),
        "58": ("WhatCMS", "https://whatcms.org/?s=domain")
    }
    
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and other Unix-like systems
        os.system('clear')
    art = """
   _____                     _           ______             _              _____                      
  / ____|                   | |         |  ____|           (_)            |  __ \                     
 | (___   ___  __ _ _ __ ___| |__ ______| |__   _ __   __ _ _ _ __   ___  | |__) |___  ___ ___  _ __  
  \___ \ / _ \/ _` | '__/ __| '_ \______|  __| | '_ \ / _` | | '_ \ / _ \ |  _  // _ \/ __/ _ \| '_ \ 
  ____) |  __/ (_| | | | (__| | | |     | |____| | | | (_| | | | | |  __/ | | \ \  __/ (_| (_) | | | |
 |_____/ \___|\__,_|_|  \___|_| |_|     |______|_| |_|\__, |_|_| |_|\___| |_|  \_\___|\___\___/|_| |_|
                                                       __/ |                                          
                                                      |___/                                           
    """
    print(art)
    domain = input("[ Domain ] #> ").strip()
    while True:
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and other Unix-like systems
            os.system('clear')
        print(art)
        print("\nDorks:\n")
        keys = list(dorks.keys())
        for i in range(0, len(keys), 2):
            key1 = keys[i]
            description1 = dorks[key1][0]
            if i + 1 < len(keys):
                key2 = keys[i + 1]
                description2 = dorks[key2][0]
                print(f"{key1: <2} {description1: <35}      {key2: <2} {description2}")
            else:
                print(f"{key1: <2} {description1: <35}")

        choice = input("\n[Select Dorks ] #> ").strip()
        if choice.lower() == 'exit':
            break
        
        if choice in dorks:
            description, query = dorks[choice]
            url = f"https://www.google.com/search?q=site:{domain} {query}"
            open_search(url)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

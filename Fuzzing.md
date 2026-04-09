**Directory Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/FUZZ -ic

Ex:
ffuf -w directory-list-2.3-small.txt -u http://94.237.51.155:46872/FUZZ -ic
```

**Extension Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/DIRECTORY/indexFUZZ

Ex:
ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/blog/indexFUZZ
```

**Page Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/DIRECTORY/FUZZ.EXTENSION

Ex:
ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/blog/indexFUZZ
```


**Recursive Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -v

Ex:
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v
```

**Subdomain Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://FUZZ.HOST/

Ex:
ffuf -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.inlanefreight.com/
```

**Vhost Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/ -H 'Host: FUZZ.HOST'

Ex:
ffuf -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb'
```

**Parameter Fuzzing - GET**

```
Payload:
ffuf -w /wordlist.txt:FUZZ -u SCHEME://HOST:PORT/DIRECTORY/ENDPOINT?FUZZ=key -fs xxx

Ex:
ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx
```

**Parameter Fuzzing - POST**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/DIRECTORY/ENDPOINT.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

Ex:
ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

cURL:
curl http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded' 

<div class='center'><p>Invalid id!</p></div> 
<...SNIP...>
```

**Value Fuzzing**
```
Payload:
ffuf -w wordlist.txt:FUZZ -u SCHEME://HOST:PORT/DIRECTORY/ENDPOINT.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

Ex:
ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
```

```
> ffuf -w /root/wordlists/bbFuzzing.txt -H "User-Agent: Mozilla/5.0" -H "Host: localhost" -u http://elearn.ing.ro/FUZZ -fr '/\..*'

> ffuf -u target.com/FUZZ -w bbFuzzing.txt
> ffuf -u target.com/FUZZ -H "Host: 127.0.0.1" -w bbFuzzing.txt
> ffuf -u target.com/FUZZ -H "Host: localhost" -w bbFuzzing.txt

> ffuf -u target.com/FUZZ.example -w bbFuzzing.txt
> ffuf -u target.com/FUZZ.sample -w bbFuzzing.txt
> ffuf -u target.com/FUZZ.template -w bbFuzzing.txt

> ffuf -u target.com/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/%3B/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/..%3B/FUZZ/ -w bbFuzzing.txt

> ffuf -u target.com/FUZZ..%2f -w bbFuzzing.txt
> ffuf -u target.com/FUZZ%09 -w bbFuzzing.txt
> ffuf -u target.com/FUZZ%23 -w bbFuzzing.txt

> ffuf -u target.com/FUZZ..%00 -w bbFuzzing.txt
> ffuf -u target.com/FUZZ;%09 -w bbFuzzing.txt
> ffuf -u target.com/FUZZ;%09.. -w bbFuzzing.txt

> ffuf -u target.com/FUZZ;%09..; -w bbFuzzing.txt
> ffuf -u target.com/FUZZ;%2f.. -w bbFuzzing.txt
> ffuf -u target.com/.FUZZ -w bbFuzzing.txt

> ffuf -u target.com/%0AFUZZ -w bbFuzzing.txt
> ffuf -u target.com/%0D%0AFUZZ -w bbFuzzing.txt
> ffuf -u target.com/%0DFUZZ -w bbFuzzing.txt

> ffuf -u target.com/%2e/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/FUZZ%20 -w bbFuzzing.txt
> ffuf -u target.com/FUZZ%2520 -w bbFuzzing.txt

> ffuf -u target.com/%u002e%u002e/%u002e%u002e/FUZZ -w bbFuzzing.txt
> ffuf -u target.com/%2e%2e%2f/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/%2EFUZZ -w bbFuzzing.txt

> ffuf -u target.com/FUZZ.old -w bbFuzzing.txt
> ffuf -u target.com/FUZZ?.css -w fuzzing.txt
> ffuf -u target.com/FUZZ?.js -w fuzzing.txt

> ffuf -u target.com/_FUZZ -w bbFuzzing.tx
> ffuf -u target.com/FUZZ_ -w bbFuzzing.txt
> ffuf -u target.com/_FUZZ_ -w bbFuzzing.txt

> ffuf -u target.com/..;/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/..;/..;/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/../FUZZ -w bbFuzzing.txt

> ffuf -u target.com/-FUZZ -w bbFuzzing.txt
> ffuf -u target.com/~FUZZ -w bbFuzzing.txt
> ffuf -u target.com/FUZZ..;/ -w bbFuzzing.txt

> ffuf -u target.com/FUZZ;/ -w bbFuzzing.txt
> ffuf -u target.com/FUZZ# -w bbFuzzing.txt
> ffuf -u target.com/FUZZ/~ -w bbFuzzing.txt

> ffuf -u target.com/!FUZZ -w bbFuzzing.txt
> ffuf -u target.com/#/FUZZ/ -w bbFuzzing.txt
> ffuf -u target.com/-/FUZZ/ -w bbFuzzing.txt

> ffuf -u target.com/FUZZ~ -w bbFuzzing.txt
> ffuf -u target.com/FUZZ/.git/config -w bbFuzzing.txt
> ffuf -u target.com/FUZZ/.env -w bbFuzzing.txt

> ffuf -u target.com/FUZZ. -w bbFuzzing.txt
> ffuf -u target.com/FUZZ/* -w bbFuzzing.txt
> ffuf -u target.com/FUZZ/? -w bbFuzzing.txt

> ffuf -u target.com/FUZZ -recursive -w fuzzing.txt
> ffuf -u target.com/FUZZ -recursive -w fuzzing.txt -e .asp,.aspx,.ashx,.ash,.jsp,.jspx,.php,.js,.dll,.json,.bak,.bkp,.conf,.txt,.py,.zip,.tar.gz,.tar,.7z,.old

Any special occasions (cookieless) - IIS + ASP
> ffuf -u target.com/(A(ABCD))/FUZZ
> ffuf -u target.com/(ABCD)/FUZZ
> ffuf -u target.com/(A(XXXXXXXX)F(YYYYYYYY))/FUZZ
> ffuf -u target.com/FUZZ/(S(X))/
> ffuf -u target.com/bin::$INDEX_ALLOCATION/FUZZ
> ffuf -u target.com/bin::$INDEX_ALLOCATION/FUZZ.dll
> ffuf -u target.com/bin::$INDEX_ALLOCATION/FUZZ -e .asp,.aspx,.ashx,.ash,.dll
```


![[pad1ryoshi - METHODOLOGY/Web Reconnaissance/Imagens/Attacking_Web_Applications_With_Ffuf_Module_Cheat_Sheet.pdf]]
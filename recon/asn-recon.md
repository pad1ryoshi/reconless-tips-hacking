postagem: https://katrinasec.com/blog/enumeracao-em-larga-escala-de-subdominios-a-partir-do-asn

```
https://bgp.he.net/dns/{dominio-alvo}#_ipinfo

whois -h whois.radb.net -- '-i origin AS-NUMBER' | grep -Eo '([0-9.]+){4}/[0-9]+' > ranges.txt

masscan -iL ranges.txt -p80,443,8080,8000,8443,8081 --rate=10000 -oG masscan.gnmap

awk '/Host: / {print $4}' masscan.gnmap > hosts

cat hosts | dnsx -resp-only -ptr > rDNS-hosts.txt
```


```bash
gobuster vhost -u http://inlanefreight.htb:59660 -w subdomains-top1million-110000.txt --append-domain
```

```bash
info de registros:

dnsx -retry 3 -a -aaaa -cname -ns -ptr -mx -soa -resp -silent -l subdomains.txt -j > dnsx_info.tx
```

```bash

cat formazionestarbucks.it-nodes.txt | zdns a --iterative -o zdns-output1.txt

cat zdns-output1.txt | jq -r 'select(.results.A.status == "NOERROR") | .name' | anew zdns-noerror.txt

Pegar todos os endereços, um por um, e realizar fuzzing de vhosts neles:

jq -r 'select(.results.A.status == "NOERROR") | .results.A.data.answers[]?.answer' zdns-output1.txt

Para pegar apenas IPV4:

jq -r 'select(.results.A.status == "NOERROR") | .results.A.data.answers[]?.answer | select(test("^([0-9]{1,3}\\.){3}[0-9]{1,3}$"))'
```

```bash
fuzzing vhost:

ffuf -c -r -u 'https://www.atg.se/' -H 'Host: FUZZ.atg.se' -w dns-wordlist.txt
ffuf -c -r -u 'https://ADDRESS/' -H 'Host: FUZZ.atg.se' -w dns-wordlist.txt
ffuf -H 'Host: FUZZ' -w hosts.txt -u http://ADDRESS/

hosts.txt (exemplo):
admin.server.com
localhost.server.com
admin.server.com
dev-admin.server.com
```

```bash

cat zdns-output1.txt|jq -r 'select(.results.A.status == "NOERROR") | .results.A.data.answers[]?.answer | select(test("^([0-9]{1,3}\\.){3}[0-9]{1,3}$"))' > ips.txt

Utilizar os endereços obtidos com o ZDNS ou de sources tipo BGP.he, shodan, virustotal...:

for i in $(cat ips.txt);do ffuf -w wordlist.txt -u http://$i -H "HOST: http://FUZZ.target.com" -H "X-Forwarded-For: 127.0.0.1" -H "X-Originating-IP: 127.0.0.1" -H "X-Forwarded-Host: localhost" -s -of csv -o $i.csv ; done

Usando em subdominios mortos:

for i in $(cat ips.txt);do ffuf -w subs.txt -u http://$i -H "Host: FUZZ" -H "X-Forwarded-For: 127.0.0.1" -H "X-Originating-IP: 127.0.0.1" -H "X-Forwarded-Host: localhost" -of csv -o [$i](https://x.com/search?q=%24i&src=cashtag_click).csv ; done
```

```bash
nmap --script http-vhosts -p 80,443 --script-args http-vhosts.domain=dominio.com,http-vhosts.filelist=wordlist.txt www.crapi.site
```

```bash
openssl s_client -connect www.crapi.site:443 2>&1 < /dev/null | openssl x509 -noout -text | grep -i dns
```

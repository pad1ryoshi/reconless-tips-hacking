# enumeração passiva

    tools:
    	subfinder -all -d {domain} -oJ domains-subfinder.{domain}.json >> domains-subfinder.{domain}.json
    	subfinder -all -d {domain} | anew domains
    	amass enum -passive -d {domain} -timeout 12 -v | anew domains
    	gau --subs {domain} | unfurl | anew domains

    dorking:
    	google: site:*.{domain} -www.
    	google: site:pastebin.com "{target}"

    certificates:
    	Todos os subdomínios:
    	curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u

    	Por certificado, tipo: Apple, Inc:
    	curl -s "https://crt.sh/?O=Apple%20Inc.&output=json" | jq -r '.[].common_name' | tr '[:upper:]' '[:lower:]' | unfurl format %r.%t | sort -u | tee apple.cert.txt

    	Enumeração horizontal:
    	curl -s "https://crt.sh/?O=Apple%20Inc.&output=json" | jq -r '.[].common_name' | tr '[:upper:]' '[:lower:]' | unfurl format %r.%t | sort -u | alterx -p '{{root}}' | tee perm-cert.txt

    	curl -L 'https://ip.thc.org/api/v1/subdomains/download?domain=bmw.cloud' \ -H 'Accept: text/csv'

    CSP:
    	curl -s -I -L “https://www.newyorker.com/" | grep -Ei ‘^Content-Security-Policy:’ | sed “s/;/;\\n/g”

    ENTs and NOERROR:
    	subfinder -d ifood.com.br | dnsx -rcode noerror -v

    	cat formazionestarbucks.it-nodes.txt | zdns a --iterative -o zdns-output1.txt -> cat zdns-output1.txt | jq -r 'select(.results.A.status == "NOERROR") | .name' | anew zdns-noerror.txt


# enumeração ativa

    enum:
    	amass enum -brute -active -d domain.com -o amass-output.txt

    permutação dns:
    	cat domains-alive.txt | dnsgen -w WORDLIST-PEQUENA -
    	subfinder -dL domains-alive.txt -silent | alterx -en -silent | dnsx | anew perm-alterx.txt
    	gobuster dns -d ovo.com -w ~/wordlists/NODES/common_nodes.txt

    ENTs and NOERROR:
    	dnsx -v -w common_nodes.txt -d <domain> -rcode noerror
    	massdns -r resolvers.txt urls.txt -o L0 -w urls_resolved.txt
    	dnsfuzz domain.com common_nodes.txt -r resolvers.txt


# info de registros:

    dnsx -retry 3 -a -aaaa -cname -ns -ptr -mx -soa -resp -silent -l subdomains.txt -j > dnsx_info.txt

# fuzzing vhost:

    ffuf -c -r -u 'https://www.atg.se/' -H 'Host: FUZZ.atg.se' -w dns-wordlist.txt

# reverse DNS lookups:

    cat ips.txt | dnsx -ptr -resp-only

# gathering info:

    amass intel -org 'Example Ltd'
    amass intel -d owasp.org -whois

    https://crt.sh/?q=DOMINIO

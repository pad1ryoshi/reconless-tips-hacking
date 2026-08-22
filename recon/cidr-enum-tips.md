>- Hackeando ranges CIDR:
>- mapcidr para ter uma lista de endereços IP de um mesmo range CIDR;
>- masscan para fazer port scanning de todo os endereços de um range CIDR;
>- httpx para pegar informações sobre os hosts que respondem;
>- dnsx para pegar o subdomínio que respondem ao um endereço.

---

```bash
mapcidr -cidr 204.14.239.0/24 > ips.txt

masscan -iL ips.txt -p1-65535 --rate=10000 --output-format json --output-filename scan-results.json

cat scan-results.json | sed -e ‘/^\[/d’ -e ‘/^\]/d’ -e ‘s/,$//’ | jq -r ‘[.ip, .ports[0].port] | @tsv’ | sed ‘s/\t/:/’ | sort -u > alive-hosts

cat alive-hosts | httpx -status-code -content-length -title -follow-redirects -threads 500 | tee probed-hosts

# Caso o endereço nao responda, fazer a enumeração reversa de IP para NOME

echo "13.227.219.100" | dnsx -ptr -resp-only
```

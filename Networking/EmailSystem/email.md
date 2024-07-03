# Email Notes

# Goal: To create a dockerImage that makes learning about email server easy

## Tools used
- maildirmake => maildrop

## Postfix Configuration
```bash
sudo apt update
sudo apt install postfix
sudo nano /etc/postfix/main.cf
```
### Postfix Parameters
```conf
myhostname = mail.example.com
mydomain = example.com
myorigin = /etc/mailname
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
relayhost =
inet_interfaces = all
inet_protocols = all
```
```bash
sudo systemctl restart postfix
```


## Devcot
**Open source IMAP and POP3 Server**
```bash
sudo apt install dovecot-core dovecot-imapd dovecot-pop3d
sudo nano /etc/dovecot/dovecot.conf
```

```conf
protocols = imap pop3 lmtp
```

### Editing mailbox location
```bash
sudo nano /etc/dovecot/conf.d/10-mail.conf
```
```conf
mail_location = maildir:~/Maildir
```
```bash
sudo systemctl restart dovecot
```

```bash
sudo systemctl restart dovecot
```

### Setting up your email client

```bash
sudo apt update
sudo apt install mutt
```

```bash
nano ~/.muttrc
```

```conf
# Basic settings
set realname = "Your Name"
set from = "you@example.com"
set use_from = yes
set envelope_from = yes

# IMAP settings
set imap_user = "you@example.com"
set imap_pass = "yourpassword"
set folder = "imaps://mail.example.com/"
set spoolfile = "+INBOX"
set postponed = "+[Gmail]/Drafts"
set trash = "+[Gmail]/Trash"

# SMTP settings
set smtp_url = "smtp://you@example.com@mail.example.com:587/"
set smtp_pass = "yourpassword"

# Mail directories
set record = "+[Gmail]/Sent Mail"
set mbox = "+[Gmail]/All Mail"
set postponed = "+[Gmail]/Drafts"
set header_cache =~/.mutt/cache/headers
set message_cachedir =~/.mutt/cache/bodies
set certificate_file =~/.mutt/certificates

# Other settings
set move = no
set imap_keepalive = 900
```


### Two reasons to use mutt:

To have just some aesthetic fun to show off to your friends that “Hey look, I am a Hacker! Mailing you straight from my green Terminal 😝”
Or get into some serious Linux Kernel Development kinda business where you are not expected to send HTML emails and base64 attachments. Well to tell you the secret — entire Linux kernel is developed and maintained over emails. So you know now how important an email client becomes 😄


## Configuring mutt

```bash
mkdir -p ~/.mutt/cache/headers
mkdir ~/.mutt/cache/bodies
touch ~/.mutt/certificates
```
```bash
touch ~/.mutt/muttrc
vim ~/.mutt/muttrc
```

```conf
# ================  IMAP ====================
set imap_user = yourusername@gmail.com
set imap_pass = yourpassword
set spoolfile = imaps://imap.gmail.com/INBOX
set folder = imaps://imap.gmail.com/
set record="imaps://imap.gmail.com/[Gmail]/Sent Mail"
set postponed="imaps://imap.gmail.com/[Gmail]/Drafts"
set mbox="imaps://imap.gmail.com/[Gmail]/All Mail"
set header_cache = "~/.mutt/cache/headers"
set message_cachedir = "~/.mutt/cache/bodies"
set certificate_file = "~/.mutt/certificates"
# ================  SMTP  ====================
set smtp_url = "smtp://yourusername@smtp.gmail.com:587/"
set smtp_pass = $imap_pass
set ssl_force_tls = yes # Require encrypted connection
# ================  Composition  ====================
set editor = "vim"      # Set your favourite editor.
set edit_headers = yes  # See the headers when editing
set charset = UTF-8     # value of $LANG; also fallback for send_charset
# Sender, email address, and sign-off line must match
unset use_domain        # because joe@localhost is just embarrassing
set realname = "Your Name"
set from = "yourusername@gmail.com"
set use_from = yes
```

### For web mail interface
```bash
sudo apt-get install roundcube roundcube-core roundcube-mysql roundcube-plugins
```

### SPAM filter service
```bash
sudo apt-get install spamassassin
sudo systemctl enable spamassassin
sudo systemctl start spamassassin
```
### Intalling mailutils
```bash
sudo apt-get install mailutils
```
### Free email client
 A lightweight and user-friendly email client developed by the GNOME project.

```bash
sudo apt install geary
sudo apt install evolution
```
### Configuring host
```bash
sudo hostnamectl set-hostname domainn.com
```

### Reconfiguring postfix
```bash
sudo dpkg-reconfigure
```
### Postfix configuraiton that changes the email storing format to Maildir
```conf
#/etc/postfix/main.cf
home_mailbox= Maildir/
```

[Dovecot configuration guide](https://ubuntu.com/server/docs/install-and-configure-dovecot)




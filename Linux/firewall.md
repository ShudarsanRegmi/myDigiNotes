## Allowing the device to access everything and disallowing others ip

`sudo ufw reset`

`sudo ufw default deny incoming`
`sudo ufw default allow outgoing`

`sudo ufw allow from 11.12.17.62`

`sudo ufw enable`
`sudo ufw status numbered`

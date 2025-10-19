## AWS Backend hosting at negces

- Nodejs backend was running on port 5000
- Nginx was forwarind traffic to :80, :443 to 5000, acting as a reverse proxy.
- pm2 was used to manage the nodejs process

```bash
[ec2-user@ip-172-31-3-159 sites-available]$ ls
express-app
```

## Nginx reverse proxy
```
server {
    if ($host = backend.negceslab.online) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name backend.negceslab.online;

    return 301 https://$host$request_uri;


}



server {
    listen 443 ssl;
    server_name backend.negceslab.online;
    ssl_certificate /etc/letsencrypt/live/backend.negceslab.online/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/backend.negceslab.online/privkey.pem; # managed by Certbot
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

}
```

## Pm2

**status**
<img width="1261" height="137" alt="image" src="https://github.com/user-attachments/assets/337c4f94-b624-4291-b037-9b7b548953e6" />


**logs**
<img width="600" height="160" alt="image" src="https://github.com/user-attachments/assets/976b3351-98d1-47c8-a508-bf612dfd5e61" />


**pm2 describe 0**

```
ec2-user@ip-172-31-3-159 sites-available]$ pm2 describe 0
 Describing process with id 0 - name express-app 
┌───────────────────┬────────────────────────────────────────────────────┐
│ status            │ online                                             │
│ name              │ express-app                                        │
│ namespace         │ default                                            │
│ version           │ 1.0.0                                              │
│ restarts          │ 2                                                  │
│ uptime            │ 2M                                                 │
│ script path       │ /home/ec2-user/negsus-lab-tracking/server/index.js │
│ script args       │ N/A                                                │
│ error log path    │ /home/ec2-user/.pm2/logs/express-app-error.log     │
│ out log path      │ /home/ec2-user/.pm2/logs/express-app-out.log       │
│ pid path          │ /home/ec2-user/.pm2/pids/express-app-0.pid         │
│ interpreter       │ node                                               │
│ interpreter args  │ N/A                                                │
│ script id         │ 0                                                  │
│ exec cwd          │ /home/ec2-user/negsus-lab-tracking/server          │
│ exec mode         │ fork_mode                                          │
│ node.js version   │ 23.6.1                                             │
│ node env          │ N/A                                                │
│ watch & reload    │ ✘                                                  │
│ unstable restarts │ 0                                                  │
│ created at        │ 2025-08-17T15:50:02.196Z                           │
└───────────────────┴────────────────────────────────────────────────────┘
 Actions available 
┌────────────────────────┐
│ km:heapdump            │
│ km:cpu:profiling:start │
│ km:cpu:profiling:stop  │
│ km:heap:sampling:start │
│ km:heap:sampling:stop  │
└────────────────────────┘
 Trigger via: pm2 trigger express-app <action_name>

 Code metrics value 
┌────────────────────────┬───────────┐
│ Used Heap Size         │ 32.88 MiB │
│ Heap Usage             │ 91.4 %    │
│ Heap Size              │ 35.98 MiB │
│ Event Loop Latency p95 │ 1.05 ms   │
│ Event Loop Latency     │ 0.33 ms   │
│ Active handles         │ 11        │
│ Active requests        │ 0         │
│ HTTP                   │ 0 req/min │
│ HTTP P95 Latency       │ 1 ms      │
│ HTTP Mean Latency      │ 0 ms      │
└────────────────────────┴───────────┘
 Divergent env variables from local env 
┌────────────────┬───────────────────────────────────────────┐
│ PWD            │ /home/ec2-user/negsus-lab-tracking/server │
│ SSH_CONNECTION │ 157.51.127.18 56082 172.31.3.159 22       │
│ XDG_SESSION_ID │ 21                                        │
│ SSH_CLIENT     │ 157.51.127.18 56082 22                    │
│ OLDPWD         │ /home/ec2-user/negsus-lab-tracking        │
└────────────────┴───────────────────────────────────────────┘

 Add your own code metrics: http://bit.ly/code-metrics
 Use `pm2 logs express-app [--lines 1000]` to display logs
 Use `pm2 env 0` to display environment variables
 Use `pm2 monit` to monitor CPU and Memory usage express-app
```


## Domain Control Panel

<img width="1011" height="380" alt="image" src="https://github.com/user-attachments/assets/c260812e-805a-45e5-aaec-29595f787e81" />


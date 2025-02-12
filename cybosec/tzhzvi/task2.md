# Tasks 

1. **Domain -> Subdomains -> IP**  
   - Identify all subdomains of a given domain.  
   - Resolve each subdomain to its corresponding IP address.  

2. **For Each IP -> Ports**  
   - Perform a port scan on each resolved IP address to find open ports.  

3. **Domain -> SPF and DMARC Record**  
   - Check and analyze the SPF (Sender Policy Framework) record of the domain.  
   - Check and analyze the DMARC (Domain-based Message Authentication, Reporting & Conformance) record of the domain.  

---

### **Framing Problems Based on This Task**  

1. **Subdomain Enumeration & IP Resolution**  
   - Given a domain (e.g., `example.com`), list all subdomains associated with it.  
   - Resolve each subdomain to its respective IP address.  
   - Tools to explore: `subfinder`, `amass`, `crt.sh`, `dnsx`, `dig`, `host`, `nslookup`.  

2. **Port Scanning on Resolved IPs**  
   - Perform a port scan on all resolved IPs.  
   - Identify open services running on these ports.  
   - Tools to explore: `nmap`, `masscan`, `rustscan`.  

3. **SPF & DMARC Record Analysis**  
   - Retrieve and analyze the SPF record of a given domain.  
   - Retrieve and analyze the DMARC record of the domain.  
   - Understand how these records affect email security and spoofing prevention.  
   - Tools to explore: `dig`, `nslookup`, `mxtoolbox`, `spf-tools`, `dmarcian`.  

---

# Solutions

## Subdomain Enumeration

### Using Amass
```bash
amass enum -d example.com
amass enum -d amrita.edu
```

### Using Subfinder
```bash
subfinder -d amrita.edu
```

#### subfinder output:
```
hpoj.cb.amrita.edu
arl.amrita.edu
www.alumninetwork.amrita.edu
pgphelpdesk.amrita.edu
aheadtestfiles.amrita.edu
vlab.amrita.edu
archive.amrita.edu
cmgmt.amrita.edu
speedtest.cb.amrita.edu
btech.amrita.edu
aums-apps-6.amrita.edu
my.cb.amrita.edu
intranet.cb.amrita.edu
amritavidya1.amrita.edu
projects.cb.amrita.edu
ample.amrita.edu
www.mbaadmissions.amrita.edu
aoap.amrita.edu
demo.ahead.amrita.edu
events.alumni.amrita.edu
intranet.av.amrita.edu
aumsam.amrita.edu
aheadonline.amrita.edu
ayurveda.amrita.edu
aumsadmin-blr.amrita.edu
cms.ahead.amrita.edu
web.amrita.edu
mail-asaskochi.amrita.edu
phd.amrita.edu
git.amrita.edu
mail1-blr.amrita.edu
smtp1-9.amrita.edu
alumninetwork.amrita.edu
aumsaims.amrita.edu
vidyalayam.amrita.edu
surveycompanies.amrita.edu
mail.my.amrita.edu
ns3.amrita.edu
oars.amrita.edu
myreport.ahead.amrita.edu
qa.ahead.amrita.edu
mun.cb.amrita.edu
cmsasb.kh.amrita.edu
sip.am.amrita.edu
lyncdiscover.am.amrita.edu
cyber.amrita.edu
mx2.aims.amrita.edu
aums-centraltest.amrita.edu
aums-students-am.amrita.edu
emap.ay.amrita.edu
landslides.amrita.edu
smtp1-8.amrita.edu
applyug.amrita.edu
asbngoconnect.cb.amrita.edu
alumni.amrita.edu
aums.amrita.edu
surveycom.amrita.edu
aheadautolab-staging.amrita.edu
ptp.amrita.edu
aheadautolab.amrita.edu
ansan.cb.amrita.edu
oceannet.amrita.edu
www.panel.anokha.amrita.edu
sree.amrita.edu
www.alumni.amrita.edu
lib.blr.amrita.edu
cmstest.cb.amrita.edu
spandanam.amrita.edu
doabuet.amrita.edu
dsp.amrita.edu
intranet.ahead.amrita.edu
staging4.cyber.amrita.edu
news.amrita.edu
cms.my.amrita.edu
verify.amrita.edu
aheadstaging.amrita.edu
aheadtest.amrita.edu
nlp.amrita.edu
cmstest.blr.amrita.edu
onlineattendance.ahead.amrita.edu
cms.kh.amrita.edu
meet.am.amrita.edu
engineering.amrita.edu
swallo.amrita.edu
www.asbngoconnect.cb.amrita.edu
dfeedback.cb.amrita.edu
tiss.blr.amrita.edu
gday.cb.amrita.edu
convocation.ch.amrita.edu
git.cb.amrita.edu
mail-amritapuri-2.amrita.edu
ns1.amrita.edu
amritavidya-am-student.amrita.edu
am.amrita.edu
convocation.amrita.edu
aums-am.amrita.edu
aumsblr.amrita.edu
my.amrita.edu
mail-amritapuri-1.amrita.edu
cms.blr.amrita.edu
aumscb.amrita.edu
staging3.cyber.amrita.edu
aims.amrita.edu
gel.amrita.edu
intranet.kh.amrita.edu
ftp.aims.amrita.edu
lews.amrita.edu
lists.amrita.edu
blr.amrita.edu
helpdesk.amrita.edu
admission.amrita.edu
aaps.amrita.edu
mites.amrita.edu
asbmbaconnect.cb.amrita.edu
oap.amrita.edu
track.amrita.edu
applypg.amrita.edu
aee.amrita.edu
www.chennai.amrita.edu
sso.amrita.edu
imapsync.cb.amrita.edu
aheadlms.cb.amrita.edu
amritavidya-am.amrita.edu
acgdoa.amrita.edu
test.ahead.amrita.edu
www.amritavidya1.amrita.edu
anokha.amrita.edu
aheadstagingfiles.amrita.edu
amritapuri.amrita.edu
mail.amrita.edu
corelab.cb.amrita.edu
aumsapp-aims.amrita.edu
gateway-am.amrita.edu
amritavidya.amrita.edu
research.amrita.edu
kripa.amrita.edu
events.amrita.edu
ahms.blr.amrita.edu
amritavidya-aims.amrita.edu
autolab.am.amrita.edu
cms.ch.amrita.edu
pragati.amrita.edu
sreedb.amrita.edu
aums-blr.amrita.edu
webext.am.amrita.edu
olp.amrita.edu
aoapm.amrita.edu
cms.cb.amrita.edu
web-blr.amrita.edu
myreport.cyber.amrita.edu
my.blr.amrita.edu
empower.amrita.edu
vidyut.amrita.edu
intranet.blr.amrita.edu
cms.av.amrita.edu
tantrotsav.amrita.edu
www.ctf.cb.amrita.edu
etrack.blr.amrita.edu
leap.amrita.edu
panel.anokha.amrita.edu
ctf.cb.amrita.edu
aeee.amrita.edu
ns4.amrita.edu
cmsagri.cb.amrita.edu
mtech.amrita.edu
ay.amrita.edu
aumscn.amrita.edu
cmstest.ch.amrita.edu
chennai.amrita.edu
events.asas.kh.amrita.edu
beta.amrita.edu
intranet.ch.amrita.edu
aheadonlinefiles.amrita.edu
dev.ahead.amrita.edu
convocation.cb.amrita.edu
csotraining.amrita.edu
cardiogpt.projects.amrita.edu
www.archive.amrita.edu
www.anokha.amrita.edu
www.admissions.amrita.edu
mail2.amrita.edu
admissions.amrita.edu
aheadhelpdesk.amrita.edu
amritawallet.cb.amrita.edu
ns2.amrita.edu
www.amrita.edu
aums-apps-pp.amrita.edu
spotlight.amrita.edu
speedtest.ch.amrita.edu
mbaadmissions.amrita.edu
www2.amrita.edu
```

### Using subfinder with different options
```bash
subfinder -d amrita.edu | htpx # filtering out live sub domains
subfinder -d amrita.edu | httpx -silent -title -status-code # output for this command is shown below
```

```
Enumerating subdomains for amrita.edu
[INF] Found 212 subdomains for amrita.edu in 1 minute 391 milliseconds
https://aheadhelpdesk.amrita.edu [302] [302 Found]
https://aeee.amrita.edu [200] [Amrita – Btech]
http://ansan.cb.amrita.edu [200] [Apache2 Ubuntu Default Page: It works]
https://aee.amrita.edu [404] [404: This page could not be found.]
https://aoap.amrita.edu [302] [Amrita Online Admissions Portal]
https://aaps.amrita.edu [302] [Amrita Online Admissions Portal]
https://applypg.amrita.edu [302] [Redirecting to https://applypg.amrita.edu/home]
https://alumni.amrita.edu [200] [Home 2024 - Amrita Alumni]
https://aheadonline.amrita.edu [302] [302 Found]
https://aheadtestfiles.amrita.edu [302]
https://applyug.amrita.edu [302] [Redirecting to https://applyug.amrita.edu/home]
http://acgdoa.amrita.edu [301] [301 Moved Permanently]
http://aheadonlinefiles.amrita.edu [302] [302 Found]
http://anokha.amrita.edu [301] [301 Moved Permanently]
http://asmfeedback.cb.amrita.edu [301] [301 Moved Permanently]
http://aeestaging.amrita.edu [301] [301 Moved Permanently]
http://asbngoconnect.cb.amrita.edu [301]
http://admissions.amrita.edu [301] [301 Moved Permanently]
http://archive.amrita.edu [301] [301 Moved Permanently]
http://ample.amrita.edu [301] [301 Moved Permanently]
http://aheadtest.amrita.edu [302] [302 Found]
http://aumsblr.amrita.edu [302]
http://chennai.amrita.edu [301] [301 Moved Permanently]
http://aumscb.amrita.edu [302]
http://cms.ahead.amrita.edu [301] [301 Moved Permanently]
http://cms.ch.amrita.edu [301] [301 Moved Permanently]
http://aumscn.amrita.edu [302]
http://cms.av.amrita.edu [301] [301 Moved Permanently]
http://cms.kh.amrita.edu [301] [301 Moved Permanently]
http://cms.cb.amrita.edu [301] [301 Moved Permanently]
http://cms.blr.amrita.edu [301] [301 Moved Permanently]
http://btech.amrita.edu [301] [301 Moved Permanently]
https://cmstest.cb.amrita.edu [302] [Redirecting to https://cmstest.cb.amrita.edu/login]
http://ay.amrita.edu [200] [403 Forbidden]
https://cmsagri.cb.amrita.edu [302] [Redirecting to https://cmsagri.cb.amrita.edu/login]
https://cms.my.amrita.edu [302] [Redirecting to https://cms.my.amrita.edu/login]
https://ctf.cb.amrita.edu [200] [AFAIK]
https://cmstest.ch.amrita.edu [302] [Redirecting to https://cmstest.ch.amrita.edu/login]
https://csotraining.amrita.edu [302]
https://cmsasb.kh.amrita.edu [302] [Redirecting to https://cmsasb.kh.amrita.edu/login]
https://cmstest.blr.amrita.edu [302] [Redirecting to https://cmstest.blr.amrita.edu/login]
https://convocation.cb.amrita.edu [200] [Convocation - 2024]
https://convocation.ch.amrita.edu [302]
https://cyber.amrita.edu [200] [This is the default server vhost]
https://corelab.cb.amrita.edu [200] [Home | Amrita CORE Lab]
https://demo.ahead.amrita.edu [302]
https://empower.amrita.edu [200] [Empower Community]
https://dfeedback.cb.amrita.edu [302]
https://doabuet.amrita.edu [302] [Redirecting to https://doabuet.amrita.edu/login]
https://demofiles.ahead.amrita.edu [302]
https://events.alumni.amrita.edu [200] [Amrita Vishwa Vidyapeetham]
https://dsp.amrita.edu [200] [Digital Social Platform]
https://git.amrita.edu [302]
https://gel.amrita.edu [200] [Gel-IoT]
https://feedback.cb.amrita.edu [302]
https://intranet.av.amrita.edu [200] [Home | Intranet Amrita Vishwa Vidyapeetham - Amaravati Campus]
https://kripa.amrita.edu [200] [amrita_kripa]
https://helpdesk.amrita.edu [200] [AOC Support]
http://lib.blr.amrita.edu [200] [Koha online catalog]
https://emap.ay.amrita.edu [200] [Home - Online e-Learning Module Application for Panchakarma]
https://events.amrita.edu [200] [Event Portal - Login]
https://intranet.ch.amrita.edu [200] [Home | Intranet | Amrita Vishwa Vidyapeetham - Chennai Campus]
https://feedback.av.amrita.edu [403] [HTTP Server Test Page powered by CentOS]
https://lmsupgrade.ahead.amrita.edu [302]
https://leap.amrita.edu [302] [302 Found]
https://intranet.cb.amrita.edu [200] [Home | Intranet Amrita Vishwa Vidyapeetham - Coimbatore Campus]
https://ignite.cb.amrita.edu [502] [502 Bad Gateway]
https://hpoj.cb.amrita.edu [302]
https://lews.amrita.edu [303]
https://lists.amrita.edu [302] [302 Found]
https://intranet.ahead.amrita.edu [302]
https://imapsync.cb.amrita.edu [200] [AVVP:: CBE::IMAPSYNC || Email migration to O365 | IMAPSYNC | Amrita Vishwa Vidyapeetham]
http://lmsupgradefiles.ahead.amrita.edu [302]
http://mbaadmissions.amrita.edu [301] [301 Moved Permanently]
http://intranet.kh.amrita.edu [301] [301 Moved Permanently]
http://mail-amritapuri-2.amrita.edu [200]
https://my.cb.amrita.edu [200]
http://mtech.amrita.edu [301]
http://landslides.amrita.edu [301] [301 Moved Permanently]
https://onlineattendance.ahead.amrita.edu [200] [ERROR]
https://oap.amrita.edu [] [WordPress › Error]
https://olp.amrita.edu [200] [Redirecting to OARS- Btech Admissions!!]
https://myreport.cyber.amrita.edu [200] [Amrita Vishwa Vidyapeetham]
https://my.amrita.edu [302]
https://projects.cb.amrita.edu [403] [403 Forbidden]
https://qa.ahead.amrita.edu [] [We're sorry, but something went wrong: Web application could not be started]
https://myreport.ahead.amrita.edu [200] [Amrita Vishwa Vidyapeetham]
https://ptp.amrita.edu [200] [Amrita Publication Tracking Portal]
https://pragati.amrita.edu [404] [Error]
https://oceannet.amrita.edu [200] [{{strings.ocean_net}}]
https://phd.amrita.edu [200] [Amrita PhD. 2024]
https://pgphelpdesk.amrita.edu [200] [pgphelpdesk.amrita.edu]
http://intranet.blr.amrita.edu [200] [Home | iNTRANET]
http://mail-asaskochi.amrita.edu [200] [Amrita Vishwa Vidyapeetham - Kochi Campus]
http://mun.cb.amrita.edu [200] [Welcome to nginx!]
http://nlp.amrita.edu [301] [301 Moved Permanently]
https://spandanam.amrita.edu [200] [Amrita Spandanam]
http://speedtest.cb.amrita.edu [301] [301 Moved Permanently]
http://sree.amrita.edu [301] [301 Moved Permanently]
http://vidyut.amrita.edu [301] [301 Moved Permanently]
http://swallo.amrita.edu [301] [301 Moved Permanently]
http://spotlight.amrita.edu [301] [301 Moved Permanently]
http://staging.amrita.edu [301] [301 Moved Permanently]
http://test.ahead.amrita.edu [302] [302 Found]
https://www.ctf.cb.amrita.edu [301] [301 Moved Permanently]
http://staging4.cyber.amrita.edu [301]
http://tantrotsav.amrita.edu [301] [301 Moved Permanently]
http://verify.amrita.edu [302] [302 Found]
http://smtp1-8.amrita.edu [200]
http://smtp1-9.amrita.edu [200]
https://webfiles.amrita.edu [403]
https://www.anokha.amrita.edu [403] [403 Forbidden]
http://sreedb.amrita.edu [302] [302 Found]
http://surveycom.amrita.edu [200] [403 Forbidden]
http://vidyalayam.amrita.edu [200] [Welcome to nginx!]
http://speedtest.ch.amrita.edu [301] [301 Moved Permanently]
https://www.alumni.amrita.edu [301]
https://www.asbngoconnect.cb.amrita.edu [404]
https://www.amrita.edu [200] [Deemed University - Private University in India | Amrita Vishwa Vidyapeetham]
http://track.amrita.edu [200]
http://staging3.cyber.amrita.edu [301]
http://surveycompanies.amrita.edu [200] [403 Forbidden]
https://vlab.amrita.edu [200] [Amrita Vishwa Vidyapeetham Virtual Lab]
https://www.admissions.amrita.edu [301] [301 Moved Permanently]
https://www.alumninetwork.amrita.edu [200] [Amrita University]
https://www.chennai.amrita.edu [200] [Amrita Institutions]
https://www.archive.amrita.edu [200] [Amrita Vishwa Vidyapeetham]
http://web-blr.amrita.edu [200] [AUMS Login Page]
```



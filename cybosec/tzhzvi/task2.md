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

#### Exploring other important commands of amass

##### Passive Enumeration (finding from passive sources, not direct scan on host)
```bash
amass enum -passive -d amrita.edu
```
##### Output

```bash
amrita.edu
www.alumni.amrita.edu
files.amrita.edu
asmfeedback.cb.amrita.edu
www.ctf.cb.amrita.edu
swallo.amrita.edu
my.cb.amrita.edu
corelab.cb.amrita.edu
leap.amrita.edu
csotraining.amrita.edu
aheadhelpdesk.amrita.edu
asbngoconnect.cb.amrita.edu
cms.ch.amrita.edu
mun.cb.amrita.edu
dsp.amrita.edu
cms.kh.amrita.edu
cmsasb.kh.amrita.edu
aheadonlinefiles.amrita.edu
aheadtestfiles.amrita.edu
landslides.amrita.edu
intranet.cb.amrita.edu
track.amrita.edu
git.amrita.edu
ay.amrita.edu
emap.ay.amrita.edu
pgphelpdesk.amrita.edu
vlab.amrita.edu
ignite.cb.amrita.edu
webfiles.amrita.edu
intranet.ch.amrita.edu
cmstest.ch.amrita.edu
cms.cb.amrita.edu
kripa.amrita.edu
test.ahead.amrita.edu
intranet.ahead.amrita.edu
spandanam.amrita.edu
cms.ahead.amrita.edu
nlp.amrita.edu
demo.ahead.amrita.edu
doaems.amrita.edu
oap.amrita.edu
events.alumni.amrita.edu
gel.amrita.edu
cmsagri.cb.amrita.edu
www.asbngoconnect.cb.amrita.edu
aheadautolab.amrita.edu
lists.amrita.edu
ansan.cb.amrita.edu
aee.amrita.edu
tantrotsav.amrita.edu
myreport.cyber.amrita.edu
phd.amrita.edu
aumsapp-aims.amrita.edu
www.sso.amrita.edu
doabuet.amrita.edu
aeestaging.amrita.edu
lews.amrita.edu
sree.amrita.edu
onlineattendance.ahead.amrita.edu
feedback.av.amrita.edu
speedtest.cb.amrita.edu
vidyut.amrita.edu
sso.amrita.edu
empower.amrita.edu
aheadtest.amrita.edu
acgdoa.amrita.edu
pragati.amrita.edu
hpoj.cb.amrita.edu
ctf.cb.amrita.edu
cirpms.amrita.edu
convocation.cb.amrita.edu
projects.cb.amrita.edu
aeee.amrita.edu
anokha.amrita.edu
dfeedback.cb.amrita.edu
qa.ahead.amrita.edu
aheadonline.amrita.edu
speedtest.ch.amrita.edu
oceannet.amrita.edu
myreport.ahead.amrita.edu
cms.blr.amrita.edu
sreedb.amrita.edu
cms.av.amrita.edu
mbaadmissions.amrita.edu
intranet.av.amrita.edu
alumni.amrita.edu
www.amrita.edu
mites.amrita.edu
www.amritapuri.amrita.edu
arl.amrita.edu
helpdesk.amrita.edu
biotech.amrita.edu
news.amrita.edu
web.amrita.edu
www2.amrita.edu
ns1.amrita.edu
aums.amrita.edu
vidyalayam.amrita.edu
engineering.amrita.edu
archive.amrita.edu
aums-apps-pp.amrita.edu
multimedia.amrita.edu
www.biotech.amrita.edu
am.amrita.edu
admission.amrita.edu
ns2.amrita.edu
aims.amrita.edu
admissions.amrita.edu
amritapuri.amrita.edu
ns3.amrita.edu
www.anokha.amrita.edu
mail-blr.amrita.edu
oars.amrita.edu
olp.amrita.edu
cb.amrita.edu
www.engineering.amrita.edu
ayurveda.amrita.edu
tedx.amrita.edu
blr.amrita.edu
research.amrita.edu
events.amrita.edu
smtp1-8.amrita.edu
etrack.blr.amrita.edu
my.amrita.edu
mail-amritapuri-1.amrita.edu
aums-blr.amrita.edu
aoapm.amrita.edu
cardiogpt.projects.amrita.edu
amritawallet.cb.amrita.edu
aums-am.amrita.edu
www.aims.amrita.edu
mtech.amrita.edu
staging4.cyber.amrita.edu
www.olp.amrita.edu
amritavidya1.amrita.edu
mail-asaskochi.amrita.edu
surveycompanies.amrita.edu
www.panel.anokha.amrita.edu
amritavidya-aims.amrita.edu
aumsadmin-blr.amrita.edu
amritavidya-am.amrita.edu
ample.amrita.edu
aheadlms.cb.amrita.edu
imapsync.cb.amrita.edu
cmstest.cb.amrita.edu
cms.my.amrita.edu
autolab.am.amrita.edu
cmstest.blr.amrita.edu
aumscn.amrita.edu
btech.amrita.edu
chennai.amrita.edu
cmgmt.amrita.edu
panel.anokha.amrita.edu
events.asas.kh.amrita.edu
aums-centraltest.amrita.edu
aheadstagingfiles.amrita.edu
aaps.amrita.edu
aumsaims.amrita.edu
aums-students-am.amrita.edu
amritavidya-am-student.amrita.edu
ptp.amrita.edu
sip.am.amrita.edu
staging3.cyber.amrita.edu
www.ayurveda.amrita.edu
asas.kh.amrita.edu
mail2.amrita.edu
convocation.amrita.edu
mail1-blr.amrita.edu
lyncdiscover.am.amrita.edu
intranet.kh.amrita.edu
aheadstaging.amrita.edu
verify.amrita.edu
mail-asas.kh.amrita.edu
mx1.aims.amrita.edu
convocation.ch.amrita.edu
my.blr.amrita.edu
git.cb.amrita.edu
aumsam.amrita.edu
www.chennai.amrita.edu
aheadautolab-staging.amrita.edu
aums-aims.amrita.edu
ns4.amrita.edu
ahms.blr.amrita.edu
beta.amrita.edu
www.nlp.amrita.edu
tiss.blr.amrita.edu
aumsblr.amrita.edu
smtp1-9.amrita.edu
dev.ahead.amrita.edu
cyber.amrita.edu
gateway-blr.amrita.edu
web-blr.amrita.edu
www.admissions.amrita.edu
contest.amrita.edu
aoap.amrita.edu
intranet.blr.amrita.edu
ftp.aims.amrita.edu
lib.blr.amrita.edu
gday.cb.amrita.edu
mail-amritapuri-2.amrita.edu
mail.amrita.edu
spotlight.amrita.edu
gateway-am.amrita.edu
amritavidya.amrita.edu
surveycom.amrita.edu
aums-apps-6.amrita.edu
asbmbaconnect.cb.amrita.edu
mx2.aims.amrita.edu
aumscb.amrita.edu
mail.my.amrita.edu
applymtech.amrita.edu
sysadmin.amrita.edu
applyug.amrita.edu
students.amrita.edu
csap.amrita.edu
swagatham.amrita.edu
applypg.amrita.edu

The enumeration has finished
Discoveries are being migrated into the local database
```


##### Agressive active enumeration using amsss
```bash
amass enum -active -d amrita.edu
```
##### Output
```

```

##


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
##### Brute forcing for more subdomains
```bash
amass enum -brute -d amrita.edu
```
##### Output
```
ns1.amrita.edu
ns3.amrita.edu
amrita.edu
my.amrita.edu
helpdesk.amrita.edu
cirpms.amrita.edu
doaems.amrita.edu
lews.amrita.edu
students.amrita.edu
ctf.cb.amrita.edu
ns4.amrita.edu
vidyut.amrita.edu
aumscb.amrita.edu
aumsadmin-blr.amrita.edu
swallo.amrita.edu
myreport.ahead.amrita.edu
admissions.amrita.edu
oceannet.amrita.edu
test.ahead.amrita.edu
leap.amrita.edu
alumni.amrita.edu
cms.cb.amrita.edu
sreedb.amrita.edu
doabuet.amrita.edu
aheadtestfiles.amrita.edu
spandanam.amrita.edu
hpoj.cb.amrita.edu
nlp.amrita.edu
archive.amrita.edu
kripa.amrita.edu
cmsasb.kh.amrita.edu
careers.amrita.edu
beta.amrita.edu
ignite.cb.amrita.edu
dfeedback.cb.amrita.edu
oap.amrita.edu
demo.ahead.amrita.edu
projects.cb.amrita.edu
aums-blr.amrita.edu
cms.av.amrita.edu
btech.amrita.edu
cms.ahead.amrita.edu
aums-am.amrita.edu
asmfeedback.cb.amrita.edu
feedback.av.amrita.edu
track.amrita.edu
phd.amrita.edu
ample.amrita.edu
www.amrita.edu
intranet.av.amrita.edu
intranet.ahead.amrita.edu
gel.amrita.edu
ansan.cb.amrita.edu
qa.ahead.amrita.edu
pragati.amrita.edu
mtech.amrita.edu
aums-centraltest.amrita.edu
csap.amrita.edu
swagatham.amrita.edu
my.cb.amrita.edu
pgphelpdesk.amrita.edu
csotraining.amrita.edu
convocation.cb.amrita.edu
git.amrita.edu
chennai.amrita.edu
aheadhelpdesk.amrita.edu
amritavidya.amrita.edu
cyber.amrita.edu
lists.amrita.edu
landslides.amrita.edu
aheadtest.amrita.edu
amritavidya1.amrita.edu
aaps.amrita.edu
aheadonlinefiles.amrita.edu
mun.cb.amrita.edu
corelab.cb.amrita.edu
aheadonline.amrita.edu
www.ctf.cb.amrita.edu
smtp1-8.amrita.edu
aoap.amrita.edu
dsp.amrita.edu
applymtech.amrita.edu
aums.amrita.edu
intranet.ch.amrita.edu
acgdoa.amrita.edu
asbmbaconnect.cb.amrita.edu
speedtest.ch.amrita.edu
applypg.amrita.edu
empower.amrita.edu
sree.amrita.edu
vidyalayam.amrita.edu
myreport.cyber.amrita.edu
applyug.amrita.edu
tantrotsav.amrita.edu
aums-apps-pp.amrita.edu
cms.ch.amrita.edu
imapsync.cb.amrita.edu
aums-students-am.amrita.edu
cmstest.ch.amrita.edu
aumscn.amrita.edu
verify.amrita.edu
onlineattendance.ahead.amrita.edu
cmgmt.amrita.edu
care.amrita.edu
smtp1-9.amrita.edu
surveycom.amrita.edu
amritawallet.cb.amrita.edu
ay.amrita.edu
amritavidya2.amrita.edu
emap.ay.amrita.edu
vlab.amrita.edu
cmstest.cb.amrita.edu
surveycompanies.amrita.edu
amritavidya-am.amrita.edu
olp.amrita.edu
speedtest.cb.amrita.edu
staging4.cyber.amrita.edu
demofiles.ahead.amrita.edu
anokha.amrita.edu
aumsam.amrita.edu
convocation.ch.amrita.edu
www.alumni.amrita.edu
staging3.cyber.amrita.edu
www.olp.amrita.edu
dev.ahead.amrita.edu
aheadautolab.amrita.edu
www.amritapuri.amrita.edu
am.amrita.edu
mail-amritapuri-1.amrita.edu
intranet.cb.amrita.edu
ptp.amrita.edu
www2.amrita.edu
www.ayurveda.amrita.edu
amritapuri.amrita.edu
gateway-am.amrita.edu
www.aims.amrita.edu
web.amrita.edu
ns2.amrita.edu
arl.amrita.edu
news.amrita.edu
aims.amrita.edu
ayurveda.amrita.edu
multimedia.amrita.edu
dastaan.amrita.edu
research.amrita.edu
aums-attapp-cb.amrita.edu
blr.amrita.edu
lmsupgrade.ahead.amrita.edu
www.nlp.amrita.edu
cms.my.amrita.edu
cms.kh.amrita.edu
biotech.amrita.edu
kalanjali.blr.amrita.edu
cmsagri.cb.amrita.edu
cardiogpt.projects.amrita.edu
www.chennai.amrita.edu
web-blr.amrita.edu
noreply.amrita.edu
admission.amrita.edu
staging.amrita.edu
intranet.kh.amrita.edu
engineering.amrita.edu
mail-asas.kh.amrita.edu
www.biotech.amrita.edu
aumsblr.amrita.edu
lmsupgradefiles.ahead.amrita.edu
mail-asaskochi.amrita.edu
cmstest.blr.amrita.edu
www.engineering.amrita.edu
lib.blr.amrita.edu
intranet.blr.amrita.edu
www.archive.amrita.edu
feedback.cb.amrita.edu
www.anokha.amrita.edu
mail-amritapuri-2.amrita.edu
www.admissions.amrita.edu
events.amrita.edu
events.alumni.amrita.edu
spotlight.amrita.edu
aee.amrita.edu
events.asas.kh.amrita.edu
aeestaging.amrita.edu
aeee.amrita.edu
aumsaims.amrita.edu
autolab.am.amrita.edu
alumninetwork.amrita.edu
etrack.blr.amrita.edu
www.alumninetwork.amrita.edu
tiss.blr.amrita.edu
bams.amrita.edu
cms.blr.amrita.edu
ftp.aims.amrita.edu
my.blr.amrita.edu
webfiles.amrita.edu
ahms.blr.amrita.edu
amritavidya-aims.amrita.edu
oars.amrita.edu
mbaadmissions.amrita.edu
aumsapp-aims.amrita.edu
mail.my.amrita.edu
autodiscover.amrita.edu

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

## Finding out Ips from those subdomains

### Using dig on list of subdomains
```bash
cat subdomains.txt | xargs -I{} dig +short {}
```
#### Output
```
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
103.10.27.3
14.139.187.131
103.10.24.200
76.223.83.62
75.2.112.164
103.10.24.250
123.63.2.21
103.10.27.53
103.10.27.53
103.10.24.180
103.10.24.244
103.10.27.21
;; communications error to 8.8.8.8#53: timed out
103.5.112.81
3.111.88.252
103.10.27.6
14.99.5.163
210.212.205.22
65.1.125.240
;; communications error to 8.8.8.8#53: timed out
103.10.27.51
103.10.24.196
103.10.24.222
103.10.27.49
103.10.27.50
160.153.0.37
103.10.27.7
103.10.24.177
103.10.27.53
123.63.2.3
103.10.24.222
103.10.27.16
103.10.27.12
103.10.24.196
65.1.125.240
103.10.27.24
103.10.24.251
13.126.34.10
103.10.27.57
103.10.27.9
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
;; no servers could be reached
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
103.10.27.48
103.10.27.32
14.99.5.164
103.10.27.40
103.10.24.196
103.10.27.47
103.10.24.239
103.10.27.17
103.10.27.40
103.96.100.9
103.10.27.8
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
103.10.24.210
75.2.112.164
76.223.83.62
103.10.27.5
103.10.27.47
65.1.125.240
103.10.27.30
103.10.27.41
103.10.27.33
35.213.147.113
103.10.24.182
103.10.24.249
103.10.24.250
103.10.27.9
103.10.27.9
;; communications error to 8.8.8.8#53: timed out
103.10.27.47
103.10.27.10
103.10.27.16
103.10.27.8
103.10.27.46
103.5.112.83
35.213.181.61
103.10.27.4
65.1.125.240
123.63.2.3
103.5.112.83
14.139.187.132
103.10.24.229
103.10.27.42
103.10.27.34
103.10.27.10
103.10.27.42
ctf.cb.amrita.edu.
103.10.27.21
103.96.100.8
103.10.24.229
65.1.125.240
103.10.24.199
103.5.112.83
117.240.224.6
14.139.187.132
136.233.45.116
103.10.27.19
103.10.27.9
136.233.45.116
103.10.24.199
;; communications error to 8.8.8.8#53: timed out
65.1.125.240
65.1.125.240
103.10.24.230
103.10.27.51
103.10.24.199
136.233.45.118
103.10.24.203
136.233.45.114
103.10.27.9
103.10.24.203
136.233.45.115
103.10.24.240
103.10.24.252
103.10.27.43
15.206.14.91
103.10.24.196
;; communications error to 8.8.8.8#53: timed out
103.96.100.9
103.10.24.204
103.10.27.29
103.10.24.204
14.139.187.132
103.5.112.83
123.63.2.7
123.63.2.7
103.10.27.25
surveycom.amrita.edu.
103.10.24.204
103.10.24.227
103.10.27.11
103.10.27.9
35.213.181.61
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
103.10.27.48
103.10.27.15
103.10.24.185
180.235.122.221
alumni.amrita.edu.
160.153.0.37
35.213.181.61
olp.amrita.edu.
103.10.27.11
103.10.27.45
103.10.27.44
amritapuri.amrita.edu.
117.193.77.235
117.193.77.235
117.193.77.233
103.10.27.5
103.10.24.229
ahs-amrita.amrita.ac.in.
117.193.77.235
ahs-amrita.amrita.ac.in.
117.193.77.235
117.193.77.235
103.10.24.194
ahs-amrita.amrita.ac.in.
117.193.77.235
117.193.77.235
117.193.77.232
117.193.77.235
ahs-amrita.amrita.ac.in.
117.193.77.235
117.193.77.235
117.193.77.235
117.193.77.235
35.154.181.106
117.193.77.235
103.10.27.8
117.193.77.235
103.10.27.56
nlp.amrita.edu.
103.10.27.12
;; communications error to 8.8.8.8#53: timed out
117.239.140.30
117.240.92.21
118.185.69.3
ahs-amrita.amrita.ac.in.
117.193.77.235
210.212.205.27
;; communications error to 8.8.8.8#53: timed out
103.10.27.17
4.224.104.228
chennai.amrita.edu.
103.10.27.8
210.212.205.26
103.10.27.38
ahs-amrita.amrita.ac.in.
117.193.77.235
Amrita-Staging-546766107.ap-south-1.elb.amazonaws.com.
3.7.14.31
3.110.21.211
118.185.69.1
117.240.92.20
ahs-amrita.amrita.ac.in.
117.193.77.235
117.240.92.20
ahs-amrita.amrita.ac.in.
117.193.77.235
61.12.92.70
210.212.205.21
103.10.27.56
117.240.92.20
210.212.205.30
ahs-amrita.amrita.ac.in.
117.193.77.235
210.212.205.25
210.212.205.29
archive.amrita.edu.
103.10.24.196
anokha.amrita.edu.
103.10.27.15
103.10.24.205
admissions.amrita.edu.
103.10.24.196
;; communications error to 8.8.8.8#53: timed out
123.63.2.25
13.228.96.213
13.200.186.109
aoap-prod-alb-291806959.ap-south-1.elb.amazonaws.com.
13.127.48.139
3.109.161.58
118.185.69.1
d3rc06r25oxu7w.cloudfront.net.
18.161.229.21
18.161.229.29
18.161.229.58
18.161.229.84
d1ldw8mvn6uyu6.cloudfront.net.
52.84.12.8
52.84.12.16
52.84.12.80
52.84.12.13
14.98.204.4
182.19.48.20
portaldns.almashines.com.
52.74.41.140
61.12.92.68
portaldns.almashines.com.
52.74.41.140
61.12.92.68
;; communications error to 8.8.8.8#53: timed out
amselb-799089873.ap-south-1.elb.amazonaws.com.
43.204.57.221
13.234.96.38
61.12.92.65
;; communications error to 8.8.8.8#53: timed out
111.93.114.99
61.12.92.66
d3m6x37ly4ajuw.cloudfront.net.
18.161.246.11
18.161.246.10
18.161.246.68
18.161.246.76
61.12.92.68
115.113.235.120
115.113.235.119
amrita-282.nopaperforms.com.
prodvpc-web-lb6-141531396.ap-south-1.elb.amazonaws.com.
35.154.13.57
65.1.71.148
3.108.47.12
aums.kubewaf.com.
dcyjpo4vfeak6.cloudfront.net.
108.158.251.38
108.158.251.45
108.158.251.16
108.158.251.23
58.68.57.52
autodiscover.outlook.com.
atod-g2.tm-4.office.com.
40.99.8.232
40.99.34.168
52.98.86.168
40.99.60.232
52.98.87.72
40.100.137.248
40.99.34.152
40.99.71.216
```

### Using dig tool

```bash
cat subdomains.txt | xargs -I{} dig +short {}
```

```
111.93.99.174
52.84.12.8
52.84.12.80
52.84.12.16
52.84.12.13
160.153.0.37
103.10.27.30
103.10.27.25
103.10.24.229
103.10.27.8
103.10.24.199
103.10.27.9
103.10.27.15
123.63.2.25
103.10.27.19
103.10.24.229
103.5.112.83
14.139.187.132
103.10.27.21
117.239.140.30
103.10.27.44
103.10.24.199
103.10.27.53
103.10.27.45
103.10.27.46
103.10.27.48
35.213.181.61
103.10.27.48
103.10.24.249
103.10.27.47
117.193.77.235
75.2.112.164
76.223.83.62
103.10.27.42
18.161.229.21
18.161.229.29
61.12.92.70
18.161.229.58
210.212.205.21
18.161.229.84
180.235.122.221
123.63.2.3
103.10.27.53
117.240.224.6
14.139.187.132
103.10.24.203
103.5.112.83
65.1.125.240
103.10.24.251
3.109.161.58
13.127.48.139
103.10.27.29
136.233.45.114
103.5.112.83
103.10.24.196
103.5.112.83
14.139.187.132
117.240.224.6
103.10.24.239
103.10.24.227
123.63.2.3
182.19.48.20
117.193.77.235
115.113.235.120
65.1.125.240
14.99.5.163
210.212.205.22
103.10.27.6
103.10.24.196
103.10.27.24
61.12.92.68
103.10.24.204
103.10.27.40
117.193.77.235
103.10.24.182
136.233.45.115
117.193.77.235
103.10.24.185
117.193.77.235
103.10.27.10
118.185.69.3
117.240.92.21
111.93.114.99
61.12.92.68
103.10.27.7
103.10.24.196
13.228.96.213
4.224.104.228
103.10.27.5
103.10.27.5
65.1.125.240
103.10.24.199
103.10.27.53
103.10.27.47
43.204.57.221
13.234.96.38
103.10.27.17
103.10.27.17
15.206.14.91
13.126.34.10
65.1.125.240
61.12.92.65
103.10.27.9
103.10.27.47
117.193.77.235
103.10.27.16
210.212.205.27
65.1.125.240
117.240.92.20
118.185.69.1
123.63.2.21
103.10.27.8
103.10.27.9
103.10.24.203
118.185.69.1
136.233.45.116
103.10.24.205
103.10.24.250
103.10.27.3
14.139.187.131
117.193.77.232
117.240.92.20
58.68.57.52
103.10.27.51
103.10.24.210
103.10.27.56
103.10.27.9
136.233.45.116
103.10.24.229
103.10.27.56
103.10.27.51
117.240.92.20
117.193.77.235
136.233.45.118
35.213.181.61
65.1.125.240
65.1.125.240
103.10.27.41
3.111.88.252
123.63.2.7
61.12.92.68
103.10.24.222
117.193.77.235
103.10.24.250
103.10.24.230
75.2.112.164
76.223.83.62
103.10.24.204
103.10.24.196
103.10.24.204
103.10.27.15
103.96.100.9
3.110.21.211
3.7.14.31
108.158.221.81
108.158.221.12
108.158.221.41
108.158.221.26
103.10.27.8
103.10.24.196
103.10.24.244
117.193.77.235
103.10.24.252
117.193.77.235
103.10.27.11
52.74.41.140
103.10.27.42
117.193.77.235
160.153.0.37
35.213.181.61
103.10.24.194
117.193.77.235
103.10.27.21
103.10.27.49
210.212.205.26
103.10.27.12
117.193.77.235
111.93.99.167
103.10.24.240
117.193.77.235
103.10.24.196
103.10.27.10
40.99.34.200
52.74.41.140
14.98.204.4
40.99.34.248
123.63.2.7
35.154.181.106
52.98.56.216
52.98.87.248
210.212.205.30
103.10.27.7
108.158.251.38
108.158.251.45
108.158.251.16
108.158.251.23
103.10.27.50
103.10.27.51
103.10.27.16
103.10.27.57
103.10.27.40
210.212.205.25
103.10.27.4
210.212.205.29
103.10.24.200
103.10.24.180
103.10.27.12
103.10.27.8
103.10.27.33
61.12.92.66
117.193.77.235
103.10.27.34
103.5.112.81
115.113.235.119
103.10.24.177
103.10.27.11
111.93.99.172
117.193.77.235
103.10.24.222
103.10.27.9
103.96.100.9
103.10.27.9
103.10.27.43
65.1.71.148
3.108.47.12
35.154.13.57
103.96.100.8
103.10.27.32
13.200.186.109
111.93.99.174
35.213.147.113
103.10.27.38
```

### Getting with proper mapping using dnsx and aux
```bash
cat subdomains.txt | dnsx -a -resp | awk '{print $1, "->", $NF}'
cat subdomains.txt | dnsx -a -resp # this too gave mapping when tried later
```

### Output
```
archive.amrita.edu -> [103.10.24.196]
aums-apps-pp.amrita.edu -> [103.10.24.203]
amritapuri.amrita.edu -> [117.193.77.235]
aums-am.amrita.edu -> [103.10.24.239]
aee.amrita.edu -> [3.109.161.58]
aee.amrita.edu -> [13.127.48.139]
aeestaging.amrita.edu -> [18.161.229.21]
aheadonlinefiles.amrita.edu -> [103.10.27.42]
```


## Port Scanning

### Using naabu 

```bash
61.12.92.66:443
180.235.122.221:80
75.2.112.164:80
75.2.112.164:80
103.10.27.21:443
ctf.cb.amrita.edu.:443
103.10.27.21:443
117.239.140.30:443
103.10.27.21:8081
ctf.cb.amrita.edu.:8081
103.10.27.21:8081
136.233.45.116:80
136.233.45.116:80
35.213.181.61:995
35.213.181.61:995
103.10.27.21:80
ctf.cb.amrita.edu.:80
103.10.27.21:80
61.12.92.70:80
210.212.205.30:443
136.233.45.114:443
40.100.137.248:80
35.213.147.113:443
prodvpc-web-lb6-141531396.ap-south-1.elb.amazonaws.com.:80
3.108.47.12:80
103.10.27.41:443
103.10.24.222:443
103.10.24.222:443
103.10.27.8:443
103.10.27.8:443
chennai.amrita.edu.:443
35.213.147.113:587
210.212.205.29:80
103.10.24.252:80
103.10.27.53:80
103.10.27.53:80
35.213.147.113:110
103.10.24.252:443
136.233.45.115:80
3.111.88.252:80
160.153.0.37:8443
alumni.amrita.edu.:8443
160.153.0.37:8443
103.10.27.42:443
103.10.27.42:443
103.10.27.57:443
103.10.24.204:8443
103.10.24.204:8443
surveycom.amrita.edu.:8443
35.154.13.57:443
103.10.24.210:80
103.10.24.249:80
103.10.27.49:80
103.10.24.205:995
103.10.27.42:80
103.10.27.42:80
123.63.2.21:80
13.228.96.213:443
13.228.96.213:110
103.10.24.205:465
103.96.100.9:443
103.96.100.9:443
76.223.83.62:80
76.223.83.62:80
amselb-799089873.ap-south-1.elb.amazonaws.com.:443
43.204.57.221:443
```

---

## Fetching SPM AND DMARC records from mail servers

### Fetching The SPF Records

#### Fetching SPK record using dig
```bash
dig TXT amrita.edu +short
```
>Above we've fetched TXT records, which will have information about SPF records
**Grepping the specfic spf record**
```bash
dig TXT example.com +short | grep "v=spf1"
```
**Using nslookup tool**
```bash
nslookup -type=TXT example.com
```

```
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
amrita.edu	text = "MS=ms48957933"
amrita.edu	text = "google-site-verification=A8whEmErlQs8pAAj5IfozkzELgbx6owO40YUAynCj7A"
amrita.edu	text = "google-site-verification=NohHy1s7gfNZSge8hcuhsNeSpy3nDOczn9noXPSfH8Y"
amrita.edu	text = "apple-domain-verification=FSyq3qG4dwnUXFKW"
amrita.edu	text = "v=spf1 ip4:168.245.10.139/32 include:spf.protection.outlook.com  include:zcsend.in include:_spf.google.com ~all"
amrita.edu	text = "\194\160" "\194\160" "google-site-verification=tg-bJK2fo2szfXudVouWu_d6xsknYiwqxpAtQKeVGgw"
```

### Fetching the DMARC records

#### Using dig tool
```bash
dig TXT _dmarc.example.com +short
```

##### Output
```
"v=DMARC1;p=quarantine;sp=none;rua=mailto:dmarc@amrita.edu;ruf=mailto:dmarc@amrita.edu;rf=afrf;pct=100;ri=86400"
```

#### Using nslookup
```bash
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
_dmarc.amrita.edu	text = "v=DMARC1;p=quarantine;sp=none;rua=mailto:dmarc@amrita.edu;ruf=mailto:dmarc@amrita.edu;rf=afrf;pct=100;ri=86400"

Authoritative answers can be found from:
```

#### DMARC record check using dmarcian
![image](https://github.com/user-attachments/assets/760ec826-6c8e-41ae-b05c-684907edb2f6)

#### DMARc info obtained from MX-Toolbox
![image](https://github.com/user-attachments/assets/c7f42aca-539d-44b9-b629-39ec6ef52ec9)

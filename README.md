# IoT_Sentinel

This program is an implementation of IoT sentinel: https://arxiv.org/pdf/1611.04880.pdf  
Device Fingerprint, it takes as input pcaps and tests each packets against 23 features: 


    Link layer protocol (2)                 ARP/LLC
    Network layer protocol (4)              IP/ICMP/ICMPv6/EAPoL
    Transport layer protocol (2)            TCP/UDP
    Application layer protocol (8)          HTTP/HTTPS/DHCP/BOOTP/SSDP/DNS/MDNS/ NTP
    IP options (2)                          Padding/RouterAlert
    Packet content (2)                      Size (int)/Raw data
    IP address (1)                          Destination IP counter (int)
    Port class (2)                          Source (int) / Destination (int)


### Dependencies

- enviornment.yml (dependencies are listed inside the environment file)


### Environment Setup
```bash
conda env create --file environment.yml
```

* A new conda environment will be created, it will be called iotpy2


### Usage  
```bash
conda activate iotpy2

python iot_fingerprint.py -d <inputdir> [or] -i <inputpcap> -l <label> [and] -o <outputdir>  
Example: python iot_fingerprint.py -d captures_IoT_Sentinel/captures_IoT-Sentinel/ -o csv_result_full/
```

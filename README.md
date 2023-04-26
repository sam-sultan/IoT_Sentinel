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

## Guide
We list the structure of this repo as follows:
```latex
.
├── [4.0K]  captures_IoT_Sentinel/      % pcap files
|   └── [4.0K]  captures_IoT-Sentinal/  % pcap files
│       ├── [ 13K]  Aria/
│           ├── [17]    _iotdevice-mac.txt
│           ├── [8.4K]  Setup-A-1-STA.pcap
│           ├── ...
│           └── [8.2K]  Setup-C-15-STA.pcap
|   └── [4.0K]  dpkt/                   % modules
│       ├── [ 1.2K]  ah.py
│       ├── ...
│       └── [1.6K]  yahoo.py
├── [1.6K]  iot_sentinel_paper.pdf      % Science Paper
├── [1.6K]  environment.yml             % environment yaml setup file
├── [8.9K]  iot_fingerprint.py          % start file
└── [2.0K]  README.md                   % README file
```


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

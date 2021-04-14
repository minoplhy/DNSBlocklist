wget -O /root/adguard-ct/adguard_cname-tracker.txt https://github.com/AdguardTeam/cname-trackers/raw/master/combined_disguised_trackers.txt
python3 /root/adguard-ct/adguard-host_rpz_sys.py /root/adguard-ct/adguard_cname-tracker.txt /root/adguard-ct/adguard_cname-tracker.rpz

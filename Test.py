from urllib.parse import urlencode
import requests

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Cookie':'H_WISE_SIDS=101556_115474_115442_114743_108373_100099_115725_106201_107320_115339_114797_115553_116093_115546_115625_115446_114329_115350_114275_116040_110085; PSTM=1494300712; BAIDUID=42FE2934E37AF7AD1FA31D8CC7006D45:FG=1; BIDUPSID=2996557DB2710279BD865C50F9A68615; MCITY=-%3A; __cfduid=da9f97dea6458ca26aa4278280752ebb01508939712; BDSFRCVID=PGLsJeCCxG3wt_3ZUrBLDfv2D_qBZSjAgcEe3J; H_BDCLCKID_SF=tJAOoCLytI03qn5zq4Oh-4oHhxoJq5QxbT7Z0l8KtfcNVJQs-lCMhbtp-l3GJPoLWK6hBKQmWIQHDnbsbq0M2tcQXR5-WROCte74KKJx-4PWeIJo5tKh04JbhUJiB5OLBan7Lq7xfDDbbDtmej_3-PC3ql6354Rj2C_X3b7EfKjIOtO_bfbT2MbyeqrNQlTkLIvXoITJQD_bEP3Fbfj2DPQ3KabZqjDjJbue_I05f-oqebT4btbMqRtthf5KeJ3KaKrKW5rJabC3hPJeKU6qLT5Xjh6B5qDfyDoAbKOt-IOjhb5hMpnx-p0njxQyaR3RL2Kj0p_EWpcxsCQqLUonDh8L3H7MJUntKjnRonTO5hvvhb6O3M7-XpOhDG0fJjtJJbksQJ5e24oqHP-kKPrV-4oH5MQy5toyHD7yWCvjWlT5OR5Jj6KMjMkb3xbz2fcpMIrjob8M5CQESInv3MA--fcLD2ch5-3eQgTI3fbIJJjWsq0x0-jle-bQypoa-U0j2COMahkMal7xO-QO05CaD53yDNDqtjn-5TIX_CjJbnA_Hn7zepoxebtpbt-qJJjzMerW_Mc8QUJBH4tR-T3keh-83xbnBT5KaKO2-RnPXbcWjt_lWh_bLf_kQN3TbxuO5bRiL66I0h6jDn3oyT3VXp0n54nTqjDHfRuDVItXf-L_qtDk-PnVeUP3DhbZKxtqtDKjXJ7X2fclHJ7z-R3IBPCD0tjk-6JnWncKaRcI3poiqKtmjJb6XJkl2HQ405OT-6-O0KJcbRodobAwhPJvyT8DXnO7-fRTfJuJ_DDMJDD3fP36q4QV-JIehmT22jnT32JeaJ5n0-nnhP3mBTbA3JDYX-Oh-jjRX56GhfO_0R3jsJKRy66jK4JKjHKet6vP; ispeed_lsm=0; H_PS_PSSID=1421_24558_21120_17001_24880_22072; BD_UPN=123253; H_PS_645EC=44be6I1wqYYVvyugm2gc3PK9PoSa26pxhzOVbeQrn2rRadHvKoI%2BCbN5K%2Bg; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
'Host':'www.baidu.com',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# response=requests.get('https://www.baidu.com/s?'+urlencode({'wd':'美女'}),headers=headers)
response=requests.get('https://www.baidu.com/s',params={'wd':'美女'},headers=headers) #params内部就是调用urlencode
print(response.text)
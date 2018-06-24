
def changeCookie(cookie):
    print(cookie.__dict__)


if __name__ == '__main__':
    cookie = 'uuid_tt_dd=10_16989775620-1528960189644-294250; __yadk_uid=ks6wb61brXZ2LwmteQjS2HHb04Di1nmf; UN=weixin_41829272; __utma=17226283.1771461358.1529322391.1529322391.1529322391.1; __utmz=17226283.1529322391.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; smidV2=20180622105248e41d477690ca387ceaa995c5952584f0007e3f9e41f5ea8f0; UserName=weixin_41829272; UserInfo=FoP3ehBiU5pAAHF5DhO15bs3hRjnLs42d3ojvSk%2BRIOZOaiYxkqpH7Kgu6a3tGJ2B3fL6T8NSPZu%2BXGqWRd3hYgDFcoHcFoBJb9oNSSiT5EfPLSaG5Uu6KC1T1rkaCvOgMwlFji72hwjtpXA%2BxAANw%3D%3D; UserNick=why1673; AU=DB0; BT=1529635972060; dc_session_id=10_1529647668124.578759; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1529633589,1529633733,1529633768,1529647667; TY_SESSION_ID=8b7e68b3-bcbb-447a-9239-95ec5474b319; is_advert=Thu%2C%2011%20Jan%202255%2006%3A27%3A05%20GMT; dc_tos=papoxs; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1529649281'
    changeCookie(cookie)
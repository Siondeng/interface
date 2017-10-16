import requests

def get_cookies():
    url = "http://qa.eipsev.com/Login/UserLogin"
    payload = {'Account':'deng.youjie','ChannlID':'4755505981213920512','DeviceType':'4','Password':'123'}
    r = requests.post(url,data = payload)
    cook = r.cookies
    return (cook)

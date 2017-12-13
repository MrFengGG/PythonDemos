import urllib.request
import urllib.parse
import json
import sys

class BAIDU:
    AK="3ghFUCcGettQOEa1PpLGzyrXAkeuIDCD"
    PLACE_URL="http://api.map.baidu.com/place/v2/search?q=%s&region=%s&scope=%s&ak=%s&output=%s"
    CITY_URL="http://api.map.baidu.com/staticimage/v2"

    def __init__(self ,ak=AK):
        self.ak = ak;

    def search_place(self,city,place,search_url=PLACE_URL,scope=1,filter=None,output="json"):
        '''
        根据地名查询信息
        :param city: 城市
        :param place: 地名
        :param search_url:百度地图api 
        :param scope: 查询结果选择
        :param filter: 查询结果过滤
        :param output: 输出格式
        :return: 地址信息
        '''
        place = urllib.parse.quote(place)
        city = urllib.parse.quote(city)
        search_url = search_url%(place,city,scope,self.ak,output)
        if scope==2 and filter!=None:
            search_url+=("filter="+filter)
        data = urllib.request.urlopen(search_url).read()
        data = data.decode()
        data = json.loads(data)
        return data




if __name__=="__main__":
    B = BAIDU()
    B.search_place("郑州","鑫苑二七鑫中心－ 二七 －大学南路")

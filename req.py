import requests
import json

def output(lt,lg):

    loc = ["amusement_park","aquarium","art_gallery","library","movie_theater","museum","zoo"]
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?radius=1500&keyword=cruise&key=AIzaSyB5xoYAKvc0G0A7Q3VV7KEghyVUQdfJuD0&location=' + str(lt) + ',' + str(lg) + '&type='
    url2 = 'https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json?app_id=LGKseBzhB368K4hkIZ7c&app_code=jj1R0tMgUUquGiZ6oe_h3Q&mode=retrieveLandmarks&prox=51.50643,-0.12721,1000'


    final = []  
    for a in range(len(loc)):
        e = requests.get(url + loc[a])
        res = e.json()

        if res['status'] != 'OK':
            continue
        for i in range(len(res['results'])):
            url2 = 'https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json?app_id=LGKseBzhB368K4hkIZ7c&app_code=jj1R0tMgUUquGiZ6oe_h3Q&mode=retrieveLandmarks&prox=' + str(res['results'][i]['geometry']['location']['lat']) + ',' + str(res['results'][i]['geometry']['location']['lng']) + ',1000'
            s = requests.get(url2)
            w = s.json()
            p = {'name': res['results'][i]['name'],'lat':res['results'][i]['geometry']['location']['lat'],'lng':res['results'][i]['geometry']['location']['lng'],'address':w['Response']['View'][0]['Result'][0]['Location']['Address']['Label'],'type':loc[a]}
            final.append(p)
    rep = {'response':final}
    z = json.dumps(rep, indent=2)
    return z

output(51.50643,-0.12721)
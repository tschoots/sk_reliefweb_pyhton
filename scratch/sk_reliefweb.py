import urllib.request, json


url_str = "http://api.reliefweb.int/v1/%s?sort[]=id:%s&appname=%s&profile=%s&preset=%s&offset=0&limit=%d", "reports", reliefweb.Sort, reliefweb.AppName, reliefweb.Profile, reliefweb.Preset, reliefweb.MaxRequests


import re
url = u"http://www.amazon.com/s/ref=sr_pg_13?rh=i%3Aaps%2Ck%3Amouse+pad&page=13&keywords=mouse+pad&ie=UTF8&qid=1429838429&spIA=B00UHJ09TG,B00SISUWIQ,B00TNJ3UXI,B00TNJ61SE,B00MNU5H7G,B00NG39PN6,B009YQCUEK,B00PARIYYM,B00E7KN204,B00V73IJ2A,B00O2IQT24,B001DXSADM,B00V73GJF4,B00V73HBNS,B00IXPSYL6,B00OX2HPZ4,B00SISUWKY,B00V73I4KM,B00V73GKNA,B00ADW4XFS,B00VCOBIP4,B00V73GHWY,B00V73I63M,B00UNPIEI2"

def getpage(url):
    print url
    regex = re.compile(r"""page=[0-9]+""")
    page_portion = regex.findall(url)[0]
    print page_portion.strip("page=")

    

#    pattern = re.compile(u'amazon.com')
#    result = re.match('amazon',url,re.L)


getpage(url)

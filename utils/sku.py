import urllib2
import os
from app01 import models
from datetime import datetime
from glob import iglob

class Product(object):
    def __init__(self,sku):
        self.skuno = sku
        self.root_path = '/www/htdocs'
        self.req_addr = 'http://img.mictester.com/purge/productimages/'
        cmd = '%s/productimages/%s/%s/%s/sku_%s_*'%(self.root_path, self.skuno[0], 
                                           self.skuno[1], self.skuno[2],
                                           self.skuno)
        #instance: ls /www/htdocs/productimages/1/0/0/sku_100035_1.jpg
        #self.gen = iglob(cmd)
        #if self.gen:
            #empty lst means no sku pic exist
        self.pic_lst = [ i.strip() for i in iglob(cmd) ]
        if self.pic_lst: 
            self.url_lst = [self.req_addr+os.path.basename(p) for p in self.pic_lst]
            self.url_dic = dict.fromkeys(self.url_lst)
    
    def clearCache(self,optuser):
        #url_lst = [pic.replace(self.root_path,self.req_addr) for pic in pic_lst]
        #url_lst = [self.req_addr+os.path.basename(p) for p in pic_lst]
        #url_dic = dict.fromkeys(url_lst)
        
        for url in self.url_lst:
            try:
                response = urllib2.urlopen(url)
                self.url_dic[url] = response.getcode()
            except urllib2.HTTPError,e:
                self.url_dic[url] = e.code
                continue
            except urllib2.URLError,e:
                print e
            finally:
                models.History.objects.create(
                    sku = int(self.skuno),
                    pic_url = url,
                    cleaned_status = self.url_dic[url],
                    cleaned_by = optuser,
                    cleaned_at = datetime.now()
                )
            #cleanedsku.append(lst_skuno[i])
        return self.url_dic
  
    
        
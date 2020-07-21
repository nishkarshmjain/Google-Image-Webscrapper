# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:00:16 2020

@author: nish
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
     
    def downloadImages( keyWord, header):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyWord)
        rawHtml = imgScrapper.scrap_html_data(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages    
   
    
    
import requests
import PIL
from bs4 import BeautifulSoup
import urllib.request
import os
from os.path import isfile, join
import re
import img2pdf
import setting 
# for now
def leading_zero(digit_len,totalimg):
  totalimg = int(totalimg)
  if totalimg<9:
    return "0"
  elif totalimg<99 and digit_len>1:
    return "0"
  elif totalimg<99 and digit_len==1:
    return "00"
  elif totalimg<999 and digit_len>2:
    return "0"
  elif totalimg<999 and digit_len>1:
    return "00"
  elif totalimg<999 and digit_len==1:
    return "000"

# config list
def makepdf(mid,hsite,cattype):
  mangaid = mid
  hentai_site = hsite
  print("Done Scrap : "+mangaid)
  if setting.verbose: print("domain     : ", domain)
  # if setting.verbose: print("first link : ", firstlink)
  if setting.verbose: print("path       : ", main_url)

  # compile to pdf pulak
  filtetype = [f.split(".")[1] for f in os.listdir(hentai_site+"/"+cattype+"/"+mangaid) if isfile(join(hentai_site+"/"+cattype+"/"+mangaid, f)) and ('.jpg' in f or '.png' in f)][0]
  onlyfiles = [f for f in os.listdir(hentai_site+"/"+cattype+"/"+mangaid) if isfile(join(hentai_site+"/"+cattype+"/"+mangaid, f)) and ('.jpg' in f or '.png' in f)]
  onlyfiles.sort()
  onlyfiles = [hentai_site+"/"+cattype+"/"+mangaid+"/"+str(f) for f in onlyfiles]
#   print(onlyfiles)
  with open(hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid.split("/")[-1]+".pdf","wb") as f:
    try:
      f.write(img2pdf.convert(onlyfiles))
      os.rename(hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid+".pdf", setting.pdfdirectory+"/"+hentai_site+"/"+cattype+"/"+mangaid+".pdf")
      print("Completed pdf at: pdfall/"+hentai_site+"/"+cattype+"/"+mangaid+".pdf")
    except Exception:
      for x in onlyfiles:
        PIL.Image.open(x).convert('RGB').save(x)
      f.write(img2pdf.convert(onlyfiles))
      os.rename(hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid+".pdf", setting.pdfdirectory+"/"+hentai_site+"/"+cattype+"/"+mangaid+".pdf")
      print("Completed pdf at: pdfall/"+hentai_site+"/"+cattype+"/"+mangaid+".pdf")
  return "pdfall/"+hentai_site+"/"+cattype+"/"+mangaid+".pdf"

def crawl_nhentai(mid,hsite,cattype):
  mangaid = mid

  hentai_site = hsite
  try:
    os.makedirs(setting.pdfdirectory+"/"+hentai_site+"/"+cattype) 
    os.makedirs(hentai_site+"/"+cattype) 
  except FileExistsError:
    pass
  domain = "https://nhentai.net"
  domaingaleries = "https://i.nhentai.net/galleries"
  main_url = domain+"/"+cattype+"/"+mangaid+"/"
  page = requests.get(main_url)
  soup = BeautifulSoup(page.content, 'html.parser')
  totalimg = len(soup.find("div",{"id":"thumbnail-container"}).find_all("div",{"class":"thumb-container"}))
  media_id = soup.find("meta",{"itemprop":"image"})["content"].split("/")[-2]

  try:
    os.makedirs(hentai_site+"/"+cattype+"/"+mangaid)
  except FileExistsError:
    pass

  # begin scrapping
  for x in range(1,int(totalimg)+1):
    
    if setting.verbose: print("Downloading.. "+url) 
    try:
      url = domaingaleries+"/"+media_id+"/"+str(x)+".png"
      urllib.request.urlretrieve(url, hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid+"_"+leading_zero(len(str(x)),totalimg)+str(x)+".png")
    except urllib.request.HTTPError:
      url = domaingaleries+"/"+media_id+"/"+str(x)+".jpg"
      urllib.request.urlretrieve(url, hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid+"_"+leading_zero(len(str(x)),totalimg)+str(x)+".jpg")
    if setting.verbose: print("Done.")

# for erolord

def crawl_erolord(mid,hsite,cattype):
  mangaid = mid
  hentai_site = hsite
  try:
    os.makedirs(setting.pdfdirectory+"/"+hentai_site+"/"+cattype) 
    os.makedirs(hentai_site+"/"+cattype) 
  except FileExistsError:
    pass
  domain = "http://erolord.com"
  ctype = cattype#"doujin"#"bayonetta"#"doujin"
  main_url = domain+"/"+ctype+"/"+mangaid+"/"
  page = requests.get(main_url)
  soup = BeautifulSoup(page.content, 'html.parser')
  firstlink = soup.find("a",{"class":"aa2","id":"ahr1"})["href"]
  totalimg  = firstlink.split("&")[-1:][0].split("=")[1]

  pagefirst = requests.get(domain+firstlink)
  soupfirst = BeautifulSoup(pagefirst.content, 'html.parser')
  img = soupfirst.find(id="slide_show")['src']

  name = img.split("/")
  path = img.strip(name[-1])
  try:
    os.makedirs(hentai_site+"/"+cattype+"/"+mangaid)
  except FileExistsError:
    pass

  # begin scrapping
  for x in range(1,int(totalimg)+1):
    url = domain+path+str(x)+".jpg"
    if setting.verbose: print("Downloading.. "+url) 
    urllib.request.urlretrieve(url, hentai_site+"/"+cattype+"/"+mangaid+"/"+mangaid+"_"+leading_zero(len(str(x)),totalimg)+str(x)+".jpg")
    if setting.verbose: print("Done.")
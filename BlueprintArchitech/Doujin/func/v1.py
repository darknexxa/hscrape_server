from BlueprintArchitech.Doujin.lib.v1 import crawl_erolord, crawl_nhentai, makepdf
class hentai_scraper:
  """docstring"""
  def __init__(self, mid,hsite,ctype):
    self.mid = mid
    self.hsite = hsite
    self.ctype = ctype 

  def scraper(self):
    if self.hsite == "erolord":
      crawl_erolord(self.mid,self.hsite,self.ctype)
    elif self.hsite == "nhentai":
      crawl_nhentai(self.mid,self.hsite,self.ctype)

  def pdfmaker(self):
    return makepdf(self.mid,self.hsite,self.ctype)

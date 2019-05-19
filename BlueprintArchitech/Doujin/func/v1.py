from BlueprintArchitech.Library.v1 import crawl_erolord, crawl_nhentai, makepdf, lister, check_pdf
class hentai_scraper:
  """docstring"""
  def __init__(self, mid,hsite,ctype):
    self.mid = mid
    self.hsite = hsite
    self.ctype = ctype 
    self.lister = lister(self.hsite,self.ctype,self.mid)
    self.pdf = check_pdf(self.hsite,self.ctype,self.mid)

  def scraper(self):
    if self.hsite == "erolord":
      crawl_erolord(self.mid,self.hsite,self.ctype)
    elif self.hsite == "nhentai":
      crawl_nhentai(self.mid,self.hsite,self.ctype)

  def pdfmaker(self):
    return makepdf(self.mid,self.hsite,self.ctype)

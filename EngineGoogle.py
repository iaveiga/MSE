from pygoogle import pygoogle
'''
def getUrls(query,ext):
    ext = "ext: " + ext
    query = query + ext
    g = pygoogle(query)
    g.pages = 10
    type(g)
    g.get_result_count()
    return g.get_urls()
'''
def searchG(query,num,lang):
    search_ = pygoogle(query,pages = num, hl=lang)
    return search_.get_urls()

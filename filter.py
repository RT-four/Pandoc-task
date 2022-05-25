import sys
import panflute as pf

headers = []

def findHeader(elem, doc):
  if (isinstance(elem, pf.Header)):
    if (elem.level > 2):
      return pf.Header(pf.Str(pf.stringify(elem).upper()), level=elem.level)

def headerSearch(elem, doc):
  if isinstance(elem, pf.Header):
    text = pf.stringify(elem)
    if (text in headers):
      sys.stderr.write("Header `" + text + "` already exists")
    else:
      headers.append(text)

def boldify(doc):
  doc.replace_keyword('BOLD', pf.Strong(pf.Str('BOLD')))

if __name__ == '__main__':
  pf.run_filters([headerSearch, findHeader], prepare=boldify)

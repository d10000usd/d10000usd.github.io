import numpy
import FinanceDataReader as fdr
dtdf =  fdr.StockListing('KRX')

tag = [
    { "차트태그":{"종가" :111,"등락률":12,"구분":"kospi"},
     "개별태그":{"종목명" :"삼성전자","Marcap":"matp"}
     }

]


print(dtdf)
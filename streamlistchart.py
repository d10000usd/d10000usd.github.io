import streamlit as st
import numpy as np
import FinanceDataReader as fdr
import plotly.offline as pyoff
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.offline as pyoff
import plotly.graph_objs as go
#from plotly.graph_objs import go
from plotly.subplots import make_subplots
pio.renderers.default='browser'
from pykrx import stock
from datetime import datetime
import os, warnings,sys
warnings.filterwarnings(action='ignore')


from  util_settings import ProjectSettiongs
ut = ProjectSettiongs()

class StockConfigSetting():
    name = 'naverblog'
    verbose_name = "네이버 블로그"
    def __call__(sefl,t):
        print(f'innit done naverPostringHtmlModule')

    def __init__(self,t) -> None:
        # super().__init__()
        self.t = t
        self.naver_search_config_stock =[
            {"검색어": "성도이엔지 디스플레이 협력","검색페이지수": 11,"요약강도":0.2,'요약강도2':2.9, '요약강도3':0.8},
            {"검색어": "자율주행 avg 협력","검색페이지수": 11,"요약강도":0.2,'요약강도2':2.9, '요약강도3':0.8},
        ]
        self.stock_searchkeyword_split = {"search" :['삼성전자','주가','모멘텀']}
        self.stock_contents_article =[
            {'tag' : '#tag-삼성전자 주가 모멘텀'},
            {'title': 'title -삼성전자 주가 모멘텀'},
            {'contents': 'contents-삼성전자 주가 모멘텀'},
            {'original': 'original-삼성전자 주가 모멘텀',}]


    def get_summary_config(self):
        return self.naver_search_config_stock
    def get_naver_search_config_stock(self):
        return self.stock_searchkeyword_split


    def get_stock_candle_ea_info(self,p0,p1, p2,p3,p4,p5,p6,p7):
        #self,ticker,tickername, candle_dmy, candle_cnt, ma1, ma2,ut.timeFunction("년월일시분초")
        #(ticker, "d", candle_cnt, ma1, ma2)
        """
        docstring
        :param0 : par - ticker
        :param1 : par - tickername
        :param2 : par - candle_cnt
        :param3 : par - candle_dmy
        :param4 : p4 - ma1
        :param5 : p5 - ma2
        :param5 : p6 - time 2020-01-01 00:00:00
        :param5 : p7 - 하락 상승
        :Returns ret - candleinfo
        """
        info = {}
        info['종목코드']=p0
        info['종목명']=p1
        info['조회수']=p2
        info['캔들타입']=p3
       
        info['ma1']=p4
        info['ma2']=p5
        info['time']=p6
        info['updown']=p7
        # info['종목코드']=p7

        # candleinfo = {
        #     "종목명"    :ticker,
        #     "캔들타입"  :candletime,
        #     "조회수"    :candle_cnt}
        # print(candleinfo)
        # print(candleinfo["조회수"])
        return info

    def get_stock_search_info(self,p1, p2,p3,p4):
        # self,days_rate, ma1, ma2,ut.timeFunction("년월일시분초")
        """
        docstring
        :param1 : par - days_rate > 20 or :param2 : par - days_rate < -15
        :param1 : par - ma1
        :param2 : par - ma2
        :param2 : par - 작성시간 > 2020-01-01
        :Returns ret - infodict
        """
        info = {}

        info['days_rate']=p1
        info['ma1']=p2
        info['ma2']=p3
        info['time']=p4
        return info

    def getStockPriceOfTop_ratex(self,df,p1):
        """
        docstring
        :param1 : par - df
        :param2 : par - p1 > 20

        """
        df=df.head(p1)
        selectdict ={}
        selectdict['ChagesRatioOver'] = p1
        df=df[((df['ChagesRatio'] > selectdict['ChagesRatioOver'] ))]
        # scbuy=df[((df['my_rate'] < leftValue )&(df['my_rate'] >rightValue)) & (df['보유평가금'] < holdAmount)]
        df.to_json('data/stocklist.json',orient='records')
        return df





class StockDataSearch():
    name = 'StockDataSearch'
    verbose_name = "StockDataSearch"
    def __call__(sefl,t):
        print(f'innit done naverPostringHtmlModule')

    def __init__(self,t) -> None:
        # super().__init__()
        self.t = t
    def get_stock_rank_list(self,compare,df,dicts):
        #self,"하락",dtdf,searchinfo_down
        """
        docstring
        :param1 : par - days_rate > 20
        :param2 : par - candle_cnt < -15
        :param1 : par - ma1
        :param2 : par - ma2
        :param2 : par - time > 2020-01-01
        :Returns ret - infodict
        """
        df =  pd.DataFrame(df[['Code', 'Name','Market','ChagesRatio','Close','Volume']]).sort_values(by='ChagesRatio' ,ascending=False)
        # df[['Code','Name']].to_csv('data/stock_ticker_data.csv',encoding='utf-8-sig',index=False)

        df.reset_index(drop=True, inplace=True)

        # st.table(df.head(3))
        if compare =='상승':
            df=df[((df['ChagesRatio'] > dicts['days_rate'] ))]
            df.to_json('data/stocklist_whitelist.json',orient='records',force_ascii=False)
        elif compare == '하락':
            df=df[((df['ChagesRatio'] < dicts['days_rate'] ))]
            df.to_json('data/stocklist_blacklist.json',orient='records',force_ascii=False)
        # scbuy=df[((df['my_rate'] < leftValue )&(cbuy['my_rate'] >rightValue)) & (cbuy['보유평가금'] < holdAmount)]
        st.table(df)
        return df['Name'].tolist()



    def 주식이름으로조회종목코드(self,ticker_):
        #문자를 포함하는 행을 찾아서 출력
        df = pd.read_csv("/Users/hg/WORKSPACE/Gitblog/stock/stockTicker.csv")
        df = df[df['종목명'].str.contains(ticker_)]#특정 문자열 포함된 행만 추출
        stocklistdf=(df.query(f'종목명 == "{ticker_}"'))
        return (stocklistdf["종목코드"].tolist())[0]


    def main(self,dicts):
        # df,dfs =self.주식조회(dicts["캔들타입"],"stock","axis",dicts["종목명"],12,150,25,80,"other")
        dfs=dfs[['Date','Open','High','Low','Close','거래량']]
        # dfs.columns = ['Date','Open','High','Low','Close','Volume']
        dfs.rename(columns={'거래량': 'Volume'}, inplace=True)
        # dfs['10_ma'] = dfs['Close'].rolling(10).mean()
        # dfs['20_ma'] = dfs['Close'].rolling(20).mean()
        # fig = get_candlestick_plot(dfs.tail(11), 10, 20,candletime)
        # fig.show()

        return dfs


    def 주식차트정보조회(self,dicts):
        df = stock.get_market_ohlcv("20220101", ut.timeFunction("년월일"), dicts['종목코드'],dicts['캔들타입'])
        if dicts['캔들타입'] == 'd':
            df=df[['시가'   ,   '고가'  ,    '저가' ,     '종가'  ,    '거래량']]
            df.columns = ['Open','High','Low','Close','Volume']
            # ohlc_data.columns = ['Open','High','Low','Close','거래량',         '거래대금' ,       '등락률']
        else :
            df=df[['시가'   ,   '고가'  ,    '저가' ,     '종가'  ,    '거래량']]
            df.columns = ['Open','High','Low','Close','Volume']
        df=df.rename_axis('Date').reset_index()
       
        return df[['Date','Open','High','Low','Close','Volume']], df

class PlotlyChartDraw():
    name = 'PlotlyChartDraw'
    verbose_name = "PlotlyChartDraw"
    def __call__(sefl,t):
        print(f'PlotlyChartDraw')

    def __init__(self,t) -> None:
        # super().__init__()
        self.t = t




    def get_candlestick_plot(self,df,dicts):
        #candleinfodict
        '''
        Create the candlestick chart with two moving avgs + a plot of the volume
        Parameters
        ----------
        df : pd.DataFrame
            The price dataframe
        ma1 : int
            The length of the first moving average (days)
        ma2 : int
            The length of the second moving average (days)
        ticker : str
            The ticker we are plotting (for the title).
        '''
        #        info['종목코드']=p0
        # info['종목명']=p1
        # info['조회수']=p3
        # info['캔들타입']=p2

        # info['ma1']=p4
        # info['ma2']=p5
        # info['time']=p6
        # info['updown']= p7, "up" or "down"
        # series :: Code,ISU_CD,Name,Market,Dept,Close,ChangeCode,Changes,ChagesRatio,Open,High,Low,Volume,Amount,Marcap,Stocks,MarketId
        ticker = dicts['종목명']
        ma1 = dicts['ma1']
        ma2 = dicts['ma2']
        ud=dicts['updown']

        #
        # 차트태그
        # charttag=self.tagMakeAllhere(df,"차트태그")
        #Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', '10_ma', '20_ma'], dtype='object')
        
       

        dflastrow = df.tail(1)
        dflastrows = dflastrow['Close'].values[0]
        fig = make_subplots(
            rows = 2,
            cols = 1,
            shared_xaxes = True,
            vertical_spacing = 0.1,
            subplot_titles = (f'{ticker} Stock Price <br>{dflastrows}{1}', 'Volume Chart'),
            row_width = [0.1, 0.9]
        )

        fig.add_trace(
            go.Candlestick(
                x = df['Date'],
                open = df['Open'],
                high = df['High'],
                low = df['Low'],
                close = df['Close'],
                name = 'Candlestick chart'
            ),
            row = 1,
            col = 1,
        )
        
        fig.add_trace(
            go.Line(x = df['Date'], y = df[f'{ma1}_ma'], name = f'{ma1} SMA'),
            row = 1,
            col = 1,
        )



        fig.add_trace(
            go.Line(x = df['Date'], y = df[f'{ma2}_ma'], name = f'{ma2} SMA'),
            row = 1,
            col = 1,
            
        )

        fig=self.addmaline(fig,df)

        # Volume Chart
        fig.add_trace(
            go.Bar(x = df['Date'], y = df['Volume'], name = 'Volume'),
            row = 2,
            col = 1,
        )

        fig['layout']['xaxis2']['title'] = 'Date'
        fig['layout']['yaxis']['title'] = 'Price'
        fig['layout']['yaxis2']['title'] = 'Volume'

        fig.update_xaxes(
            rangebreaks = [{'bounds': ['sat', 'mon']}],
            rangeslider_visible = False,
        )
        savePathes_    =f"/Users/hg/WORKSPACE/Gitblog/stock/chart/data/img/{ud}_{ticker}.png"
        fig.write_image(savePathes_)
        return fig


class streamlitApp():


    def __init__(self,t) -> None:
        # super().__init__()
        self.t = t
        t = self.tagMakeAllhere
    def __call__(sefl,t):
        print(f'innit done naverPostringHtmlModule')
    # Sidebar options
    def dayofrangkfromstockprice(self):
        st.sidebar.title('주식캔들차트')
        st.sidebar.markdown('''
        주식캔들차트를 그립니다.
        ''')
        st.sidebar.markdown('''[주식캔들차트]''')




    def addmaline(self,fig,df):
        fig = fig
        malist =  [3,5,10,14,25,40,60,90,120,180,250,300]
        for i in malist:
            df[f'{i}_ma'] = df['Close'].rolling(i).mean()
        
        for i in malist:
            fig.add_trace(
                go.Line(x = df['Date'], y = df[f'{i}_ma'], name = f'{i} SMA'),
                row = 1,
                col = 1,
            )
        return fig

    def tagMakeAllhere(self,df,tagno):
# series :: Code,ISU_CD,Name,Market,Dept,Close,ChangeCode,Changes,ChagesRatio,Open,High,Low,Volume,Amount,Marcap,Stocks,MarketId
        sr=df.iloc[-1]
        tag = [
            { 
                "차트태그":{"종가" :sr['Close'],"등락률":sr['Chagerate'],"구분":sr['Market']},
                "개별태그":{"종목명" :sr['Name'],"Marcap":sr['Marcap']}
            }
        ]
        return tag[0][tagno]


    def mainCover(self):
  


        fdrdf =  fdr.StockListing('KRX')
        sd=fdrdf['Name']


        days_uprate = st.sidebar.slider(
            'days_uprate',
            min_value = -28,
            max_value = 28,
            value = 25,
        )
        days_downrate = st.sidebar.slider(
            'days_downrate',
            min_value = -28,
            max_value = 28,
            value = -7,
        )
        tickername = st.sidebar.selectbox(
            'Ticker to Plot',
            options = sd
        )
        candle_dmy = st.sidebar.selectbox(
            'candle_dmy',
            options = ['d', 'm', 'y']
        )
        candle_cnt = st.sidebar.slider(
            'Days to Plot',
            min_value = 1,
            max_value = 1000,
            value = 120,
        )
        ma1 = st.sidebar.number_input(
            'Moving Average #1 Length',
            value = 10,
            min_value = 1,
            max_value = 300,
            step = 1,
        )
        ma2 = st.sidebar.number_input(
            'Moving Average #2 Length',
            value = 20,
            min_value = 1,
            max_value = 300,
            step = 1,
        )









        #############################
        ##
        ##  All, blacklist
        st.title('주식캔들차트')
        tickercode=sdserch.주식이름으로조회종목코드(tickername)
        st.text(f'{tickername}-({tickercode})')

        candleinfodict=StockConfigSetting.get_stock_candle_ea_info(self,tickercode,tickername, candle_cnt,candle_dmy,  ma1, ma2,ut.timeFunction("년월일시분초"),"nomal")
        self.chartdraw(candleinfodict)
        
        ##


        #############################
        st.title(f'전체 상승 종목중 ')
        searchinfo_up=StockConfigSetting.get_stock_search_info(self,days_uprate, ma1, ma2,ut.timeFunction("년월일시분초"))
        wstocklist=sdserch.get_stock_rank_list("상승",fdrdf,searchinfo_up)
        tickername = st.sidebar.selectbox(
            'white list',
            options = wstocklist
        )
        ##
        tickercode=sdserch.주식이름으로조회종목코드(tickername)
        st.text(f'{tickername}-({tickercode})')
        candleinfodict=StockConfigSetting.get_stock_candle_ea_info(self,tickercode,tickername, candle_cnt,candle_dmy,  ma1, ma2,ut.timeFunction("년월일시분초"),'up')
        self.chartdraw(candleinfodict)
        st.text(f'{tickername}-({tickercode})')

        ######################
        st.title(f'전체 하락 종목중 ')
        searchinfo_down=StockConfigSetting.get_stock_search_info(self,days_downrate, ma1, ma2,ut.timeFunction("년월일시분초"))
        bstocklist=sdserch.get_stock_rank_list("하락",fdrdf,searchinfo_down)
        tickername = st.sidebar.selectbox(
            'black list',
            options = bstocklist
        )
        ##
        tickercode=sdserch.주식이름으로조회종목코드(tickername)
        st.text(f'{tickername}-({tickercode})')
        candleinfodict=StockConfigSetting.get_stock_candle_ea_info(self,tickercode,tickername, candle_cnt,candle_dmy,  ma1, ma2,ut.timeFunction("년월일시분초"),'down')
        self.chartdraw(candleinfodict)


        #candleinfodict=StockConfigSetting.get_stock_candle_ea_info(self,tickercode,tickername, candle_cnt,candle_dmy,  ma1, ma2,ut.timeFunction("년월일시분초"))
    def chartdraw(self,candleinfodict):
            """
            docstring
            :param0 : par - ticker
            :param1 : par - tickername
            :param2 : par - candle_dmy
            :param3 : par - candle_cnt
            :param4 : p4 - ma1
            :param5 : p5 - ma2
            :param5 : p6 - time 2020-01-01 00:00:00
            :param5 : p7 - updown  ++ 하락 "down", 상승 "up"
            :Returns ret - candleinfo
            """
            ma1 = candleinfodict['ma1']
            ma2 = candleinfodict['ma2']
            c = candleinfodict['조회수']
            df,dfrate=sdserch.주식차트정보조회(candleinfodict)
            df[f'{ma1}_ma'] = df['Close'].rolling(ma1).mean()
            df[f'{ma2}_ma'] = df['Close'].rolling(ma2).mean()
            df = df[-c:]
            # Display the plotly chart on the dashboard
            st.plotly_chart(
                PlotlyChartDraw.get_candlestick_plot(self,df,candleinfodict),
                use_container_width = True,
            )


if __name__ == "__main__":
    stapp = streamlitApp("streamlitApp")
    sdserch = StockDataSearch("StockDataSearch")

    stapp.mainCover()
    # stapp.mainCover()

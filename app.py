from flask import Flask
import requests

app = Flask(__name__)

def getDate(raw_html):
    pattern_start = 'ประจำวันที่ <span id="DetailPlace_uc_goldprices1_lblAsTime"><b><font size="3">'
    pattern_end = 'เ'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            date = raw_html[start:end]
            index = end
        else:
            break
    return date

def getTime(raw_html):
    pattern_start = 'เวลา'
    pattern_end = 'น.'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            time = raw_html[start:end]
            index = end
        else:
            break
    return time

# ราคาขายออกทองคำแท่ง 96.5%
def getGoldBullionSellingPrice(raw_html):
    pattern_start = '<span id="DetailPlace_uc_goldprices1_lblBLSell"><b><font color='
    pattern_end = '</font>'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            cost = raw_html[start:end]
            cost = cost.replace('"','')
            costNtrend = cost.split(">")
            index = end
        else:
            break
    return costNtrend

# ราคารับซื้อทองคำแท่ง 96.5%
def getGoldBullionPurchasePrice(raw_html):
    pattern_start = '<span id="DetailPlace_uc_goldprices1_lblBLBuy"><b><font color='
    pattern_end = '</font>'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            cost = raw_html[start:end]
            cost = cost.replace('"','')
            costNtrend = cost.split(">")
            index = end
        else:
            break
    return costNtrend

# ราคาขายออกทองรูปพรรณ 96.5%
def getGoldJewelrySellingPrice(raw_html):
    pattern_start = '<span id="DetailPlace_uc_goldprices1_lblOMSell"><b><font color='
    pattern_end = '</font>'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            cost = raw_html[start:end]
            cost = cost.replace('"','')
            costNtrend = cost.split(">")
            index = end
        else:
            break
    return costNtrend

# ฐานภาษีทองคำรูปพรรณ 96.5%
def getTaxBase(raw_html):
    pattern_start = '<span id="DetailPlace_uc_goldprices1_lblOMBuy"><b><font color='
    pattern_end = '</font>'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            cost = raw_html[start:end]
            cost = cost.replace('"','')
            costNtrend = cost.split(">")
            index = end
        else:
            break
    return costNtrend

# main proccess
url = "https://www.goldtraders.or.th"
raw_html = requests.get(url).text
# print(raw_html)
# print(getDate(raw_html))
# print(getTime(raw_html))
# print(getGoldBullionSellingPrice(raw_html))
# print(getGoldBullionPurchasePrice(raw_html))
# print(getGoldJewelrySellingPrice(raw_html))
# print(getTaxBase(raw_html))

gold = {
    # ข้อมูลประจำวันที่
    "Date":getDate(raw_html),
    # ณ เวลา
    "Time":getTime(raw_html), 
    # ราคาขายออกทองคำแท่ง 96.5%
    "Gold bullion selling price 96.5%":getGoldBullionSellingPrice(raw_html),
    # ราคารับซื้อทองคำแท่ง 96.5%
    "Gold bullion purchase price 96.5%":getGoldBullionPurchasePrice(raw_html),
    # ราคาขายออกทองคำรูปพรรณ 96.5%
    "Gold jewelry selling price 96.5%":getGoldJewelrySellingPrice(raw_html),
    # ฐานภาษี ทองคำรูปประพรรณ
    "Tax base":getTaxBase(raw_html),
}
# print(gold)

@app.route('/')
def index():
    return gold

if __name__ == '__main__':
    app.run(debug=True)
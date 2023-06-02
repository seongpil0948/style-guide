from sele import get_chrome_driver
from currency_converter import CurrencyConverter
import sys, time
sys.path.append("/home/sp/codes/personal/best_performance-python")
sys.path.append("/Users/sp/Codes/Personal/Python/best_performance-python")
from utils.logger import Logger  # ignore autupep8


class Crawler(Logger):
    def __init__(self, *args, **kwargs):
        self.init_logger("./", "test")
        self.driver = get_chrome_driver(chrome_debug=True)


if __name__ == '__main__':
    c = Crawler()
    d = c.driver
    c_conv = CurrencyConverter()
    d.get("https://www.amazon.com/s?k=camping+tent&ref=nb_sb_noss")
    items = d.find_elements_by_class_name("s-result-item")
    won_form = "{}원"


    for i in items:
        try:
            symbol = i.find_element_by_class_name("a-price-symbol").text
            if symbol != "$":
                continue
            dolor = i.find_element_by_class_name("a-price-whole").text
            cent = i.find_element_by_class_name("a-price-fraction").text
            
            krw = round(c_conv.convert(int(dolor) +(int(cent) * 0.01) , "USD", "KRW"))
            s = ""
            for idx, k in enumerate(str(krw)[::-1]):
                if idx % 3 == 0:
                    s += f",{k}"
                else:
                    s += k
            s = s[::-1]
            if s.rfind(",") + 1 == len(s):
                s = s[:-1]
            krw_won = won_form.format(s)

            print(f"Sym: {symbol}  Dolor: {dolor} Cent: {cent} -> TO: {krw_won}")
        except Exception as e:
            continue
        

## zle_pkg: package for text tokenization - version 1.5.0
​
### **from zle_pkg.date import DateToken()**
​
* __DateToken().us_month(self, string)__:
​
    Replace any month in US date format with the <month> token surrounded by spaces
​
    param string<br>
    return string (<token>)
    
    
* __DateToken().us_day(self, string)__:
​
    Replace any day in US date format with the <day> token surrounded by spaces
​
    param string<br/>
    return string (<day>)
    
​
* __DateToken().us_year(self, string)__:
​
    Replace any month in US date format with the <year> token surrounded by spaces
​
    param string<br>
    return string (<year>)
    
    
* __DateToken().us_date(self, string)__:
​
    Replace any month in US date format with the <date> token surrounded by spaces
​
    param string<br>
    return string (<date>)
    
### **from zle_pkg.currency import CurrencyToken()**
​
* __CurrencyToken().dollar(self, string)__:
    
    This function takes a string input and replaces all instances 
    of dollars signs and trailing numerica values to the '<dollar>'
    tag
​
    param string<br>
    return string (<dollar>)
    
    
* __CurrencyToken().euro(self, date_string)__:
    
    This function takes a string input and replaces all instances 
    of euro signs and trailing numeric values to the '<euro>'
    tag
​
    param string<br>
    return string (<euro>)
    
​
* __CurrencyToken().pound(self, string)__:
    
    This function takes a string input and replaces all instances 
    of pound signs and trailing numeric values to the '<pound>'
    tag
​
    param string<br>
    return string (<pound>)
    
    
* __CurrencyToken().yen(self, string)__:
    
    This function takes a string input and replaces all instances 
    of yen signs and trailing numeric values to the '<yen>'
    tag
​
    param string<br>
    return string (<yen>)
    
 
* __CurrencyToken().money(self, string)__:
    
    This function takes a string input and replaces all instances 
    of yen/pound/euro/dollar signs and trailing numeric values to the '<money>'
    tag
​
    param string<br>
    return string (<money>)
    
### **from zle_pkg.numbers import NumberToken()**
​
* __NumberToken().number(self, string)__:
​
    This function takes a string input and replaces all instances 
    of numeric data and trailing numeric values to the '<numeric>'
    tag
​
    param string<br>
    return string (<numeric>)
    
### **from zle_pkg.tokenize import Tokenize()**
​
* __tokenize()(self, string)__:
​
    This function takes a string input and executes three functions:
​
    1. CurrencyToken.money(): if we see any currency symbols, then we convert
       those numbers following that symbol to the <currency> token
    2. DateToken.us_date(): if we see any dates (numbers/strings with date
       naming convension) then we convert these to the <date> token
    3. NumberToken.number(): convert all remaining numbers to the <number> token  
​
   param string<br>
   return string

​

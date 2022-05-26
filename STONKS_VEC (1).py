#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import FundamentalAnalysis as fa
import pandas as pd
import matplotlib.pyplot as plt


# In[1]:


import FundamentalAnalysis as fa
import pandas as pd
import matplotlib.pyplot as plt
names = ["BABA"]
api_key = "0b9a435e8f3cb60c3c52739a9d4b5eac"
 
for ticker in names:
   
# Show the available companies
    companies = fa.available_companies(api_key)
 
# Collect general company information
    profile = fa.profile(ticker, api_key)
 
# Collect recent company quotes
    quotes = fa.quote(ticker, api_key)
 
# Collect market cap and enterprise value
    entreprise_value = fa.enterprise(ticker, api_key)
 
# Show recommendations of Analysts
    ratings = fa.rating(ticker, api_key)
 
# Obtain DCFs over time
    dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
    dcf_quarterly = fa.discounted_cash_flow(ticker, api_key, period="quarter")
 
# Collect the Balance Sheet statements
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    balance_sheet_quarterly = fa.balance_sheet_statement(ticker, api_key, period="quarter")
 
# Collect the Income Statements
    income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
    income_statement_quarterly = fa.income_statement(ticker, api_key, period="quarter")
 
# Collect the Cash Flow Statements
    cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")
    cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, api_key, period="quarter")
 
# Show Key Metrics
    key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
    key_metrics_quarterly = fa.key_metrics(ticker, api_key, period="quarter")
 
# Show a large set of in-depth ratios
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
    financial_ratios_quarterly = fa.financial_ratios(ticker, api_key, period="quarter")
 
# Show the growth of the company
    growth_annually = fa.financial_statement_growth(ticker, api_key, period="annual")
    growth_quarterly = fa.financial_statement_growth(ticker, api_key, period="quarter")
 
# Download general stock data
    stock_data = fa.stock_data(ticker, period="ytd", interval="1d")
 
# Download detailed stock data
    stock_data_detailed = fa.stock_data_detailed(ticker, api_key, begin="2000-01-01", end="2020-01-01")
   


# In[3]:


def Fair_Value(years, years_growth_rate_3, growth_rate_3,  years_growth_rate_2,growth_rate_2, discount_rate):
    starting_PE = key_metrics_annually.loc['netIncomePerShare'][0]
    discount_prices = []
    non_discount_prices = []
    for x in range(1,years+1):
        if x >years_growth_rate_2:
            starting_PE = starting_PE*(1+growth_rate_2)
            #print(starting_PE)
            non_discount_prices.append(starting_PE)
            discount_price = starting_PE/((1+discount_rate)**x)
            #print(discount_price)
            discount_prices.append(discount_price)
            #print(discount_prices)
        else:
            starting_PE = starting_PE*(1+growth_rate_3)
            non_discount_prices.append(starting_PE)
            #print(starting_PE)
            discount_price = starting_PE/((1+discount_rate)**x)
            #print(discount_price)
            discount_prices.append(discount_price)
            #print(discount_prices)
    terminal_value_non_disc = non_discount_prices[-2]*Terminal_Value(years)
    termina_value_disc = terminal_value_non_disc/((1+discount_rate)**years)
    intrinsic_value = np.cumsum(discount_prices)[-1]+termina_value_disc
    
    return intrinsic_value


# In[4]:


def WACC(risk_free_rate, beta):
    
    #COST OF EQUITY
    market_return = 0.0851
    costofequity = risk_free_rate+(beta*(market_return-risk_free_rate))
    costofequity = round(costofequity*100,2)
    
    #COST OF DEBT
    interestExpense = income_statement_annually.loc['interestExpense'][0]
    total_debt = balance_sheet_annually.loc['longTermDebt'][0]+balance_sheet_annually.loc['shortTermDebt'][0]
    cost_of_debt = interestExpense/total_debt
    income_tax_expense = income_statement_annually.loc['incomeTaxExpense'][0]
    income_before_tax = income_statement_annually.loc['incomeBeforeTax'][0]
    Effective_tax_rate = income_tax_expense/income_before_tax
    Cost_of_Debt2 = round(cost_of_debt*(1-Effective_tax_rate)*100,2)
    
    #WEIGHTS
    total = entreprise_value.loc['marketCapitalization'][0]+total_debt
    weight_of_debt = total_debt/total
    weight_of_equity = entreprise_value.loc['marketCapitalization'][0]/total
    
    #WACC FORMULA
    wacc = (weight_of_debt*Cost_of_Debt2)+(weight_of_equity*costofequity)
    return wacc/100


# In[5]:


def Terminal_Value(years):
    mean = cash_flow_statement_annually.loc['freeCashFlow'][0:5]
    mean_growth = ((mean[0]-mean[4])/mean[4])/len(mean)
    WACCC = 1+WACC(0.001, 1.29)
    total = []
    freecashflow = key_metrics_annually.loc['freeCashFlowPerShare'][0]  
    for x in range(1,years+1):    
        freecashflow = freecashflow*(1+mean_growth)
        WAC = WACCC**x
        Ratio = freecashflow/WAC
        total.append(Ratio)
    return np.cumsum(total)[-1]


# In[6]:


WACC(0.001,1.29)


# In[9]:


import numpy as np
Terminal_Value(10)


# In[ ]:


Terminal_Value(years)


# In[ ]:


pip install ipympl


# In[ ]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


def Cash_flow_return():
    mean = cash_flow_statement_annually.loc['freeCashFlow'][0:5]
    mean_growth = ((mean[0]-mean[4])/mean[4])/len(mean)
    return mean_growth


# In[ ]:


Cash_flow_return()


# In[ ]:


x = ["A", "B", "C", "D"]
y = [1, 2, 3, 4]
plt. barh(x, y)
)


# In[ ]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
y = np.linspace(2020,2016,5)
for company in d:
    x = d[company].loc['stockPrice'][0:5]
    plt.plot(y, x,  label=str(company))
    for a,b in zip(y, x): 
        plt.text(a, b, str(round(b,2)))
plt.legend(title = 'stonks')  


plt.show()


# In[ ]:





# In[ ]:





# In[ ]:


d["TSLA"].loc["stockPrice"]


# In[ ]:


d


# In[ ]:


income_statement_annually.loc['interestExpense'][0]
balance_sheet_annually.loc['longtermdebt']


# In[ ]:


def WACC():


# In[ ]:


interestExpense = income_statement_annually.loc['interestExpense'][0]
total_debt = balance_sheet_annually.loc['longTermDebt'][0]+balance_sheet_annually.loc['shortTermDebt'][0]
cost_of_debt = interestExpense/total_debt
income_tax_expense = income_statement_annually.loc['incomeTaxExpense'][0]
income_before_tax = income_statement_annually.loc['incomeBeforeTax'][0]
Effective_tax_rate = income_tax_expense/income_before_tax
Cost_of_Debt2 = round(cost_of_debt*(1-Effective_tax_rate)*100,2)


# In[ ]:


def Cost_of_equity(risk_free_rate, beta):
    market_return = 0.0851
    costofequity = risk_free_rate+(beta*(market_return-risk_free_rate))
    return round(costofequity*100,2)


# In[ ]:


def Cost_of_debt():
    interestExpense = income_statement_annually.loc['interestExpense'][0]
    total_debt = balance_sheet_annually.loc['longTermDebt'][0]+balance_sheet_annually.loc['shortTermDebt'][0]
    cost_of_debt = interestExpense/total_debt
    income_tax_expense = income_statement_annually.loc['incomeTaxExpense'][0]
    income_before_tax = income_statement_annually.loc['incomeBeforeTax'][0]
    Effective_tax_rate = income_tax_expense/income_before_tax
    Cost_of_Debt2 = round(cost_of_debt*(1-Effective_tax_rate)*100,2)
    return Cost_of_Debt2


# In[ ]:


def weight_of_debts():
    total = entreprise_value.loc['marketCapitalization'][0]+total_debt
    weight_of_debt = total_debt/total
    weight_of_equity = entreprise_value.loc['marketCapitalization'][0]/total
    return {'weight_of_debt':weight_of_debt , 'weight_of_equity':weight_of_equity}


# In[10]:


def WACC(risk_free_rate, beta):
    
    #COST OF EQUITY
    market_return = 0.0851
    costofequity = risk_free_rate+(beta*(market_return-risk_free_rate))
    costofequity = round(costofequity*100,2)
    
    #COST OF DEBT
    interestExpense = income_statement_annually.loc['interestExpense'][0]
    total_debt = balance_sheet_annually.loc['longTermDebt'][0]+balance_sheet_annually.loc['shortTermDebt'][0]
    cost_of_debt = interestExpense/total_debt
    income_tax_expense = income_statement_annually.loc['incomeTaxExpense'][0]
    income_before_tax = income_statement_annually.loc['incomeBeforeTax'][0]
    Effective_tax_rate = income_tax_expense/income_before_tax
    Cost_of_Debt2 = round(cost_of_debt*(1-Effective_tax_rate)*100,2)
    
    #WEIGHTS
    total = entreprise_value.loc['marketCapitalization'][0]+total_debt
    weight_of_debt = total_debt/total
    weight_of_equity = entreprise_value.loc['marketCapitalization'][0]/total
    
    #WACC FORMULA
    wacc = (weight_of_debt*Cost_of_Debt2)+(weight_of_equity*costofequity)
    return wacc


# In[11]:


WACC(0.001,1.29)


# In[ ]:


cash_flow_statement_annually


# In[12]:


def Fair_Value(years, years_growth_rate_3, growth_rate_3,  years_growth_rate_2,growth_rate_2, discount_rate):
    starting_PE = key_metrics_annually.loc['netIncomePerShare'][0]
    discount_prices = []
    non_discount_prices = []
    for x in range(1,years+1):
        if x >years_growth_rate_2:
            starting_PE = starting_PE*(1+growth_rate_2)
            #print(starting_PE)
            non_discount_prices.append(starting_PE)
            discount_price = starting_PE/((1+discount_rate)**x)
            #print(discount_price)
            discount_prices.append(discount_price)
            #print(discount_prices)
        else:
            starting_PE = starting_PE*(1+growth_rate_3)
            non_discount_prices.append(starting_PE)
            #print(starting_PE)
            discount_price = starting_PE/((1+discount_rate)**x)
            #print(discount_price)
            discount_prices.append(discount_price)
            #print(discount_prices)
    terminal_value_non_disc = non_discount_prices[-2]*Terminal_Value(years)
    termina_value_disc = terminal_value_non_disc/((1+discount_rate)**years)
    intrinsic_value = np.cumsum(discount_prices)[-1]+termina_value_disc
    
    return intrinsic_value


# In[13]:


Fair_Value(10,5,0.15,5,0.1,0.08)


# In[ ]:





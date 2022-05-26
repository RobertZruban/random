#!/usr/bin/env python
# coding: utf-8

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


def Cost_of_equity(risk_free_rate, beta):
    market_return = 0.0851
    costofequity = risk_free_rate+(beta*(market_return-risk_free_rate))
    return round(costofequity*100,2)


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


def Cash_flow_return():
    mean = cash_flow_statement_annually.loc['freeCashFlow'][0:5]
    mean_growth = ((mean[0]-mean[4])/mean[4])/len(mean)
    return mean_growth


# In[ ]:





import pandas as pd
import matplotlib.pyplot as plt
x=pd.read_csv('dataset/Superstore.csv',encoding='latin1')

#Data Cleaning and Organising
x.dropna(inplace=True)
x=x.drop_duplicates()
pd.set_option('display.max_columns', None)
x['Order Date'] = pd.to_datetime(x['Order Date'])
x['Year'] = x['Order Date'].dt.year
x['Month'] = x['Order Date'].dt.month
x['Day'] = x['Order Date'].dt.day
x['Weekday'] = x['Order Date'].dt.day_name()

#overall profit margin and sales analysis
print('\nOverall profit margin and sales analysis\n')
total_sales = x['Sales'].sum()
total_profit = x['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
print(f'Total Sales: ${total_sales:.2f}')
print(f'Total Profit: ${total_profit:.2f}')
print(f'Profit Margin: {profit_margin:.2f}%')

#Sub Category Sales Analysis
print('\nSub Category Sales Analysis\n')
sub_category_sales = x.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
print(sub_category_sales)

#category wise sales and profit analysis
print('\nCategory wise sales and profit analysis\n')
category_sales_profit = x.groupby('Category')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
category_sales_profit['avg_discount (%)'] = x.groupby('Category')['Discount'].mean()*100
category_sales_profit['profit_margin (%)'] = (category_sales_profit['Profit'] / category_sales_profit['Sales']) * 100
print(category_sales_profit)

#Segment wise analysis
print('\nSegment wise analysis\n')
segment_sales_profit = x.groupby('Segment')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
segment_sales_profit['profit_margin (%)'] = (segment_sales_profit['Profit'] / segment_sales_profit['Sales']) * 100
segment_sales_profit.sort_values(by='profit_margin (%)', ascending=False, inplace=True)
print(segment_sales_profit)

#State wise analysis
print('\nState wise analysis\n')
state_sales_profit = x.groupby('State')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
state_sales_profit['profit_margin (%)'] = (state_sales_profit['Profit'] / state_sales_profit['Sales']) * 100
state_sales_profit.sort_values(by='profit_margin (%)', ascending=False, inplace=True)
print(state_sales_profit)

#Shipping Analysis
print('\nShipping Analysis\n')
shipping_analysis = x.groupby('Ship Mode')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
avg_profit_shipping = x.groupby('Ship Mode')[['Profit']].mean().sort_values(by='Profit', ascending=False)
print(shipping_analysis)
print(avg_profit_shipping)

#Loss making products 
print('\nLoss making products\n')
product_loss= x.groupby('Product Name')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=True)
product_loss= product_loss[product_loss['Profit']<0]
product_loss['profit_margin (%)'] = (product_loss['Profit'] / product_loss['Sales']) * 100
#product_loss.sort_values(by='profit_margin (%)', ascending=True, inplace=True)
print(product_loss.head(10))

#discount analysis
print('\nDiscount Analysis\n')
discount_sales_profit= x.groupby('Discount')[['Profit','Sales']].mean().sort_values(by='Discount', ascending=True)
print(discount_sales_profit)







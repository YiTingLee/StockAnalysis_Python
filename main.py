import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file

def inc_dec(c,o):
    if(c>o):
        value="Increase"
    elif(c<o):
        value="Decrease"
    else:
        value="Equal"
    return value

start = datetime.datetime(2016,3,1)
end = datetime.datetime(2017,7,10)

df = data.DataReader(name="GOOG", data_source="google", start=start, end=end)

df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open+df.Close)/2
df["Height"] = abs(df.Open-df.Close)

print(df)

# date_increase = df.index[df.Close > df.Open]
# date_decrease = df.index[df.Close < df.Open]

# print(date_increase)

p = figure(x_axis_type='datetime', width=1600, height=500, title="Candlestick Chart")
p.grid.grid_line_alpha = 0.3

hours_12=12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color = 'Black')

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"], fill_color='green', line_color='black')
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], fill_color='red', line_color='black')
output_file("CS.html")
show(p)
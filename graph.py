import os
import pprint
import random
import sys
import wx
import krakenex
import decimal
import time

import json
import requests

import wx.html
import webbrowser
import wx.html2
import wx.richtext

import urllib

from requests_futures.sessions import FuturesSession

session = FuturesSession()

class MyBrowser(wx.Dialog):
  def __init__(self, *args, **kwds):
    wx.Dialog.__init__(self, *args, **kwds)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.browser = wx.html2.WebView.New(self)
    sizer.Add(self.browser, 1, wx.EXPAND, 10)
    self.SetSizer(sizer)
    self.SetSize((700, 800))


global app, pairs, pair_pcts, pair_first_vals

pairs = []
pair_pcts = []
pair_first_vals = []

# start with this list id:
global list_id
global app
list_id = 1

k = krakenex.API()

# The recommended way to use wx with mpl is with the WXAgg backend.
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
import pylab

ymin_control_auto = True
ymax_control_auto = True
xmin_control_auto = True
xmax_control_auto = True

class RateVisualizer(object):
    def __init__(self, init=-1):
        self.data = self.init = init

    def next(self):
        self._recalc_data()
        return self.data

    def _recalc_data(self):
        pass

class BoundControlBox(wx.Panel):
    """ A static box with a couple of radio buttons and a text
        box. Allows to switch between an automatic mode and a 
        manual mode with an associated value.
    """
    def __init__(self, parent, ID, label, initval):
        wx.Panel.__init__(self, parent, ID)

        self.value = initval

        box = wx.StaticBox(self, -1, label)
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        self.SetSizer(sizer)
        sizer.Fit(self)

class GraphFrame(wx.Frame):
    """ The main frame of the application
    """
    title = 'Coinium Portfolio Manager'

    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title, pos = wx.Point(50,50))#size = wx.Size(200, 200))

        self.modify_boxes_visible = False
        self.add_boxes_visible = False

        self.rate_visualizer = RateVisualizer()
        self.data = [self.rate_visualizer.next()]
        self.paused = False

        self.create_menu()
        self.create_status_bar()
        self.create_main_panel()

        self.redraw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_redraw_timer, self.redraw_timer)
        self.redraw_timer.Start(1500)

    def create_menu(self):
        self.menubar = wx.MenuBar()

        menu_file = wx.Menu()
        m_expt = menu_file.Append(-1, "&Save plot\tCtrl-S", "Save plot to file")
        self.Bind(wx.EVT_MENU, self.on_save_plot, m_expt)
        menu_file.AppendSeparator()
        m_exit = menu_file.Append(-1, "E&xit\tCtrl-X", "Exit")
        self.Bind(wx.EVT_MENU, self.on_exit, m_exit)

        self.menubar.Append(menu_file, "&File")
        self.SetMenuBar(self.menubar)

    def create_main_panel(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((255,255,255))

        self.init_plot()
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        api_token = 'your_api_token'
        api_url_base = 'https://coinium.app/api.php/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token)}
        api_url = '{0}Distributions'.format(api_url_base)
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            val = json.loads(response.content.decode('utf-8'))
        else:
            val = None
        print("val", val)
        print("first distribution:", val['Distributions']['records'][0])

        first_dist = val['Distributions']['records'][0]
        tmp_pair_pcts = [first_dist[1] / 100.0, first_dist[2] / 100.0, first_dist[3] / 100.0]
        tmp_pairs = ["XXBTZUSD", "XETHZUSD", "XXRPZUSD"]
        title_str = ""
        for i in range(len(tmp_pairs)):
            title_str += str(tmp_pairs[i]) + ": " + str(tmp_pair_pcts[i] * 100) + "%, "
        self.axes.set_title(title_str, size=12)

        self.axes.text(0.64, 0.03, 'http://coinium.app',
            verticalalignment='bottom', horizontalalignment='right',
            transform=self.axes.transAxes,
            color='lightblue', fontsize=13)

        distributions = []
        for dist in val['Distributions']['records']:
            api_url = "https://coinium.app/api.php/ListHasDistribution?filter=distribution_id,eq," + str(dist[0])
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                val = json.loads(response.content.decode('utf-8'))
                print("val", val)
            else:
                val = None
            if val and len(val["ListHasDistribution"]["records"]):
                strval = "list#" + str(val["ListHasDistribution"]["records"][0][1]) + " BTC: " + str(dist[1]) + "% "
                strval += "ETH: " + str(dist[2]) + "% "
                strval += "XRP: " + str(dist[3]) + "%"
                distributions.append(strval)

        # logo & text
        png = wx.Image("/Users/seckin/coinium/coinium.png", wx.BITMAP_TYPE_ANY).Rescale(50, 50).ConvertToBitmap()
        self.coinium_image = wx.StaticBitmap(self.panel, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))
        # portfolio list
        self.lst = wx.ListBox(self.panel, size = (260,500), choices = distributions, style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst)
        self.lst.Bind(wx.EVT_KILL_FOCUS, self.onListBoxUnfocused)
        self.coinium_text = wx.StaticText(self.panel, -1, label="Coinium", size = (150,50))
        self.coinium_text.SetLabelMarkup("<span foreground='blue' size='30720' font_weight='ultrabold'>Coinium</span>")
        self.portfolio_list_text = wx.StaticText(self.panel, -1, label="Portfolio List", size = (85,15))
        # adding logo, text and portfolio list
        self.hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox11.Add(self.coinium_image, border=5, flag=wx.ALL | wx.ALIGN_LEFT)
        self.hbox11.Add(self.coinium_text, border=5, flag=wx.ALL | wx.ALIGN_LEFT)
        self.vbox4 = wx.BoxSizer(wx.VERTICAL)
        self.vbox4.Add(self.hbox11, border=5, flag=wx.ALL | wx.ALIGN_LEFT)
        self.vbox4.Add(self.portfolio_list_text, border=5, flag=wx.ALL | wx.ALIGN_LEFT)
        self.vbox4.AddSpacer(0)
        self.vbox4.Add(self.lst, border=5, flag=wx.ALL | wx.ALIGN_LEFT)

        # interval choice
        self.interval_choice_text = wx.StaticText(self.panel, -1, label="Interval:", size = (55,20))
        self.choice = wx.Choice(self.panel,choices = ["30 secs", "5 mins", "2 hours", "1 day"])
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        self.hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox0.Add(self.interval_choice_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT)
        self.hbox0.AddSpacer(2)
        self.hbox0.Add(self.choice, border=5, flag=wx.ALL | wx.ALIGN_TOP)

        # edit portfolio
        self.modify_btc_text = wx.StaticText(self.panel, -1, label="BTC:", size = (35,20))
        self.modify_btc_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.modify_eth_text = wx.StaticText(self.panel, -1, label="ETH:", size = (35,20))
        self.modify_eth_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.modify_xrp_text = wx.StaticText(self.panel, -1, label="XRP:", size = (35,20))
        self.modify_xrp_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.modify_distribution_button = wx.Button(self.panel, -1, "Edit Portfolio")
        self.Bind(wx.EVT_BUTTON, self.on_modify_distribution_button, self.modify_distribution_button)
        self.submit_distribution_modification_button = wx.Button(self.panel, -1, "Submit")
        self.Bind(wx.EVT_BUTTON, self.on_submit_distribution_modification_button, self.submit_distribution_modification_button)
        self.cancel_distribution_modification_button = wx.Button(self.panel, -1, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.on_cancel_distribution_modification_button, self.cancel_distribution_modification_button)
        self.modify_distribution_button.Hide()
        self.modify_eth_input_box.Hide()
        self.modify_btc_input_box.Hide()
        self.modify_xrp_input_box.Hide()
        self.modify_btc_text.Hide()
        self.modify_eth_text.Hide()
        self.modify_xrp_text.Hide()
        self.submit_distribution_modification_button.Hide()
        self.cancel_distribution_modification_button.Hide()
        # edit portfolio placing
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # self.hbox2.Add(self.modify_btc_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(2)
        # self.hbox2.Add(self.modify_btc_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.Add(self.modify_eth_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(2)
        # self.hbox2.Add(self.modify_eth_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.Add(self.modify_xrp_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(2)
        # self.hbox2.Add(self.modify_xrp_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(5)
        # self.hbox2.Add(self.modify_distribution_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(5)
        # self.hbox2.Add(self.submit_distribution_modification_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(5)
        # self.hbox2.Add(self.cancel_distribution_modification_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        # self.hbox2.AddSpacer(25)

        # add portfolio buttons
        self.btc_text = wx.StaticText(self.panel, -1, label="BTC:", size = (35,20))
        self.btc_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.eth_text = wx.StaticText(self.panel, -1, label="ETH:", size = (35,20))
        self.eth_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.xrp_text = wx.StaticText(self.panel, -1, label="XRP:", size = (35,20))
        self.xrp_input_box = wx.TextCtrl(self.panel,size = (35,20))
        self.add_distribution_button = wx.Button(self.panel, -1, "Add New Portfolio")
        self.Bind(wx.EVT_BUTTON, self.on_add_distribution_button, self.add_distribution_button)
        self.submit_new_distribution_button = wx.Button(self.panel, -1, "Submit")
        self.Bind(wx.EVT_BUTTON, self.on_submit_new_distribution_button, self.submit_new_distribution_button)
        self.cancel_new_distribution_button = wx.Button(self.panel, -1, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.on_cancel_new_distribution_button, self.cancel_new_distribution_button)
        self.eth_input_box.Hide()
        self.btc_input_box.Hide()
        self.xrp_input_box.Hide()
        self.btc_text.Hide()
        self.eth_text.Hide()
        self.xrp_text.Hide()
        self.submit_new_distribution_button.Hide()
        self.cancel_new_distribution_button.Hide()
        # add portfolio placing
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1.Add(self.btc_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(2)
        self.hbox1.Add(self.btc_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.Add(self.eth_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(2)
        self.hbox1.Add(self.eth_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.Add(self.xrp_text, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(2)
        self.hbox1.Add(self.xrp_input_box, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(5)
        self.hbox1.Add(self.add_distribution_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(5)
        self.hbox1.Add(self.submit_new_distribution_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(5)
        self.hbox1.Add(self.cancel_new_distribution_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(24)

        # Current prices
        self.current_prices = wx.StaticText(self.panel, -1, label="Current prices", size = (95,20))
        self.btc_price_text_name = wx.StaticText(self.panel, -1, label="BTC:", size = (35,20))
        self.btc_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.eth_price_text_name = wx.StaticText(self.panel, -1, label="ETH:", size = (35,20))
        self.eth_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.xrp_price_text_name = wx.StaticText(self.panel, -1, label="XRP:", size = (35,20))
        self.xrp_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox4.AddSpacer(45)
        self.hbox4.Add(self.current_prices, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox5.Add(self.btc_price_text_name, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox5.AddSpacer(2)
        self.hbox5.Add(self.btc_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox6.Add(self.eth_price_text_name, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox6.AddSpacer(2)
        self.hbox6.Add(self.eth_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox7.Add(self.xrp_price_text_name, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox7.AddSpacer(2)
        self.hbox7.Add(self.xrp_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        # last 24 hours
        self.last_24_hours_prices = wx.StaticText(self.panel, -1, label="Last 24 hours", size = (95,20))
        self.last_24_hours_btc_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.last_24_hours_eth_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.last_24_hours_xrp_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.hbox4.AddSpacer(20)
        self.hbox4.Add(self.last_24_hours_prices, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox5.AddSpacer(40)
        self.hbox5.Add(self.last_24_hours_btc_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox6.AddSpacer(40)
        self.hbox6.Add(self.last_24_hours_eth_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox7.AddSpacer(40)
        self.hbox7.Add(self.last_24_hours_xrp_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        # last week
        self.last_week_prices = wx.StaticText(self.panel, -1, label="Last week", size = (95,20))
        self.last_week_btc_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.last_week_eth_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.last_week_xrp_price_text = wx.StaticText(self.panel, -1, label="...", size = (75,20))
        self.hbox4.AddSpacer(20)
        self.hbox4.Add(self.last_week_prices, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox5.AddSpacer(40)
        self.hbox5.Add(self.last_week_btc_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox6.AddSpacer(40)
        self.hbox6.Add(self.last_week_eth_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        self.hbox7.AddSpacer(40)
        self.hbox7.Add(self.last_week_xrp_price_text, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)

        # add usd
        # self.add_usd_label = wx.StaticText(self.panel, -1, label="Add USD:", size = (65,20))
        # self.add_usd_input_box = wx.TextCtrl(self.panel,size = (30,20))
        # self.add_usd_button = wx.Button(self.panel, -1, "Checkout")
        # self.Bind(wx.EVT_BUTTON, self.on_add_usd_button, self.add_usd_button)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # self.hbox3.Add(self.add_usd_label, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        # self.hbox3.AddSpacer(2)
        # self.hbox3.Add(self.add_usd_input_box, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        # self.hbox3.AddSpacer(2)
        # self.hbox3.Add(self.add_usd_button, border=5, flag=wx.ALL | wx.ALIGN_BOTTOM)
        # self.hbox3.AddSpacer(2)

        self.vbox5 = wx.BoxSizer(wx.VERTICAL)
        self.vbox5.Add(self.canvas, 1, flag=wx.ALIGN_LEFT | wx.TOP | wx.GROW)
        self.vbox5.Add(self.hbox0, 0, flag=wx.ALIGN_RIGHT | wx.TOP)
        self.vbox5.Add(self.hbox4, 0, flag=wx.ALIGN_LEFT | wx.TOP)
        self.vbox5.Add(self.hbox5, 0, flag=wx.ALIGN_LEFT | wx.TOP)
        self.vbox5.Add(self.hbox6, 0, flag=wx.ALIGN_LEFT | wx.TOP)
        self.vbox5.Add(self.hbox7, 0, flag=wx.ALIGN_LEFT | wx.TOP)

        self.hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox8.Add(self.vbox4, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.GROW)
        self.hbox8.Add(self.vbox5, 1, flag=wx.ALIGN_RIGHT | wx.BOTTOM)

        self.vbox9 = wx.BoxSizer(wx.VERTICAL)
        self.vbox9.Add(self.hbox1, 1, flag=wx.ALIGN_LEFT | wx.TOP)
        self.vbox9.Add(self.hbox2, 1, flag=wx.ALIGN_LEFT | wx.BOTTOM)
        self.vbox9.Add(self.hbox3, 1, flag=wx.ALIGN_RIGHT | wx.BOTTOM)

        self.vbox6 = wx.BoxSizer(wx.VERTICAL)
        self.vbox6.Add(self.hbox8, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.GROW)
        self.vbox6.Add(self.vbox9, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.GROW)

        # self.vbox6 = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.vbox6)
        self.vbox6.Fit(self)
        self.vbox6.Layout()

        # self.vbox5.Fit(self)
        # self.vbox5.Layout()


    def create_status_bar(self):
        self.statusbar = self.CreateStatusBar()

    def init_plot(self):
        global pairs, pair_pcts
        self.dpi = 100
        self.fig = Figure((3.0, 3.0), dpi=self.dpi)

        self.axes = self.fig.add_subplot(111)
        self.axes.set_axis_bgcolor('gray')
        title_str = ""
        for i in range(len(pairs)):
            title_str += str(pairs[i]) + ": " + str(pair_pcts[i] * 100) + "%, "
        self.axes.set_title(title_str, size=12)

        pylab.setp(self.axes.get_xticklabels(), fontsize=8)
        pylab.setp(self.axes.get_yticklabels(), fontsize=8)

        # plot the data as a line series, and save the reference to the plotted line series
        self.plot_data = self.axes.plot(
            self.data,
            linewidth=1,
            color=(1, 1, 0),
            )[0]

    def draw_plot(self):
        """ Redraws the plot
        """
        # print("self.data", self.data)
        if xmax_control_auto or self.xmax_control.is_auto():
            xmax = len(self.data)# if len(self.data) > 75 else 75
        else:
            xmax = int(self.xmax_control.manual_value())

        if xmin_control_auto or self.xmin_control.is_auto():
            xmin = xmax - 75
        else:
            xmin = int(self.xmin_control.manual_value())

        if ymin_control_auto or self.ymin_control.is_auto():
            ymin = min(self.data[-75:-1]) * (1.0 - 0.004) #- (max(self.data) - 1.0) * 2
        else:
            ymin = int(self.ymin_control.manual_value())

        if ymax_control_auto or self.ymax_control.is_auto():
            ymax = max(self.data[-75:-1]) * (1.0 + 0.004) #+ (max(self.data) - 1.0) * 2
        else:
            ymax = int(self.ymax_control.manual_value())

        self.axes.set_xbound(lower=xmin, upper=xmax)
        self.axes.set_ybound(lower=ymin, upper=ymax)
        # print("ymin", ymin, "ymax", ymax)
        # print("xmin", xmin, "xmax", xmax)

        # anecdote: axes.grid assumes b=True if any other flag is
        # given even if b is set to False.
        # so just passing the flag into the first statement won't
        # work.
        #
        if True:
            self.axes.grid(True, color='white')
        else:
            self.axes.grid(False)

        # print("calling annotate")
        # self.axes.annotate('annotate', xy=(1, 1.0), xytext=(40, 1.0), arrowprops=dict(facecolor='black', shrink=0.05))
        # self.axes.annotate('Now', xy=(xmax, ymin), xytext=(xmax, (ymin + ymax) / 2.0), arrowprops=dict(facecolor='black', shrink=0.05))
        # self.axes.text(2, 1, r'an equation: $E=mc^2$', fontsize=15)

        # Using setp here is convenient, because get_xticklabels
        # returns a list over which one needs to explicitly 
        # iterate, and setp already handles this.
        #  
        lst = self.axes.get_xticklabels()
        # setp_xlabels = []
        i = 0
        text = lst[0].get_text()
        interval_in_secs = self.get_interval_in_secs_chosen()
        for x in lst:
            # x.set_text(str((0 if x.get_text() == '' else float(x.get_text().replace("−","-"))) - xmax) + "s ago")
            val = (i - len(lst) + 1) * 10 * interval_in_secs
            absval = abs(val)
            strval = ""
            if int(absval / 3600) > 0:
                strval += str(int(absval / 3600)) + "h "
                absval = absval % 3600
            if int(absval / 60) > 0:
                strval += str(int(absval / 60)) + "m "
                absval = absval % 60
            if absval > 0:
                strval += str(int(absval)) + "s "

            if strval == "":
                result_strval = ""
            else:
                if i == len(lst) - 2:
                    result_strval = "<" + str(strval) + "ago"
                else:
                    result_strval = str(strval) + "ago"
            x.set_text(result_strval)
            # setp_xlabels.append(x)
            i+=1
        self.axes.set_xticklabels(lst)
        pylab.setp(lst,
            visible=True)

        self.plot_data.set_xdata(np.arange(len(self.data)))
        self.plot_data.set_ydata(np.array(self.data))

        self.canvas.draw()

    def onListBoxUnfocused(self, event):
        print("onListBoxUnfocused")
        focused_elem = wx.Window.FindFocus()
        if focused_elem != self.lst and \
           focused_elem != self.modify_eth_input_box and \
           focused_elem != self.modify_btc_input_box and \
           focused_elem != self.modify_xrp_input_box and \
           focused_elem != self.submit_distribution_modification_button:
            self.modify_eth_input_box.Hide()
            self.modify_btc_input_box.Hide()
            self.modify_xrp_input_box.Hide()
            self.modify_btc_text.Hide()
            self.modify_eth_text.Hide()
            self.modify_xrp_text.Hide()
            self.modify_boxes_visible = False
            self.submit_distribution_modification_button.Hide()
            self.cancel_distribution_modification_button.Hide()
        self.modify_distribution_button.Hide()
        self.vbox6.Layout()

    def OnChoice(self, event):
        print("self.choice.GetSelection()", self.choice.GetSelection())
        print("choice updated to", self.choice.GetString(self.choice.GetSelection()))

    def update_pair_distributions(self, list_id):
        global app, pairs, pair_pcts, pair_first_vals
        print("update_pair_distributions called")
        headers = {'Content-Type': 'application/json'}
        response = requests.get("https://coinium.app/api.php/ListHasDistribution?filter=list_id,eq," + str(list_id), headers=headers)
        if response.status_code == 200:
            list_has_distributions = json.loads(response.content.decode('utf-8'))
        else:
            list_has_distributions = None

        # get the distribution id of the first distribution(of the list with id = list_id)
        distribution_id = list_has_distributions["ListHasDistribution"]["records"][0][2]

        headers = {'Content-Type': 'application/json'}
        response = requests.get("https://coinium.app/api.php/Distributions?filter=id,eq," + str(distribution_id), headers=headers)
        if response.status_code == 200:
            distributions = json.loads(response.content.decode('utf-8'))
        else:
            distributions = None

        distribution_record = distributions["Distributions"]["records"][0]
        pair_pcts = [distribution_record[1] / 100.0, distribution_record[2] / 100.0, distribution_record[3] / 100.0]
        pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
        pair_first_vals = [-1, -1, -1]
        print("pairs", pairs)
        print("pair_pcts", pair_pcts)
        print("")

    def onListBox(self, event):
        global list_id
        global app, pairs, pair_pcts, pair_first_vals
        print( "Current selection: \
            "+event.GetEventObject().GetStringSelection()+"\n")
        print("calling self.modify_distribution_button.Show()")
        if self.modify_boxes_visible:
            self.modify_distribution_button.Hide()
        else:
            self.modify_distribution_button.Show()
        self.vbox6.Layout()

        strval = event.GetEventObject().GetStringSelection()
        strs = strval.split(":")
        list_id = int(strs[0].split("#")[1].split(" ")[0])
        print("list_id updated to:", list_id)
        self.update_pair_distributions(list_id)
        title_str = ""
        for i in range(len(pairs)):
            title_str += str(pairs[i]) + ": " + str(pair_pcts[i] * 100) + "%, "
        self.axes.set_title(title_str, size=12)
        btc_pct = int(strs[1].split("%")[0])
        eth_pct = int(strs[2].split("%")[0])
        xrp_pct = int(strs[3].split("%")[0])
        self.modify_btc_input_box.SetValue(str(btc_pct))
        self.modify_eth_input_box.SetValue(str(eth_pct))
        self.modify_xrp_input_box.SetValue(str(xrp_pct))

    def on_add_distribution_button(self, event):
        self.eth_input_box.Show()
        self.btc_input_box.Show()
        self.xrp_input_box.Show()
        self.btc_text.Show()
        self.eth_text.Show()
        self.xrp_text.Show()
        self.add_distribution_button.Hide()
        self.submit_new_distribution_button.Show()
        self.cancel_new_distribution_button.Show()
        self.add_boxes_visible = True
        self.vbox6.Layout()

    def hide_all_add_boxes_except_add_new_pv_button(self):
        self.eth_input_box.Hide()
        self.btc_input_box.Hide()
        self.xrp_input_box.Hide()
        self.btc_text.Hide()
        self.eth_text.Hide()
        self.xrp_text.Hide()
        self.add_distribution_button.Show()
        self.submit_new_distribution_button.Hide()
        self.cancel_new_distribution_button.Hide()
        self.add_boxes_visible = False
        self.vbox6.Layout()

    def on_cancel_new_distribution_button(self, event):
        self.hide_all_add_boxes_except_add_new_pv_button()

    def on_submit_new_distribution_button(self, event):
        ethval = int(self.eth_input_box.GetValue())
        btcval = int(self.btc_input_box.GetValue())
        xrpval = int(self.xrp_input_box.GetValue())
        if abs(ethval) + abs(btcval) + abs(xrpval) != 100:
            print(str(ethval) + " " + str(btcval) + " " + str(xrpval) + " absolute values don't add up to 100")
            return

        self.hide_all_add_boxes_except_add_new_pv_button()

        api_token = 'your_api_token'
        api_url_base = 'https://coinium.app/api.php/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token)}
        api_url = '{0}Distributions'.format(api_url_base)
        response = requests.post(api_url, headers=headers, data = {"btc":btcval, "xrp":xrpval, "eth":ethval})
        if response.status_code == 200:
            val = json.loads(response.content.decode('utf-8'))
            print("distribution creation server response:", val)
            api_url = '{0}Lists'.format(api_url_base)
            response = requests.post(api_url, headers=headers, data = {"name":"list with dist#" + str(val)})
            if response.status_code == 200:
                val2 = json.loads(response.content.decode('utf-8'))
                print("list creation server response:", val2)
                strval = "list#" + str(val2) + " BTC: " + str(btcval) + "% "
                strval += "ETH: " + str(ethval) + "% "
                strval += "XRP: " + str(xrpval) + "%"
                print("adding new list to listbox:", strval)
                self.lst.Append(strval)
                api_url = '{0}ListHasDistribution'.format(api_url_base)
                response = requests.post(api_url, headers=headers, data = {"list_id":val2, "distribution_id":val, "timestamp": int(time.time())})
                if response.status_code == 200:
                    val3 = json.loads(response.content.decode('utf-8'))
                    print("ListHasDistribution creation server response:", val3)
        else:
            val = None

    def on_modify_distribution_button(self, event):
        self.modify_eth_input_box.Show()
        self.modify_btc_input_box.Show()
        self.modify_xrp_input_box.Show()
        self.modify_btc_text.Show()
        self.modify_eth_text.Show()
        self.modify_xrp_text.Show()
        self.submit_distribution_modification_button.Show()
        self.cancel_distribution_modification_button.Show()
        self.modify_boxes_visible = True
        self.vbox6.Layout()

    def hide_all_modification_boxes_except_edit_button(self):
        self.modify_eth_input_box.Hide()
        self.modify_btc_input_box.Hide()
        self.modify_xrp_input_box.Hide()
        self.modify_btc_text.Hide()
        self.modify_eth_text.Hide()
        self.modify_xrp_text.Hide()
        self.submit_distribution_modification_button.Hide()
        self.cancel_distribution_modification_button.Hide()
        self.modify_distribution_button.Show()
        self.modify_boxes_visible = False
        self.vbox6.Layout()

    def on_cancel_distribution_modification_button(self, event):
        self.hide_all_modification_boxes_except_edit_button()

    def on_submit_distribution_modification_button(self, event):
        cnt = self.lst.GetCount()
        ethval = int(self.modify_eth_input_box.GetValue())
        btcval = int(self.modify_btc_input_box.GetValue())
        xrpval = int(self.modify_xrp_input_box.GetValue())
        if abs(ethval) + abs(btcval) + abs(xrpval) != 100:
            print(str(ethval) + " " + str(btcval) + " " + str(xrpval) + " absolute values don't add up to 100")
            return

        self.hide_all_modification_boxes_except_edit_button()

        for i in range(cnt):
            if self.lst.IsSelected(i):
                strval = self.lst.GetStringSelection()
        strs = strval.split(":")
        list_id = int(strs[0].split("#")[1].split(" ")[0])
        print("list_id:", list_id)



        headers = {'Content-Type': 'application/json'}
        response = requests.get("https://coinium.app/api.php/ListHasDistribution?filter=list_id,eq," + str(list_id), headers=headers)
        if response.status_code == 200:
            list_has_distributions = json.loads(response.content.decode('utf-8'))
        else:
            list_has_distributions = None

        if not list_has_distributions:
            print("not list_has_distributions")
            return
        # get the distribution id of the first distribution(of the list with id = list_id)
        distribution_id = list_has_distributions["ListHasDistribution"]["records"][0][2]
        print("distribution_id", distribution_id)


        api_token = 'your_api_token'
        api_url_base = 'https://coinium.app/api.php/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token)}
        api_url = '{0}Distributions/{1}'.format(api_url_base, distribution_id)
        response = requests.put(api_url, headers=headers, data = {"btc":btcval, "xrp":xrpval, "eth":ethval})
        if response.status_code == 200:
            num_distributions_affected = json.loads(response.content.decode('utf-8'))
            print("num_distributions_affected", num_distributions_affected)
        else:
            print("couldn't update distribution")


        # to test:
        # headers = {'Content-Type': 'application/json'}
        # response = requests.get("https://coinium.app/api.php/Distributions?filter=id,eq," + str(distribution_id), headers=headers)
        # if response.status_code == 200:
        #     distributions = json.loads(response.content.decode('utf-8'))
        # else:
        #     distributions = None
        # print("distributions returned:", distributions)


        for i in range(cnt):
            if self.lst.IsSelected(i):
                strval = "list#" + str(list_id) + " BTC: " + str(btcval) + "% "
                strval += "ETH: " + str(ethval) + "% "
                strval += "XRP: " + str(xrpval) + "%"
                print("updating distribution to:", strval)
                self.lst.SetString(i, strval)

    def on_add_usd_button(self, event):
        api_token = 'your_api_token'
        api_url_base = 'https://coinium.app/api.php/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token)}
        api_url = '{0}Subscription'.format(api_url_base)
        response = requests.post(api_url, headers=headers, data = {"list_id":list_id, "user_id":1, "dollar_amount":float(self.add_usd_input_box.GetValue()), "timestamp": int(time.time()), "approved": 0})
        if response.status_code == 200:
            subscription_val = json.loads(response.content.decode('utf-8'))
        else:
            subscription_val = None

        dialog = MyBrowser(None, -1)
        item_name = urllib.parse.quote("Fund for Coinium Account. Invoice #" + str(subscription_val))
        dollar_amount = str(float(self.add_usd_input_box.GetValue()))
        invoice_name = urllib.parse.quote("Coinium Invoice #" + str(subscription_val))
        link = "https://www.coinpayments.net/index.php?cmd=_pay&reset=1&merchant=e3e3958eff15be8c85dcbe83c3803da4&item_name=" + item_name + "&invoice=" + invoice_name + "&currency=USD&amountf=" + dollar_amount + "&quantity=1&allow_quantity=0&want_shipping=0&allow_extra=0&"
        print("link", link)
        dialog.browser.LoadURL(link)
        dialog.Show()

    def on_save_plot(self, event):
        file_choices = "PNG (*.png)|*.png"

        dlg = wx.FileDialog(
            self, 
            message="Save plot as...",
            defaultDir=os.getcwd(),
            defaultFile="coinium plot.png",
            wildcard=file_choices,
            style=wx.FD_SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas.print_figure(path, dpi=self.dpi)
            self.flash_status_message("Saved to %s" % path)

    def bg_cb(self, sess, resp):
        resp.data = resp.json()

    def get_interval_in_secs_chosen(self):
        selection = self.choice.GetSelection()
        selected_int_str = self.choice.GetString(selection) #["30 secs", "5 mins", "2 hours", "1 day"])
        if selected_int_str == "30 secs":
            interval_in_secs = 30
        elif selected_int_str == "5 mins":
            interval_in_secs = 300
        elif selected_int_str == "2 hours":
            interval_in_secs = 7200
        elif selected_int_str == "1 day":
            interval_in_secs = 86400
        return interval_in_secs

    def update_current_prices(self):
        headers = {'Content-Type': 'application/json'}
        timestamp = int(time.time())
        timestamp -= 7500
        api_url = "http://104.131.139.250/api.php/Spreads?filter=timestamp,gt," + str(timestamp)
        print("update_current_prices api_url:", api_url)
        future = session.get(api_url, background_callback=self.bg_cb)
        response = future.result()
        # response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            retval = json.loads(response.content.decode('utf-8'))
        else:
            retval = None

        if retval:
            latest_prices = retval["Spreads"]["records"]
            # print("latest_prices", latest_prices)
            #btc
            i = len(latest_prices) - 1
            while i > 0:
                if latest_prices[i][1] == "XXBTZUSD":
                    break
                else:
                    i -= 1
            btc_mid_mkt = (latest_prices[i][2] + latest_prices[i][3]) / 2.0
            self.btc_price_text.SetLabel("$" + str(round(btc_mid_mkt, 4)))

            #eth
            i = len(latest_prices) - 1
            while i > 0:
                if latest_prices[i][1] == "XETHZUSD":
                    break
                else:
                    i -= 1
            eth_mid_mkt = (latest_prices[i][2] + latest_prices[i][3]) / 2.0
            self.eth_price_text.SetLabel("$" + str(round(eth_mid_mkt, 4)))

            #xrp
            i = len(latest_prices) - 1
            while i > 0:
                if latest_prices[i][1] == "XXRPZUSD":
                    break
                else:
                    i -= 1
            xrp_mid_mkt = (latest_prices[i][2] + latest_prices[i][3]) / 2.0
            self.xrp_price_text.SetLabel("$" + str(round(xrp_mid_mkt, 4)))

            # last 24 hours
            headers = {'Content-Type': 'application/json'}
            timestamp = int(time.time())
            timestamp -= (24 * 60 * 60)
            api_url = "http://104.131.139.250/api.php/Spreads?filter=timestamp,bt," + str(timestamp) + "," + str(timestamp + 250)
            # print("update_24_hour_prices api_url:", api_url)
            future = session.get(api_url, background_callback=self.bg_cb)
            response = future.result()
            # response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                retval = json.loads(response.content.decode('utf-8'))
            else:
                retval = None
            if retval:
                last_24_hour_prices = retval["Spreads"]["records"]
                # print("last_24_hour_prices", last_24_hour_prices)
                #btc
                i = 0
                while i < len(last_24_hour_prices):
                    if last_24_hour_prices[i][1] == "XXBTZUSD":
                        break
                    else:
                        i += 1
                btc_24_hour_mid_mkt = (last_24_hour_prices[i][2] + last_24_hour_prices[i][3]) / 2.0
                self.last_24_hours_btc_price_text.SetLabel(("+" if btc_mid_mkt > btc_24_hour_mid_mkt else "") + \
                    str(round(100.0 * (btc_mid_mkt / btc_24_hour_mid_mkt) - 100.0, 1)) + "%")

                #eth
                i = 0
                while i < len(last_24_hour_prices):
                    if last_24_hour_prices[i][1] == "XETHZUSD":
                        break
                    else:
                        i += 1
                eth_24_hour_mid_mkt = (last_24_hour_prices[i][2] + last_24_hour_prices[i][3]) / 2.0
                self.last_24_hours_eth_price_text.SetLabel(("+" if eth_mid_mkt > eth_24_hour_mid_mkt else "") + \
                    str(round(100.0 * (eth_mid_mkt / eth_24_hour_mid_mkt) - 100.0, 1)) + "%")

                #xrp
                i = 0
                while i < len(last_24_hour_prices):
                    if last_24_hour_prices[i][1] == "XXRPZUSD":
                        break
                    else:
                        i += 1
                xrp_24_hour_mid_mkt = (last_24_hour_prices[i][2] + last_24_hour_prices[i][3]) / 2.0
                self.last_24_hours_xrp_price_text.SetLabel(("+" if xrp_mid_mkt > xrp_24_hour_mid_mkt else "") + \
                    str(round(100.0 * (xrp_mid_mkt / xrp_24_hour_mid_mkt) - 100.0, 1)) + "%")

            # last week
            headers = {'Content-Type': 'application/json'}
            timestamp = int(time.time())
            timestamp -= (7 * 24 * 60 * 60)
            api_url = "http://104.131.139.250/api.php/Spreads?filter=timestamp,bt," + str(timestamp) + "," + str(timestamp + 250)
            # print("update_24_hour_prices api_url:", api_url)
            future = session.get(api_url, background_callback=self.bg_cb)
            response = future.result()
            # response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                retval = json.loads(response.content.decode('utf-8'))
            else:
                retval = None
            if retval:
                last_week_prices = retval["Spreads"]["records"]
                #btc
                i = 0
                while i < len(last_week_prices):
                    if last_week_prices[i][1] == "XXBTZUSD":
                        break
                    else:
                        i += 1
                btc_week_mid_mkt = (last_week_prices[i][2] + last_week_prices[i][3]) / 2.0
                self.last_week_btc_price_text.SetLabel(("+" if btc_mid_mkt > btc_week_mid_mkt else "") + \
                    str(round(100.0 * (btc_mid_mkt / btc_week_mid_mkt) - 100.0, 1)) + "%")

                #eth
                i = 0
                while i < len(last_week_prices):
                    if last_week_prices[i][1] == "XETHZUSD":
                        break
                    else:
                        i += 1
                eth_week_mid_mkt = (last_week_prices[i][2] + last_week_prices[i][3]) / 2.0
                self.last_week_eth_price_text.SetLabel(("+" if eth_mid_mkt > eth_week_mid_mkt else "") + \
                    str(round(100.0 * (eth_mid_mkt / eth_week_mid_mkt) - 100.0, 1)) + "%")

                #xrp
                i = 0
                while i < len(last_week_prices):
                    if last_week_prices[i][1] == "XXRPZUSD":
                        break
                    else:
                        i += 1
                xrp_week_mid_mkt = (last_week_prices[i][2] + last_week_prices[i][3]) / 2.0
                self.last_week_xrp_price_text.SetLabel(("+" if xrp_mid_mkt > xrp_week_mid_mkt else "") + \
                    str(round(100.0 * (xrp_mid_mkt / xrp_week_mid_mkt) - 100.0, 1)) + "%")


    def on_redraw_timer(self, event):
        global list_id
        # if paused do not add data, but still redraw the plot
        # (to respond to scale modifications, grid change, etc.)
        #
        # if not self.paused:
        #     #self.data.append(self.datagen.next())
        #     self.data.append(self.rate_visualizer.next())
        interval_in_secs = self.get_interval_in_secs_chosen()
        headers = {'Content-Type': 'application/json'}
        api_url = "http://104.131.139.250:5000/?list_id=" + str(list_id) + "&interval_in_secs=" + str(interval_in_secs)
        print("api_url:", api_url)
        t1 = time.time()
        future = session.get(api_url, background_callback=self.bg_cb)
        response = future.result()
        # response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            graphvals = json.loads(response.content.decode('utf-8'))
        else:
            graphvals = None
        t2 = time.time()
        print("t2 - t1:", t2 - t1)

        self.data = []
        for val_and_timestamp in graphvals:
            self.data.append(val_and_timestamp[1])
        print("displaying ", len(self.data), " values")

        self.update_current_prices()

        self.draw_plot()

    def on_exit(self, event):
        self.Destroy()

    def flash_status_message(self, msg, flash_len_ms=1500):
        self.statusbar.SetStatusText(msg)
        self.timeroff = wx.Timer(self)
        self.Bind(
            wx.EVT_TIMER, 
            self.on_flash_status_off, 
            self.timeroff)
        self.timeroff.Start(flash_len_ms, oneShot=True)

    def on_flash_status_off(self, event):
        self.statusbar.SetStatusText('')


if __name__ == '__main__':
    app = wx.App()
    app.frame = GraphFrame()
    app.frame.Show()
    app.frame.SetSize((1000, 800))
    app.MainLoop()

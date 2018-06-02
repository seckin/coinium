import os
import pprint
import random
import sys
import wx
import krakenex
import decimal
import time
if 64 - 64: i11iIiiIii
import json
import requests
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import wx . html
import webbrowser
import wx . html2
import wx . richtext
if 73 - 73: II111iiii
import urllib
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
from requests_futures . sessions import FuturesSession
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = FuturesSession ( )
IiII = 1
iI1Ii11111iIi = open ( "/Users/seckin/coinium/output.txt" , 'w' , IiII )
if 41 - 41: I1II1
class Ooo0OO0oOO ( wx . Dialog ) :
 def __init__ ( self , * args , ** kwds ) :
  wx . Dialog . __init__ ( self , * args , ** kwds )
  oooO0oo0oOOOO = wx . BoxSizer ( wx . VERTICAL )
  self . browser = wx . html2 . WebView . New ( self )
  oooO0oo0oOOOO . Add ( self . browser , 1 , wx . EXPAND , 10 )
  self . SetSizer ( oooO0oo0oOOOO )
  self . SetSize ( ( 700 , 800 ) )
  if 53 - 53: o0oo0o / Oo + OOo00O0Oo0oO / iIii1I11I1II1 * iIii1I11I1II1 . I1ii11iIi11i
  if 28 - 28: i1IIi % II111iiii - Oo + I1II1
global ii1Ii , Ooo00O0 , oo0 , Oooo00OOo000
if 82 - 82: I11i . Oo / o0oo0o % II111iiii % iIii1I11I1II1 % o0oo0o
Ooo00O0 = [ ]
oo0 = [ ]
Oooo00OOo000 = [ ]
if 86 - 86: OoOoOO00 % I1IiiI
# start with this list id:
global oo
global ii1Ii
oo = 1
if 33 - 33: II111iiii * Oo0Ooo - o0oOOo0O0Ooo * iIii1I11I1II1 * OoooooooOO * OOo00O0Oo0oO
i1iIIII = krakenex . API ( )
if 26 - 26: Oo . I11i - OOooOOo % O0 + OOooOOo
if 34 - 34: I11i * I1IiiI
import matplotlib
matplotlib . use ( 'WXAgg' )
from matplotlib . figure import Figure
from matplotlib . backends . backend_wxagg import FigureCanvasWxAgg as FigCanvas , NavigationToolbar2WxAgg as NavigationToolbar
if 31 - 31: II111iiii + OoO0O00 . Oo
if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
import numpy as np
import pylab
if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
i1iIIi1 = True
ii11iIi1I = True
iI111I11I1I1 = True
OOooO0OOoo = True
if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
class IiIIIiI1I1 ( object ) :
 def __init__ ( self , init = - 1 ) :
  self . data = self . init = init
  if 86 - 86: i11iIiiIii + Ii1I + OOo00O0Oo0oO * I11i + o0oOOo0O0Ooo
 def next ( self ) :
  self . _recalc_data ( )
  return self . data
  if 61 - 61: OoO0O00 / i11iIiiIii
 def _recalc_data ( self ) :
  pass
  if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
class ooOoo0O ( wx . Panel ) :
 def __init__ ( self , parent , ID , label , initval ) :
  if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
  if 75 - 75: I1II1
  if 97 - 97: i11iIiiIii
  wx . Panel . __init__ ( self , parent , ID )
  if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . o0oo0o
  self . value = initval
  if 61 - 61: OOo00O0Oo0oO
  oOOO00o = wx . StaticBox ( self , - 1 , label )
  oooO0oo0oOOOO = wx . StaticBoxSizer ( oOOO00o , wx . VERTICAL )
  if 97 - 97: I11i % I11i + II111iiii * I1II1
  self . SetSizer ( oooO0oo0oOOOO )
  oooO0oo0oOOOO . Fit ( self )
  if 54 - 54: I11i + o0oo0o / I1II1
class IIII ( wx . Frame ) :
 title = 'Coinium Portfolio Manager'
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
 if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
 def __init__ ( self ) :
  wx . Frame . __init__ ( self , None , - 1 , self . title , pos = wx . Point ( 50 , 50 ) )
  if 20 - 20: o0oOOo0O0Ooo
  self . modify_boxes_visible = False
  self . add_boxes_visible = False
  if 77 - 77: OoOoOO00 / I11i
  self . rate_visualizer = IiIIIiI1I1 ( )
  self . data = [ self . rate_visualizer . next ( ) ]
  self . paused = False
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
  self . create_menu ( )
  self . create_status_bar ( )
  self . create_main_panel ( )
  if 28 - 28: OOooOOo - o0oo0o . o0oo0o + OoOoOO00 - OoooooooOO + O0
  self . redraw_timer = wx . Timer ( self )
  self . Bind ( wx . EVT_TIMER , self . on_redraw_timer , self . redraw_timer )
  self . redraw_timer . Start ( 1500 )
  if 95 - 95: OoO0O00 % oO0o . O0
 def create_menu ( self ) :
  self . menubar = wx . MenuBar ( )
  if 15 - 15: OOo00O0Oo0oO / Ii1I . Ii1I - i1IIi
  o00oOO0 = wx . Menu ( )
  oOoo = o00oOO0 . Append ( - 1 , "&Save plot\tCtrl-S" , "Save plot to file" )
  self . Bind ( wx . EVT_MENU , self . on_save_plot , oOoo )
  o00oOO0 . AppendSeparator ( )
  iIii11I = o00oOO0 . Append ( - 1 , "E&xit\tCtrl-X" , "Exit" )
  self . Bind ( wx . EVT_MENU , self . on_exit , iIii11I )
  if 69 - 69: oO0o % Oo - o0oOOo0O0Ooo + Oo - O0 % OoooooooOO
  self . menubar . Append ( o00oOO0 , "&File" )
  self . SetMenuBar ( self . menubar )
  if 31 - 31: II111iiii - OOooOOo . Oo % OoOoOO00 - O0
 def create_main_panel ( self ) :
  self . panel = wx . Panel ( self )
  self . panel . SetBackgroundColour ( ( 255 , 255 , 255 ) )
  if 4 - 4: II111iiii / OOo00O0Oo0oO . I1II1
  self . init_plot ( )
  self . canvas = FigCanvas ( self . panel , - 1 , self . fig )
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % Oo - I1ii11iIi11i / oO0o
  ii11i1 = 'your_api_token'
  IIIii1II1II = 'http://104.131.139.250/api.php/'
  i1I1iI = { 'Content-Type' : 'application/json' ,
 'Authorization' : 'Bearer {0}' . format ( ii11i1 ) }
  oo0OooOOo0 = '{0}Distributions' . format ( IIIii1II1II )
  o0O = requests . get ( oo0OooOOo0 , headers = i1I1iI )
  if o0O . status_code == 200 :
   O00oO = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   O00oO = None
  iI1Ii11111iIi . write ( "val" + str ( O00oO ) + "\n" )
  iI1Ii11111iIi . write ( "first distribution:" + str ( O00oO [ 'Distributions' ] [ 'records' ] [ 0 ] ) + "\n" )
  if 39 - 39: o0oo0o - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  OoOOOOO = O00oO [ 'Distributions' ] [ 'records' ] [ 0 ]
  iIi1i111II = [ OoOOOOO [ 1 ] / 100.0 , OoOOOOO [ 2 ] / 100.0 , OoOOOOO [ 3 ] / 100.0 ]
  OoOO00O = [ "XXBTZUSD" , "XETHZUSD" , "XXRPZUSD" ]
  oOOoO0O0O0 = ""
  for Oo000o in range ( len ( OoOO00O ) ) :
   oOOoO0O0O0 += str ( OoOO00O [ Oo000o ] ) + ": " + str ( iIi1i111II [ Oo000o ] * 100 ) + "%, "
  self . axes . set_title ( oOOoO0O0O0 , size = 12 )
  if 7 - 7: OOo00O0Oo0oO * OoO0O00 % oO0o . o0oo0o
  self . axes . text ( 0.64 , 0.03 , 'http://coinium.app' ,
 verticalalignment = 'bottom' , horizontalalignment = 'right' ,
 transform = self . axes . transAxes ,
 color = 'lightblue' , fontsize = 13 )
  if 45 - 45: i11iIiiIii * II111iiii % iIii1I11I1II1 + I1ii11iIi11i - Ii1I
  iIi1iIiii111 = [ ]
  for iIIIi1 in O00oO [ 'Distributions' ] [ 'records' ] :
   oo0OooOOo0 = "http://104.131.139.250/api.php/ListHasDistribution?filter=distribution_id,eq," + str ( iIIIi1 [ 0 ] )
   o0O = requests . get ( oo0OooOOo0 , headers = i1I1iI )
   if o0O . status_code == 200 :
    O00oO = json . loads ( o0O . content . decode ( 'utf-8' ) )
    iI1Ii11111iIi . write ( "val" + str ( O00oO ) + "\n" )
   else :
    O00oO = None
   if O00oO and len ( O00oO [ "ListHasDistribution" ] [ "records" ] ) :
    iiII1i1 = "list#" + str ( O00oO [ "ListHasDistribution" ] [ "records" ] [ 0 ] [ 1 ] ) + " BTC: " + str ( iIIIi1 [ 1 ] ) + "% "
    iiII1i1 += "ETH: " + str ( iIIIi1 [ 2 ] ) + "% "
    iiII1i1 += "XRP: " + str ( iIIIi1 [ 3 ] ) + "%"
    iIi1iIiii111 . append ( iiII1i1 )
    if 66 - 66: OOooOOo - I11i
    if 5 - 5: Oo + Ii1I / Oo0Ooo - oO0o
  OO0O0OoOO0 = wx . Image ( "/Users/seckin/coinium/coinium.png" , wx . BITMAP_TYPE_ANY ) . Rescale ( 50 , 50 ) . ConvertToBitmap ( )
  self . coinium_image = wx . StaticBitmap ( self . panel , - 1 , OO0O0OoOO0 , ( 10 , 5 ) , ( OO0O0OoOO0 . GetWidth ( ) , OO0O0OoOO0 . GetHeight ( ) ) )
  if 10 - 10: OoooooooOO % iIii1I11I1II1
  self . lst = wx . ListBox ( self . panel , size = ( 260 , 500 ) , choices = iIi1iIiii111 , style = wx . LB_SINGLE )
  self . Bind ( wx . EVT_LISTBOX , self . onListBox , self . lst )
  self . lst . Bind ( wx . EVT_KILL_FOCUS , self . onListBoxUnfocused )
  self . coinium_text = wx . StaticText ( self . panel , - 1 , label = "Coinium" , size = ( 150 , 50 ) )
  self . coinium_text . SetLabelMarkup ( "<span foreground='blue' size='30720' font_weight='ultrabold'>Coinium</span>" )
  self . portfolio_list_text = wx . StaticText ( self . panel , - 1 , label = "Portfolio List" , size = ( 85 , 15 ) )
  if 54 - 54: Oo - II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + OOo00O0Oo0oO
  self . hbox11 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox11 . Add ( self . coinium_image , border = 5 , flag = wx . ALL | wx . ALIGN_LEFT )
  self . hbox11 . Add ( self . coinium_text , border = 5 , flag = wx . ALL | wx . ALIGN_LEFT )
  self . vbox4 = wx . BoxSizer ( wx . VERTICAL )
  self . vbox4 . Add ( self . hbox11 , border = 5 , flag = wx . ALL | wx . ALIGN_LEFT )
  self . vbox4 . Add ( self . portfolio_list_text , border = 5 , flag = wx . ALL | wx . ALIGN_LEFT )
  self . vbox4 . AddSpacer ( 0 )
  self . vbox4 . Add ( self . lst , border = 5 , flag = wx . ALL | wx . ALIGN_LEFT )
  if 15 - 15: I11i * OOo00O0Oo0oO * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: Oo % i1IIi . o0oo0o . I1ii11iIi11i
  self . interval_choice_text = wx . StaticText ( self . panel , - 1 , label = "Interval:" , size = ( 55 , 20 ) )
  self . choice = wx . Choice ( self . panel , choices = [ "30 secs" , "5 mins" , "2 hours" , "1 day" ] )
  self . choice . Bind ( wx . EVT_CHOICE , self . OnChoice )
  self . hbox0 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox0 . Add ( self . interval_choice_text , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL | wx . ALIGN_RIGHT )
  self . hbox0 . AddSpacer ( 2 )
  self . hbox0 . Add ( self . choice , border = 5 , flag = wx . ALL | wx . ALIGN_TOP )
  if 92 - 92: I1II1 . Oo
  if 31 - 31: Oo . OoOoOO00 / O0
  if 89 - 89: OoOoOO00
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + OOo00O0Oo0oO
  if 4 - 4: OOo00O0Oo0oO + O0 * OOooOOo
  if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
  if 25 - 25: I1ii11iIi11i
  if 7 - 7: i1IIi / I1IiiI * Oo . o0oo0o . iIii1I11I1II1
  if 13 - 13: OOooOOo / i11iIiiIii
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  if 52 - 52: o0oOOo0O0Ooo
  if 95 - 95: Ii1I
  if 87 - 87: OOo00O0Oo0oO + OoOoOO00 . OOooOOo + OoOoOO00
  if 91 - 91: O0
  if 61 - 61: II111iiii
  if 64 - 64: OOo00O0Oo0oO / OoOoOO00 - O0 - I11i
  if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
  if 42 - 42: OoO0O00
  if 67 - 67: Oo . I1II1 . O0
  if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
  if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / I1II1
  if 37 - 37: I1II1 - OOo00O0Oo0oO * oO0o % i11iIiiIii - Oo
  if 83 - 83: I11i / I1IiiI
  if 34 - 34: o0oo0o
  self . hbox2 = wx . BoxSizer ( wx . HORIZONTAL )
  if 57 - 57: oO0o . I11i . i1IIi
  if 42 - 42: I11i + I1ii11iIi11i % O0
  if 6 - 6: oO0o
  if 68 - 68: OoOoOO00 - OoO0O00
  if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
  if 1 - 1: iIii1I11I1II1 / II111iiii
  if 33 - 33: I11i
  if 18 - 18: o0oOOo0O0Ooo % I1II1 * O0
  if 87 - 87: i11iIiiIii
  if 93 - 93: I1ii11iIi11i - OoO0O00 % i11iIiiIii . I1II1 / I1II1 - Oo
  if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
  if 91 - 91: I1II1 % i1IIi % iIii1I11I1II1
  if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
  if 45 - 45: oO0o - o0oo0o - OoooooooOO - OoO0O00 . II111iiii / O0
  if 51 - 51: O0 + I1II1
  if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
  if 48 - 48: O0
  if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  self . btc_text = wx . StaticText ( self . panel , - 1 , label = "BTC:" , size = ( 35 , 20 ) )
  self . btc_input_box = wx . TextCtrl ( self . panel , size = ( 35 , 20 ) )
  self . eth_text = wx . StaticText ( self . panel , - 1 , label = "ETH:" , size = ( 35 , 20 ) )
  self . eth_input_box = wx . TextCtrl ( self . panel , size = ( 35 , 20 ) )
  self . xrp_text = wx . StaticText ( self . panel , - 1 , label = "XRP:" , size = ( 35 , 20 ) )
  self . xrp_input_box = wx . TextCtrl ( self . panel , size = ( 35 , 20 ) )
  self . add_distribution_button = wx . Button ( self . panel , - 1 , "Add New Portfolio" )
  self . Bind ( wx . EVT_BUTTON , self . on_add_distribution_button , self . add_distribution_button )
  self . submit_new_distribution_button = wx . Button ( self . panel , - 1 , "Submit" )
  self . Bind ( wx . EVT_BUTTON , self . on_submit_new_distribution_button , self . submit_new_distribution_button )
  self . cancel_new_distribution_button = wx . Button ( self . panel , - 1 , "Cancel" )
  self . Bind ( wx . EVT_BUTTON , self . on_cancel_new_distribution_button , self . cancel_new_distribution_button )
  self . eth_input_box . Hide ( )
  self . btc_input_box . Hide ( )
  self . xrp_input_box . Hide ( )
  self . btc_text . Hide ( )
  self . eth_text . Hide ( )
  self . xrp_text . Hide ( )
  self . submit_new_distribution_button . Hide ( )
  self . cancel_new_distribution_button . Hide ( )
  if 41 - 41: Ii1I - O0 - O0
  self . hbox1 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox1 . Add ( self . btc_text , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 2 )
  self . hbox1 . Add ( self . btc_input_box , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . Add ( self . eth_text , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 2 )
  self . hbox1 . Add ( self . eth_input_box , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . Add ( self . xrp_text , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 2 )
  self . hbox1 . Add ( self . xrp_input_box , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 5 )
  self . hbox1 . Add ( self . add_distribution_button , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 5 )
  self . hbox1 . Add ( self . submit_new_distribution_button , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 5 )
  self . hbox1 . Add ( self . cancel_new_distribution_button , border = 5 , flag = wx . ALL | wx . ALIGN_CENTER_VERTICAL )
  self . hbox1 . AddSpacer ( 24 )
  if 68 - 68: OOooOOo % Oo
  if 88 - 88: iIii1I11I1II1 - OOo00O0Oo0oO + OOooOOo
  self . current_prices = wx . StaticText ( self . panel , - 1 , label = "Current prices" , size = ( 95 , 20 ) )
  self . btc_price_text_name = wx . StaticText ( self . panel , - 1 , label = "BTC:" , size = ( 35 , 20 ) )
  self . btc_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . eth_price_text_name = wx . StaticText ( self . panel , - 1 , label = "ETH:" , size = ( 35 , 20 ) )
  self . eth_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . xrp_price_text_name = wx . StaticText ( self . panel , - 1 , label = "XRP:" , size = ( 35 , 20 ) )
  self . xrp_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . hbox4 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox4 . AddSpacer ( 45 )
  self . hbox4 . Add ( self . current_prices , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox5 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox5 . Add ( self . btc_price_text_name , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox5 . AddSpacer ( 2 )
  self . hbox5 . Add ( self . btc_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox6 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox6 . Add ( self . eth_price_text_name , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox6 . AddSpacer ( 2 )
  self . hbox6 . Add ( self . eth_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox7 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox7 . Add ( self . xrp_price_text_name , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox7 . AddSpacer ( 2 )
  self . hbox7 . Add ( self . xrp_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  if 40 - 40: I1IiiI * Ii1I + OOooOOo % I1II1
  if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + Oo / OoOoOO00
  self . last_24_hours_prices = wx . StaticText ( self . panel , - 1 , label = "Last 24 hours" , size = ( 95 , 20 ) )
  self . last_24_hours_btc_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . last_24_hours_eth_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . last_24_hours_xrp_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . hbox4 . AddSpacer ( 20 )
  self . hbox4 . Add ( self . last_24_hours_prices , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox5 . AddSpacer ( 40 )
  self . hbox5 . Add ( self . last_24_hours_btc_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox6 . AddSpacer ( 40 )
  self . hbox6 . Add ( self . last_24_hours_eth_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox7 . AddSpacer ( 40 )
  self . hbox7 . Add ( self . last_24_hours_xrp_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  if 23 - 23: O0
  if 85 - 85: Ii1I
  self . last_week_prices = wx . StaticText ( self . panel , - 1 , label = "Last week" , size = ( 95 , 20 ) )
  self . last_week_btc_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . last_week_eth_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . last_week_xrp_price_text = wx . StaticText ( self . panel , - 1 , label = "..." , size = ( 75 , 20 ) )
  self . hbox4 . AddSpacer ( 20 )
  self . hbox4 . Add ( self . last_week_prices , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox5 . AddSpacer ( 40 )
  self . hbox5 . Add ( self . last_week_btc_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox6 . AddSpacer ( 40 )
  self . hbox6 . Add ( self . last_week_eth_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  self . hbox7 . AddSpacer ( 40 )
  self . hbox7 . Add ( self . last_week_xrp_price_text , border = 5 , flag = wx . ALL | wx . ALIGN_BOTTOM )
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + I1II1 / OoOoOO00
  if 84 - 84: OOo00O0Oo0oO * II111iiii + Oo0Ooo
  if 53 - 53: I1II1 % II111iiii . o0oo0o - iIii1I11I1II1 - o0oo0o * II111iiii
  if 77 - 77: iIii1I11I1II1 * OoO0O00
  if 95 - 95: I1IiiI + i11iIiiIii
  self . hbox3 = wx . BoxSizer ( wx . HORIZONTAL )
  if 6 - 6: OOo00O0Oo0oO / i11iIiiIii + I1II1 * oO0o
  if 80 - 80: II111iiii
  if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
  if 53 - 53: II111iiii
  if 31 - 31: OoO0O00
  if 80 - 80: Oo . i11iIiiIii - o0oOOo0O0Ooo
  if 25 - 25: OoO0O00
  self . vbox5 = wx . BoxSizer ( wx . VERTICAL )
  self . vbox5 . Add ( self . canvas , 1 , flag = wx . ALIGN_LEFT | wx . TOP | wx . GROW )
  self . vbox5 . Add ( self . hbox0 , 0 , flag = wx . ALIGN_RIGHT | wx . TOP )
  self . vbox5 . Add ( self . hbox4 , 0 , flag = wx . ALIGN_LEFT | wx . TOP )
  self . vbox5 . Add ( self . hbox5 , 0 , flag = wx . ALIGN_LEFT | wx . TOP )
  self . vbox5 . Add ( self . hbox6 , 0 , flag = wx . ALIGN_LEFT | wx . TOP )
  self . vbox5 . Add ( self . hbox7 , 0 , flag = wx . ALIGN_LEFT | wx . TOP )
  if 62 - 62: OOooOOo + O0
  self . hbox8 = wx . BoxSizer ( wx . HORIZONTAL )
  self . hbox8 . Add ( self . vbox4 , 0 , flag = wx . ALIGN_LEFT | wx . TOP | wx . GROW )
  self . hbox8 . Add ( self . vbox5 , 1 , flag = wx . ALIGN_RIGHT | wx . BOTTOM )
  if 98 - 98: o0oOOo0O0Ooo
  self . vbox9 = wx . BoxSizer ( wx . VERTICAL )
  self . vbox9 . Add ( self . hbox1 , 1 , flag = wx . ALIGN_LEFT | wx . TOP )
  self . vbox9 . Add ( self . hbox2 , 1 , flag = wx . ALIGN_LEFT | wx . BOTTOM )
  self . vbox9 . Add ( self . hbox3 , 1 , flag = wx . ALIGN_RIGHT | wx . BOTTOM )
  if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
  self . vbox6 = wx . BoxSizer ( wx . VERTICAL )
  self . vbox6 . Add ( self . hbox8 , 0 , flag = wx . ALIGN_LEFT | wx . TOP | wx . GROW )
  self . vbox6 . Add ( self . vbox9 , 0 , flag = wx . ALIGN_LEFT | wx . TOP | wx . GROW )
  if 78 - 78: i11iIiiIii / I1II1 - Ii1I / OOooOOo + oO0o
  if 82 - 82: Ii1I
  self . panel . SetSizer ( self . vbox6 )
  self . vbox6 . Fit ( self )
  self . vbox6 . Layout ( )
  if 46 - 46: OoooooooOO . i11iIiiIii
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if 87 - 87: Oo0Ooo . o0oo0o
  if 75 - 75: OOo00O0Oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . I1II1
  if 55 - 55: OOooOOo . I1IiiI
 def create_status_bar ( self ) :
  self . statusbar = self . CreateStatusBar ( )
  if 61 - 61: Oo0Ooo % o0oo0o . Oo0Ooo
 def init_plot ( self ) :
  global Ooo00O0 , oo0
  self . dpi = 100
  self . fig = Figure ( ( 3.0 , 3.0 ) , dpi = self . dpi )
  if 100 - 100: Oo * O0
  self . axes = self . fig . add_subplot ( 111 )
  self . axes . set_axis_bgcolor ( 'gray' )
  oOOoO0O0O0 = ""
  for Oo000o in range ( len ( Ooo00O0 ) ) :
   oOOoO0O0O0 += str ( Ooo00O0 [ Oo000o ] ) + ": " + str ( oo0 [ Oo000o ] * 100 ) + "%, "
  self . axes . set_title ( oOOoO0O0O0 , size = 12 )
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  pylab . setp ( self . axes . get_xticklabels ( ) , fontsize = 8 )
  pylab . setp ( self . axes . get_yticklabels ( ) , fontsize = 8 )
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + OOooOOo - Oo
  self . plot_data = self . axes . plot (
 self . data ,
 linewidth = 1 ,
 color = ( 1 , 1 , 0 ) ,
 ) [ 0 ]
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 def draw_plot ( self ) :
  if 57 - 57: OoO0O00 / OOo00O0Oo0oO
  if OOooO0OOoo or self . xmax_control . is_auto ( ) :
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
   if 7 - 7: o0oo0o * Oo % Ii1I - o0oOOo0O0Ooo
   i1i = len ( self . data )
  else :
   i1i = int ( self . xmax_control . manual_value ( ) )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  if iI111I11I1I1 or self . xmin_control . is_auto ( ) :
   O00o0OO0 = i1i - 75
  else :
   O00o0OO0 = int ( self . xmin_control . manual_value ( ) )
   if 35 - 35: oO0o % OOo00O0Oo0oO / Oo + iIii1I11I1II1 . OoooooooOO . I1IiiI
  if i1iIIi1 or self . ymin_control . is_auto ( ) :
   o00oOOooOOo0o = min ( self . data [ - 75 : - 1 ] ) * ( 1.0 - 0.004 )
  else :
   o00oOOooOOo0o = int ( self . ymin_control . manual_value ( ) )
   if 66 - 66: I1II1 - I1II1 - i11iIiiIii . I1ii11iIi11i - OOooOOo
  if ii11iIi1I or self . ymax_control . is_auto ( ) :
   oOOo0O00o = max ( self . data [ - 75 : - 1 ] ) * ( 1.0 + 0.004 )
  else :
   oOOo0O00o = int ( self . ymax_control . manual_value ( ) )
   if 8 - 8: OoO0O00
  self . axes . set_xbound ( lower = O00o0OO0 , upper = i1i )
  self . axes . set_ybound ( lower = o00oOOooOOo0o , upper = oOOo0O00o )
  if 49 - 49: I1IiiI - I11i
  if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
  if 62 - 62: OoooooooOO * I1IiiI
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  if 50 - 50: Oo . o0oOOo0O0Ooo
  if 97 - 97: O0 + OoOoOO00
  if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
  if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  if True :
   self . axes . grid ( True , color = 'white' )
  else :
   self . axes . grid ( False )
   if 77 - 77: OOooOOo * iIii1I11I1II1
   if 98 - 98: I1IiiI % Ii1I * OoooooooOO
   if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
   if 33 - 33: OOo00O0Oo0oO . II111iiii % I1II1 + o0oOOo0O0Ooo
   if 71 - 71: Oo0Ooo % OOooOOo
   if 98 - 98: I11i % i11iIiiIii % OOo00O0Oo0oO + Ii1I
   if 78 - 78: I1ii11iIi11i % oO0o / I1II1 - iIii1I11I1II1
   if 69 - 69: Oo
   if 11 - 11: I1IiiI
   if 16 - 16: Ii1I + o0oo0o * O0 % i1IIi . I1IiiI
  Oo0OO = self . axes . get_xticklabels ( )
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / OOo00O0Oo0oO / II111iiii
  Oo000o = 0
  iiI11ii1I1 = Oo0OO [ 0 ] . get_text ( )
  Ooo0OOoOoO0 = self . get_interval_in_secs_chosen ( )
  for oOo0OOoO0 in Oo0OO :
   if 11 - 11: I1ii11iIi11i . OoO0O00 * o0oo0o * OoooooooOO + OOo00O0Oo0oO
   O00oO = ( Oo000o - len ( Oo0OO ) + 1 ) * 10 * Ooo0OOoOoO0
   IiII111i1i11 = abs ( O00oO )
   iiII1i1 = ""
   if int ( IiII111i1i11 / 3600 ) > 0 :
    iiII1i1 += str ( int ( IiII111i1i11 / 3600 ) ) + "h "
    IiII111i1i11 = IiII111i1i11 % 3600
   if int ( IiII111i1i11 / 60 ) > 0 :
    iiII1i1 += str ( int ( IiII111i1i11 / 60 ) ) + "m "
    IiII111i1i11 = IiII111i1i11 % 60
   if IiII111i1i11 > 0 :
    iiII1i1 += str ( int ( IiII111i1i11 ) ) + "s "
    if 40 - 40: OOo00O0Oo0oO * o0oo0o * i11iIiiIii
   if iiII1i1 == "" :
    oo0OO00OoooOo = ""
   else :
    if Oo000o == len ( Oo0OO ) - 2 :
     oo0OO00OoooOo = "<" + str ( iiII1i1 ) + "ago"
    else :
     oo0OO00OoooOo = str ( iiII1i1 ) + "ago"
   oOo0OOoO0 . set_text ( oo0OO00OoooOo )
   if 19 - 19: I1ii11iIi11i % OoooooooOO % o0oo0o * o0oOOo0O0Ooo % O0
   Oo000o += 1
  self . axes . set_xticklabels ( Oo0OO )
  pylab . setp ( Oo0OO ,
 visible = True )
  if 67 - 67: I1IiiI . i1IIi
  self . plot_data . set_xdata ( np . arange ( len ( self . data ) ) )
  self . plot_data . set_ydata ( np . array ( self . data ) )
  if 27 - 27: OOo00O0Oo0oO % I1IiiI
  self . canvas . draw ( )
  if 73 - 73: OOooOOo
 def onListBoxUnfocused ( self , event ) :
  iI1Ii11111iIi . write ( "onListBoxUnfocused" + "\n" )
  if 70 - 70: iIii1I11I1II1
  if 31 - 31: o0oo0o - I1IiiI % iIii1I11I1II1
  if 92 - 92: i1IIi - iIii1I11I1II1
  if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
  if 88 - 88: OoO0O00
  if 71 - 71: I1ii11iIi11i
  if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
  if 59 - 59: o0oOOo0O0Ooo
  if 81 - 81: OoOoOO00 - OoOoOO00 . I1II1
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  if 7 - 7: O0 * i11iIiiIii * Ii1I + OOo00O0Oo0oO % OoO0O00 - OOo00O0Oo0oO
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: o0oo0o % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / o0oo0o
  if 6 - 6: I1II1 / I1IiiI % OOooOOo - I1IiiI
  if 31 - 31: OOooOOo
 def OnChoice ( self , event ) :
  iI1Ii11111iIi . write ( "self.choice.GetSelection()" + str ( self . choice . GetSelection ( ) ) + "\n" )
  iI1Ii11111iIi . write ( "choice updated to" + str ( self . choice . GetString ( self . choice . GetSelection ( ) ) ) + "\n" )
  if 23 - 23: Oo . o0oo0o
 def update_pair_distributions ( self , list_id ) :
  global ii1Ii , Ooo00O0 , oo0 , Oooo00OOo000
  iI1Ii11111iIi . write ( "update_pair_distributions called" + "\n" )
  i1I1iI = { 'Content-Type' : 'application/json' }
  o0O = requests . get ( "http://104.131.139.250/api.php/ListHasDistribution?filter=list_id,eq," + str ( list_id ) , headers = i1I1iI )
  if o0O . status_code == 200 :
   OO0000o = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   OO0000o = None
   if 42 - 42: Oo0Ooo
   if 76 - 76: I1IiiI * I1II1 % Oo
  OoooO00o = OO0000o [ "ListHasDistribution" ] [ "records" ] [ 0 ] [ 2 ]
  if 73 - 73: OOooOOo / oO0o
  i1I1iI = { 'Content-Type' : 'application/json' }
  o0O = requests . get ( "http://104.131.139.250/api.php/Distributions?filter=id,eq," + str ( OoooO00o ) , headers = i1I1iI )
  if o0O . status_code == 200 :
   iIi1iIiii111 = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   iIi1iIiii111 = None
   if 88 - 88: I11i % I1ii11iIi11i
  I1i11 = iIi1iIiii111 [ "Distributions" ] [ "records" ] [ 0 ]
  oo0 = [ I1i11 [ 1 ] / 100.0 , I1i11 [ 2 ] / 100.0 , I1i11 [ 3 ] / 100.0 ]
  Ooo00O0 = [ 'XXBTZUSD' , 'XETHZUSD' , 'XXRPZUSD' ]
  Oooo00OOo000 = [ - 1 , - 1 , - 1 ]
  iI1Ii11111iIi . write ( "pairs" + str ( Ooo00O0 ) + "\n" )
  iI1Ii11111iIi . write ( "pair_pcts" + str ( oo0 ) + "\n" )
  iI1Ii11111iIi . write ( "" + "\n" )
  if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
 def onListBox ( self , event ) :
  global oo
  global ii1Ii , Ooo00O0 , oo0 , Oooo00OOo000
  iI1Ii11111iIi . write ( "Current selection:  \
            " + event . GetEventObject ( ) . GetStringSelection ( ) + "\n" )
  if 52 - 52: OOo00O0Oo0oO . I1II1 + Oo
  if 38 - 38: i1IIi - II111iiii . Oo
  if 58 - 58: I1IiiI . I1II1 + OoOoOO00
  if 66 - 66: I1II1 / oO0o * OoooooooOO + OoooooooOO % I11i
  if 49 - 49: oO0o - i11iIiiIii . Oo * Ii1I % I1II1 + i1IIi
  if 71 - 71: o0oOOo0O0Ooo
  if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  iiII1i1 = event . GetEventObject ( ) . GetStringSelection ( )
  oo0000ooooO0o = iiII1i1 . split ( ":" )
  oo = int ( oo0000ooooO0o [ 0 ] . split ( "#" ) [ 1 ] . split ( " " ) [ 0 ] )
  iI1Ii11111iIi . write ( "list_id updated to:" + str ( oo ) + "\n" )
  self . update_pair_distributions ( oo )
  oOOoO0O0O0 = ""
  for Oo000o in range ( len ( Ooo00O0 ) ) :
   oOOoO0O0O0 += str ( Ooo00O0 [ Oo000o ] ) + ": " + str ( oo0 [ Oo000o ] * 100 ) + "%, "
  self . axes . set_title ( oOOoO0O0O0 , size = 12 )
  iI1i11 = int ( oo0000ooooO0o [ 1 ] . split ( "%" ) [ 0 ] )
  OoOOoooOO0O = int ( oo0000ooooO0o [ 2 ] . split ( "%" ) [ 0 ] )
  ooo00Ooo = int ( oo0000ooooO0o [ 3 ] . split ( "%" ) [ 0 ] )
  if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  if 25 - 25: o0oo0o + Ii1I / OOo00O0Oo0oO . o0oOOo0O0Ooo % O0 * OoO0O00
  if 84 - 84: OOo00O0Oo0oO % Ii1I + i11iIiiIii
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 def on_add_distribution_button ( self , event ) :
  self . eth_input_box . Show ( )
  self . btc_input_box . Show ( )
  self . xrp_input_box . Show ( )
  self . btc_text . Show ( )
  self . eth_text . Show ( )
  self . xrp_text . Show ( )
  self . add_distribution_button . Hide ( )
  self . submit_new_distribution_button . Show ( )
  self . cancel_new_distribution_button . Show ( )
  self . add_boxes_visible = True
  self . vbox6 . Layout ( )
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
 def hide_all_add_boxes_except_add_new_pv_button ( self ) :
  self . eth_input_box . Hide ( )
  self . btc_input_box . Hide ( )
  self . xrp_input_box . Hide ( )
  self . btc_text . Hide ( )
  self . eth_text . Hide ( )
  self . xrp_text . Hide ( )
  self . add_distribution_button . Show ( )
  self . submit_new_distribution_button . Hide ( )
  self . cancel_new_distribution_button . Hide ( )
  self . add_boxes_visible = False
  self . vbox6 . Layout ( )
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
 def on_cancel_new_distribution_button ( self , event ) :
  self . hide_all_add_boxes_except_add_new_pv_button ( )
  if 60 - 60: II111iiii + Oo0Ooo
 def on_submit_new_distribution_button ( self , event ) :
  I1IiIiiIiIII = int ( self . eth_input_box . GetValue ( ) )
  iIIi = int ( self . btc_input_box . GetValue ( ) )
  iiI1iI111ii1i = int ( self . xrp_input_box . GetValue ( ) )
  if abs ( I1IiIiiIiIII ) + abs ( iIIi ) + abs ( iiI1iI111ii1i ) != 100 :
   iI1Ii11111iIi . write ( str ( I1IiIiiIiIII ) + " " + str ( iIIi ) + " " + str ( iiI1iI111ii1i ) + " absolute values don't add up to 100" + "\n" )
   return
   if 32 - 32: II111iiii * OoOoOO00 % i1IIi - I1II1 + iIii1I11I1II1 + I1ii11iIi11i
  self . hide_all_add_boxes_except_add_new_pv_button ( )
  if 60 - 60: I1ii11iIi11i % OoOoOO00 * OoO0O00 % II111iiii
  ii11i1 = 'your_api_token'
  IIIii1II1II = 'http://104.131.139.250/api.php/'
  i1I1iI = { 'Content-Type' : 'application/json' ,
 'Authorization' : 'Bearer {0}' . format ( ii11i1 ) }
  oo0OooOOo0 = '{0}Distributions' . format ( IIIii1II1II )
  o0O = requests . post ( oo0OooOOo0 , headers = i1I1iI , data = { "btc" : iIIi , "xrp" : iiI1iI111ii1i , "eth" : I1IiIiiIiIII } )
  if o0O . status_code == 200 :
   O00oO = json . loads ( o0O . content . decode ( 'utf-8' ) )
   iI1Ii11111iIi . write ( "distribution creation server response:" , str ( O00oO ) + "\n" )
   oo0OooOOo0 = '{0}Lists' . format ( IIIii1II1II )
   o0O = requests . post ( oo0OooOOo0 , headers = i1I1iI , data = { "name" : "list with dist#" + str ( O00oO ) } )
   if o0O . status_code == 200 :
    OOOOoO00o0O = json . loads ( o0O . content . decode ( 'utf-8' ) )
    iI1Ii11111iIi . write ( "list creation server response:" + str ( OOOOoO00o0O ) + "\n" )
    iiII1i1 = "list#" + str ( OOOOoO00o0O ) + " BTC: " + str ( iIIi ) + "% "
    iiII1i1 += "ETH: " + str ( I1IiIiiIiIII ) + "% "
    iiII1i1 += "XRP: " + str ( iiI1iI111ii1i ) + "%"
    iI1Ii11111iIi . write ( "adding new list to listbox:" + str ( iiII1i1 ) + "\n" )
    self . lst . Append ( iiII1i1 )
    oo0OooOOo0 = '{0}ListHasDistribution' . format ( IIIii1II1II )
    o0O = requests . post ( oo0OooOOo0 , headers = i1I1iI , data = { "list_id" : OOOOoO00o0O , "distribution_id" : O00oO , "timestamp" : int ( time . time ( ) ) } )
    if o0O . status_code == 200 :
     I1I1I1IIi1III = json . loads ( o0O . content . decode ( 'utf-8' ) )
     iI1Ii11111iIi . write ( "ListHasDistribution creation server response:" + str ( I1I1I1IIi1III ) + "\n" )
  else :
   O00oO = None
   if 5 - 5: Oo0Ooo % OOo00O0Oo0oO % i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - I1ii11iIi11i
 def on_modify_distribution_button ( self , event ) :
  if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
  if 46 - 46: OoOoOO00 + OoO0O00
  if 70 - 70: I1II1 / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
  if 96 - 96: OoooooooOO + oO0o
  if 44 - 44: oO0o
  if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
  if 88 - 88: OoOoOO00 / II111iiii
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - I1II1 + oO0o
  pass
  if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
 def hide_all_modification_boxes_except_edit_button ( self ) :
  if 42 - 42: Oo0Ooo
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  if 46 - 46: Oo0Ooo
  if 1 - 1: I1II1
  if 97 - 97: OOooOOo + I1II1 + O0 + i11iIiiIii
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . I1II1 % I1II1 + i11iIiiIii
  if 72 - 72: iIii1I11I1II1 * Ii1I % OOo00O0Oo0oO / OoO0O00
  if 35 - 35: OOo00O0Oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
  if 17 - 17: i1IIi
  if 21 - 21: Oo0Ooo
  pass
  if 29 - 29: I11i / II111iiii / OOo00O0Oo0oO * OOooOOo
 def on_cancel_distribution_modification_button ( self , event ) :
  self . hide_all_modification_boxes_except_edit_button ( )
  if 10 - 10: Oo % o0oo0o * o0oo0o . I11i / Ii1I % OOooOOo
 def on_submit_distribution_modification_button ( self , event ) :
  IIII1 = self . lst . GetCount ( )
  I1IiIiiIiIII = int ( self . modify_eth_input_box . GetValue ( ) )
  iIIi = int ( self . modify_btc_input_box . GetValue ( ) )
  iiI1iI111ii1i = int ( self . modify_xrp_input_box . GetValue ( ) )
  if abs ( I1IiIiiIiIII ) + abs ( iIIi ) + abs ( iiI1iI111ii1i ) != 100 :
   iI1Ii11111iIi . write ( str ( I1IiIiiIiIII ) + " " + str ( iIIi ) + " " + str ( iiI1iI111ii1i ) + " absolute values don't add up to 100" + "\n" )
   return
   if 10 - 10: Oo / OOo00O0Oo0oO + i11iIiiIii / Ii1I
  self . hide_all_modification_boxes_except_edit_button ( )
  if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
  for Oo000o in range ( IIII1 ) :
   if self . lst . IsSelected ( Oo000o ) :
    iiII1i1 = self . lst . GetStringSelection ( )
  oo0000ooooO0o = iiII1i1 . split ( ":" )
  oo = int ( oo0000ooooO0o [ 0 ] . split ( "#" ) [ 1 ] . split ( " " ) [ 0 ] )
  iI1Ii11111iIi . write ( "list_id:" + str ( oo ) + "\n" )
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if 5 - 5: Ii1I
  if 46 - 46: o0oo0o
  i1I1iI = { 'Content-Type' : 'application/json' }
  o0O = requests . get ( "http://104.131.139.250/api.php/ListHasDistribution?filter=list_id,eq," + str ( oo ) , headers = i1I1iI )
  if o0O . status_code == 200 :
   OO0000o = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   OO0000o = None
   if 45 - 45: OOo00O0Oo0oO
  if not OO0000o :
   iI1Ii11111iIi . write ( "not list_has_distributions" + "\n" )
   return
   if 21 - 21: oO0o . Oo . OOooOOo / Oo0Ooo / Oo
  OoooO00o = OO0000o [ "ListHasDistribution" ] [ "records" ] [ 0 ] [ 2 ]
  iI1Ii11111iIi . write ( "distribution_id" + str ( OoooO00o ) + "\n" )
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  ii11i1 = 'your_api_token'
  IIIii1II1II = 'http://104.131.139.250/api.php/'
  i1I1iI = { 'Content-Type' : 'application/json' ,
 'Authorization' : 'Bearer {0}' . format ( ii11i1 ) }
  oo0OooOOo0 = '{0}Distributions/{1}' . format ( IIIii1II1II , OoooO00o )
  o0O = requests . put ( oo0OooOOo0 , headers = i1I1iI , data = { "btc" : iIIi , "xrp" : iiI1iI111ii1i , "eth" : I1IiIiiIiIII } )
  if o0O . status_code == 200 :
   OooO0oo = json . loads ( o0O . content . decode ( 'utf-8' ) )
   iI1Ii11111iIi . write ( "num_distributions_affected" + str ( OooO0oo ) + "\n" )
  else :
   iI1Ii11111iIi . write ( "couldn't update distribution" + "\n" )
   if 89 - 89: Ii1I
   if 76 - 76: OOo00O0Oo0oO
   if 15 - 15: OOooOOo . I11i + OoooooooOO - OoO0O00
   if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % OOo00O0Oo0oO + iIii1I11I1II1 / O0 / I1ii11iIi11i
   if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   if 75 - 75: o0oo0o . OOo00O0Oo0oO
   if 50 - 50: OoOoOO00
   if 60 - 60: OOo00O0Oo0oO * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
   if 69 - 69: Ii1I * O0 . i11iIiiIii / Ii1I . o0oOOo0O0Ooo
   if 63 - 63: I11i + o0oOOo0O0Ooo . II111iiii - I1IiiI
   if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
   if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
  for Oo000o in range ( IIII1 ) :
   if self . lst . IsSelected ( Oo000o ) :
    iiII1i1 = "list#" + str ( oo ) + " BTC: " + str ( iIIi ) + "% "
    iiII1i1 += "ETH: " + str ( I1IiIiiIiIII ) + "% "
    iiII1i1 += "XRP: " + str ( iiI1iI111ii1i ) + "%"
    iI1Ii11111iIi . write ( "updating distribution to:" + str ( iiII1i1 ) + "\n" )
    self . lst . SetString ( Oo000o , iiII1i1 )
    if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
 def on_add_usd_button ( self , event ) :
  ii11i1 = 'your_api_token'
  IIIii1II1II = 'http://104.131.139.250/api.php/'
  i1I1iI = { 'Content-Type' : 'application/json' ,
 'Authorization' : 'Bearer {0}' . format ( ii11i1 ) }
  oo0OooOOo0 = '{0}Subscription' . format ( IIIii1II1II )
  o0O = requests . post ( oo0OooOOo0 , headers = i1I1iI , data = { "list_id" : oo , "user_id" : 1 , "dollar_amount" : float ( self . add_usd_input_box . GetValue ( ) ) , "timestamp" : int ( time . time ( ) ) , "approved" : 0 } )
  if o0O . status_code == 200 :
   I11i1 = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   I11i1 = None
   if 28 - 28: I11i
  oOOOOoo = Ooo0OO0oOO ( None , - 1 )
  OOo0 = urllib . parse . quote ( "Fund for Coinium Account. Invoice #" + str ( I11i1 ) )
  ii11I1 = str ( float ( self . add_usd_input_box . GetValue ( ) ) )
  oO0oo = urllib . parse . quote ( "Coinium Invoice #" + str ( I11i1 ) )
  Ii111iIi1iIi = "https://www.coinpayments.net/index.php?cmd=_pay&reset=1&merchant=e3e3958eff15be8c85dcbe83c3803da4&item_name=" + OOo0 + "&invoice=" + oO0oo + "&currency=USD&amountf=" + ii11I1 + "&quantity=1&allow_quantity=0&want_shipping=0&allow_extra=0&"
  iI1Ii11111iIi . write ( "link" + str ( Ii111iIi1iIi ) + "\n" )
  oOOOOoo . browser . LoadURL ( Ii111iIi1iIi )
  oOOOOoo . Show ( )
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 def on_save_plot ( self , event ) :
  OoOo = "PNG (*.png)|*.png"
  if 35 - 35: OOo00O0Oo0oO * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
  O00 = wx . FileDialog (
 self ,
 message = "Save plot as..." ,
 defaultDir = os . getcwd ( ) ,
 defaultFile = "coinium plot.png" ,
 wildcard = OoOo ,
 style = wx . FD_SAVE )
  if 52 - 52: OOo00O0Oo0oO + O0 . I1II1 . I1ii11iIi11i . OoO0O00
  if O00 . ShowModal ( ) == wx . ID_OK :
   oo000 = O00 . GetPath ( )
   self . canvas . print_figure ( oo000 , dpi = self . dpi )
   self . flash_status_message ( "Saved to %s" % oo000 )
   if 32 - 32: i1IIi . Ii1I
 def bg_cb ( self , sess , resp ) :
  resp . data = resp . json ( )
  if 59 - 59: OoooooooOO
 def get_interval_in_secs_chosen ( self ) :
  i1iiiii1 = self . choice . GetSelection ( )
  O0iII1 = self . choice . GetString ( i1iiiii1 )
  if O0iII1 == "30 secs" :
   Ooo0OOoOoO0 = 30
  elif O0iII1 == "5 mins" :
   Ooo0OOoOoO0 = 300
  elif O0iII1 == "2 hours" :
   Ooo0OOoOoO0 = 7200
  elif O0iII1 == "1 day" :
   Ooo0OOoOoO0 = 86400
  return Ooo0OOoOoO0
  if 27 - 27: OoO0O00 . I11i + OoOoOO00 / iIii1I11I1II1 % I1II1 . OOo00O0Oo0oO
 def update_current_prices ( self ) :
  i1I1iI = { 'Content-Type' : 'application/json' }
  IIIIi1 = int ( time . time ( ) )
  IIIIi1 -= 7500
  oo0OooOOo0 = "http://104.131.139.250/api.php/Spreads?filter=timestamp,gt," + str ( IIIIi1 )
  iI1Ii11111iIi . write ( "update_current_prices api_url:" + str ( oo0OooOOo0 ) + "\n" )
  iIi11iiIiI1I = IiiIII111iI . get ( oo0OooOOo0 , background_callback = self . bg_cb )
  o0O = iIi11iiIiI1I . result ( )
  if 3 - 3: i1IIi / II111iiii / i11iIiiIii * i1IIi - II111iiii
  if o0O . status_code == 200 :
   Ii = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   Ii = None
   if 14 - 14: o0oOOo0O0Ooo * oO0o
  if Ii :
   O0OOO0OOooo00 = Ii [ "Spreads" ] [ "records" ]
   if 6 - 6: Ii1I - OOo00O0Oo0oO * OOooOOo . I1II1 / O0 * OOo00O0Oo0oO
   if 22 - 22: Oo0Ooo % I1II1 * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
   Oo000o = len ( O0OOO0OOooo00 ) - 1
   while Oo000o > 0 :
    if O0OOO0OOooo00 [ Oo000o ] [ 1 ] == "XXBTZUSD" :
     break
    else :
     Oo000o -= 1
   Oo00OoOo = ( O0OOO0OOooo00 [ Oo000o ] [ 2 ] + O0OOO0OOooo00 [ Oo000o ] [ 3 ] ) / 2.0
   self . btc_price_text . SetLabel ( "$" + str ( round ( Oo00OoOo , 4 ) ) )
   if 24 - 24: i11iIiiIii - Oo
   if 21 - 21: I11i
   Oo000o = len ( O0OOO0OOooo00 ) - 1
   while Oo000o > 0 :
    if O0OOO0OOooo00 [ Oo000o ] [ 1 ] == "XETHZUSD" :
     break
    else :
     Oo000o -= 1
   OoO00 = ( O0OOO0OOooo00 [ Oo000o ] [ 2 ] + O0OOO0OOooo00 [ Oo000o ] [ 3 ] ) / 2.0
   self . eth_price_text . SetLabel ( "$" + str ( round ( OoO00 , 4 ) ) )
   if 85 - 85: Oo0Ooo * Oo0Ooo * I1IiiI . OoooooooOO . Ii1I * OOo00O0Oo0oO
   if 65 - 65: OOooOOo * Oo
   Oo000o = len ( O0OOO0OOooo00 ) - 1
   while Oo000o > 0 :
    if O0OOO0OOooo00 [ Oo000o ] [ 1 ] == "XXRPZUSD" :
     break
    else :
     Oo000o -= 1
   ooo0o000O = ( O0OOO0OOooo00 [ Oo000o ] [ 2 ] + O0OOO0OOooo00 [ Oo000o ] [ 3 ] ) / 2.0
   self . xrp_price_text . SetLabel ( "$" + str ( round ( ooo0o000O , 4 ) ) )
   if 100 - 100: oO0o . OOo00O0Oo0oO * I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OOo00O0Oo0oO
   if 17 - 17: I11i . o0oo0o - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   i1I1iI = { 'Content-Type' : 'application/json' }
   IIIIi1 = int ( time . time ( ) )
   IIIIi1 -= ( 24 * 60 * 60 )
   oo0OooOOo0 = "http://104.131.139.250/api.php/Spreads?filter=timestamp,bt," + str ( IIIIi1 ) + "," + str ( IIIIi1 + 7500 )
   if 39 - 39: o0oo0o * Oo0Ooo + iIii1I11I1II1 - o0oo0o + OOooOOo
   iIi11iiIiI1I = IiiIII111iI . get ( oo0OooOOo0 , background_callback = self . bg_cb )
   o0O = iIi11iiIiI1I . result ( )
   if 69 - 69: O0
   if o0O . status_code == 200 :
    Ii = json . loads ( o0O . content . decode ( 'utf-8' ) )
   else :
    Ii = None
   if Ii :
    o0ooO = Ii [ "Spreads" ] [ "records" ]
    if 74 - 74: O0 * oO0o - i11iIiiIii + Oo
    if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
    Oo000o = 0
    while Oo000o < len ( o0ooO ) :
     if o0ooO [ Oo000o ] [ 1 ] == "XXBTZUSD" :
      break
     else :
      Oo000o += 1
    OOO = ( o0ooO [ Oo000o ] [ 2 ] + o0ooO [ Oo000o ] [ 3 ] ) / 2.0
    self . last_24_hours_btc_price_text . SetLabel ( ( "+" if Oo00OoOo > OOO else "" ) + str ( round ( 100.0 * ( Oo00OoOo / OOO ) - 100.0 , 1 ) ) + "%" )
    if 30 - 30: OoooooooOO - OoooooooOO . O0 / I1II1
    if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
    if 89 - 89: II111iiii + i1IIi + II111iiii
    Oo000o = 0
    while Oo000o < len ( o0ooO ) :
     if o0ooO [ Oo000o ] [ 1 ] == "XETHZUSD" :
      break
     else :
      Oo000o += 1
    IiII1II11I = ( o0ooO [ Oo000o ] [ 2 ] + o0ooO [ Oo000o ] [ 3 ] ) / 2.0
    self . last_24_hours_eth_price_text . SetLabel ( ( "+" if OoO00 > IiII1II11I else "" ) + str ( round ( 100.0 * ( OoO00 / IiII1II11I ) - 100.0 , 1 ) ) + "%" )
    if 54 - 54: o0oo0o + O0 + I11i * Oo - OOooOOo % oO0o
    if 13 - 13: OOo00O0Oo0oO / I1II1 * OoO0O00 . OoO0O00 * OOo00O0Oo0oO
    if 63 - 63: Oo / O0 * Oo0Ooo + II111iiii / o0oo0o + Ii1I
    Oo000o = 0
    while Oo000o < len ( o0ooO ) :
     if o0ooO [ Oo000o ] [ 1 ] == "XXRPZUSD" :
      break
     else :
      Oo000o += 1
    OOoO000 = ( o0ooO [ Oo000o ] [ 2 ] + o0ooO [ Oo000o ] [ 3 ] ) / 2.0
    self . last_24_hours_xrp_price_text . SetLabel ( ( "+" if ooo0o000O > OOoO000 else "" ) + str ( round ( 100.0 * ( ooo0o000O / OOoO000 ) - 100.0 , 1 ) ) + "%" )
    if 57 - 57: II111iiii
    if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
    if 28 - 28: oO0o
   i1I1iI = { 'Content-Type' : 'application/json' }
   IIIIi1 = int ( time . time ( ) )
   IIIIi1 -= ( 7 * 24 * 60 * 60 )
   oo0OooOOo0 = "http://104.131.139.250/api.php/Spreads?filter=timestamp,bt," + str ( IIIIi1 ) + "," + str ( IIIIi1 + 250 )
   if 70 - 70: o0oo0o
   iIi11iiIiI1I = IiiIII111iI . get ( oo0OooOOo0 , background_callback = self . bg_cb )
   o0O = iIi11iiIiI1I . result ( )
   if 34 - 34: Oo % o0oo0o
   if o0O . status_code == 200 :
    Ii = json . loads ( o0O . content . decode ( 'utf-8' ) )
   else :
    Ii = None
   if Ii :
    IiI1i = Ii [ "Spreads" ] [ "records" ]
    if 87 - 87: OOo00O0Oo0oO
    Oo000o = 0
    while Oo000o < len ( IiI1i ) :
     if IiI1i [ Oo000o ] [ 1 ] == "XXBTZUSD" :
      break
     else :
      Oo000o += 1
    IIIii = ( IiI1i [ Oo000o ] [ 2 ] + IiI1i [ Oo000o ] [ 3 ] ) / 2.0
    self . last_week_btc_price_text . SetLabel ( ( "+" if Oo00OoOo > IIIii else "" ) + str ( round ( 100.0 * ( Oo00OoOo / IIIii ) - 100.0 , 1 ) ) + "%" )
    if 83 - 83: o0oo0o % o0oOOo0O0Ooo % I1IiiI . iIii1I11I1II1 - o0oo0o
    if 88 - 88: OoooooooOO
    if 84 - 84: OoOoOO00 / I11i * I1II1 / oO0o - i11iIiiIii . Oo0Ooo
    Oo000o = 0
    while Oo000o < len ( IiI1i ) :
     if IiI1i [ Oo000o ] [ 1 ] == "XETHZUSD" :
      break
     else :
      Oo000o += 1
    oOOo000oOoO0 = ( IiI1i [ Oo000o ] [ 2 ] + IiI1i [ Oo000o ] [ 3 ] ) / 2.0
    self . last_week_eth_price_text . SetLabel ( ( "+" if OoO00 > oOOo000oOoO0 else "" ) + str ( round ( 100.0 * ( OoO00 / oOOo000oOoO0 ) - 100.0 , 1 ) ) + "%" )
    if 86 - 86: II111iiii % i11iIiiIii + Ii1I % i11iIiiIii
    if 92 - 92: i11iIiiIii - I1II1 / OOo00O0Oo0oO / oO0o
    if 43 - 43: II111iiii + OOooOOo + I1II1
    Oo000o = 0
    while Oo000o < len ( IiI1i ) :
     if IiI1i [ Oo000o ] [ 1 ] == "XXRPZUSD" :
      break
     else :
      Oo000o += 1
    iI1IIIii = ( IiI1i [ Oo000o ] [ 2 ] + IiI1i [ Oo000o ] [ 3 ] ) / 2.0
    self . last_week_xrp_price_text . SetLabel ( ( "+" if ooo0o000O > iI1IIIii else "" ) + str ( round ( 100.0 * ( ooo0o000O / iI1IIIii ) - 100.0 , 1 ) ) + "%" )
    if 7 - 7: o0oo0o - I11i / II111iiii * Ii1I . I1II1 * I1II1
    if 61 - 61: I11i % OOo00O0Oo0oO - OoO0O00 / Oo0Ooo
    if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
 def on_redraw_timer ( self , event ) :
  global oo
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . I1II1 / OoooooooOO % I1IiiI % O0
  if 36 - 36: Ii1I / II111iiii / o0oo0o / o0oo0o + I1ii11iIi11i
  if 95 - 95: o0oo0o
  if 51 - 51: II111iiii + o0oo0o . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
  if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
  if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  Ooo0OOoOoO0 = self . get_interval_in_secs_chosen ( )
  i1I1iI = { 'Content-Type' : 'application/json' }
  oo0OooOOo0 = "http://104.131.139.250:5000/?list_id=" + str ( oo ) + "&interval_in_secs=" + str ( Ooo0OOoOoO0 )
  iI1Ii11111iIi . write ( "api_url:" + oo0OooOOo0 + "\n" )
  ii1Ii1IiIIi = time . time ( )
  iIi11iiIiI1I = IiiIII111iI . get ( oo0OooOOo0 , background_callback = self . bg_cb )
  o0O = iIi11iiIiI1I . result ( )
  if 83 - 83: I11i / I1ii11iIi11i
  if o0O . status_code == 200 :
   II1Ii11Ii1i1I = json . loads ( o0O . content . decode ( 'utf-8' ) )
  else :
   II1Ii11Ii1i1I = None
  ii1iIi1II = time . time ( )
  iI1Ii11111iIi . write ( "t2 - t1:" + str ( ii1iIi1II - ii1Ii1IiIIi ) + "\n" )
  if 2 - 2: Oo0Ooo + OoOoOO00 - OOooOOo . I1IiiI - OOooOOo
  self . data = [ ]
  for oo0o0oooo in II1Ii11Ii1i1I :
   self . data . append ( oo0o0oooo [ 1 ] )
  iI1Ii11111iIi . write ( "displaying " + str ( len ( self . data ) ) + " values" + "\n" )
  if 20 - 20: i1IIi - I11i
  self . update_current_prices ( )
  if 30 - 30: OoOoOO00
  self . draw_plot ( )
  if 21 - 21: i11iIiiIii / Oo % OOooOOo * O0 . I11i - iIii1I11I1II1
 def on_exit ( self , event ) :
  self . Destroy ( )
  if 26 - 26: II111iiii * OoOoOO00
 def flash_status_message ( self , msg , flash_len_ms = 1500 ) :
  self . statusbar . SetStatusText ( msg )
  self . timeroff = wx . Timer ( self )
  self . Bind (
 wx . EVT_TIMER ,
 self . on_flash_status_off ,
 self . timeroff )
  self . timeroff . Start ( flash_len_ms , oneShot = True )
  if 10 - 10: II111iiii . I1II1
 def on_flash_status_off ( self , event ) :
  self . statusbar . SetStatusText ( '' )
  if 32 - 32: Ii1I . o0oo0o . OoooooooOO - OoO0O00 + oO0o
  if 88 - 88: I1II1
if __name__ == '__main__' :
 ii1Ii = wx . App ( )
 ii1Ii . frame = IIII ( )
 ii1Ii . frame . Show ( )
 ii1Ii . frame . SetSize ( ( 1000 , 800 ) )
 ii1Ii . MainLoop ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3

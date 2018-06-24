from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage

from background_task import background
from accounts.models import Investor, Document
from .models import Choice, Question, Portfolio, Investment, EmbeddedTweet, PricingData
from .forms import PortfolioForm
from .utils import get_pairs_and_pcts, get_investment_array, get_all_pairs, get_latest_prices_arr
import pymysql
import pymysql.cursors
import decimal
import time
import datetime
import requests
from django.conf import settings

pair_reverse_idx = {'BTC':0,'ETH':1,'XRP':2,'BCH':3,'EOS':4,'LTC':5,'XLM':6,'ADA':7,'TRX':8,'MIOTA':9,'USDT':10,'NEO':11,'DASH':12,'XMR':13,'BNB':14,'VEN':15,'ETC':16,'XEM':17,'OMG':18,'QTUM':19,'ONT':20,'ZEC':21,'ICX':22,'LSK':23,'DCR':24,'BCN':25,'ZIL':26,'AE':27,'BTG':28,'BTM':29,'SC':30,'ZRX':31,'XVG':32,'BTS':33,'STEEM':34,'MKR':35,'REP':36,'NANO':37,'DOGE':38,'RHOC':39,'WAVES':40,'BCD':41,'BAT':42,'WAN':43,'GNT':44,'BTCP':45,'STRAT':46,'DGB':47,'KCS':48,'WTC':49,'PPT':50,'SNT':51,'HSR':52,'DGD':53,'NAS':54,'HT':55,'IOST':56,'AION':57,'LRC':58,'KMD':59,'GXS':60,'CNX':61,'RDD':62,'BNT':63,'ARDR':64,'MAID':65,'ARK':66,'MOAC':67,'MONA':68,'ELF':69,'CENNZ':70,'DCN':71,'FUN':72,'BIX':73,'GAS':74,'MITH':75,'ENG':76,'PIVX':77,'VERI':78,'KNC':79,'ELA':80,'EMC':81,'FSN':82,'SYS':83,'DROP':84,'CMT':85,'KIN':86,'MANA':87,'NXT':88,'ETHOS':89,'DDD':90,'QASH':91,'DRGN':92,'FCT':93,'LOOM':94,'MTC':95,'GTC':96,'XZC':97,'POLY':98,'NULS':99,'SMART':100,'SUB':101,'CTXC':102,'THETA':103,'BFT':104,'PAYX':105,'STORM':106,'POWR':107,'BLOCK':108,'NXS':109,'MCO':110,'ETN':111,'GBYTE':112,'WAX':113,'TUSD':114,'ZEN':115,'WICC':116,'EOSDAC':117,'RLC':118,'GTO':119,'R':120,'DBC':121,'LINK':122,'SNM':123,'STORJ':124,'MAN':125,'ICN':126,'SALT':127,'NEXO':128,'DATA':129,'BTCD':130,'HOT':131,'CVC':132,'REQ':133,'NCASH':134,'PAY':135,'AGI':136,'HPB':137,'SKY':138,'TNB':139,'ACT':140,'XAS':141,'CVT':142,'ANT':143,'BCI':144,'GNO':145,'MDS':146,'NEBL':147,'BTO':148,'SAN':149,'RUFF':150,'ABT':151,'TRUE':152,'CND':153,'EKT':154,'GAME':155,'SMT':156,'DENT':157,'GRS':158,'DTR':159,'CRPT':160,'QSP':161,'DAI':162,'SOC':163,'CS':164,'IGNIS':165,'XDN':166,'PLR':167,'ENJ':168,'C20':169,'STQ':170,'VTC':171,'BLZ':172,'TKY':173,'BOS':174,'PART':175,'XSN':176,'EDR':177,'TPAY':178,'RDN':179,'AMB':180,'QKC':181,'OCN':182,'GNX':183,'PPC':184,'BRD':185,'ODE':186,'NKN':187,'ZCL':188,'POA':189,'SRN':190,'SPHTX':191,'VEE':192,'UBQ':193,'NANJ':194,'MTL':195,'GVT':196,'CPX':197,'IOTX':198,'TIO':199,'IHT':200,'POE':201,'REN':202,'JNT':203,'AUTO':204,'TEL':205,'BTX':206,'INT':207,'BURST':208,'SAFEX':209,'ITC':210,'EDG':211,'LINDA':212,'XPM':213,'INK':214,'ECA':215,'BITCNY':216,'RKT':217,'DAX':218,'TEN':219,'NAV':220,'SPANK':221,'TRAC':222,'LCC':223,'DTA':224,'NLG':225,'EDO':226,'WGR':227,'RPX':228,'DPY':229,'LEND':230,'EXC':231,'UNO':232,'EMC2':233,'BAY':234,'LYM':235,'ADX':236,'FTC':237,'CPT':238,'APIS':239,'QRL':240,'RVN':241,'BAX':242,'RNTB':243,'PPP':244,'TKN':245,'SLS':246,'TOMO':247,'DATX':248,'LGO':249,'PZM':250,'ETP':251,'CLOAK':252,'EVN':253,'XCP':254,'SWM':255,'TNT':256,'RCN':257,'TCT':258,'SWFTC':259,'VIA':260,'SNGLS':261,'ZCO':262,'GIN':263,'OST':264,'FXT':265,'AST':266,'HAV':267,'PAC':268,'KICK':269,'PRE':270,'SXDT':271,'DNT':272,'XWC':273,'UTK':274,'INS':275,'ATN':276,'UTNP':277,'WINGS':278,'CPC':279,'MGO':280,'DAT':281,'XP':282,'NGC':283,'BCO':284,'ZPT':285,'RNT':286,'AEON':287,'MSP':288,'HTML':289,'CDT':290,'LYL':291,'NMC':292,'MOD':293,'MNX':294,'WPR':295,'HST':296,'LBC':297,'CREDO':298,'ION':299,'YOYOW':300,'ART':301,'MLN':302,'CMCT':303,'FUEL':304,'HVN':305,'DCT':306,'APPC':307,'MED':308,'PHR':309,'BANCA':310,'LET':311,'ECC':312,'LUN':313,'DAG':314,'UUU':315,'SBD':316,'SENT':317,'DBET':318,'TAAS':319,'QLC':320,'WABI':321,'PCN':322,'PURA':323,'XDCE':324,'SSC':325,'VIBE':326,'ELEC':327,'MEDIC':328,'COSS':329,'YEE':330,'AURA':331,'CSC':332,'MOBI':333,'PRL':334,'QUN':335,'SHIFT':336,'CAS':337,'SOAR':338,'BITG':339,'BKX':340,'DOCK':341,'KEY':342,'XES':343,'POT':344,'QBT':345,'DXT':346,'IXT':347,'BMC':348,'PEPECASH':349,'COB':350,'GRID':351,'BITUSD':352,'KRM':353,'HMQ':354,'VIB':355,'PPY':356,'XEL':357,'1ST':358,'NLC2':359,'MTN':360,'THC':361,'TNC':362,'NTK':363,'COLX':364,'COV':365,'DIME':366,'FOTA':367,'LIFE':368,'XBY':369,'MER':370,'RFR':371,'PST':372,'ZSC':373,'PRA':374,'CFI':375,'BIS':376,'QAU':377,'LEO':378,'BRM':379,'BCPT':380,'AMP':381,'TIME':382,'BITB':383,'BLT':384,'LUX':385,'SPC':386,'ONION':387,'RVR':388,'CEEK':389,'TRIG':390,'LATX':391,'ACAT':392,'ALQO':393,'MOT':394,'XSH':395,'EVX':396,'DIVX':397,'DMT':398,'CRW':399,'MWAT':400,'UKG':401,'PASC':402,'TAU':403,'OXY':404,'OMX':405,'BBR':406,'TSL':407,'DIM':408,'PRO':409,'PLBT':410,'DADI':411,'UGC':412,'DMD':413,'BLK':414,'SNC':415,'BETR':416,'GRC':417,'BOT':418,'FLASH':419,'TFD':420,'DBIX':421,'UQC':422,'SWTH':423,'SKB':424,'BCA':425,'SOUL':426,'GUP':427,'MUSE':428,'SNTR':429,'GEM':430,'LA':431,'NKC':432,'MUE':433,'BPT':434,'STK':435,'NMR':436,'CV':437,'OMNI':438,'REM':439,'HYDRO':440,'RBY':441,'ORME':442,'SSP':443,'EVR':444,'MTH':445,'SHND':446,'NEU':447,'RADS':448,'CAPP':449,'STX':450,'MDA':451,'RMT':452,'TIX':453,'MDT':454,'SLR':455,'OAX':456,'ADT':457,'FLO':458,'ARN':459,'BBN':460,'MOON':461,'CHP':462,'AIT':463,'CLO':464,'AIDOC':465,'FDZ':466,'LOC':467,'PAL':468,'IOC':469,'PKC':470,'HXX':471,'UP':472,'SLT':473,'PAT':474,'DICE':475,'EXRN':476,'HMC':477,'SENC':478,'DLT':479,'GEN':480,'CHSB':481,'ABYSS':482,'BQ':483,'EXP':484,'EKO':485,'ZIPT':486,'CLAM':487,'IDH':488,'SRCOIN':489,'ATM':490,'NYC':491,'DEV':492,'GCR':493,'NBAI':494,'POLIS':495,'DTB':496,'CVCOIN':497,'MRK':498,'SHIP':499,'INCNT':500,'HER':501,'AXP':502,'LMC':503,'REBL':504,'APH':505,'DRT':506,'HKN':507,'UBT':508,'XMY':509,'RVT':510,'SEXC':511,'ECOB':512,'SIB':513,'RED':514,'ICOS':515,'SPRTS':516,'GET':517,'PCL':518,'NEOS':519,'BWK':520,'NPX':521,'DYN':522,'BEZ':523,'XST':524,'IPL':525,'VRC':526,'IFT':527,'MUSIC':528,'CAT':529,'LOKI':530,'UCASH':531,'BSD':532,'PIRL':533,'DEB':534,'HWC':535,'NVC':536,'XAUR':537,'FLIXX':538,'RMC':539,'PKT':540,'GBX':541,'NCT':542,'GRFT':543,'EFX':544,'NXC':545,'XPA':546,'AU':547,'SS':548,'APX':549,'PARETO':550,'AIR':551,'PINK':552,'GETX':553,'ZLA':554,'LEV':555,'SWT':556,'AID':557,'TUBE':558,'OK':559,'DGTX':560,'BIO':561,'AVT':562,'MTX':563,'CAG':564,'FLDC':565,'SPD':566,'CXO':567,'PRG':568,'CAN':569,'HBT':570,'PTOY':571,'ZAP':572,'LALA':573,'HBZ':574,'ZOI':575,'PND':576,'ERO':577,'BDG':578,'ADB':579,'ZRC':580,'GOLOS':581,'DERO':582,'MINT':583,'LNC':584,'LWF':585,'DNA':586,'BCC':587,'ADH':588,'PUT':589,'DOT':590,'XNK':591,'SIG':592,'SENSE':593,'MLM':594,'IDXM':595,'FLUZ':596,'BET':597,'NET':598,'BERRY':599,'ELIX':600,'TRST':601,'SEQ':602,'YOC':603,'ADI':604,'BNTY':605,'HEAT':606,'ALIS':607,'B2B':608,'TGT':609,'ENRG':610,'ESP':611,'APR':612,'MITX':613,'1WO':614,'XLR':615,'XSPEC':616,'CBT':617,'CURE':618,'CFUN':619,'COFI':620,'CLN':621,'BEE':622,'BCY':623,'FID':624,'LDC':625,'FACE':626,'MORPH':627,'MYST':628,'PBT':629,'GLD':630,'ADST':631,'LND':632,'COVAL':633,'AUR':634,'SETH':635,'SNOV':636,'EVE':637,'ATB':638,'TOA':639,'TFL':640,'SPHR':641,'MYB':642,'PRIX':643,'POLL':644,'EZT':645,'WCT':646,'MAX':647,'CSNO':648,'TRF':649,'AVA':650,'SYNX':651,'GLA':652,'REAL':653,'IPSX':654,'ABY':655,'TX':656,'NPER':657,'KORE':658,'TIPS':659,'ARY':660,'VIT':661,'OBITS':662,'SHL':663,'WRC':664,'SHP':665,'HQX':666,'J8T':667,'INXT':668,'BRX':669,'VME':670,'BTCZ':671,'PTC':672,'MONK':673,'HUR':674,'GEO':675,'2GIVE':676,'ASTRO':677,'AUC':678,'DTH':679,'OTN':680,'BLUE':681,'PLAY':682,'XBC':683,'FND':684,'PFR':685,'HYP':686,'GCC':687,'IOP':688,'FDX':689,'ATL':690,'INSTAR':691,'HGT':692,'LEDU':693,'UNIT':694,'USNBT':695,'SUMO':696,'EXY':697,'0xBTC':698,'SPR':699,'ERC':700,'XHV':701,'INV':702,'CPAY':703,'IXC':704,'BUZZ':705,'BBO':706,'HAC':707,'BSTN':708,'NTRN':709,'XMCC':710,'SXUT':711,'UFR':712,'SPF':713,'GMT':714,'SEND':715,'AMLT':716,'SCL':717,'QWARK':718,'DOPE':719,'TKS':720,'MSR':721,'FTX':722,'TKA':723,'VRM':724,'RIC':725,'PING':726,'PBL':727,'RUPX':728,'GAT':729,'ZEIT':730,'VOISE':731,'ING':732,'EXCL':733,'HOLD':734,'WISH':735,'IND':736,'MEME':737,'ALT':738,'BON':739,'BRK':740,'EBST':741,'BTDX':742,'I0C':743,'TRC':744,'KRB':745,'SSS':746,'PURE':747,'XHI':748,'CRAVE':749,'ORE':750,'HUSH':751,'VTR':752,'ANC':753,'CMPCO':754,'ETBS':755,'REF':756,'DNR':757,'XGOX':758,'CHX':759,'MVC':760,'FOR':761,'CANN':762,'VIU':763,'NAVI':764,'FYP':765,'CPY':766,'STAC':767,'GENE':768,'SGR':769,'NIO':770,'PIX':771,'MAGE':772,'NLX':773,'EGC':774,'CL':775,'ZEPH':776,'MFG':777,'BBP':778,'BUN':779,'PYLNT':780,'CDX':781,'DAN':782,'TRAK':783,'LDOGE':784,'TES':785,'FGC':786,'AIX':787,'WSX':788,'MAC':789,'NOBL':790,'DP':791,'LOCI':792,'HIRE':793,'OPC':794,'GCN':795,'IC':796,'ACE':797,'BOUTS':798,'XNN':799,'CREA':800,'EFYT':801,'XTL':802,'TEAM':803,'XMG':804,'HUC':805,'RAIN':806,'MNTP':807,'TRCT':808,'EFL':809,'XBP':810,'BTW':811,'TZC':812,'DIX':813,'ODN':814,'STAK':815,'FT':816,'CRB':817,'HAT':818,'SWIFT':819,'ZER':820,'BYC':821,'AMM':822,'EBTC':823,'FRST':824,'ITNS':825,'ESZ':826,'BTRN':827,'UCOM':828,'SKIN':829,'MAG':830,'DGC':831,'VIVO':832,'PHO':833,'FCN':834,'MRT':835,'RNS':836,'SCT':837,'DAY':838,'JEW':839,'JC':840,'SGN':841,'ADZ':842,'HERO':843,'TDX':844,'ZNY':845,'808':846,'EPY':847,'TDS':848,'UIS':849,'DTRC':850,'ELLA':851,'EBCH':852,'UNB':853,'FYN':854,'TIG':855,'AMN':856,'ATS':857,'DFT':858,'NOX':859,'STU':860,'EARTH':861,'JIYO':862,'MEC':863,'ORI':864,'DRPU':865,'MORE':866,'INN':867,'EVC':868,'TNS':869,'LINX':870,'SAGA':871,'MBI':872,'ZET':873,'ARC':874,'EL':875,'UNIFY':876,'EQT':877,'VULC':878,'KLN':879,'QVT':880,'PLAN':881,'VRS':882,'IFLT':883,'BTA':884,'MCAP':885,'SUR':886,'HPC':887,'ELTCOIN':888,'XPD':889,'CRM':890,'RLT':891,'WILD':892,'XTO':893,'DGPT':894,'CJT':895,'BTB':896,'ZBC':897,'1337':898,'42':899,'GAM':900,'KB3':901,'NSR':902,'CRC':903,'BDL':904,'CHC':905,'GRMD':906,'MBRS':907,'EQL':908,'JET':909,'BITSILVER':910,'PIPL':911,'XCN':912,'BBI':913,'NMS':914,'OCT':915,'QBIC':916,'FANS':917,'ADC':918,'TRUST':919,'VZT':920,'TBX':921,'XRL':922,'ARG':923,'SMS':924,'CRED':925,'ONG':926,'DEW':927,'OPT':928,'DOVU':929,'DEM':930,'SXC':931,'HORSE':932,'LIVE':933}

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app/results.html'

def portfolio(request, pk):
    user = request.user
    all_portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.get(pk=pk)
    all_investments = Investment.objects.filter(portfolio=portfolio)
    BTC_latest_val= ETH_latest_val= XRP_latest_val= BCH_latest_val= EOS_latest_val= LTC_latest_val= XLM_latest_val= ADA_latest_val= TRX_latest_val= MIOTA_latest_val= USDT_latest_val= NEO_latest_val= DASH_latest_val= XMR_latest_val= BNB_latest_val= VEN_latest_val= ETC_latest_val= XEM_latest_val= OMG_latest_val= QTUM_latest_val= ONT_latest_val= ZEC_latest_val= ICX_latest_val= LSK_latest_val= DCR_latest_val= BCN_latest_val= ZIL_latest_val= AE_latest_val= BTG_latest_val= BTM_latest_val= SC_latest_val= ZRX_latest_val= XVG_latest_val= BTS_latest_val= STEEM_latest_val= MKR_latest_val= REP_latest_val= NANO_latest_val= DOGE_latest_val= RHOC_latest_val= WAVES_latest_val= BCD_latest_val= BAT_latest_val= WAN_latest_val= GNT_latest_val= BTCP_latest_val= STRAT_latest_val= DGB_latest_val= KCS_latest_val= WTC_latest_val= PPT_latest_val= SNT_latest_val= HSR_latest_val= DGD_latest_val= NAS_latest_val= HT_latest_val= IOST_latest_val= AION_latest_val= LRC_latest_val= KMD_latest_val= GXS_latest_val= CNX_latest_val= RDD_latest_val= BNT_latest_val= ARDR_latest_val= MAID_latest_val= ARK_latest_val= MOAC_latest_val= MONA_latest_val= ELF_latest_val= CENNZ_latest_val= DCN_latest_val= FUN_latest_val= BIX_latest_val= GAS_latest_val= MITH_latest_val= ENG_latest_val= PIVX_latest_val= VERI_latest_val= KNC_latest_val= ELA_latest_val= EMC_latest_val= FSN_latest_val= SYS_latest_val= DROP_latest_val= CMT_latest_val= KIN_latest_val= MANA_latest_val= NXT_latest_val= ETHOS_latest_val= DDD_latest_val= QASH_latest_val= DRGN_latest_val= FCT_latest_val= LOOM_latest_val= MTC_latest_val= GTC_latest_val= XZC_latest_val= POLY_latest_val= NULS_latest_val= SMART_latest_val= SUB_latest_val= CTXC_latest_val= THETA_latest_val= BFT_latest_val= PAYX_latest_val= STORM_latest_val= POWR_latest_val= BLOCK_latest_val= NXS_latest_val= MCO_latest_val= ETN_latest_val= GBYTE_latest_val= WAX_latest_val= TUSD_latest_val= ZEN_latest_val= WICC_latest_val= EOSDAC_latest_val= RLC_latest_val= GTO_latest_val= R_latest_val= DBC_latest_val= LINK_latest_val= SNM_latest_val= STORJ_latest_val= MAN_latest_val= ICN_latest_val= SALT_latest_val= NEXO_latest_val= DATA_latest_val= BTCD_latest_val= HOT_latest_val= CVC_latest_val= REQ_latest_val= NCASH_latest_val= PAY_latest_val= AGI_latest_val= HPB_latest_val= SKY_latest_val= TNB_latest_val= ACT_latest_val= XAS_latest_val= CVT_latest_val= ANT_latest_val= BCI_latest_val= GNO_latest_val= MDS_latest_val= NEBL_latest_val= BTO_latest_val= SAN_latest_val= RUFF_latest_val= ABT_latest_val= TRUE_latest_val= CND_latest_val= EKT_latest_val= GAME_latest_val= SMT_latest_val= DENT_latest_val= GRS_latest_val= DTR_latest_val= CRPT_latest_val= QSP_latest_val= DAI_latest_val= SOC_latest_val= CS_latest_val= IGNIS_latest_val= XDN_latest_val= PLR_latest_val= ENJ_latest_val= C20_latest_val= STQ_latest_val= VTC_latest_val= BLZ_latest_val= TKY_latest_val= BOS_latest_val= PART_latest_val= XSN_latest_val= EDR_latest_val= TPAY_latest_val= RDN_latest_val= AMB_latest_val= QKC_latest_val= OCN_latest_val= GNX_latest_val= PPC_latest_val= BRD_latest_val= ODE_latest_val= NKN_latest_val= ZCL_latest_val= POA_latest_val= SRN_latest_val= SPHTX_latest_val= VEE_latest_val= UBQ_latest_val= NANJ_latest_val= MTL_latest_val= GVT_latest_val= CPX_latest_val= IOTX_latest_val= TIO_latest_val= IHT_latest_val= POE_latest_val= REN_latest_val= JNT_latest_val= AUTO_latest_val= TEL_latest_val= BTX_latest_val= INT_latest_val= BURST_latest_val= SAFEX_latest_val= ITC_latest_val= EDG_latest_val= LINDA_latest_val= XPM_latest_val= INK_latest_val= ECA_latest_val= BITCNY_latest_val= RKT_latest_val= DAX_latest_val= TEN_latest_val= NAV_latest_val= SPANK_latest_val= TRAC_latest_val= LCC_latest_val= DTA_latest_val= NLG_latest_val= EDO_latest_val= WGR_latest_val= RPX_latest_val= DPY_latest_val= LEND_latest_val= EXC_latest_val= UNO_latest_val= EMC2_latest_val= BAY_latest_val= LYM_latest_val= ADX_latest_val= FTC_latest_val= CPT_latest_val= APIS_latest_val= QRL_latest_val= RVN_latest_val= BAX_latest_val= RNTB_latest_val= PPP_latest_val= TKN_latest_val= SLS_latest_val= TOMO_latest_val= DATX_latest_val= LGO_latest_val= PZM_latest_val= ETP_latest_val= CLOAK_latest_val= EVN_latest_val= XCP_latest_val= SWM_latest_val= TNT_latest_val= RCN_latest_val= TCT_latest_val= SWFTC_latest_val= VIA_latest_val= SNGLS_latest_val= ZCO_latest_val= GIN_latest_val= OST_latest_val= FXT_latest_val= AST_latest_val= HAV_latest_val= PAC_latest_val= KICK_latest_val= PRE_latest_val= SXDT_latest_val= DNT_latest_val= XWC_latest_val= UTK_latest_val= INS_latest_val= ATN_latest_val= UTNP_latest_val= WINGS_latest_val= CPC_latest_val= MGO_latest_val= DAT_latest_val= XP_latest_val= NGC_latest_val= BCO_latest_val= ZPT_latest_val= RNT_latest_val= AEON_latest_val= MSP_latest_val= HTML_latest_val= CDT_latest_val= LYL_latest_val= NMC_latest_val= MOD_latest_val= MNX_latest_val= WPR_latest_val= HST_latest_val= LBC_latest_val= CREDO_latest_val= ION_latest_val= YOYOW_latest_val= ART_latest_val= MLN_latest_val= CMCT_latest_val= FUEL_latest_val= HVN_latest_val= DCT_latest_val= APPC_latest_val= MED_latest_val= PHR_latest_val= BANCA_latest_val= LET_latest_val= ECC_latest_val= LUN_latest_val= DAG_latest_val= UUU_latest_val= SBD_latest_val= SENT_latest_val= DBET_latest_val= TAAS_latest_val= QLC_latest_val= WABI_latest_val= PCN_latest_val= PURA_latest_val= XDCE_latest_val= SSC_latest_val= VIBE_latest_val= ELEC_latest_val= MEDIC_latest_val= COSS_latest_val= YEE_latest_val= AURA_latest_val= CSC_latest_val= MOBI_latest_val= PRL_latest_val= QUN_latest_val= SHIFT_latest_val= CAS_latest_val= SOAR_latest_val= BITG_latest_val= BKX_latest_val= DOCK_latest_val= KEY_latest_val= XES_latest_val= POT_latest_val= QBT_latest_val= DXT_latest_val= IXT_latest_val= BMC_latest_val= PEPECASH_latest_val= COB_latest_val= GRID_latest_val= BITUSD_latest_val= KRM_latest_val= HMQ_latest_val= VIB_latest_val= PPY_latest_val= XEL_latest_val= e_1ST_latest_val= NLC2_latest_val= MTN_latest_val= THC_latest_val= TNC_latest_val= NTK_latest_val= COLX_latest_val= COV_latest_val= DIME_latest_val= FOTA_latest_val= LIFE_latest_val= XBY_latest_val= MER_latest_val= RFR_latest_val= PST_latest_val= ZSC_latest_val= PRA_latest_val= CFI_latest_val= BIS_latest_val= QAU_latest_val= LEO_latest_val= BRM_latest_val= BCPT_latest_val= AMP_latest_val= TIME_latest_val= BITB_latest_val= BLT_latest_val= LUX_latest_val= SPC_latest_val= ONION_latest_val= RVR_latest_val= CEEK_latest_val= TRIG_latest_val= LATX_latest_val= ACAT_latest_val= ALQO_latest_val= MOT_latest_val= XSH_latest_val= EVX_latest_val= DIVX_latest_val= DMT_latest_val= CRW_latest_val= MWAT_latest_val= UKG_latest_val= PASC_latest_val= TAU_latest_val= OXY_latest_val= OMX_latest_val= BBR_latest_val= TSL_latest_val= DIM_latest_val= PRO_latest_val= PLBT_latest_val= DADI_latest_val= UGC_latest_val= DMD_latest_val= BLK_latest_val= SNC_latest_val= BETR_latest_val= GRC_latest_val= BOT_latest_val= FLASH_latest_val= TFD_latest_val= DBIX_latest_val= UQC_latest_val= SWTH_latest_val= SKB_latest_val= BCA_latest_val= SOUL_latest_val= GUP_latest_val= MUSE_latest_val= SNTR_latest_val= GEM_latest_val= LA_latest_val= NKC_latest_val= MUE_latest_val= BPT_latest_val= STK_latest_val= NMR_latest_val= CV_latest_val= OMNI_latest_val= REM_latest_val= HYDRO_latest_val= RBY_latest_val= ORME_latest_val= SSP_latest_val= EVR_latest_val= MTH_latest_val= SHND_latest_val= NEU_latest_val= RADS_latest_val= CAPP_latest_val= STX_latest_val= MDA_latest_val= RMT_latest_val= TIX_latest_val= MDT_latest_val= SLR_latest_val= OAX_latest_val= ADT_latest_val= FLO_latest_val= ARN_latest_val= BBN_latest_val= MOON_latest_val= CHP_latest_val= AIT_latest_val= CLO_latest_val= AIDOC_latest_val= FDZ_latest_val= LOC_latest_val= PAL_latest_val= IOC_latest_val= PKC_latest_val= HXX_latest_val= UP_latest_val= SLT_latest_val= PAT_latest_val= DICE_latest_val= EXRN_latest_val= HMC_latest_val= SENC_latest_val= DLT_latest_val= GEN_latest_val= CHSB_latest_val= ABYSS_latest_val= BQ_latest_val= EXP_latest_val= EKO_latest_val= ZIPT_latest_val= CLAM_latest_val= IDH_latest_val= SRCOIN_latest_val= ATM_latest_val= NYC_latest_val= DEV_latest_val= GCR_latest_val= NBAI_latest_val= POLIS_latest_val= DTB_latest_val= CVCOIN_latest_val= MRK_latest_val= SHIP_latest_val= INCNT_latest_val= HER_latest_val= AXP_latest_val= LMC_latest_val= REBL_latest_val= APH_latest_val= DRT_latest_val= HKN_latest_val= UBT_latest_val= XMY_latest_val= RVT_latest_val= SEXC_latest_val= ECOB_latest_val= SIB_latest_val= RED_latest_val= ICOS_latest_val= SPRTS_latest_val= GET_latest_val= PCL_latest_val= NEOS_latest_val= BWK_latest_val= NPX_latest_val= DYN_latest_val= BEZ_latest_val= XST_latest_val= IPL_latest_val= VRC_latest_val= IFT_latest_val= MUSIC_latest_val= CAT_latest_val= LOKI_latest_val= UCASH_latest_val= BSD_latest_val= PIRL_latest_val= DEB_latest_val= HWC_latest_val= NVC_latest_val= XAUR_latest_val= FLIXX_latest_val= RMC_latest_val= PKT_latest_val= GBX_latest_val= NCT_latest_val= GRFT_latest_val= EFX_latest_val= NXC_latest_val= XPA_latest_val= AU_latest_val= SS_latest_val= APX_latest_val= PARETO_latest_val= AIR_latest_val= PINK_latest_val= GETX_latest_val= ZLA_latest_val= LEV_latest_val= SWT_latest_val= AID_latest_val= TUBE_latest_val= OK_latest_val= DGTX_latest_val= BIO_latest_val= AVT_latest_val= MTX_latest_val= CAG_latest_val= FLDC_latest_val= SPD_latest_val= CXO_latest_val= PRG_latest_val= CAN_latest_val= HBT_latest_val= PTOY_latest_val= ZAP_latest_val= LALA_latest_val= HBZ_latest_val= ZOI_latest_val= PND_latest_val= ERO_latest_val= BDG_latest_val= ADB_latest_val= ZRC_latest_val= GOLOS_latest_val= DERO_latest_val= MINT_latest_val= LNC_latest_val= LWF_latest_val= DNA_latest_val= BCC_latest_val= ADH_latest_val= PUT_latest_val= DOT_latest_val= XNK_latest_val= SIG_latest_val= SENSE_latest_val= MLM_latest_val= IDXM_latest_val= FLUZ_latest_val= BET_latest_val= NET_latest_val= BERRY_latest_val= ELIX_latest_val= TRST_latest_val= SEQ_latest_val= YOC_latest_val= ADI_latest_val= BNTY_latest_val= HEAT_latest_val= ALIS_latest_val= B2B_latest_val= TGT_latest_val= ENRG_latest_val= ESP_latest_val= APR_latest_val= MITX_latest_val= e_1WO_latest_val= XLR_latest_val= XSPEC_latest_val= CBT_latest_val= CURE_latest_val= CFUN_latest_val= COFI_latest_val= CLN_latest_val= BEE_latest_val= BCY_latest_val= FID_latest_val= LDC_latest_val= FACE_latest_val= MORPH_latest_val= MYST_latest_val= PBT_latest_val= GLD_latest_val= ADST_latest_val= LND_latest_val= COVAL_latest_val= AUR_latest_val= SETH_latest_val= SNOV_latest_val= EVE_latest_val= ATB_latest_val= TOA_latest_val= TFL_latest_val= SPHR_latest_val= MYB_latest_val= PRIX_latest_val= POLL_latest_val= EZT_latest_val= WCT_latest_val= MAX_latest_val= CSNO_latest_val= TRF_latest_val= AVA_latest_val= SYNX_latest_val= GLA_latest_val= REAL_latest_val= IPSX_latest_val= ABY_latest_val= TX_latest_val= NPER_latest_val= KORE_latest_val= TIPS_latest_val= ARY_latest_val= VIT_latest_val= OBITS_latest_val= SHL_latest_val= WRC_latest_val= SHP_latest_val= HQX_latest_val= J8T_latest_val= INXT_latest_val= BRX_latest_val= VME_latest_val= BTCZ_latest_val= PTC_latest_val= MONK_latest_val= HUR_latest_val= GEO_latest_val= e_2GIVE_latest_val= ASTRO_latest_val= AUC_latest_val= DTH_latest_val= OTN_latest_val= BLUE_latest_val= PLAY_latest_val= XBC_latest_val= FND_latest_val= PFR_latest_val= HYP_latest_val= GCC_latest_val= IOP_latest_val= FDX_latest_val= ATL_latest_val= INSTAR_latest_val= HGT_latest_val= LEDU_latest_val= UNIT_latest_val= USNBT_latest_val= SUMO_latest_val= EXY_latest_val= e_0xBTC_latest_val= SPR_latest_val= ERC_latest_val= XHV_latest_val= INV_latest_val= CPAY_latest_val= IXC_latest_val= BUZZ_latest_val= BBO_latest_val= HAC_latest_val= BSTN_latest_val= NTRN_latest_val= XMCC_latest_val= SXUT_latest_val= UFR_latest_val= SPF_latest_val= GMT_latest_val= SEND_latest_val= AMLT_latest_val= SCL_latest_val= QWARK_latest_val= DOPE_latest_val= TKS_latest_val= MSR_latest_val= FTX_latest_val= TKA_latest_val= VRM_latest_val= RIC_latest_val= PING_latest_val= PBL_latest_val= RUPX_latest_val= GAT_latest_val= ZEIT_latest_val= VOISE_latest_val= ING_latest_val= EXCL_latest_val= HOLD_latest_val= WISH_latest_val= IND_latest_val= MEME_latest_val= ALT_latest_val= BON_latest_val= BRK_latest_val= EBST_latest_val= BTDX_latest_val= I0C_latest_val= TRC_latest_val= KRB_latest_val= SSS_latest_val= PURE_latest_val= XHI_latest_val= CRAVE_latest_val= ORE_latest_val= HUSH_latest_val= VTR_latest_val= ANC_latest_val= CMPCO_latest_val= ETBS_latest_val= REF_latest_val= DNR_latest_val= XGOX_latest_val= CHX_latest_val= MVC_latest_val= FOR_latest_val= CANN_latest_val= VIU_latest_val= NAVI_latest_val= FYP_latest_val= CPY_latest_val= STAC_latest_val= GENE_latest_val= SGR_latest_val= NIO_latest_val= PIX_latest_val= MAGE_latest_val= NLX_latest_val= EGC_latest_val= CL_latest_val= ZEPH_latest_val= MFG_latest_val= BBP_latest_val= BUN_latest_val= PYLNT_latest_val= CDX_latest_val= DAN_latest_val= TRAK_latest_val= LDOGE_latest_val= TES_latest_val= FGC_latest_val= AIX_latest_val= WSX_latest_val= MAC_latest_val= NOBL_latest_val= DP_latest_val= LOCI_latest_val= HIRE_latest_val= OPC_latest_val= GCN_latest_val= IC_latest_val= ACE_latest_val= BOUTS_latest_val= XNN_latest_val= CREA_latest_val= EFYT_latest_val= XTL_latest_val= TEAM_latest_val= XMG_latest_val= HUC_latest_val= RAIN_latest_val= MNTP_latest_val= TRCT_latest_val= EFL_latest_val= XBP_latest_val= BTW_latest_val= TZC_latest_val= DIX_latest_val= ODN_latest_val= STAK_latest_val= FT_latest_val= CRB_latest_val= HAT_latest_val= SWIFT_latest_val= ZER_latest_val= BYC_latest_val= AMM_latest_val= EBTC_latest_val= FRST_latest_val= ITNS_latest_val= ESZ_latest_val= BTRN_latest_val= UCOM_latest_val= SKIN_latest_val= MAG_latest_val= DGC_latest_val= VIVO_latest_val= PHO_latest_val= FCN_latest_val= MRT_latest_val= RNS_latest_val= SCT_latest_val= DAY_latest_val= JEW_latest_val= JC_latest_val= SGN_latest_val= ADZ_latest_val= HERO_latest_val= TDX_latest_val= ZNY_latest_val= e_808_latest_val= EPY_latest_val= TDS_latest_val= UIS_latest_val= DTRC_latest_val= ELLA_latest_val= EBCH_latest_val= UNB_latest_val= FYN_latest_val= TIG_latest_val= AMN_latest_val= ATS_latest_val= DFT_latest_val= NOX_latest_val= STU_latest_val= EARTH_latest_val= JIYO_latest_val= MEC_latest_val= ORI_latest_val= DRPU_latest_val= MORE_latest_val= INN_latest_val= EVC_latest_val= TNS_latest_val= LINX_latest_val= SAGA_latest_val= MBI_latest_val= ZET_latest_val= ARC_latest_val= EL_latest_val= UNIFY_latest_val= EQT_latest_val= VULC_latest_val= KLN_latest_val= QVT_latest_val= PLAN_latest_val= VRS_latest_val= IFLT_latest_val= BTA_latest_val= MCAP_latest_val= SUR_latest_val= HPC_latest_val= ELTCOIN_latest_val= XPD_latest_val= CRM_latest_val= RLT_latest_val= WILD_latest_val= XTO_latest_val= DGPT_latest_val= CJT_latest_val= BTB_latest_val= ZBC_latest_val= e_1337_latest_val= e_42_latest_val= GAM_latest_val= KB3_latest_val= NSR_latest_val= CRC_latest_val= BDL_latest_val= CHC_latest_val= GRMD_latest_val= MBRS_latest_val= EQL_latest_val= JET_latest_val= BITSILVER_latest_val= PIPL_latest_val= XCN_latest_val= BBI_latest_val= NMS_latest_val= OCT_latest_val= QBIC_latest_val= FANS_latest_val= ADC_latest_val= TRUST_latest_val= VZT_latest_val= TBX_latest_val= XRL_latest_val= ARG_latest_val= SMS_latest_val= CRED_latest_val= ONG_latest_val= DEW_latest_val= OPT_latest_val= DOVU_latest_val= DEM_latest_val= SXC_latest_val= HORSE_latest_val= LIVE_latest_val= 0.0
    aum = 0.0
    for i in all_investments:
        aum += float(i.original_amt)
    aum = round(aum)
    # get latest valuations to embed in the page
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='01990199',#settings.SPREADS_DB_PASSWD,
                                 db='coiniumweb',#settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            #pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
            (pairs, pair_pcts) = get_pairs_and_pcts(pk)
            spreads_for_pair = dict()
            for i in range(len(pairs)):
                pair = pairs[i]
                pair_pct = pair_pcts[i]
                if pair_pct > 0:
                    #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                    sql = "select * from app_pricingdata where shorthand = %s order by created_at desc limit 1"
                    cursor.execute(sql, (pair,))
                    spreads = cursor.fetchall()
                    spreads_for_pair[pair] = spreads
                    print("spreads", spreads)
                    if not spreads:
                        spreads = [{'shorthand':pair, 'price': 0}]
                    if spreads[0]['shorthand'] == 'BTC':
                        BTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETH':
                        ETH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XRP':
                        XRP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCH':
                        BCH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EOS':
                        EOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LTC':
                        LTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XLM':
                        XLM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADA':
                        ADA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRX':
                        TRX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MIOTA':
                        MIOTA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'USDT':
                        USDT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NEO':
                        NEO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DASH':
                        DASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XMR':
                        XMR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BNB':
                        BNB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VEN':
                        VEN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETC':
                        ETC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XEM':
                        XEM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OMG':
                        OMG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QTUM':
                        QTUM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ONT':
                        ONT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZEC':
                        ZEC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ICX':
                        ICX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LSK':
                        LSK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DCR':
                        DCR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCN':
                        BCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZIL':
                        ZIL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AE':
                        AE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTG':
                        BTG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTM':
                        BTM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SC':
                        SC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZRX':
                        ZRX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XVG':
                        XVG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTS':
                        BTS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STEEM':
                        STEEM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MKR':
                        MKR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REP':
                        REP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NANO':
                        NANO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DOGE':
                        DOGE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RHOC':
                        RHOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WAVES':
                        WAVES_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCD':
                        BCD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BAT':
                        BAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WAN':
                        WAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GNT':
                        GNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTCP':
                        BTCP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STRAT':
                        STRAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DGB':
                        DGB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KCS':
                        KCS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WTC':
                        WTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PPT':
                        PPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNT':
                        SNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HSR':
                        HSR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DGD':
                        DGD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NAS':
                        NAS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HT':
                        HT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IOST':
                        IOST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AION':
                        AION_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LRC':
                        LRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KMD':
                        KMD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GXS':
                        GXS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CNX':
                        CNX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RDD':
                        RDD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BNT':
                        BNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARDR':
                        ARDR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAID':
                        MAID_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARK':
                        ARK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MOAC':
                        MOAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MONA':
                        MONA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELF':
                        ELF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CENNZ':
                        CENNZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DCN':
                        DCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FUN':
                        FUN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BIX':
                        BIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GAS':
                        GAS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MITH':
                        MITH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ENG':
                        ENG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PIVX':
                        PIVX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VERI':
                        VERI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KNC':
                        KNC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELA':
                        ELA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EMC':
                        EMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FSN':
                        FSN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SYS':
                        SYS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DROP':
                        DROP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CMT':
                        CMT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KIN':
                        KIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MANA':
                        MANA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NXT':
                        NXT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETHOS':
                        ETHOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DDD':
                        DDD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QASH':
                        QASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DRGN':
                        DRGN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FCT':
                        FCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LOOM':
                        LOOM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MTC':
                        MTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GTC':
                        GTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XZC':
                        XZC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POLY':
                        POLY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NULS':
                        NULS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SMART':
                        SMART_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SUB':
                        SUB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CTXC':
                        CTXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'THETA':
                        THETA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BFT':
                        BFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PAYX':
                        PAYX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STORM':
                        STORM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POWR':
                        POWR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BLOCK':
                        BLOCK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NXS':
                        NXS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MCO':
                        MCO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETN':
                        ETN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GBYTE':
                        GBYTE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WAX':
                        WAX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TUSD':
                        TUSD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZEN':
                        ZEN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WICC':
                        WICC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EOSDAC':
                        EOSDAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RLC':
                        RLC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GTO':
                        GTO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'R':
                        R_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DBC':
                        DBC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LINK':
                        LINK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNM':
                        SNM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STORJ':
                        STORJ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAN':
                        MAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ICN':
                        ICN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SALT':
                        SALT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NEXO':
                        NEXO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DATA':
                        DATA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTCD':
                        BTCD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HOT':
                        HOT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CVC':
                        CVC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REQ':
                        REQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NCASH':
                        NCASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PAY':
                        PAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AGI':
                        AGI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HPB':
                        HPB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SKY':
                        SKY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TNB':
                        TNB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ACT':
                        ACT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XAS':
                        XAS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CVT':
                        CVT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ANT':
                        ANT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCI':
                        BCI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GNO':
                        GNO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MDS':
                        MDS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NEBL':
                        NEBL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTO':
                        BTO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SAN':
                        SAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RUFF':
                        RUFF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ABT':
                        ABT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRUE':
                        TRUE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CND':
                        CND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EKT':
                        EKT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GAME':
                        GAME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SMT':
                        SMT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DENT':
                        DENT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GRS':
                        GRS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DTR':
                        DTR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRPT':
                        CRPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QSP':
                        QSP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAI':
                        DAI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SOC':
                        SOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CS':
                        CS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IGNIS':
                        IGNIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XDN':
                        XDN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PLR':
                        PLR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ENJ':
                        ENJ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'C20':
                        C20_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STQ':
                        STQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VTC':
                        VTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BLZ':
                        BLZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TKY':
                        TKY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BOS':
                        BOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PART':
                        PART_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XSN':
                        XSN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EDR':
                        EDR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TPAY':
                        TPAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RDN':
                        RDN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AMB':
                        AMB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QKC':
                        QKC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OCN':
                        OCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GNX':
                        GNX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PPC':
                        PPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BRD':
                        BRD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ODE':
                        ODE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NKN':
                        NKN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZCL':
                        ZCL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POA':
                        POA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SRN':
                        SRN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPHTX':
                        SPHTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VEE':
                        VEE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UBQ':
                        UBQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NANJ':
                        NANJ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MTL':
                        MTL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GVT':
                        GVT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CPX':
                        CPX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IOTX':
                        IOTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TIO':
                        TIO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IHT':
                        IHT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POE':
                        POE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REN':
                        REN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'JNT':
                        JNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AUTO':
                        AUTO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TEL':
                        TEL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTX':
                        BTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INT':
                        INT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BURST':
                        BURST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SAFEX':
                        SAFEX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ITC':
                        ITC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EDG':
                        EDG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LINDA':
                        LINDA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XPM':
                        XPM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INK':
                        INK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ECA':
                        ECA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BITCNY':
                        BITCNY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RKT':
                        RKT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAX':
                        DAX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TEN':
                        TEN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NAV':
                        NAV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPANK':
                        SPANK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRAC':
                        TRAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LCC':
                        LCC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DTA':
                        DTA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NLG':
                        NLG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EDO':
                        EDO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WGR':
                        WGR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RPX':
                        RPX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DPY':
                        DPY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LEND':
                        LEND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EXC':
                        EXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UNO':
                        UNO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EMC2':
                        EMC2_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BAY':
                        BAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LYM':
                        LYM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADX':
                        ADX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FTC':
                        FTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CPT':
                        CPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'APIS':
                        APIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QRL':
                        QRL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RVN':
                        RVN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BAX':
                        BAX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RNTB':
                        RNTB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PPP':
                        PPP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TKN':
                        TKN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SLS':
                        SLS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TOMO':
                        TOMO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DATX':
                        DATX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LGO':
                        LGO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PZM':
                        PZM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETP':
                        ETP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CLOAK':
                        CLOAK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EVN':
                        EVN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XCP':
                        XCP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SWM':
                        SWM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TNT':
                        TNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RCN':
                        RCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TCT':
                        TCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SWFTC':
                        SWFTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIA':
                        VIA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNGLS':
                        SNGLS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZCO':
                        ZCO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GIN':
                        GIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OST':
                        OST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FXT':
                        FXT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AST':
                        AST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HAV':
                        HAV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PAC':
                        PAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KICK':
                        KICK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRE':
                        PRE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SXDT':
                        SXDT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DNT':
                        DNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XWC':
                        XWC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UTK':
                        UTK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INS':
                        INS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ATN':
                        ATN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UTNP':
                        UTNP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WINGS':
                        WINGS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CPC':
                        CPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MGO':
                        MGO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAT':
                        DAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XP':
                        XP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NGC':
                        NGC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCO':
                        BCO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZPT':
                        ZPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RNT':
                        RNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AEON':
                        AEON_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MSP':
                        MSP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HTML':
                        HTML_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CDT':
                        CDT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LYL':
                        LYL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NMC':
                        NMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MOD':
                        MOD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MNX':
                        MNX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WPR':
                        WPR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HST':
                        HST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LBC':
                        LBC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CREDO':
                        CREDO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ION':
                        ION_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'YOYOW':
                        YOYOW_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ART':
                        ART_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MLN':
                        MLN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CMCT':
                        CMCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FUEL':
                        FUEL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HVN':
                        HVN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DCT':
                        DCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'APPC':
                        APPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MED':
                        MED_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PHR':
                        PHR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BANCA':
                        BANCA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LET':
                        LET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ECC':
                        ECC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LUN':
                        LUN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAG':
                        DAG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UUU':
                        UUU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SBD':
                        SBD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SENT':
                        SENT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DBET':
                        DBET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TAAS':
                        TAAS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QLC':
                        QLC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WABI':
                        WABI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PCN':
                        PCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PURA':
                        PURA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XDCE':
                        XDCE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SSC':
                        SSC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIBE':
                        VIBE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELEC':
                        ELEC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MEDIC':
                        MEDIC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COSS':
                        COSS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'YEE':
                        YEE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AURA':
                        AURA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CSC':
                        CSC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MOBI':
                        MOBI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRL':
                        PRL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QUN':
                        QUN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SHIFT':
                        SHIFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CAS':
                        CAS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SOAR':
                        SOAR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BITG':
                        BITG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BKX':
                        BKX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DOCK':
                        DOCK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KEY':
                        KEY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XES':
                        XES_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POT':
                        POT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QBT':
                        QBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DXT':
                        DXT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IXT':
                        IXT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BMC':
                        BMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PEPECASH':
                        PEPECASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COB':
                        COB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GRID':
                        GRID_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BITUSD':
                        BITUSD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KRM':
                        KRM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HMQ':
                        HMQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIB':
                        VIB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PPY':
                        PPY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XEL':
                        XEL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '1ST':
                        e_1ST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NLC2':
                        NLC2_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MTN':
                        MTN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'THC':
                        THC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TNC':
                        TNC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NTK':
                        NTK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COLX':
                        COLX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COV':
                        COV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DIME':
                        DIME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FOTA':
                        FOTA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LIFE':
                        LIFE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XBY':
                        XBY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MER':
                        MER_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RFR':
                        RFR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PST':
                        PST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZSC':
                        ZSC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRA':
                        PRA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CFI':
                        CFI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BIS':
                        BIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QAU':
                        QAU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LEO':
                        LEO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BRM':
                        BRM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCPT':
                        BCPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AMP':
                        AMP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TIME':
                        TIME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BITB':
                        BITB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BLT':
                        BLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LUX':
                        LUX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPC':
                        SPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ONION':
                        ONION_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RVR':
                        RVR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CEEK':
                        CEEK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRIG':
                        TRIG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LATX':
                        LATX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ACAT':
                        ACAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ALQO':
                        ALQO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MOT':
                        MOT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XSH':
                        XSH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EVX':
                        EVX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DIVX':
                        DIVX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DMT':
                        DMT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRW':
                        CRW_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MWAT':
                        MWAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UKG':
                        UKG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PASC':
                        PASC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TAU':
                        TAU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OXY':
                        OXY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OMX':
                        OMX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BBR':
                        BBR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TSL':
                        TSL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DIM':
                        DIM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRO':
                        PRO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PLBT':
                        PLBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DADI':
                        DADI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UGC':
                        UGC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DMD':
                        DMD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BLK':
                        BLK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNC':
                        SNC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BETR':
                        BETR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GRC':
                        GRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BOT':
                        BOT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FLASH':
                        FLASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TFD':
                        TFD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DBIX':
                        DBIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UQC':
                        UQC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SWTH':
                        SWTH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SKB':
                        SKB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCA':
                        BCA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SOUL':
                        SOUL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GUP':
                        GUP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MUSE':
                        MUSE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNTR':
                        SNTR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GEM':
                        GEM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LA':
                        LA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NKC':
                        NKC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MUE':
                        MUE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BPT':
                        BPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STK':
                        STK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NMR':
                        NMR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CV':
                        CV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OMNI':
                        OMNI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REM':
                        REM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HYDRO':
                        HYDRO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RBY':
                        RBY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ORME':
                        ORME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SSP':
                        SSP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EVR':
                        EVR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MTH':
                        MTH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SHND':
                        SHND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NEU':
                        NEU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RADS':
                        RADS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CAPP':
                        CAPP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STX':
                        STX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MDA':
                        MDA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RMT':
                        RMT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TIX':
                        TIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MDT':
                        MDT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SLR':
                        SLR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OAX':
                        OAX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADT':
                        ADT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FLO':
                        FLO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARN':
                        ARN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BBN':
                        BBN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MOON':
                        MOON_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CHP':
                        CHP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AIT':
                        AIT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CLO':
                        CLO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AIDOC':
                        AIDOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FDZ':
                        FDZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LOC':
                        LOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PAL':
                        PAL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IOC':
                        IOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PKC':
                        PKC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HXX':
                        HXX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UP':
                        UP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SLT':
                        SLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PAT':
                        PAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DICE':
                        DICE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EXRN':
                        EXRN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HMC':
                        HMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SENC':
                        SENC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DLT':
                        DLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GEN':
                        GEN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CHSB':
                        CHSB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ABYSS':
                        ABYSS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BQ':
                        BQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EXP':
                        EXP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EKO':
                        EKO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZIPT':
                        ZIPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CLAM':
                        CLAM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IDH':
                        IDH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SRCOIN':
                        SRCOIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ATM':
                        ATM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NYC':
                        NYC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DEV':
                        DEV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GCR':
                        GCR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NBAI':
                        NBAI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POLIS':
                        POLIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DTB':
                        DTB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CVCOIN':
                        CVCOIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MRK':
                        MRK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SHIP':
                        SHIP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INCNT':
                        INCNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HER':
                        HER_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AXP':
                        AXP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LMC':
                        LMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REBL':
                        REBL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'APH':
                        APH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DRT':
                        DRT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HKN':
                        HKN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UBT':
                        UBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XMY':
                        XMY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RVT':
                        RVT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SEXC':
                        SEXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ECOB':
                        ECOB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SIB':
                        SIB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RED':
                        RED_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ICOS':
                        ICOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPRTS':
                        SPRTS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GET':
                        GET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PCL':
                        PCL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NEOS':
                        NEOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BWK':
                        BWK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NPX':
                        NPX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DYN':
                        DYN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BEZ':
                        BEZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XST':
                        XST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IPL':
                        IPL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VRC':
                        VRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IFT':
                        IFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MUSIC':
                        MUSIC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CAT':
                        CAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LOKI':
                        LOKI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UCASH':
                        UCASH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BSD':
                        BSD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PIRL':
                        PIRL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DEB':
                        DEB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HWC':
                        HWC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NVC':
                        NVC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XAUR':
                        XAUR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FLIXX':
                        FLIXX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RMC':
                        RMC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PKT':
                        PKT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GBX':
                        GBX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NCT':
                        NCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GRFT':
                        GRFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EFX':
                        EFX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NXC':
                        NXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XPA':
                        XPA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AU':
                        AU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SS':
                        SS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'APX':
                        APX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PARETO':
                        PARETO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AIR':
                        AIR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PINK':
                        PINK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GETX':
                        GETX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZLA':
                        ZLA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LEV':
                        LEV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SWT':
                        SWT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AID':
                        AID_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TUBE':
                        TUBE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OK':
                        OK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DGTX':
                        DGTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BIO':
                        BIO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AVT':
                        AVT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MTX':
                        MTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CAG':
                        CAG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FLDC':
                        FLDC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPD':
                        SPD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CXO':
                        CXO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRG':
                        PRG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CAN':
                        CAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HBT':
                        HBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PTOY':
                        PTOY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZAP':
                        ZAP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LALA':
                        LALA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HBZ':
                        HBZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZOI':
                        ZOI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PND':
                        PND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ERO':
                        ERO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BDG':
                        BDG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADB':
                        ADB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZRC':
                        ZRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GOLOS':
                        GOLOS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DERO':
                        DERO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MINT':
                        MINT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LNC':
                        LNC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LWF':
                        LWF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DNA':
                        DNA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCC':
                        BCC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADH':
                        ADH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PUT':
                        PUT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DOT':
                        DOT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XNK':
                        XNK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SIG':
                        SIG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SENSE':
                        SENSE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MLM':
                        MLM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IDXM':
                        IDXM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FLUZ':
                        FLUZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BET':
                        BET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NET':
                        NET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BERRY':
                        BERRY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELIX':
                        ELIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRST':
                        TRST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SEQ':
                        SEQ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'YOC':
                        YOC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADI':
                        ADI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BNTY':
                        BNTY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HEAT':
                        HEAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ALIS':
                        ALIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'B2B':
                        B2B_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TGT':
                        TGT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ENRG':
                        ENRG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ESP':
                        ESP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'APR':
                        APR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MITX':
                        MITX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '1WO':
                        e_1WO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XLR':
                        XLR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XSPEC':
                        XSPEC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CBT':
                        CBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CURE':
                        CURE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CFUN':
                        CFUN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COFI':
                        COFI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CLN':
                        CLN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BEE':
                        BEE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BCY':
                        BCY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FID':
                        FID_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LDC':
                        LDC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FACE':
                        FACE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MORPH':
                        MORPH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MYST':
                        MYST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PBT':
                        PBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GLD':
                        GLD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADST':
                        ADST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LND':
                        LND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'COVAL':
                        COVAL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AUR':
                        AUR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SETH':
                        SETH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SNOV':
                        SNOV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EVE':
                        EVE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ATB':
                        ATB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TOA':
                        TOA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TFL':
                        TFL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPHR':
                        SPHR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MYB':
                        MYB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PRIX':
                        PRIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'POLL':
                        POLL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EZT':
                        EZT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WCT':
                        WCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAX':
                        MAX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CSNO':
                        CSNO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRF':
                        TRF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AVA':
                        AVA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SYNX':
                        SYNX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GLA':
                        GLA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REAL':
                        REAL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IPSX':
                        IPSX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ABY':
                        ABY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TX':
                        TX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NPER':
                        NPER_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KORE':
                        KORE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TIPS':
                        TIPS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARY':
                        ARY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIT':
                        VIT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OBITS':
                        OBITS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SHL':
                        SHL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WRC':
                        WRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SHP':
                        SHP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HQX':
                        HQX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'J8T':
                        J8T_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INXT':
                        INXT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BRX':
                        BRX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VME':
                        VME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTCZ':
                        BTCZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PTC':
                        PTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MONK':
                        MONK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HUR':
                        HUR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GEO':
                        GEO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '2GIVE':
                        e_2GIVE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ASTRO':
                        ASTRO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AUC':
                        AUC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DTH':
                        DTH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OTN':
                        OTN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BLUE':
                        BLUE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PLAY':
                        PLAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XBC':
                        XBC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FND':
                        FND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PFR':
                        PFR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HYP':
                        HYP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GCC':
                        GCC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IOP':
                        IOP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FDX':
                        FDX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ATL':
                        ATL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INSTAR':
                        INSTAR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HGT':
                        HGT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LEDU':
                        LEDU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UNIT':
                        UNIT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'USNBT':
                        USNBT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SUMO':
                        SUMO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EXY':
                        EXY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '0xBTC':
                        e_0xBTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPR':
                        SPR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ERC':
                        ERC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XHV':
                        XHV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INV':
                        INV_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CPAY':
                        CPAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IXC':
                        IXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BUZZ':
                        BUZZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BBO':
                        BBO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HAC':
                        HAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BSTN':
                        BSTN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NTRN':
                        NTRN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XMCC':
                        XMCC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SXUT':
                        SXUT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UFR':
                        UFR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SPF':
                        SPF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GMT':
                        GMT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SEND':
                        SEND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AMLT':
                        AMLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SCL':
                        SCL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QWARK':
                        QWARK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DOPE':
                        DOPE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TKS':
                        TKS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MSR':
                        MSR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FTX':
                        FTX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TKA':
                        TKA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VRM':
                        VRM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RIC':
                        RIC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PING':
                        PING_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PBL':
                        PBL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RUPX':
                        RUPX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GAT':
                        GAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZEIT':
                        ZEIT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VOISE':
                        VOISE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ING':
                        ING_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EXCL':
                        EXCL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HOLD':
                        HOLD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WISH':
                        WISH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IND':
                        IND_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MEME':
                        MEME_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ALT':
                        ALT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BON':
                        BON_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BRK':
                        BRK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EBST':
                        EBST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTDX':
                        BTDX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'I0C':
                        I0C_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRC':
                        TRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KRB':
                        KRB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SSS':
                        SSS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PURE':
                        PURE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XHI':
                        XHI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRAVE':
                        CRAVE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ORE':
                        ORE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HUSH':
                        HUSH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VTR':
                        VTR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ANC':
                        ANC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CMPCO':
                        CMPCO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ETBS':
                        ETBS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'REF':
                        REF_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DNR':
                        DNR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XGOX':
                        XGOX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CHX':
                        CHX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MVC':
                        MVC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FOR':
                        FOR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CANN':
                        CANN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIU':
                        VIU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NAVI':
                        NAVI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FYP':
                        FYP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CPY':
                        CPY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STAC':
                        STAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GENE':
                        GENE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SGR':
                        SGR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NIO':
                        NIO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PIX':
                        PIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAGE':
                        MAGE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NLX':
                        NLX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EGC':
                        EGC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CL':
                        CL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZEPH':
                        ZEPH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MFG':
                        MFG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BBP':
                        BBP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BUN':
                        BUN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PYLNT':
                        PYLNT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CDX':
                        CDX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAN':
                        DAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRAK':
                        TRAK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LDOGE':
                        LDOGE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TES':
                        TES_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FGC':
                        FGC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AIX':
                        AIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WSX':
                        WSX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAC':
                        MAC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NOBL':
                        NOBL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DP':
                        DP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LOCI':
                        LOCI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HIRE':
                        HIRE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OPC':
                        OPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GCN':
                        GCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IC':
                        IC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ACE':
                        ACE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BOUTS':
                        BOUTS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XNN':
                        XNN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CREA':
                        CREA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EFYT':
                        EFYT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XTL':
                        XTL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TEAM':
                        TEAM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XMG':
                        XMG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HUC':
                        HUC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RAIN':
                        RAIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MNTP':
                        MNTP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRCT':
                        TRCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EFL':
                        EFL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XBP':
                        XBP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTW':
                        BTW_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TZC':
                        TZC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DIX':
                        DIX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ODN':
                        ODN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STAK':
                        STAK_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FT':
                        FT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRB':
                        CRB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HAT':
                        HAT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SWIFT':
                        SWIFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZER':
                        ZER_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BYC':
                        BYC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AMM':
                        AMM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EBTC':
                        EBTC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FRST':
                        FRST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ITNS':
                        ITNS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ESZ':
                        ESZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTRN':
                        BTRN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UCOM':
                        UCOM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SKIN':
                        SKIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MAG':
                        MAG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DGC':
                        DGC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VIVO':
                        VIVO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PHO':
                        PHO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FCN':
                        FCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MRT':
                        MRT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RNS':
                        RNS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SCT':
                        SCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DAY':
                        DAY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'JEW':
                        JEW_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'JC':
                        JC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SGN':
                        SGN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADZ':
                        ADZ_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HERO':
                        HERO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TDX':
                        TDX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZNY':
                        ZNY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '808':
                        e_808_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EPY':
                        EPY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TDS':
                        TDS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UIS':
                        UIS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DTRC':
                        DTRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELLA':
                        ELLA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EBCH':
                        EBCH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UNB':
                        UNB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FYN':
                        FYN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TIG':
                        TIG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'AMN':
                        AMN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ATS':
                        ATS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DFT':
                        DFT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NOX':
                        NOX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'STU':
                        STU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EARTH':
                        EARTH_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'JIYO':
                        JIYO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MEC':
                        MEC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ORI':
                        ORI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DRPU':
                        DRPU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MORE':
                        MORE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'INN':
                        INN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EVC':
                        EVC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TNS':
                        TNS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LINX':
                        LINX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SAGA':
                        SAGA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MBI':
                        MBI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZET':
                        ZET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARC':
                        ARC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EL':
                        EL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'UNIFY':
                        UNIFY_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EQT':
                        EQT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VULC':
                        VULC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KLN':
                        KLN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QVT':
                        QVT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PLAN':
                        PLAN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VRS':
                        VRS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'IFLT':
                        IFLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTA':
                        BTA_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MCAP':
                        MCAP_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SUR':
                        SUR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HPC':
                        HPC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ELTCOIN':
                        ELTCOIN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XPD':
                        XPD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRM':
                        CRM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'RLT':
                        RLT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'WILD':
                        WILD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XTO':
                        XTO_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DGPT':
                        DGPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CJT':
                        CJT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BTB':
                        BTB_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ZBC':
                        ZBC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '1337':
                        e_1337_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == '42':
                        e_42_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GAM':
                        GAM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'KB3':
                        KB3_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NSR':
                        NSR_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRC':
                        CRC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BDL':
                        BDL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CHC':
                        CHC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'GRMD':
                        GRMD_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'MBRS':
                        MBRS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'EQL':
                        EQL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'JET':
                        JET_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BITSILVER':
                        BITSILVER_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'PIPL':
                        PIPL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XCN':
                        XCN_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'BBI':
                        BBI_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'NMS':
                        NMS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OCT':
                        OCT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'QBIC':
                        QBIC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'FANS':
                        FANS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ADC':
                        ADC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TRUST':
                        TRUST_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'VZT':
                        VZT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'TBX':
                        TBX_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'XRL':
                        XRL_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ARG':
                        ARG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SMS':
                        SMS_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'CRED':
                        CRED_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'ONG':
                        ONG_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DEW':
                        DEW_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'OPT':
                        OPT_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DOVU':
                        DOVU_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'DEM':
                        DEM_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'SXC':
                        SXC_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'HORSE':
                        HORSE_latest_val = spreads[0]['price']
                    if spreads[0]['shorthand'] == 'LIVE':
                        LIVE_latest_val = spreads[0]['price']

                    #print("for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

            # for i in range(len(pairs)):
            #     latest_vals.append(float(spreads_for_pair[pairs[i]][0]["price"]))
            # eth_latest_val = float(spreads_for_pair[pairs[1]][0]["bestbid"])
            # xrp_latest_val = float(spreads_for_pair[pairs[2]][0]["bestbid"])
            # xlm_latest_val = 0.5
    finally:
        connection.close()
    investment_created = False
    if 'investment_created' in request.session and request.session['investment_created'] == True:
        request.session['investment_created'] = False
        investment_created = True

    just_signed_up = False
    if 'just_signed_up' in request.session and request.session['just_signed_up'] == True:
        request.session['just_signed_up'] = False
        just_signed_up = True

    not_enough_usd = False
    if 'not_enough_usd' in request.session and request.session['not_enough_usd'] == True:
        request.session['not_enough_usd'] = False
        not_enough_usd = True

    tweet_embedded = False
    if 'tweet_embedded' in request.session and request.session['tweet_embedded'] == True:
        request.session['tweet_embedded'] = False
        tweet_embedded = True

    embedded_tweets = EmbeddedTweet.objects.filter(portfolio=portfolio)

    return render(request, 'app/portfolio.html', {'all_portfolios': all_portfolios, \
        'pk': pk,\
        'user': user,\
        'portfolio': portfolio,\
        'all_investments': all_investments,\
        'aum': aum,\
        'user': request.user,\
        'BTC_latest_val': BTC_latest_val, 'ETH_latest_val': ETH_latest_val, 'XRP_latest_val': XRP_latest_val, 'BCH_latest_val': BCH_latest_val, 'EOS_latest_val': EOS_latest_val, 'LTC_latest_val': LTC_latest_val, 'XLM_latest_val': XLM_latest_val, 'ADA_latest_val': ADA_latest_val, 'TRX_latest_val': TRX_latest_val, 'MIOTA_latest_val': MIOTA_latest_val, 'USDT_latest_val': USDT_latest_val, 'NEO_latest_val': NEO_latest_val, 'DASH_latest_val': DASH_latest_val, 'XMR_latest_val': XMR_latest_val, 'BNB_latest_val': BNB_latest_val, 'VEN_latest_val': VEN_latest_val, 'ETC_latest_val': ETC_latest_val, 'XEM_latest_val': XEM_latest_val, 'OMG_latest_val': OMG_latest_val, 'QTUM_latest_val': QTUM_latest_val, 'ONT_latest_val': ONT_latest_val, 'ZEC_latest_val': ZEC_latest_val, 'ICX_latest_val': ICX_latest_val, 'LSK_latest_val': LSK_latest_val, 'DCR_latest_val': DCR_latest_val, 'BCN_latest_val': BCN_latest_val, 'ZIL_latest_val': ZIL_latest_val, 'AE_latest_val': AE_latest_val, 'BTG_latest_val': BTG_latest_val, 'BTM_latest_val': BTM_latest_val, 'SC_latest_val': SC_latest_val, 'ZRX_latest_val': ZRX_latest_val, 'XVG_latest_val': XVG_latest_val, 'BTS_latest_val': BTS_latest_val, 'STEEM_latest_val': STEEM_latest_val, 'MKR_latest_val': MKR_latest_val, 'REP_latest_val': REP_latest_val, 'NANO_latest_val': NANO_latest_val, 'DOGE_latest_val': DOGE_latest_val, 'RHOC_latest_val': RHOC_latest_val, 'WAVES_latest_val': WAVES_latest_val, 'BCD_latest_val': BCD_latest_val, 'BAT_latest_val': BAT_latest_val, 'WAN_latest_val': WAN_latest_val, 'GNT_latest_val': GNT_latest_val, 'BTCP_latest_val': BTCP_latest_val, 'STRAT_latest_val': STRAT_latest_val, 'DGB_latest_val': DGB_latest_val, 'KCS_latest_val': KCS_latest_val, 'WTC_latest_val': WTC_latest_val, 'PPT_latest_val': PPT_latest_val, 'SNT_latest_val': SNT_latest_val, 'HSR_latest_val': HSR_latest_val, 'DGD_latest_val': DGD_latest_val, 'NAS_latest_val': NAS_latest_val, 'HT_latest_val': HT_latest_val, 'IOST_latest_val': IOST_latest_val, 'AION_latest_val': AION_latest_val, 'LRC_latest_val': LRC_latest_val, 'KMD_latest_val': KMD_latest_val, 'GXS_latest_val': GXS_latest_val, 'CNX_latest_val': CNX_latest_val, 'RDD_latest_val': RDD_latest_val, 'BNT_latest_val': BNT_latest_val, 'ARDR_latest_val': ARDR_latest_val, 'MAID_latest_val': MAID_latest_val, 'ARK_latest_val': ARK_latest_val, 'MOAC_latest_val': MOAC_latest_val, 'MONA_latest_val': MONA_latest_val, 'ELF_latest_val': ELF_latest_val, 'CENNZ_latest_val': CENNZ_latest_val, 'DCN_latest_val': DCN_latest_val, 'FUN_latest_val': FUN_latest_val, 'BIX_latest_val': BIX_latest_val, 'GAS_latest_val': GAS_latest_val, 'MITH_latest_val': MITH_latest_val, 'ENG_latest_val': ENG_latest_val, 'PIVX_latest_val': PIVX_latest_val, 'VERI_latest_val': VERI_latest_val, 'KNC_latest_val': KNC_latest_val, 'ELA_latest_val': ELA_latest_val, 'EMC_latest_val': EMC_latest_val, 'FSN_latest_val': FSN_latest_val, 'SYS_latest_val': SYS_latest_val, 'DROP_latest_val': DROP_latest_val, 'CMT_latest_val': CMT_latest_val, 'KIN_latest_val': KIN_latest_val, 'MANA_latest_val': MANA_latest_val, 'NXT_latest_val': NXT_latest_val, 'ETHOS_latest_val': ETHOS_latest_val, 'DDD_latest_val': DDD_latest_val, 'QASH_latest_val': QASH_latest_val, 'DRGN_latest_val': DRGN_latest_val, 'FCT_latest_val': FCT_latest_val, 'LOOM_latest_val': LOOM_latest_val, 'MTC_latest_val': MTC_latest_val, 'GTC_latest_val': GTC_latest_val, 'XZC_latest_val': XZC_latest_val, 'POLY_latest_val': POLY_latest_val, 'NULS_latest_val': NULS_latest_val, 'SMART_latest_val': SMART_latest_val, 'SUB_latest_val': SUB_latest_val, 'CTXC_latest_val': CTXC_latest_val, 'THETA_latest_val': THETA_latest_val, 'BFT_latest_val': BFT_latest_val, 'PAYX_latest_val': PAYX_latest_val, 'STORM_latest_val': STORM_latest_val, 'POWR_latest_val': POWR_latest_val, 'BLOCK_latest_val': BLOCK_latest_val, 'NXS_latest_val': NXS_latest_val, 'MCO_latest_val': MCO_latest_val, 'ETN_latest_val': ETN_latest_val, 'GBYTE_latest_val': GBYTE_latest_val, 'WAX_latest_val': WAX_latest_val, 'TUSD_latest_val': TUSD_latest_val, 'ZEN_latest_val': ZEN_latest_val, 'WICC_latest_val': WICC_latest_val, 'EOSDAC_latest_val': EOSDAC_latest_val, 'RLC_latest_val': RLC_latest_val, 'GTO_latest_val': GTO_latest_val, 'R_latest_val': R_latest_val, 'DBC_latest_val': DBC_latest_val, 'LINK_latest_val': LINK_latest_val, 'SNM_latest_val': SNM_latest_val, 'STORJ_latest_val': STORJ_latest_val, 'MAN_latest_val': MAN_latest_val, 'ICN_latest_val': ICN_latest_val, 'SALT_latest_val': SALT_latest_val, 'NEXO_latest_val': NEXO_latest_val, 'DATA_latest_val': DATA_latest_val, 'BTCD_latest_val': BTCD_latest_val, 'HOT_latest_val': HOT_latest_val, 'CVC_latest_val': CVC_latest_val, 'REQ_latest_val': REQ_latest_val, 'NCASH_latest_val': NCASH_latest_val, 'PAY_latest_val': PAY_latest_val, 'AGI_latest_val': AGI_latest_val, 'HPB_latest_val': HPB_latest_val, 'SKY_latest_val': SKY_latest_val, 'TNB_latest_val': TNB_latest_val, 'ACT_latest_val': ACT_latest_val, 'XAS_latest_val': XAS_latest_val, 'CVT_latest_val': CVT_latest_val, 'ANT_latest_val': ANT_latest_val, 'BCI_latest_val': BCI_latest_val, 'GNO_latest_val': GNO_latest_val, 'MDS_latest_val': MDS_latest_val, 'NEBL_latest_val': NEBL_latest_val, 'BTO_latest_val': BTO_latest_val, 'SAN_latest_val': SAN_latest_val, 'RUFF_latest_val': RUFF_latest_val, 'ABT_latest_val': ABT_latest_val, 'TRUE_latest_val': TRUE_latest_val, 'CND_latest_val': CND_latest_val, 'EKT_latest_val': EKT_latest_val, 'GAME_latest_val': GAME_latest_val, 'SMT_latest_val': SMT_latest_val, 'DENT_latest_val': DENT_latest_val, 'GRS_latest_val': GRS_latest_val, 'DTR_latest_val': DTR_latest_val, 'CRPT_latest_val': CRPT_latest_val, 'QSP_latest_val': QSP_latest_val, 'DAI_latest_val': DAI_latest_val, 'SOC_latest_val': SOC_latest_val, 'CS_latest_val': CS_latest_val, 'IGNIS_latest_val': IGNIS_latest_val, 'XDN_latest_val': XDN_latest_val, 'PLR_latest_val': PLR_latest_val, 'ENJ_latest_val': ENJ_latest_val, 'C20_latest_val': C20_latest_val, 'STQ_latest_val': STQ_latest_val, 'VTC_latest_val': VTC_latest_val, 'BLZ_latest_val': BLZ_latest_val, 'TKY_latest_val': TKY_latest_val, 'BOS_latest_val': BOS_latest_val, 'PART_latest_val': PART_latest_val, 'XSN_latest_val': XSN_latest_val, 'EDR_latest_val': EDR_latest_val, 'TPAY_latest_val': TPAY_latest_val, 'RDN_latest_val': RDN_latest_val, 'AMB_latest_val': AMB_latest_val, 'QKC_latest_val': QKC_latest_val, 'OCN_latest_val': OCN_latest_val, 'GNX_latest_val': GNX_latest_val, 'PPC_latest_val': PPC_latest_val, 'BRD_latest_val': BRD_latest_val, 'ODE_latest_val': ODE_latest_val, 'NKN_latest_val': NKN_latest_val, 'ZCL_latest_val': ZCL_latest_val, 'POA_latest_val': POA_latest_val, 'SRN_latest_val': SRN_latest_val, 'SPHTX_latest_val': SPHTX_latest_val, 'VEE_latest_val': VEE_latest_val, 'UBQ_latest_val': UBQ_latest_val, 'NANJ_latest_val': NANJ_latest_val, 'MTL_latest_val': MTL_latest_val, 'GVT_latest_val': GVT_latest_val, 'CPX_latest_val': CPX_latest_val, 'IOTX_latest_val': IOTX_latest_val, 'TIO_latest_val': TIO_latest_val, 'IHT_latest_val': IHT_latest_val, 'POE_latest_val': POE_latest_val, 'REN_latest_val': REN_latest_val, 'JNT_latest_val': JNT_latest_val, 'AUTO_latest_val': AUTO_latest_val, 'TEL_latest_val': TEL_latest_val, 'BTX_latest_val': BTX_latest_val, 'INT_latest_val': INT_latest_val, 'BURST_latest_val': BURST_latest_val, 'SAFEX_latest_val': SAFEX_latest_val, 'ITC_latest_val': ITC_latest_val, 'EDG_latest_val': EDG_latest_val, 'LINDA_latest_val': LINDA_latest_val, 'XPM_latest_val': XPM_latest_val, 'INK_latest_val': INK_latest_val, 'ECA_latest_val': ECA_latest_val, 'BITCNY_latest_val': BITCNY_latest_val, 'RKT_latest_val': RKT_latest_val, 'DAX_latest_val': DAX_latest_val, 'TEN_latest_val': TEN_latest_val, 'NAV_latest_val': NAV_latest_val, 'SPANK_latest_val': SPANK_latest_val, 'TRAC_latest_val': TRAC_latest_val, 'LCC_latest_val': LCC_latest_val, 'DTA_latest_val': DTA_latest_val, 'NLG_latest_val': NLG_latest_val, 'EDO_latest_val': EDO_latest_val, 'WGR_latest_val': WGR_latest_val, 'RPX_latest_val': RPX_latest_val, 'DPY_latest_val': DPY_latest_val, 'LEND_latest_val': LEND_latest_val, 'EXC_latest_val': EXC_latest_val, 'UNO_latest_val': UNO_latest_val, 'EMC2_latest_val': EMC2_latest_val, 'BAY_latest_val': BAY_latest_val, 'LYM_latest_val': LYM_latest_val, 'ADX_latest_val': ADX_latest_val, 'FTC_latest_val': FTC_latest_val, 'CPT_latest_val': CPT_latest_val, 'APIS_latest_val': APIS_latest_val, 'QRL_latest_val': QRL_latest_val, 'RVN_latest_val': RVN_latest_val, 'BAX_latest_val': BAX_latest_val, 'RNTB_latest_val': RNTB_latest_val, 'PPP_latest_val': PPP_latest_val, 'TKN_latest_val': TKN_latest_val, 'SLS_latest_val': SLS_latest_val, 'TOMO_latest_val': TOMO_latest_val, 'DATX_latest_val': DATX_latest_val, 'LGO_latest_val': LGO_latest_val, 'PZM_latest_val': PZM_latest_val, 'ETP_latest_val': ETP_latest_val, 'CLOAK_latest_val': CLOAK_latest_val, 'EVN_latest_val': EVN_latest_val, 'XCP_latest_val': XCP_latest_val, 'SWM_latest_val': SWM_latest_val, 'TNT_latest_val': TNT_latest_val, 'RCN_latest_val': RCN_latest_val, 'TCT_latest_val': TCT_latest_val, 'SWFTC_latest_val': SWFTC_latest_val, 'VIA_latest_val': VIA_latest_val, 'SNGLS_latest_val': SNGLS_latest_val, 'ZCO_latest_val': ZCO_latest_val, 'GIN_latest_val': GIN_latest_val, 'OST_latest_val': OST_latest_val, 'FXT_latest_val': FXT_latest_val, 'AST_latest_val': AST_latest_val, 'HAV_latest_val': HAV_latest_val, 'PAC_latest_val': PAC_latest_val, 'KICK_latest_val': KICK_latest_val, 'PRE_latest_val': PRE_latest_val, 'SXDT_latest_val': SXDT_latest_val, 'DNT_latest_val': DNT_latest_val, 'XWC_latest_val': XWC_latest_val, 'UTK_latest_val': UTK_latest_val, 'INS_latest_val': INS_latest_val, 'ATN_latest_val': ATN_latest_val, 'UTNP_latest_val': UTNP_latest_val, 'WINGS_latest_val': WINGS_latest_val, 'CPC_latest_val': CPC_latest_val, 'MGO_latest_val': MGO_latest_val, 'DAT_latest_val': DAT_latest_val, 'XP_latest_val': XP_latest_val, 'NGC_latest_val': NGC_latest_val, 'BCO_latest_val': BCO_latest_val, 'ZPT_latest_val': ZPT_latest_val, 'RNT_latest_val': RNT_latest_val, 'AEON_latest_val': AEON_latest_val, 'MSP_latest_val': MSP_latest_val, 'HTML_latest_val': HTML_latest_val, 'CDT_latest_val': CDT_latest_val, 'LYL_latest_val': LYL_latest_val, 'NMC_latest_val': NMC_latest_val, 'MOD_latest_val': MOD_latest_val, 'MNX_latest_val': MNX_latest_val, 'WPR_latest_val': WPR_latest_val, 'HST_latest_val': HST_latest_val, 'LBC_latest_val': LBC_latest_val, 'CREDO_latest_val': CREDO_latest_val, 'ION_latest_val': ION_latest_val, 'YOYOW_latest_val': YOYOW_latest_val, 'ART_latest_val': ART_latest_val, 'MLN_latest_val': MLN_latest_val, 'CMCT_latest_val': CMCT_latest_val, 'FUEL_latest_val': FUEL_latest_val, 'HVN_latest_val': HVN_latest_val, 'DCT_latest_val': DCT_latest_val, 'APPC_latest_val': APPC_latest_val, 'MED_latest_val': MED_latest_val, 'PHR_latest_val': PHR_latest_val, 'BANCA_latest_val': BANCA_latest_val, 'LET_latest_val': LET_latest_val, 'ECC_latest_val': ECC_latest_val, 'LUN_latest_val': LUN_latest_val, 'DAG_latest_val': DAG_latest_val, 'UUU_latest_val': UUU_latest_val, 'SBD_latest_val': SBD_latest_val, 'SENT_latest_val': SENT_latest_val, 'DBET_latest_val': DBET_latest_val, 'TAAS_latest_val': TAAS_latest_val, 'QLC_latest_val': QLC_latest_val, 'WABI_latest_val': WABI_latest_val, 'PCN_latest_val': PCN_latest_val, 'PURA_latest_val': PURA_latest_val, 'XDCE_latest_val': XDCE_latest_val, 'SSC_latest_val': SSC_latest_val, 'VIBE_latest_val': VIBE_latest_val, 'ELEC_latest_val': ELEC_latest_val, 'MEDIC_latest_val': MEDIC_latest_val, 'COSS_latest_val': COSS_latest_val, 'YEE_latest_val': YEE_latest_val, 'AURA_latest_val': AURA_latest_val, 'CSC_latest_val': CSC_latest_val, 'MOBI_latest_val': MOBI_latest_val, 'PRL_latest_val': PRL_latest_val, 'QUN_latest_val': QUN_latest_val, 'SHIFT_latest_val': SHIFT_latest_val, 'CAS_latest_val': CAS_latest_val, 'SOAR_latest_val': SOAR_latest_val, 'BITG_latest_val': BITG_latest_val, 'BKX_latest_val': BKX_latest_val, 'DOCK_latest_val': DOCK_latest_val, 'KEY_latest_val': KEY_latest_val, 'XES_latest_val': XES_latest_val, 'POT_latest_val': POT_latest_val, 'QBT_latest_val': QBT_latest_val, 'DXT_latest_val': DXT_latest_val, 'IXT_latest_val': IXT_latest_val, 'BMC_latest_val': BMC_latest_val, 'PEPECASH_latest_val': PEPECASH_latest_val, 'COB_latest_val': COB_latest_val, 'GRID_latest_val': GRID_latest_val, 'BITUSD_latest_val': BITUSD_latest_val, 'KRM_latest_val': KRM_latest_val, 'HMQ_latest_val': HMQ_latest_val, 'VIB_latest_val': VIB_latest_val, 'PPY_latest_val': PPY_latest_val, 'XEL_latest_val': XEL_latest_val, 'e_1ST_latest_val': e_1ST_latest_val, 'NLC2_latest_val': NLC2_latest_val, 'MTN_latest_val': MTN_latest_val, 'THC_latest_val': THC_latest_val, 'TNC_latest_val': TNC_latest_val, 'NTK_latest_val': NTK_latest_val, 'COLX_latest_val': COLX_latest_val, 'COV_latest_val': COV_latest_val, 'DIME_latest_val': DIME_latest_val, 'FOTA_latest_val': FOTA_latest_val, 'LIFE_latest_val': LIFE_latest_val, 'XBY_latest_val': XBY_latest_val, 'MER_latest_val': MER_latest_val, 'RFR_latest_val': RFR_latest_val, 'PST_latest_val': PST_latest_val, 'ZSC_latest_val': ZSC_latest_val, 'PRA_latest_val': PRA_latest_val, 'CFI_latest_val': CFI_latest_val, 'BIS_latest_val': BIS_latest_val, 'QAU_latest_val': QAU_latest_val, 'LEO_latest_val': LEO_latest_val, 'BRM_latest_val': BRM_latest_val, 'BCPT_latest_val': BCPT_latest_val, 'AMP_latest_val': AMP_latest_val, 'TIME_latest_val': TIME_latest_val, 'BITB_latest_val': BITB_latest_val, 'BLT_latest_val': BLT_latest_val, 'LUX_latest_val': LUX_latest_val, 'SPC_latest_val': SPC_latest_val, 'ONION_latest_val': ONION_latest_val, 'RVR_latest_val': RVR_latest_val, 'CEEK_latest_val': CEEK_latest_val, 'TRIG_latest_val': TRIG_latest_val, 'LATX_latest_val': LATX_latest_val, 'ACAT_latest_val': ACAT_latest_val, 'ALQO_latest_val': ALQO_latest_val, 'MOT_latest_val': MOT_latest_val, 'XSH_latest_val': XSH_latest_val, 'EVX_latest_val': EVX_latest_val, 'DIVX_latest_val': DIVX_latest_val, 'DMT_latest_val': DMT_latest_val, 'CRW_latest_val': CRW_latest_val, 'MWAT_latest_val': MWAT_latest_val, 'UKG_latest_val': UKG_latest_val, 'PASC_latest_val': PASC_latest_val, 'TAU_latest_val': TAU_latest_val, 'OXY_latest_val': OXY_latest_val, 'OMX_latest_val': OMX_latest_val, 'BBR_latest_val': BBR_latest_val, 'TSL_latest_val': TSL_latest_val, 'DIM_latest_val': DIM_latest_val, 'PRO_latest_val': PRO_latest_val, 'PLBT_latest_val': PLBT_latest_val, 'DADI_latest_val': DADI_latest_val, 'UGC_latest_val': UGC_latest_val, 'DMD_latest_val': DMD_latest_val, 'BLK_latest_val': BLK_latest_val, 'SNC_latest_val': SNC_latest_val, 'BETR_latest_val': BETR_latest_val, 'GRC_latest_val': GRC_latest_val, 'BOT_latest_val': BOT_latest_val, 'FLASH_latest_val': FLASH_latest_val, 'TFD_latest_val': TFD_latest_val, 'DBIX_latest_val': DBIX_latest_val, 'UQC_latest_val': UQC_latest_val, 'SWTH_latest_val': SWTH_latest_val, 'SKB_latest_val': SKB_latest_val, 'BCA_latest_val': BCA_latest_val, 'SOUL_latest_val': SOUL_latest_val, 'GUP_latest_val': GUP_latest_val, 'MUSE_latest_val': MUSE_latest_val, 'SNTR_latest_val': SNTR_latest_val, 'GEM_latest_val': GEM_latest_val, 'LA_latest_val': LA_latest_val, 'NKC_latest_val': NKC_latest_val, 'MUE_latest_val': MUE_latest_val, 'BPT_latest_val': BPT_latest_val, 'STK_latest_val': STK_latest_val, 'NMR_latest_val': NMR_latest_val, 'CV_latest_val': CV_latest_val, 'OMNI_latest_val': OMNI_latest_val, 'REM_latest_val': REM_latest_val, 'HYDRO_latest_val': HYDRO_latest_val, 'RBY_latest_val': RBY_latest_val, 'ORME_latest_val': ORME_latest_val, 'SSP_latest_val': SSP_latest_val, 'EVR_latest_val': EVR_latest_val, 'MTH_latest_val': MTH_latest_val, 'SHND_latest_val': SHND_latest_val, 'NEU_latest_val': NEU_latest_val, 'RADS_latest_val': RADS_latest_val, 'CAPP_latest_val': CAPP_latest_val, 'STX_latest_val': STX_latest_val, 'MDA_latest_val': MDA_latest_val, 'RMT_latest_val': RMT_latest_val, 'TIX_latest_val': TIX_latest_val, 'MDT_latest_val': MDT_latest_val, 'SLR_latest_val': SLR_latest_val, 'OAX_latest_val': OAX_latest_val, 'ADT_latest_val': ADT_latest_val, 'FLO_latest_val': FLO_latest_val, 'ARN_latest_val': ARN_latest_val, 'BBN_latest_val': BBN_latest_val, 'MOON_latest_val': MOON_latest_val, 'CHP_latest_val': CHP_latest_val, 'AIT_latest_val': AIT_latest_val, 'CLO_latest_val': CLO_latest_val, 'AIDOC_latest_val': AIDOC_latest_val, 'FDZ_latest_val': FDZ_latest_val, 'LOC_latest_val': LOC_latest_val, 'PAL_latest_val': PAL_latest_val, 'IOC_latest_val': IOC_latest_val, 'PKC_latest_val': PKC_latest_val, 'HXX_latest_val': HXX_latest_val, 'UP_latest_val': UP_latest_val, 'SLT_latest_val': SLT_latest_val, 'PAT_latest_val': PAT_latest_val, 'DICE_latest_val': DICE_latest_val, 'EXRN_latest_val': EXRN_latest_val, 'HMC_latest_val': HMC_latest_val, 'SENC_latest_val': SENC_latest_val, 'DLT_latest_val': DLT_latest_val, 'GEN_latest_val': GEN_latest_val, 'CHSB_latest_val': CHSB_latest_val, 'ABYSS_latest_val': ABYSS_latest_val, 'BQ_latest_val': BQ_latest_val, 'EXP_latest_val': EXP_latest_val, 'EKO_latest_val': EKO_latest_val, 'ZIPT_latest_val': ZIPT_latest_val, 'CLAM_latest_val': CLAM_latest_val, 'IDH_latest_val': IDH_latest_val, 'SRCOIN_latest_val': SRCOIN_latest_val, 'ATM_latest_val': ATM_latest_val, 'NYC_latest_val': NYC_latest_val, 'DEV_latest_val': DEV_latest_val, 'GCR_latest_val': GCR_latest_val, 'NBAI_latest_val': NBAI_latest_val, 'POLIS_latest_val': POLIS_latest_val, 'DTB_latest_val': DTB_latest_val, 'CVCOIN_latest_val': CVCOIN_latest_val, 'MRK_latest_val': MRK_latest_val, 'SHIP_latest_val': SHIP_latest_val, 'INCNT_latest_val': INCNT_latest_val, 'HER_latest_val': HER_latest_val, 'AXP_latest_val': AXP_latest_val, 'LMC_latest_val': LMC_latest_val, 'REBL_latest_val': REBL_latest_val, 'APH_latest_val': APH_latest_val, 'DRT_latest_val': DRT_latest_val, 'HKN_latest_val': HKN_latest_val, 'UBT_latest_val': UBT_latest_val, 'XMY_latest_val': XMY_latest_val, 'RVT_latest_val': RVT_latest_val, 'SEXC_latest_val': SEXC_latest_val, 'ECOB_latest_val': ECOB_latest_val, 'SIB_latest_val': SIB_latest_val, 'RED_latest_val': RED_latest_val, 'ICOS_latest_val': ICOS_latest_val, 'SPRTS_latest_val': SPRTS_latest_val, 'GET_latest_val': GET_latest_val, 'PCL_latest_val': PCL_latest_val, 'NEOS_latest_val': NEOS_latest_val, 'BWK_latest_val': BWK_latest_val, 'NPX_latest_val': NPX_latest_val, 'DYN_latest_val': DYN_latest_val, 'BEZ_latest_val': BEZ_latest_val, 'XST_latest_val': XST_latest_val, 'IPL_latest_val': IPL_latest_val, 'VRC_latest_val': VRC_latest_val, 'IFT_latest_val': IFT_latest_val, 'MUSIC_latest_val': MUSIC_latest_val, 'CAT_latest_val': CAT_latest_val, 'LOKI_latest_val': LOKI_latest_val, 'UCASH_latest_val': UCASH_latest_val, 'BSD_latest_val': BSD_latest_val, 'PIRL_latest_val': PIRL_latest_val, 'DEB_latest_val': DEB_latest_val, 'HWC_latest_val': HWC_latest_val, 'NVC_latest_val': NVC_latest_val, 'XAUR_latest_val': XAUR_latest_val, 'FLIXX_latest_val': FLIXX_latest_val, 'RMC_latest_val': RMC_latest_val, 'PKT_latest_val': PKT_latest_val, 'GBX_latest_val': GBX_latest_val, 'NCT_latest_val': NCT_latest_val, 'GRFT_latest_val': GRFT_latest_val, 'EFX_latest_val': EFX_latest_val, 'NXC_latest_val': NXC_latest_val, 'XPA_latest_val': XPA_latest_val, 'AU_latest_val': AU_latest_val, 'SS_latest_val': SS_latest_val, 'APX_latest_val': APX_latest_val, 'PARETO_latest_val': PARETO_latest_val, 'AIR_latest_val': AIR_latest_val, 'PINK_latest_val': PINK_latest_val, 'GETX_latest_val': GETX_latest_val, 'ZLA_latest_val': ZLA_latest_val, 'LEV_latest_val': LEV_latest_val, 'SWT_latest_val': SWT_latest_val, 'AID_latest_val': AID_latest_val, 'TUBE_latest_val': TUBE_latest_val, 'OK_latest_val': OK_latest_val, 'DGTX_latest_val': DGTX_latest_val, 'BIO_latest_val': BIO_latest_val, 'AVT_latest_val': AVT_latest_val, 'MTX_latest_val': MTX_latest_val, 'CAG_latest_val': CAG_latest_val, 'FLDC_latest_val': FLDC_latest_val, 'SPD_latest_val': SPD_latest_val, 'CXO_latest_val': CXO_latest_val, 'PRG_latest_val': PRG_latest_val, 'CAN_latest_val': CAN_latest_val, 'HBT_latest_val': HBT_latest_val, 'PTOY_latest_val': PTOY_latest_val, 'ZAP_latest_val': ZAP_latest_val, 'LALA_latest_val': LALA_latest_val, 'HBZ_latest_val': HBZ_latest_val, 'ZOI_latest_val': ZOI_latest_val, 'PND_latest_val': PND_latest_val, 'ERO_latest_val': ERO_latest_val, 'BDG_latest_val': BDG_latest_val, 'ADB_latest_val': ADB_latest_val, 'ZRC_latest_val': ZRC_latest_val, 'GOLOS_latest_val': GOLOS_latest_val, 'DERO_latest_val': DERO_latest_val, 'MINT_latest_val': MINT_latest_val, 'LNC_latest_val': LNC_latest_val, 'LWF_latest_val': LWF_latest_val, 'DNA_latest_val': DNA_latest_val, 'BCC_latest_val': BCC_latest_val, 'ADH_latest_val': ADH_latest_val, 'PUT_latest_val': PUT_latest_val, 'DOT_latest_val': DOT_latest_val, 'XNK_latest_val': XNK_latest_val, 'SIG_latest_val': SIG_latest_val, 'SENSE_latest_val': SENSE_latest_val, 'MLM_latest_val': MLM_latest_val, 'IDXM_latest_val': IDXM_latest_val, 'FLUZ_latest_val': FLUZ_latest_val, 'BET_latest_val': BET_latest_val, 'NET_latest_val': NET_latest_val, 'BERRY_latest_val': BERRY_latest_val, 'ELIX_latest_val': ELIX_latest_val, 'TRST_latest_val': TRST_latest_val, 'SEQ_latest_val': SEQ_latest_val, 'YOC_latest_val': YOC_latest_val, 'ADI_latest_val': ADI_latest_val, 'BNTY_latest_val': BNTY_latest_val, 'HEAT_latest_val': HEAT_latest_val, 'ALIS_latest_val': ALIS_latest_val, 'B2B_latest_val': B2B_latest_val, 'TGT_latest_val': TGT_latest_val, 'ENRG_latest_val': ENRG_latest_val, 'ESP_latest_val': ESP_latest_val, 'APR_latest_val': APR_latest_val, 'MITX_latest_val': MITX_latest_val, 'e_1WO_latest_val': e_1WO_latest_val, 'XLR_latest_val': XLR_latest_val, 'XSPEC_latest_val': XSPEC_latest_val, 'CBT_latest_val': CBT_latest_val, 'CURE_latest_val': CURE_latest_val, 'CFUN_latest_val': CFUN_latest_val, 'COFI_latest_val': COFI_latest_val, 'CLN_latest_val': CLN_latest_val, 'BEE_latest_val': BEE_latest_val, 'BCY_latest_val': BCY_latest_val, 'FID_latest_val': FID_latest_val, 'LDC_latest_val': LDC_latest_val, 'FACE_latest_val': FACE_latest_val, 'MORPH_latest_val': MORPH_latest_val, 'MYST_latest_val': MYST_latest_val, 'PBT_latest_val': PBT_latest_val, 'GLD_latest_val': GLD_latest_val, 'ADST_latest_val': ADST_latest_val, 'LND_latest_val': LND_latest_val, 'COVAL_latest_val': COVAL_latest_val, 'AUR_latest_val': AUR_latest_val, 'SETH_latest_val': SETH_latest_val, 'SNOV_latest_val': SNOV_latest_val, 'EVE_latest_val': EVE_latest_val, 'ATB_latest_val': ATB_latest_val, 'TOA_latest_val': TOA_latest_val, 'TFL_latest_val': TFL_latest_val, 'SPHR_latest_val': SPHR_latest_val, 'MYB_latest_val': MYB_latest_val, 'PRIX_latest_val': PRIX_latest_val, 'POLL_latest_val': POLL_latest_val, 'EZT_latest_val': EZT_latest_val, 'WCT_latest_val': WCT_latest_val, 'MAX_latest_val': MAX_latest_val, 'CSNO_latest_val': CSNO_latest_val, 'TRF_latest_val': TRF_latest_val, 'AVA_latest_val': AVA_latest_val, 'SYNX_latest_val': SYNX_latest_val, 'GLA_latest_val': GLA_latest_val, 'REAL_latest_val': REAL_latest_val, 'IPSX_latest_val': IPSX_latest_val, 'ABY_latest_val': ABY_latest_val, 'TX_latest_val': TX_latest_val, 'NPER_latest_val': NPER_latest_val, 'KORE_latest_val': KORE_latest_val, 'TIPS_latest_val': TIPS_latest_val, 'ARY_latest_val': ARY_latest_val, 'VIT_latest_val': VIT_latest_val, 'OBITS_latest_val': OBITS_latest_val, 'SHL_latest_val': SHL_latest_val, 'WRC_latest_val': WRC_latest_val, 'SHP_latest_val': SHP_latest_val, 'HQX_latest_val': HQX_latest_val, 'J8T_latest_val': J8T_latest_val, 'INXT_latest_val': INXT_latest_val, 'BRX_latest_val': BRX_latest_val, 'VME_latest_val': VME_latest_val, 'BTCZ_latest_val': BTCZ_latest_val, 'PTC_latest_val': PTC_latest_val, 'MONK_latest_val': MONK_latest_val, 'HUR_latest_val': HUR_latest_val, 'GEO_latest_val': GEO_latest_val, 'e_2GIVE_latest_val': e_2GIVE_latest_val, 'ASTRO_latest_val': ASTRO_latest_val, 'AUC_latest_val': AUC_latest_val, 'DTH_latest_val': DTH_latest_val, 'OTN_latest_val': OTN_latest_val, 'BLUE_latest_val': BLUE_latest_val, 'PLAY_latest_val': PLAY_latest_val, 'XBC_latest_val': XBC_latest_val, 'FND_latest_val': FND_latest_val, 'PFR_latest_val': PFR_latest_val, 'HYP_latest_val': HYP_latest_val, 'GCC_latest_val': GCC_latest_val, 'IOP_latest_val': IOP_latest_val, 'FDX_latest_val': FDX_latest_val, 'ATL_latest_val': ATL_latest_val, 'INSTAR_latest_val': INSTAR_latest_val, 'HGT_latest_val': HGT_latest_val, 'LEDU_latest_val': LEDU_latest_val, 'UNIT_latest_val': UNIT_latest_val, 'USNBT_latest_val': USNBT_latest_val, 'SUMO_latest_val': SUMO_latest_val, 'EXY_latest_val': EXY_latest_val, 'e_0xBTC_latest_val': e_0xBTC_latest_val, 'SPR_latest_val': SPR_latest_val, 'ERC_latest_val': ERC_latest_val, 'XHV_latest_val': XHV_latest_val, 'INV_latest_val': INV_latest_val, 'CPAY_latest_val': CPAY_latest_val, 'IXC_latest_val': IXC_latest_val, 'BUZZ_latest_val': BUZZ_latest_val, 'BBO_latest_val': BBO_latest_val, 'HAC_latest_val': HAC_latest_val, 'BSTN_latest_val': BSTN_latest_val, 'NTRN_latest_val': NTRN_latest_val, 'XMCC_latest_val': XMCC_latest_val, 'SXUT_latest_val': SXUT_latest_val, 'UFR_latest_val': UFR_latest_val, 'SPF_latest_val': SPF_latest_val, 'GMT_latest_val': GMT_latest_val, 'SEND_latest_val': SEND_latest_val, 'AMLT_latest_val': AMLT_latest_val, 'SCL_latest_val': SCL_latest_val, 'QWARK_latest_val': QWARK_latest_val, 'DOPE_latest_val': DOPE_latest_val, 'TKS_latest_val': TKS_latest_val, 'MSR_latest_val': MSR_latest_val, 'FTX_latest_val': FTX_latest_val, 'TKA_latest_val': TKA_latest_val, 'VRM_latest_val': VRM_latest_val, 'RIC_latest_val': RIC_latest_val, 'PING_latest_val': PING_latest_val, 'PBL_latest_val': PBL_latest_val, 'RUPX_latest_val': RUPX_latest_val, 'GAT_latest_val': GAT_latest_val, 'ZEIT_latest_val': ZEIT_latest_val, 'VOISE_latest_val': VOISE_latest_val, 'ING_latest_val': ING_latest_val, 'EXCL_latest_val': EXCL_latest_val, 'HOLD_latest_val': HOLD_latest_val, 'WISH_latest_val': WISH_latest_val, 'IND_latest_val': IND_latest_val, 'MEME_latest_val': MEME_latest_val, 'ALT_latest_val': ALT_latest_val, 'BON_latest_val': BON_latest_val, 'BRK_latest_val': BRK_latest_val, 'EBST_latest_val': EBST_latest_val, 'BTDX_latest_val': BTDX_latest_val, 'I0C_latest_val': I0C_latest_val, 'TRC_latest_val': TRC_latest_val, 'KRB_latest_val': KRB_latest_val, 'SSS_latest_val': SSS_latest_val, 'PURE_latest_val': PURE_latest_val, 'XHI_latest_val': XHI_latest_val, 'CRAVE_latest_val': CRAVE_latest_val, 'ORE_latest_val': ORE_latest_val, 'HUSH_latest_val': HUSH_latest_val, 'VTR_latest_val': VTR_latest_val, 'ANC_latest_val': ANC_latest_val, 'CMPCO_latest_val': CMPCO_latest_val, 'ETBS_latest_val': ETBS_latest_val, 'REF_latest_val': REF_latest_val, 'DNR_latest_val': DNR_latest_val, 'XGOX_latest_val': XGOX_latest_val, 'CHX_latest_val': CHX_latest_val, 'MVC_latest_val': MVC_latest_val, 'FOR_latest_val': FOR_latest_val, 'CANN_latest_val': CANN_latest_val, 'VIU_latest_val': VIU_latest_val, 'NAVI_latest_val': NAVI_latest_val, 'FYP_latest_val': FYP_latest_val, 'CPY_latest_val': CPY_latest_val, 'STAC_latest_val': STAC_latest_val, 'GENE_latest_val': GENE_latest_val, 'SGR_latest_val': SGR_latest_val, 'NIO_latest_val': NIO_latest_val, 'PIX_latest_val': PIX_latest_val, 'MAGE_latest_val': MAGE_latest_val, 'NLX_latest_val': NLX_latest_val, 'EGC_latest_val': EGC_latest_val, 'CL_latest_val': CL_latest_val, 'ZEPH_latest_val': ZEPH_latest_val, 'MFG_latest_val': MFG_latest_val, 'BBP_latest_val': BBP_latest_val, 'BUN_latest_val': BUN_latest_val, 'PYLNT_latest_val': PYLNT_latest_val, 'CDX_latest_val': CDX_latest_val, 'DAN_latest_val': DAN_latest_val, 'TRAK_latest_val': TRAK_latest_val, 'LDOGE_latest_val': LDOGE_latest_val, 'TES_latest_val': TES_latest_val, 'FGC_latest_val': FGC_latest_val, 'AIX_latest_val': AIX_latest_val, 'WSX_latest_val': WSX_latest_val, 'MAC_latest_val': MAC_latest_val, 'NOBL_latest_val': NOBL_latest_val, 'DP_latest_val': DP_latest_val, 'LOCI_latest_val': LOCI_latest_val, 'HIRE_latest_val': HIRE_latest_val, 'OPC_latest_val': OPC_latest_val, 'GCN_latest_val': GCN_latest_val, 'IC_latest_val': IC_latest_val, 'ACE_latest_val': ACE_latest_val, 'BOUTS_latest_val': BOUTS_latest_val, 'XNN_latest_val': XNN_latest_val, 'CREA_latest_val': CREA_latest_val, 'EFYT_latest_val': EFYT_latest_val, 'XTL_latest_val': XTL_latest_val, 'TEAM_latest_val': TEAM_latest_val, 'XMG_latest_val': XMG_latest_val, 'HUC_latest_val': HUC_latest_val, 'RAIN_latest_val': RAIN_latest_val, 'MNTP_latest_val': MNTP_latest_val, 'TRCT_latest_val': TRCT_latest_val, 'EFL_latest_val': EFL_latest_val, 'XBP_latest_val': XBP_latest_val, 'BTW_latest_val': BTW_latest_val, 'TZC_latest_val': TZC_latest_val, 'DIX_latest_val': DIX_latest_val, 'ODN_latest_val': ODN_latest_val, 'STAK_latest_val': STAK_latest_val, 'FT_latest_val': FT_latest_val, 'CRB_latest_val': CRB_latest_val, 'HAT_latest_val': HAT_latest_val, 'SWIFT_latest_val': SWIFT_latest_val, 'ZER_latest_val': ZER_latest_val, 'BYC_latest_val': BYC_latest_val, 'AMM_latest_val': AMM_latest_val, 'EBTC_latest_val': EBTC_latest_val, 'FRST_latest_val': FRST_latest_val, 'ITNS_latest_val': ITNS_latest_val, 'ESZ_latest_val': ESZ_latest_val, 'BTRN_latest_val': BTRN_latest_val, 'UCOM_latest_val': UCOM_latest_val, 'SKIN_latest_val': SKIN_latest_val, 'MAG_latest_val': MAG_latest_val, 'DGC_latest_val': DGC_latest_val, 'VIVO_latest_val': VIVO_latest_val, 'PHO_latest_val': PHO_latest_val, 'FCN_latest_val': FCN_latest_val, 'MRT_latest_val': MRT_latest_val, 'RNS_latest_val': RNS_latest_val, 'SCT_latest_val': SCT_latest_val, 'DAY_latest_val': DAY_latest_val, 'JEW_latest_val': JEW_latest_val, 'JC_latest_val': JC_latest_val, 'SGN_latest_val': SGN_latest_val, 'ADZ_latest_val': ADZ_latest_val, 'HERO_latest_val': HERO_latest_val, 'TDX_latest_val': TDX_latest_val, 'ZNY_latest_val': ZNY_latest_val, 'e_808_latest_val': e_808_latest_val, 'EPY_latest_val': EPY_latest_val, 'TDS_latest_val': TDS_latest_val, 'UIS_latest_val': UIS_latest_val, 'DTRC_latest_val': DTRC_latest_val, 'ELLA_latest_val': ELLA_latest_val, 'EBCH_latest_val': EBCH_latest_val, 'UNB_latest_val': UNB_latest_val, 'FYN_latest_val': FYN_latest_val, 'TIG_latest_val': TIG_latest_val, 'AMN_latest_val': AMN_latest_val, 'ATS_latest_val': ATS_latest_val, 'DFT_latest_val': DFT_latest_val, 'NOX_latest_val': NOX_latest_val, 'STU_latest_val': STU_latest_val, 'EARTH_latest_val': EARTH_latest_val, 'JIYO_latest_val': JIYO_latest_val, 'MEC_latest_val': MEC_latest_val, 'ORI_latest_val': ORI_latest_val, 'DRPU_latest_val': DRPU_latest_val, 'MORE_latest_val': MORE_latest_val, 'INN_latest_val': INN_latest_val, 'EVC_latest_val': EVC_latest_val, 'TNS_latest_val': TNS_latest_val, 'LINX_latest_val': LINX_latest_val, 'SAGA_latest_val': SAGA_latest_val, 'MBI_latest_val': MBI_latest_val, 'ZET_latest_val': ZET_latest_val, 'ARC_latest_val': ARC_latest_val, 'EL_latest_val': EL_latest_val, 'UNIFY_latest_val': UNIFY_latest_val, 'EQT_latest_val': EQT_latest_val, 'VULC_latest_val': VULC_latest_val, 'KLN_latest_val': KLN_latest_val, 'QVT_latest_val': QVT_latest_val, 'PLAN_latest_val': PLAN_latest_val, 'VRS_latest_val': VRS_latest_val, 'IFLT_latest_val': IFLT_latest_val, 'BTA_latest_val': BTA_latest_val, 'MCAP_latest_val': MCAP_latest_val, 'SUR_latest_val': SUR_latest_val, 'HPC_latest_val': HPC_latest_val, 'ELTCOIN_latest_val': ELTCOIN_latest_val, 'XPD_latest_val': XPD_latest_val, 'CRM_latest_val': CRM_latest_val, 'RLT_latest_val': RLT_latest_val, 'WILD_latest_val': WILD_latest_val, 'XTO_latest_val': XTO_latest_val, 'DGPT_latest_val': DGPT_latest_val, 'CJT_latest_val': CJT_latest_val, 'BTB_latest_val': BTB_latest_val, 'ZBC_latest_val': ZBC_latest_val, 'e_1337_latest_val': e_1337_latest_val, 'e_42_latest_val': e_42_latest_val, 'GAM_latest_val': GAM_latest_val, 'KB3_latest_val': KB3_latest_val, 'NSR_latest_val': NSR_latest_val, 'CRC_latest_val': CRC_latest_val, 'BDL_latest_val': BDL_latest_val, 'CHC_latest_val': CHC_latest_val, 'GRMD_latest_val': GRMD_latest_val, 'MBRS_latest_val': MBRS_latest_val, 'EQL_latest_val': EQL_latest_val, 'JET_latest_val': JET_latest_val, 'BITSILVER_latest_val': BITSILVER_latest_val, 'PIPL_latest_val': PIPL_latest_val, 'XCN_latest_val': XCN_latest_val, 'BBI_latest_val': BBI_latest_val, 'NMS_latest_val': NMS_latest_val, 'OCT_latest_val': OCT_latest_val, 'QBIC_latest_val': QBIC_latest_val, 'FANS_latest_val': FANS_latest_val, 'ADC_latest_val': ADC_latest_val, 'TRUST_latest_val': TRUST_latest_val, 'VZT_latest_val': VZT_latest_val, 'TBX_latest_val': TBX_latest_val, 'XRL_latest_val': XRL_latest_val, 'ARG_latest_val': ARG_latest_val, 'SMS_latest_val': SMS_latest_val, 'CRED_latest_val': CRED_latest_val, 'ONG_latest_val': ONG_latest_val, 'DEW_latest_val': DEW_latest_val, 'OPT_latest_val': OPT_latest_val, 'DOVU_latest_val': DOVU_latest_val, 'DEM_latest_val': DEM_latest_val, 'SXC_latest_val': SXC_latest_val, 'HORSE_latest_val': HORSE_latest_val, 'LIVE_latest_val': LIVE_latest_val,\
        'pairs': pairs,\
        # 'latest_vals': latest_vals,\
        'investment_created': investment_created,\
        'just_signed_up': just_signed_up,\
        'not_enough_usd': not_enough_usd,\
        'tweet_embedded': tweet_embedded,\
        'embedded_tweets': embedded_tweets\
        })

def create_investment(request, portfolio_id):
    usd_amt = float(request.GET.get('usd_amt'))
    if usd_amt > request.user.investor.usd_amt:
        request.session["not_enough_usd"] = True
        return redirect("/app/portfolio/" + str(portfolio_id))
    else:
        request.user.investor.usd_amt = float(request.user.investor.usd_amt) - usd_amt
        request.user.investor.save()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    usd_amt = request.GET.get('usd_amt')
    investment = Investment.objects.create(portfolio=portfolio,
                              original_amt=usd_amt,
                              owner=request.user,
                              is_active=False)
    from .utils import fill_investment
    fill_investment(investment, portfolio, float(usd_amt))
    request.session['investment_created'] = True

    current_site = get_current_site(request)
    mail_subject = 'New Investment Received for ' + portfolio.portfolio_name
    html_content = render_to_string('new_investment.html', {
        'investor': request.user,
        'investment': investment,
        'user': portfolio.owner,
        'domain': current_site.domain,
        'portfolio': portfolio
    })
    text_content = strip_tags(html_content)
    to_email = portfolio.owner.email
    email = EmailMultiAlternatives(mail_subject, text_content, 'info@coinium.app', to=[to_email], reply_to=['info@coinium.app'],)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("/app/portfolio/" + str(portfolio_id))

def newportfolio(request):
    success = 0
    portfolio = None
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.owner = request.user
            portfolio.save()
            success = 1
    else:
        form = PortfolioForm()
    return render(request, 'app/new_portfolio.html', {'form': form, 'success': success, 'portfolio': portfolio})

def portfolio_perf(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk = portfolio_id)
    if request.method == 'GET':
        connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='01990199',#settings.SPREADS_DB_PASSWD,
                                 db='coiniumweb',#settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                #pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD', 'XXLMZUSD']
                pairs = []
                pair_pcts = []
                (pairs, pair_pcts) = get_pairs_and_pcts(portfolio_id)
                pair_pcts = [x for x in pair_pcts]
                #pair_pcts = [float(portfolio.btc_pct) / 100.0, float(portfolio.eth_pct) / 100, float(portfolio.xrp_pct) / 100, float(portfolio.xlm_pct) / 100]
                # pair_pcts = [list_has_distributions[0]["btc"] / 100.0, list_has_distributions[0]["eth"] / 100.0, list_has_distributions[0]["xrp"] / 100.0]
                pair_first_vals = [-1 for i in range(len(pairs))]
                aggr_appreciation_in_pcts = []
                # print("list['created_at']", list['created_at'])
                #start_from_timestamp = time.mktime(datetime.datetime.strptime(list['created_at'], "%Y-%m-%d %H:%M:%S").timetuple())
                # start_from_timestamp = time.mktime(list['created_at'].timetuple())
                # print("start_from_timestamp", start_from_timestamp)
                start_from_timestamp = 1

                until = int(decimal.Decimal(time.time()))
                iteration_time = 1528060609
                #print("iteration_time", iteration_time)
                #print("until", until)
                #print("")

                spreads_for_pair = dict()
                spreads_idx_for_pair = dict()
                for pair in pairs:
                    #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                    sql = """select round(avg(price),6) as price, convert((min(created_at) div 1000)*1000, datetime) as time
from app_pricingdata where shorthand = %s and created_at >= DATE_SUB(curdate(), INTERVAL 6 WEEK)
group by created_at div 1000;"""
                    cursor.execute(sql, (pair,))
                    spreads = cursor.fetchall()
                    spreads_for_pair[pair] = spreads
                    spreads_idx_for_pair[pair] = len(spreads) - 1
                    #print("for coin ", pair, " found ", len(spreads), " spreads")

                tm = spreads_for_pair[pairs[0]][0]["time"]
                tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                appreciations = [[tmstmp, 100.0]]
                ln = 1000000000
                for i in range(len(pairs)):
                    ln = min(ln, len(spreads_for_pair[pairs[i]]))
                for i in range(1, ln):
                    appreciation = 0.0
                    for j in range(len(pairs)):
                        # hack for missing stellar pricing data
                        if j == 3 and i >= len(spreads_for_pair[pairs[j]]):
                            px = 0.5
                        else:
                            px = float(spreads_for_pair[pairs[j]][i]["price"])
                        # print ("i", i, "px", px)
                        appreciation += pair_pcts[j] * (px / float(spreads_for_pair[pairs[j]][0]["price"]))
                    tm = spreads_for_pair[pairs[0]][i]["time"]
                    tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                    appreciations.append([tmstmp, appreciation])

                # tm = spreads_for_pair[pairs[0]][0]["time"]
                # tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                # dct = {"pointStart":tmstmp,"pointInterval":60000,"dataLength":len(spreads_for_pair[pairs[0]]),"data":appreciations}
                return JsonResponse(appreciations, safe=False)
        finally:
            connection.close()
    return JsonResponse({'error': 'Unsupported method'})

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    investments = Investment.objects.filter(owner=user)
    portfolios = Portfolio.objects.filter(owner=user)
    portfolio_ids = Portfolio.objects.filter(owner=user).values_list('id', flat=True)

    total_investment_amts = [0.0 for i in range(934)]
    for investment in investments:
        i_arr = get_investment_array(investment)
        for i in range(934):
            total_investment_amts[i] += float(i_arr[i])

    # get latest valuations
    latest_prices_arr = get_latest_prices_arr(portfolio_ids)

    # for i in range(934):
    #     if latest_prices_arr[i] > 0:
    #         print("latest_prices_arr i", i, latest_prices_arr[i])
    #     if total_investment_amts[i] > 0:
    #         print("total_investment_amts i", i, total_investment_amts[i])

    total_pv_val = 0.0
    for i in range(934):
        total_pv_val += latest_prices_arr[i] * total_investment_amts[i]

    coin_pcts_array = [0.0 for i in range(934)]
    for i in range(934):
        if total_pv_val > 0:
            coin_pcts_array[i] = round(100.0 * latest_prices_arr[i] * total_investment_amts[i] / total_pv_val, 2)

    #calculate investment amounts
    investments_with_amts = []
    for investment in investments:
        amt = 0
        investments_with_amts.append([investment, amt])

    # investments made to user's portfolios for each month
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password="01990199",#settings.SPREADS_DB_PASSWD,
                                 db="coiniumweb",#settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    investment_amts_for_months = [0.0] * 13
    all_portfolios_coin_amts_for_individual_months = [[0.0 for i in range(934)] for j in range(13)]
    # end_of_month_coin_prices = [[0.0 for i in range(934)] for j in range(13)]
    latest_prices_of_month_arr = [[0.0 for i in range(934)] for j in range(13)]
    cur_month = 0
    try:
        with connection.cursor() as cursor:
            sql = "SELECT MONTH(CURDATE()) as month";
            cursor.execute(sql, ())
            cur_month = int(cursor.fetchall()[0]["month"])
            for i in range(0, 3):
                # pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
                print("portfolio_ids", portfolio_ids)
                pairs = get_all_pairs(portfolio_ids)
                spreads_for_pair = dict()
                for j in range(len(pairs)):
                    pair = pairs[j]
                    if total_investment_amts[j] > 0:
                        sql = "select * from app_pricingdata where shorthand = %s AND YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i-1) + " MONTH)) \
                                                AND MONTH(created_at) < MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i-1) + " MONTH)) order by created_at desc limit 1"
                        cursor.execute(sql, (pair))
                        spreads = cursor.fetchall()
                        spreads_for_pair[pair] = spreads
                        latest_prices_of_month_arr[cur_month - i][j] = float(spreads[0]["price"])
                        #print("2 for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

                end_of_month_amt = 0.0
                users_portfolios = Portfolio.objects.filter(owner = user)
                portfolio_ids = ["-1"]
                for p in users_portfolios:
                    portfolio_ids.append(str(p.id))
                portfolio_ids_str = ','.join(portfolio_ids)
                for investment in Investment.objects.raw("SELECT * \
                                                FROM app_investment \
                                                WHERE YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                                AND MONTH(created_at) = MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                                AND portfolio_id in (" + portfolio_ids_str + ")"):
                    inv_arr = get_investment_array(investment)
                    for k in range(934):
                        # print("k", k, "inv_arr[k]", float(inv_arr[k]), "latest_prices_of_month_arr[cur_month - i][k]", latest_prices_of_month_arr[cur_month - i][k])
                        end_of_month_amt += float(inv_arr[k]) * latest_prices_of_month_arr[cur_month - i][k]
                    for k in range(934):
                        all_portfolios_coin_amts_for_individual_months[cur_month - i][k] += float(inv_arr[k])
                    # print("after all_portfolios_coin_amts_for_individual_months", all_portfolios_coin_amts_for_individual_months)

                investment_amts_for_months[cur_month - i] = end_of_month_amt

    finally:
        connection.close()
        pass

    # user's portfolios investments and performances over months
    all_portfolios_coin_amts_till_month = [[0.0 for i in range(934)] for j in range(13)]
    end_of_month_usd_amt = [0.0 for i in range(13)]
    investment_in_month_usd_amt = [0.0 for i in range(13)]
    # print("all_portfolios_coin_amts_for_individual_months", all_portfolios_coin_amts_for_individual_months)
    for i in range(1,13):
        for k in range(934):
            all_portfolios_coin_amts_till_month[i][k] = all_portfolios_coin_amts_till_month[i-1][k] + all_portfolios_coin_amts_for_individual_months[i][k]
            end_of_month_usd_amt[i] = all_portfolios_coin_amts_till_month[i][k] * latest_prices_of_month_arr[i][k]
            investment_in_month_usd_amt[i] = all_portfolios_coin_amts_for_individual_months[i][k] * latest_prices_of_month_arr[i][k]
        #hack:
        end_of_month_usd_amt[i] -= investment_in_month_usd_amt[i]
    # print("all_portfolios_coin_amts_till_month", all_portfolios_coin_amts_till_month)
    # print("end_of_month_usd_amt", end_of_month_usd_amt)
    # print("investment_in_month_usd_amt", investment_in_month_usd_amt)

    # bottom right - all investments by user
    all_investments_by_user_in_original_usd_amt_in_month = [0 for x in range(13)]
    for i in range(0, 3):
        for investment in Investment.objects.raw("SELECT * \
                                              FROM app_investment \
                                              WHERE YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                              AND MONTH(created_at) = MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                              AND owner_id = " + str(user.id)):
            all_investments_by_user_in_original_usd_amt_in_month[cur_month - i] += investment.original_amt

    for k in range(934):
        total_investment_usd_amt = total_investment_amts[k] * latest_prices_of_month_arr[cur_month][k]
    total_investment_usd_amt = round(total_investment_usd_amt, 2)

    # portfolios with AUM
    portfolios_with_aum = []
    for i in range(len(portfolios)):
        aum = 0.0
        for investment in Investment.objects.raw("SELECT * \
                                              FROM app_investment \
                                              WHERE portfolio_id = " + str(portfolios[i].id)):
            aum += float(investment.original_amt)
        portfolios_with_aum.append([portfolios[i], aum])

    request_user = request.user;

    uploaded_file_url = False
    if 'uploaded_file_url' in request.session and request.session['uploaded_file_url']:
        uploaded_file_url = request.session['uploaded_file_url']
        request.session['uploaded_file_url'] = False

    if len(Document.objects.filter(user=request.user)):
        fs = FileSystemStorage()
        profile_pic_url = fs.url(request.user.document.document_filename)
    else:
        profile_pic_url = "https://storage.googleapis.com/indie-hackers.appspot.com/avatars/P0jgWBHyYbaC9wp1GEjGELwjsL63"

    for i in range(len(coin_pcts_array)):
        if coin_pcts_array[i] > 0:
            print("coin_pcts_array i =", i, coin_pcts_array[i])

    return render(request, 'app/profile.html', {"user": user, "request_user": request_user, "investments": investments, \
        "investments_with_amts": investments_with_amts,\
        "investment_amts_for_months": investment_amts_for_months,\
        "end_of_month_usd_amt": end_of_month_usd_amt,\
        "investment_in_month_usd_amt": investment_in_month_usd_amt,\
        "all_investments_by_user_in_original_usd_amt_in_month": all_investments_by_user_in_original_usd_amt_in_month,\
        "total_investment_usd_amt": total_investment_usd_amt,\
        "portfolios_with_aum": portfolios_with_aum,\
        "uploaded_file_url": uploaded_file_url,\
        "profile_pic_url": profile_pic_url,\
        "total_pv_val": total_pv_val,\
        # "total_btc": total_btc,\
        # "total_eth": total_eth,\
        # "total_xrp": total_xrp,\
        # "total_xlm": total_xlm,\
        "total_investment_amts": total_investment_amts,\
        # "btc_latest_val": btc_latest_val,\
        # "eth_latest_val": eth_latest_val,\
        # "xrp_latest_val": xrp_latest_val,\
        # "xlm_latest_val": xlm_latest_val,\
        "latest_prices_arr": latest_prices_arr,\
        # "btc_pct": btc_pct,\
        # "eth_pct": eth_pct,\
        # "xrp_pct": xrp_pct,\
        # "xlm_pct": xlm_pct
        "coin_pcts_array": coin_pcts_array,\
        })

def embed_tweet(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if portfolio.owner.id == request.user.id:
        url = request.GET.get('url')
        r = requests.get('https://api.twitter.com/1/statuses/oembed.json?url=' + url)
        res_json = r.json()
        EmbeddedTweet.objects.create(portfolio = portfolio,
                                     owner = request.user,
                                     url = url,
                                     embed_code = res_json['html'])
        request.session["tweet_embedded"] = True
    return redirect("/app/portfolio/" + str(portfolio_id))

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        document = Document.objects.create(user=request.user,
                                document_filename=filename)
        document.save()
        request.session["uploaded_file_url"] = uploaded_file_url
        return redirect("/app/profile/" + str(request.user.id))
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })

@background()
def fetch_prices_bg():
    # print("in fetch_prices_bg")
    from pyquery import PyQuery as pq
    url = 'https://coinmarketcap.com/all/views/all/'
    d = pq(url=url)
    res = [[] for x in range(900)]
    link_secondary = d('.link-secondary')
    for i in range(len(res)):
        shorthand = pq(link_secondary[2 * i]).html() # coin shorthand
        #res[i].append(shorthand)

        name = pq(link_secondary[2 * i + 1]).html() # coin name
        #res[i].append(name)

        mkt_cap = pq(d('.market-cap')[i]).html() # mkt cap
        mkt_cap = mkt_cap.strip()[1:]
        mkt_cap = "".join(mkt_cap.split(","))
        #res[i].append(mkt_cap)

        price = pq(d("td")[i*11+4]).text()[1:] # price
        #res[i].append(price)

        circ_supply = pq(d("td")[i*11+5]).text() # circulating supply
        circ_supply = "".join(circ_supply.split(","))
        circ_supply = circ_supply.strip("*").strip()
        circ_supply = round(float(circ_supply))
        #res[i].append(circ_supply)

        vol_24h_in_usd = pq(d("td")[i*11+6]).text()[1:] # volume 24h
        vol_24h_in_usd = "".join(vol_24h_in_usd.split(","))
        if not vol_24h_in_usd or vol_24h_in_usd == '?':
            vol_24h_in_usd = -1
        #res[i].append(vol_24h_in_usd)

        pct_1h = pq(d("td")[i*11+7]).text()[:-1] # % 1h
        pct_1h = pct_1h.strip()
        if not pct_1h or pct_1h == '?':
            pct_1h = -1
        #res[i].append(pct_1h)

        pct_24h = pq(d("td")[i*11+8]).text()[:-1] # % 24h
        pct_24h = pct_24h.strip()
        if not pct_24h or pct_24h == '?':
            pct_24h = -1
        #res[i].append(pct_24h)

        pct_7d = pq(d("td")[i*11+9]).text()[:-1] # % 7d
        pct_7d = pct_7d.strip()
        if not pct_7d or pct_7d == '?':
            pct_7d = -1
        #res[i].append(pct_7d)

        # print("shorthand", shorthand)
        # print("name", name)
        # print("mkt_cap", mkt_cap)
        # print("price", price)
        # print("circ_supply", circ_supply)
        # print("vol_24h_in_usd", vol_24h_in_usd)
        # print("pct_1h", pct_1h)
        # print("pct_24h", pct_24h)
        # print("pct_7d", pct_7d)
        # print("\n\n")
        PricingData.objects.create(shorthand = shorthand,
                                   name = name,
                                   mkt_cap = mkt_cap,
                                   price = price,
                                   circ_supply = circ_supply,
                                   vol_24h_in_usd = vol_24h_in_usd,
                                   pct_1h = pct_1h,
                                   pct_24h = pct_24h,
                                   pct_7d = pct_7d)

def fetch_prices(request):
    fetch_prices_bg(repeat=120, repeat_until=None)
    return JsonResponse({"result": "success"}, safe=False)

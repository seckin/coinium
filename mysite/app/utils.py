from .models import PricingData, Portfolio
import pymysql
import pymysql.cursors
import decimal
import time
pair_reverse_idx = {'BTC':0,'ETH':1,'XRP':2,'BCH':3,'EOS':4,'LTC':5,'XLM':6,'ADA':7,'TRX':8,'MIOTA':9,'USDT':10,'NEO':11,'DASH':12,'XMR':13,'BNB':14,'VEN':15,'ETC':16,'XEM':17,'OMG':18,'QTUM':19,'ONT':20,'ZEC':21,'ICX':22,'LSK':23,'DCR':24,'BCN':25,'ZIL':26,'AE':27,'BTG':28,'BTM':29,'SC':30,'ZRX':31,'XVG':32,'BTS':33,'STEEM':34,'MKR':35,'REP':36,'NANO':37,'DOGE':38,'RHOC':39,'WAVES':40,'BCD':41,'BAT':42,'WAN':43,'GNT':44,'BTCP':45,'STRAT':46,'DGB':47,'KCS':48,'WTC':49,'PPT':50,'SNT':51,'HSR':52,'DGD':53,'NAS':54,'HT':55,'IOST':56,'AION':57,'LRC':58,'KMD':59,'GXS':60,'CNX':61,'RDD':62,'BNT':63,'ARDR':64,'MAID':65,'ARK':66,'MOAC':67,'MONA':68,'ELF':69,'CENNZ':70,'DCN':71,'FUN':72,'BIX':73,'GAS':74,'MITH':75,'ENG':76,'PIVX':77,'VERI':78,'KNC':79,'ELA':80,'EMC':81,'FSN':82,'SYS':83,'DROP':84,'CMT':85,'KIN':86,'MANA':87,'NXT':88,'ETHOS':89,'DDD':90,'QASH':91,'DRGN':92,'FCT':93,'LOOM':94,'MTC':95,'GTC':96,'XZC':97,'POLY':98,'NULS':99,'SMART':100,'SUB':101,'CTXC':102,'THETA':103,'BFT':104,'PAYX':105,'STORM':106,'POWR':107,'BLOCK':108,'NXS':109,'MCO':110,'ETN':111,'GBYTE':112,'WAX':113,'TUSD':114,'ZEN':115,'WICC':116,'EOSDAC':117,'RLC':118,'GTO':119,'R':120,'DBC':121,'LINK':122,'SNM':123,'STORJ':124,'MAN':125,'ICN':126,'SALT':127,'NEXO':128,'DATA':129,'BTCD':130,'HOT':131,'CVC':132,'REQ':133,'NCASH':134,'PAY':135,'AGI':136,'HPB':137,'SKY':138,'TNB':139,'ACT':140,'XAS':141,'CVT':142,'ANT':143,'BCI':144,'GNO':145,'MDS':146,'NEBL':147,'BTO':148,'SAN':149,'RUFF':150,'ABT':151,'TRUE':152,'CND':153,'EKT':154,'GAME':155,'SMT':156,'DENT':157,'GRS':158,'DTR':159,'CRPT':160,'QSP':161,'DAI':162,'SOC':163,'CS':164,'IGNIS':165,'XDN':166,'PLR':167,'ENJ':168,'C20':169,'STQ':170,'VTC':171,'BLZ':172,'TKY':173,'BOS':174,'PART':175,'XSN':176,'EDR':177,'TPAY':178,'RDN':179,'AMB':180,'QKC':181,'OCN':182,'GNX':183,'PPC':184,'BRD':185,'ODE':186,'NKN':187,'ZCL':188,'POA':189,'SRN':190,'SPHTX':191,'VEE':192,'UBQ':193,'NANJ':194,'MTL':195,'GVT':196,'CPX':197,'IOTX':198,'TIO':199,'IHT':200,'POE':201,'REN':202,'JNT':203,'AUTO':204,'TEL':205,'BTX':206,'INT':207,'BURST':208,'SAFEX':209,'ITC':210,'EDG':211,'LINDA':212,'XPM':213,'INK':214,'ECA':215,'BITCNY':216,'RKT':217,'DAX':218,'TEN':219,'NAV':220,'SPANK':221,'TRAC':222,'LCC':223,'DTA':224,'NLG':225,'EDO':226,'WGR':227,'RPX':228,'DPY':229,'LEND':230,'EXC':231,'UNO':232,'EMC2':233,'BAY':234,'LYM':235,'ADX':236,'FTC':237,'CPT':238,'APIS':239,'QRL':240,'RVN':241,'BAX':242,'RNTB':243,'PPP':244,'TKN':245,'SLS':246,'TOMO':247,'DATX':248,'LGO':249,'PZM':250,'ETP':251,'CLOAK':252,'EVN':253,'XCP':254,'SWM':255,'TNT':256,'RCN':257,'TCT':258,'SWFTC':259,'VIA':260,'SNGLS':261,'ZCO':262,'GIN':263,'OST':264,'FXT':265,'AST':266,'HAV':267,'PAC':268,'KICK':269,'PRE':270,'SXDT':271,'DNT':272,'XWC':273,'UTK':274,'INS':275,'ATN':276,'UTNP':277,'WINGS':278,'CPC':279,'MGO':280,'DAT':281,'XP':282,'NGC':283,'BCO':284,'ZPT':285,'RNT':286,'AEON':287,'MSP':288,'HTML':289,'CDT':290,'LYL':291,'NMC':292,'MOD':293,'MNX':294,'WPR':295,'HST':296,'LBC':297,'CREDO':298,'ION':299,'YOYOW':300,'ART':301,'MLN':302,'CMCT':303,'FUEL':304,'HVN':305,'DCT':306,'APPC':307,'MED':308,'PHR':309,'BANCA':310,'LET':311,'ECC':312,'LUN':313,'DAG':314,'UUU':315,'SBD':316,'SENT':317,'DBET':318,'TAAS':319,'QLC':320,'WABI':321,'PCN':322,'PURA':323,'XDCE':324,'SSC':325,'VIBE':326,'ELEC':327,'MEDIC':328,'COSS':329,'YEE':330,'AURA':331,'CSC':332,'MOBI':333,'PRL':334,'QUN':335,'SHIFT':336,'CAS':337,'SOAR':338,'BITG':339,'BKX':340,'DOCK':341,'KEY':342,'XES':343,'POT':344,'QBT':345,'DXT':346,'IXT':347,'BMC':348,'PEPECASH':349,'COB':350,'GRID':351,'BITUSD':352,'KRM':353,'HMQ':354,'VIB':355,'PPY':356,'XEL':357,'1ST':358,'NLC2':359,'MTN':360,'THC':361,'TNC':362,'NTK':363,'COLX':364,'COV':365,'DIME':366,'FOTA':367,'LIFE':368,'XBY':369,'MER':370,'RFR':371,'PST':372,'ZSC':373,'PRA':374,'CFI':375,'BIS':376,'QAU':377,'LEO':378,'BRM':379,'BCPT':380,'AMP':381,'TIME':382,'BITB':383,'BLT':384,'LUX':385,'SPC':386,'ONION':387,'RVR':388,'CEEK':389,'TRIG':390,'LATX':391,'ACAT':392,'ALQO':393,'MOT':394,'XSH':395,'EVX':396,'DIVX':397,'DMT':398,'CRW':399,'MWAT':400,'UKG':401,'PASC':402,'TAU':403,'OXY':404,'OMX':405,'BBR':406,'TSL':407,'DIM':408,'PRO':409,'PLBT':410,'DADI':411,'UGC':412,'DMD':413,'BLK':414,'SNC':415,'BETR':416,'GRC':417,'BOT':418,'FLASH':419,'TFD':420,'DBIX':421,'UQC':422,'SWTH':423,'SKB':424,'BCA':425,'SOUL':426,'GUP':427,'MUSE':428,'SNTR':429,'GEM':430,'LA':431,'NKC':432,'MUE':433,'BPT':434,'STK':435,'NMR':436,'CV':437,'OMNI':438,'REM':439,'HYDRO':440,'RBY':441,'ORME':442,'SSP':443,'EVR':444,'MTH':445,'SHND':446,'NEU':447,'RADS':448,'CAPP':449,'STX':450,'MDA':451,'RMT':452,'TIX':453,'MDT':454,'SLR':455,'OAX':456,'ADT':457,'FLO':458,'ARN':459,'BBN':460,'MOON':461,'CHP':462,'AIT':463,'CLO':464,'AIDOC':465,'FDZ':466,'LOC':467,'PAL':468,'IOC':469,'PKC':470,'HXX':471,'UP':472,'SLT':473,'PAT':474,'DICE':475,'EXRN':476,'HMC':477,'SENC':478,'DLT':479,'GEN':480,'CHSB':481,'ABYSS':482,'BQ':483,'EXP':484,'EKO':485,'ZIPT':486,'CLAM':487,'IDH':488,'SRCOIN':489,'ATM':490,'NYC':491,'DEV':492,'GCR':493,'NBAI':494,'POLIS':495,'DTB':496,'CVCOIN':497,'MRK':498,'SHIP':499,'INCNT':500,'HER':501,'AXP':502,'LMC':503,'REBL':504,'APH':505,'DRT':506,'HKN':507,'UBT':508,'XMY':509,'RVT':510,'SEXC':511,'ECOB':512,'SIB':513,'RED':514,'ICOS':515,'SPRTS':516,'GET':517,'PCL':518,'NEOS':519,'BWK':520,'NPX':521,'DYN':522,'BEZ':523,'XST':524,'IPL':525,'VRC':526,'IFT':527,'MUSIC':528,'CAT':529,'LOKI':530,'UCASH':531,'BSD':532,'PIRL':533,'DEB':534,'HWC':535,'NVC':536,'XAUR':537,'FLIXX':538,'RMC':539,'PKT':540,'GBX':541,'NCT':542,'GRFT':543,'EFX':544,'NXC':545,'XPA':546,'AU':547,'SS':548,'APX':549,'PARETO':550,'AIR':551,'PINK':552,'GETX':553,'ZLA':554,'LEV':555,'SWT':556,'AID':557,'TUBE':558,'OK':559,'DGTX':560,'BIO':561,'AVT':562,'MTX':563,'CAG':564,'FLDC':565,'SPD':566,'CXO':567,'PRG':568,'CAN':569,'HBT':570,'PTOY':571,'ZAP':572,'LALA':573,'HBZ':574,'ZOI':575,'PND':576,'ERO':577,'BDG':578,'ADB':579,'ZRC':580,'GOLOS':581,'DERO':582,'MINT':583,'LNC':584,'LWF':585,'DNA':586,'BCC':587,'ADH':588,'PUT':589,'DOT':590,'XNK':591,'SIG':592,'SENSE':593,'MLM':594,'IDXM':595,'FLUZ':596,'BET':597,'NET':598,'BERRY':599,'ELIX':600,'TRST':601,'SEQ':602,'YOC':603,'ADI':604,'BNTY':605,'HEAT':606,'ALIS':607,'B2B':608,'TGT':609,'ENRG':610,'ESP':611,'APR':612,'MITX':613,'1WO':614,'XLR':615,'XSPEC':616,'CBT':617,'CURE':618,'CFUN':619,'COFI':620,'CLN':621,'BEE':622,'BCY':623,'FID':624,'LDC':625,'FACE':626,'MORPH':627,'MYST':628,'PBT':629,'GLD':630,'ADST':631,'LND':632,'COVAL':633,'AUR':634,'SETH':635,'SNOV':636,'EVE':637,'ATB':638,'TOA':639,'TFL':640,'SPHR':641,'MYB':642,'PRIX':643,'POLL':644,'EZT':645,'WCT':646,'MAX':647,'CSNO':648,'TRF':649,'AVA':650,'SYNX':651,'GLA':652,'REAL':653,'IPSX':654,'ABY':655,'TX':656,'NPER':657,'KORE':658,'TIPS':659,'ARY':660,'VIT':661,'OBITS':662,'SHL':663,'WRC':664,'SHP':665,'HQX':666,'J8T':667,'INXT':668,'BRX':669,'VME':670,'BTCZ':671,'PTC':672,'MONK':673,'HUR':674,'GEO':675,'2GIVE':676,'ASTRO':677,'AUC':678,'DTH':679,'OTN':680,'BLUE':681,'PLAY':682,'XBC':683,'FND':684,'PFR':685,'HYP':686,'GCC':687,'IOP':688,'FDX':689,'ATL':690,'INSTAR':691,'HGT':692,'LEDU':693,'UNIT':694,'USNBT':695,'SUMO':696,'EXY':697,'0xBTC':698,'SPR':699,'ERC':700,'XHV':701,'INV':702,'CPAY':703,'IXC':704,'BUZZ':705,'BBO':706,'HAC':707,'BSTN':708,'NTRN':709,'XMCC':710,'SXUT':711,'UFR':712,'SPF':713,'GMT':714,'SEND':715,'AMLT':716,'SCL':717,'QWARK':718,'DOPE':719,'TKS':720,'MSR':721,'FTX':722,'TKA':723,'VRM':724,'RIC':725,'PING':726,'PBL':727,'RUPX':728,'GAT':729,'ZEIT':730,'VOISE':731,'ING':732,'EXCL':733,'HOLD':734,'WISH':735,'IND':736,'MEME':737,'ALT':738,'BON':739,'BRK':740,'EBST':741,'BTDX':742,'I0C':743,'TRC':744,'KRB':745,'SSS':746,'PURE':747,'XHI':748,'CRAVE':749,'ORE':750,'HUSH':751,'VTR':752,'ANC':753,'CMPCO':754,'ETBS':755,'REF':756,'DNR':757,'XGOX':758,'CHX':759,'MVC':760,'FOR':761,'CANN':762,'VIU':763,'NAVI':764,'FYP':765,'CPY':766,'STAC':767,'GENE':768,'SGR':769,'NIO':770,'PIX':771,'MAGE':772,'NLX':773,'EGC':774,'CL':775,'ZEPH':776,'MFG':777,'BBP':778,'BUN':779,'PYLNT':780,'CDX':781,'DAN':782,'TRAK':783,'LDOGE':784,'TES':785,'FGC':786,'AIX':787,'WSX':788,'MAC':789,'NOBL':790,'DP':791,'LOCI':792,'HIRE':793,'OPC':794,'GCN':795,'IC':796,'ACE':797,'BOUTS':798,'XNN':799,'CREA':800,'EFYT':801,'XTL':802,'TEAM':803,'XMG':804,'HUC':805,'RAIN':806,'MNTP':807,'TRCT':808,'EFL':809,'XBP':810,'BTW':811,'TZC':812,'DIX':813,'ODN':814,'STAK':815,'FT':816,'CRB':817,'HAT':818,'SWIFT':819,'ZER':820,'BYC':821,'AMM':822,'EBTC':823,'FRST':824,'ITNS':825,'ESZ':826,'BTRN':827,'UCOM':828,'SKIN':829,'MAG':830,'DGC':831,'VIVO':832,'PHO':833,'FCN':834,'MRT':835,'RNS':836,'SCT':837,'DAY':838,'JEW':839,'JC':840,'SGN':841,'ADZ':842,'HERO':843,'TDX':844,'ZNY':845,'808':846,'EPY':847,'TDS':848,'UIS':849,'DTRC':850,'ELLA':851,'EBCH':852,'UNB':853,'FYN':854,'TIG':855,'AMN':856,'ATS':857,'DFT':858,'NOX':859,'STU':860,'EARTH':861,'JIYO':862,'MEC':863,'ORI':864,'DRPU':865,'MORE':866,'INN':867,'EVC':868,'TNS':869,'LINX':870,'SAGA':871,'MBI':872,'ZET':873,'ARC':874,'EL':875,'UNIFY':876,'EQT':877,'VULC':878,'KLN':879,'QVT':880,'PLAN':881,'VRS':882,'IFLT':883,'BTA':884,'MCAP':885,'SUR':886,'HPC':887,'ELTCOIN':888,'XPD':889,'CRM':890,'RLT':891,'WILD':892,'XTO':893,'DGPT':894,'CJT':895,'BTB':896,'ZBC':897,'1337':898,'42':899,'GAM':900,'KB3':901,'NSR':902,'CRC':903,'BDL':904,'CHC':905,'GRMD':906,'MBRS':907,'EQL':908,'JET':909,'BITSILVER':910,'PIPL':911,'XCN':912,'BBI':913,'NMS':914,'OCT':915,'QBIC':916,'FANS':917,'ADC':918,'TRUST':919,'VZT':920,'TBX':921,'XRL':922,'ARG':923,'SMS':924,'CRED':925,'ONG':926,'DEW':927,'OPT':928,'DOVU':929,'DEM':930,'SXC':931,'HORSE':932,'LIVE':933}

def get_pairs_and_pcts(portfolio_id):
    # print("portfolio_id", portfolio_id)
    portfolio = Portfolio.objects.get(pk = portfolio_id)
    pairs = []
    pair_pcts = []
    if portfolio.BTC_pct > 0.0:
        pairs.append("BTC")
        pair_pcts.append(float(portfolio.BTC_pct))
    if portfolio.ETH_pct > 0.0:
        pairs.append("ETH")
        pair_pcts.append(float(portfolio.ETH_pct))
    if portfolio.XRP_pct > 0.0:
        pairs.append("XRP")
        pair_pcts.append(float(portfolio.XRP_pct))
    if portfolio.BCH_pct > 0.0:
        pairs.append("BCH")
        pair_pcts.append(float(portfolio.BCH_pct))
    if portfolio.EOS_pct > 0.0:
        pairs.append("EOS")
        pair_pcts.append(float(portfolio.EOS_pct))
    if portfolio.LTC_pct > 0.0:
        pairs.append("LTC")
        pair_pcts.append(float(portfolio.LTC_pct))
    if portfolio.XLM_pct > 0.0:
        pairs.append("XLM")
        pair_pcts.append(float(portfolio.XLM_pct))
    if portfolio.ADA_pct > 0.0:
        pairs.append("ADA")
        pair_pcts.append(float(portfolio.ADA_pct))
    if portfolio.TRX_pct > 0.0:
        pairs.append("TRX")
        pair_pcts.append(float(portfolio.TRX_pct))
    if portfolio.MIOTA_pct > 0.0:
        pairs.append("MIOTA")
        pair_pcts.append(float(portfolio.MIOTA_pct))
    if portfolio.USDT_pct > 0.0:
        pairs.append("USDT")
        pair_pcts.append(float(portfolio.USDT_pct))
    if portfolio.NEO_pct > 0.0:
        pairs.append("NEO")
        pair_pcts.append(float(portfolio.NEO_pct))
    if portfolio.DASH_pct > 0.0:
        pairs.append("DASH")
        pair_pcts.append(float(portfolio.DASH_pct))
    if portfolio.XMR_pct > 0.0:
        pairs.append("XMR")
        pair_pcts.append(float(portfolio.XMR_pct))
    if portfolio.BNB_pct > 0.0:
        pairs.append("BNB")
        pair_pcts.append(float(portfolio.BNB_pct))
    if portfolio.VEN_pct > 0.0:
        pairs.append("VEN")
        pair_pcts.append(float(portfolio.VEN_pct))
    if portfolio.ETC_pct > 0.0:
        pairs.append("ETC")
        pair_pcts.append(float(portfolio.ETC_pct))
    if portfolio.XEM_pct > 0.0:
        pairs.append("XEM")
        pair_pcts.append(float(portfolio.XEM_pct))
    if portfolio.OMG_pct > 0.0:
        pairs.append("OMG")
        pair_pcts.append(float(portfolio.OMG_pct))
    if portfolio.QTUM_pct > 0.0:
        pairs.append("QTUM")
        pair_pcts.append(float(portfolio.QTUM_pct))
    if portfolio.ONT_pct > 0.0:
        pairs.append("ONT")
        pair_pcts.append(float(portfolio.ONT_pct))
    if portfolio.ZEC_pct > 0.0:
        pairs.append("ZEC")
        pair_pcts.append(float(portfolio.ZEC_pct))
    if portfolio.ICX_pct > 0.0:
        pairs.append("ICX")
        pair_pcts.append(float(portfolio.ICX_pct))
    if portfolio.LSK_pct > 0.0:
        pairs.append("LSK")
        pair_pcts.append(float(portfolio.LSK_pct))
    if portfolio.DCR_pct > 0.0:
        pairs.append("DCR")
        pair_pcts.append(float(portfolio.DCR_pct))
    if portfolio.BCN_pct > 0.0:
        pairs.append("BCN")
        pair_pcts.append(float(portfolio.BCN_pct))
    if portfolio.ZIL_pct > 0.0:
        pairs.append("ZIL")
        pair_pcts.append(float(portfolio.ZIL_pct))
    if portfolio.AE_pct > 0.0:
        pairs.append("AE")
        pair_pcts.append(float(portfolio.AE_pct))
    if portfolio.BTG_pct > 0.0:
        pairs.append("BTG")
        pair_pcts.append(float(portfolio.BTG_pct))
    if portfolio.BTM_pct > 0.0:
        pairs.append("BTM")
        pair_pcts.append(float(portfolio.BTM_pct))
    if portfolio.SC_pct > 0.0:
        pairs.append("SC")
        pair_pcts.append(float(portfolio.SC_pct))
    if portfolio.ZRX_pct > 0.0:
        pairs.append("ZRX")
        pair_pcts.append(float(portfolio.ZRX_pct))
    if portfolio.XVG_pct > 0.0:
        pairs.append("XVG")
        pair_pcts.append(float(portfolio.XVG_pct))
    if portfolio.BTS_pct > 0.0:
        pairs.append("BTS")
        pair_pcts.append(float(portfolio.BTS_pct))
    if portfolio.STEEM_pct > 0.0:
        pairs.append("STEEM")
        pair_pcts.append(float(portfolio.STEEM_pct))
    if portfolio.MKR_pct > 0.0:
        pairs.append("MKR")
        pair_pcts.append(float(portfolio.MKR_pct))
    if portfolio.REP_pct > 0.0:
        pairs.append("REP")
        pair_pcts.append(float(portfolio.REP_pct))
    if portfolio.NANO_pct > 0.0:
        pairs.append("NANO")
        pair_pcts.append(float(portfolio.NANO_pct))
    if portfolio.DOGE_pct > 0.0:
        pairs.append("DOGE")
        pair_pcts.append(float(portfolio.DOGE_pct))
    if portfolio.RHOC_pct > 0.0:
        pairs.append("RHOC")
        pair_pcts.append(float(portfolio.RHOC_pct))
    if portfolio.WAVES_pct > 0.0:
        pairs.append("WAVES")
        pair_pcts.append(float(portfolio.WAVES_pct))
    if portfolio.BCD_pct > 0.0:
        pairs.append("BCD")
        pair_pcts.append(float(portfolio.BCD_pct))
    if portfolio.BAT_pct > 0.0:
        pairs.append("BAT")
        pair_pcts.append(float(portfolio.BAT_pct))
    if portfolio.WAN_pct > 0.0:
        pairs.append("WAN")
        pair_pcts.append(float(portfolio.WAN_pct))
    if portfolio.GNT_pct > 0.0:
        pairs.append("GNT")
        pair_pcts.append(float(portfolio.GNT_pct))
    if portfolio.BTCP_pct > 0.0:
        pairs.append("BTCP")
        pair_pcts.append(float(portfolio.BTCP_pct))
    if portfolio.STRAT_pct > 0.0:
        pairs.append("STRAT")
        pair_pcts.append(float(portfolio.STRAT_pct))
    if portfolio.DGB_pct > 0.0:
        pairs.append("DGB")
        pair_pcts.append(float(portfolio.DGB_pct))
    if portfolio.KCS_pct > 0.0:
        pairs.append("KCS")
        pair_pcts.append(float(portfolio.KCS_pct))
    if portfolio.WTC_pct > 0.0:
        pairs.append("WTC")
        pair_pcts.append(float(portfolio.WTC_pct))
    if portfolio.PPT_pct > 0.0:
        pairs.append("PPT")
        pair_pcts.append(float(portfolio.PPT_pct))
    if portfolio.SNT_pct > 0.0:
        pairs.append("SNT")
        pair_pcts.append(float(portfolio.SNT_pct))
    if portfolio.HSR_pct > 0.0:
        pairs.append("HSR")
        pair_pcts.append(float(portfolio.HSR_pct))
    if portfolio.DGD_pct > 0.0:
        pairs.append("DGD")
        pair_pcts.append(float(portfolio.DGD_pct))
    if portfolio.NAS_pct > 0.0:
        pairs.append("NAS")
        pair_pcts.append(float(portfolio.NAS_pct))
    if portfolio.HT_pct > 0.0:
        pairs.append("HT")
        pair_pcts.append(float(portfolio.HT_pct))
    if portfolio.IOST_pct > 0.0:
        pairs.append("IOST")
        pair_pcts.append(float(portfolio.IOST_pct))
    if portfolio.AION_pct > 0.0:
        pairs.append("AION")
        pair_pcts.append(float(portfolio.AION_pct))
    if portfolio.LRC_pct > 0.0:
        pairs.append("LRC")
        pair_pcts.append(float(portfolio.LRC_pct))
    if portfolio.KMD_pct > 0.0:
        pairs.append("KMD")
        pair_pcts.append(float(portfolio.KMD_pct))
    if portfolio.GXS_pct > 0.0:
        pairs.append("GXS")
        pair_pcts.append(float(portfolio.GXS_pct))
    if portfolio.CNX_pct > 0.0:
        pairs.append("CNX")
        pair_pcts.append(float(portfolio.CNX_pct))
    if portfolio.RDD_pct > 0.0:
        pairs.append("RDD")
        pair_pcts.append(float(portfolio.RDD_pct))
    if portfolio.BNT_pct > 0.0:
        pairs.append("BNT")
        pair_pcts.append(float(portfolio.BNT_pct))
    if portfolio.ARDR_pct > 0.0:
        pairs.append("ARDR")
        pair_pcts.append(float(portfolio.ARDR_pct))
    if portfolio.MAID_pct > 0.0:
        pairs.append("MAID")
        pair_pcts.append(float(portfolio.MAID_pct))
    if portfolio.ARK_pct > 0.0:
        pairs.append("ARK")
        pair_pcts.append(float(portfolio.ARK_pct))
    if portfolio.MOAC_pct > 0.0:
        pairs.append("MOAC")
        pair_pcts.append(float(portfolio.MOAC_pct))
    if portfolio.MONA_pct > 0.0:
        pairs.append("MONA")
        pair_pcts.append(float(portfolio.MONA_pct))
    if portfolio.ELF_pct > 0.0:
        pairs.append("ELF")
        pair_pcts.append(float(portfolio.ELF_pct))
    if portfolio.CENNZ_pct > 0.0:
        pairs.append("CENNZ")
        pair_pcts.append(float(portfolio.CENNZ_pct))
    if portfolio.DCN_pct > 0.0:
        pairs.append("DCN")
        pair_pcts.append(float(portfolio.DCN_pct))
    if portfolio.FUN_pct > 0.0:
        pairs.append("FUN")
        pair_pcts.append(float(portfolio.FUN_pct))
    if portfolio.BIX_pct > 0.0:
        pairs.append("BIX")
        pair_pcts.append(float(portfolio.BIX_pct))
    if portfolio.GAS_pct > 0.0:
        pairs.append("GAS")
        pair_pcts.append(float(portfolio.GAS_pct))
    if portfolio.MITH_pct > 0.0:
        pairs.append("MITH")
        pair_pcts.append(float(portfolio.MITH_pct))
    if portfolio.ENG_pct > 0.0:
        pairs.append("ENG")
        pair_pcts.append(float(portfolio.ENG_pct))
    if portfolio.PIVX_pct > 0.0:
        pairs.append("PIVX")
        pair_pcts.append(float(portfolio.PIVX_pct))
    if portfolio.VERI_pct > 0.0:
        pairs.append("VERI")
        pair_pcts.append(float(portfolio.VERI_pct))
    if portfolio.KNC_pct > 0.0:
        pairs.append("KNC")
        pair_pcts.append(float(portfolio.KNC_pct))
    if portfolio.ELA_pct > 0.0:
        pairs.append("ELA")
        pair_pcts.append(float(portfolio.ELA_pct))
    if portfolio.EMC_pct > 0.0:
        pairs.append("EMC")
        pair_pcts.append(float(portfolio.EMC_pct))
    if portfolio.FSN_pct > 0.0:
        pairs.append("FSN")
        pair_pcts.append(float(portfolio.FSN_pct))
    if portfolio.SYS_pct > 0.0:
        pairs.append("SYS")
        pair_pcts.append(float(portfolio.SYS_pct))
    if portfolio.DROP_pct > 0.0:
        pairs.append("DROP")
        pair_pcts.append(float(portfolio.DROP_pct))
    if portfolio.CMT_pct > 0.0:
        pairs.append("CMT")
        pair_pcts.append(float(portfolio.CMT_pct))
    if portfolio.KIN_pct > 0.0:
        pairs.append("KIN")
        pair_pcts.append(float(portfolio.KIN_pct))
    if portfolio.MANA_pct > 0.0:
        pairs.append("MANA")
        pair_pcts.append(float(portfolio.MANA_pct))
    if portfolio.NXT_pct > 0.0:
        pairs.append("NXT")
        pair_pcts.append(float(portfolio.NXT_pct))
    if portfolio.ETHOS_pct > 0.0:
        pairs.append("ETHOS")
        pair_pcts.append(float(portfolio.ETHOS_pct))
    if portfolio.DDD_pct > 0.0:
        pairs.append("DDD")
        pair_pcts.append(float(portfolio.DDD_pct))
    if portfolio.QASH_pct > 0.0:
        pairs.append("QASH")
        pair_pcts.append(float(portfolio.QASH_pct))
    if portfolio.DRGN_pct > 0.0:
        pairs.append("DRGN")
        pair_pcts.append(float(portfolio.DRGN_pct))
    if portfolio.FCT_pct > 0.0:
        pairs.append("FCT")
        pair_pcts.append(float(portfolio.FCT_pct))
    if portfolio.LOOM_pct > 0.0:
        pairs.append("LOOM")
        pair_pcts.append(float(portfolio.LOOM_pct))
    if portfolio.MTC_pct > 0.0:
        pairs.append("MTC")
        pair_pcts.append(float(portfolio.MTC_pct))
    if portfolio.GTC_pct > 0.0:
        pairs.append("GTC")
        pair_pcts.append(float(portfolio.GTC_pct))
    if portfolio.XZC_pct > 0.0:
        pairs.append("XZC")
        pair_pcts.append(float(portfolio.XZC_pct))
    if portfolio.POLY_pct > 0.0:
        pairs.append("POLY")
        pair_pcts.append(float(portfolio.POLY_pct))
    if portfolio.NULS_pct > 0.0:
        pairs.append("NULS")
        pair_pcts.append(float(portfolio.NULS_pct))
    if portfolio.SMART_pct > 0.0:
        pairs.append("SMART")
        pair_pcts.append(float(portfolio.SMART_pct))
    if portfolio.SUB_pct > 0.0:
        pairs.append("SUB")
        pair_pcts.append(float(portfolio.SUB_pct))
    if portfolio.CTXC_pct > 0.0:
        pairs.append("CTXC")
        pair_pcts.append(float(portfolio.CTXC_pct))
    if portfolio.THETA_pct > 0.0:
        pairs.append("THETA")
        pair_pcts.append(float(portfolio.THETA_pct))
    if portfolio.BFT_pct > 0.0:
        pairs.append("BFT")
        pair_pcts.append(float(portfolio.BFT_pct))
    if portfolio.PAYX_pct > 0.0:
        pairs.append("PAYX")
        pair_pcts.append(float(portfolio.PAYX_pct))
    if portfolio.STORM_pct > 0.0:
        pairs.append("STORM")
        pair_pcts.append(float(portfolio.STORM_pct))
    if portfolio.POWR_pct > 0.0:
        pairs.append("POWR")
        pair_pcts.append(float(portfolio.POWR_pct))
    if portfolio.BLOCK_pct > 0.0:
        pairs.append("BLOCK")
        pair_pcts.append(float(portfolio.BLOCK_pct))
    if portfolio.NXS_pct > 0.0:
        pairs.append("NXS")
        pair_pcts.append(float(portfolio.NXS_pct))
    if portfolio.MCO_pct > 0.0:
        pairs.append("MCO")
        pair_pcts.append(float(portfolio.MCO_pct))
    if portfolio.ETN_pct > 0.0:
        pairs.append("ETN")
        pair_pcts.append(float(portfolio.ETN_pct))
    if portfolio.GBYTE_pct > 0.0:
        pairs.append("GBYTE")
        pair_pcts.append(float(portfolio.GBYTE_pct))
    if portfolio.WAX_pct > 0.0:
        pairs.append("WAX")
        pair_pcts.append(float(portfolio.WAX_pct))
    if portfolio.TUSD_pct > 0.0:
        pairs.append("TUSD")
        pair_pcts.append(float(portfolio.TUSD_pct))
    if portfolio.ZEN_pct > 0.0:
        pairs.append("ZEN")
        pair_pcts.append(float(portfolio.ZEN_pct))
    if portfolio.WICC_pct > 0.0:
        pairs.append("WICC")
        pair_pcts.append(float(portfolio.WICC_pct))
    if portfolio.EOSDAC_pct > 0.0:
        pairs.append("EOSDAC")
        pair_pcts.append(float(portfolio.EOSDAC_pct))
    if portfolio.RLC_pct > 0.0:
        pairs.append("RLC")
        pair_pcts.append(float(portfolio.RLC_pct))
    if portfolio.GTO_pct > 0.0:
        pairs.append("GTO")
        pair_pcts.append(float(portfolio.GTO_pct))
    if portfolio.R_pct > 0.0:
        pairs.append("R")
        pair_pcts.append(float(portfolio.R_pct))
    if portfolio.DBC_pct > 0.0:
        pairs.append("DBC")
        pair_pcts.append(float(portfolio.DBC_pct))
    if portfolio.LINK_pct > 0.0:
        pairs.append("LINK")
        pair_pcts.append(float(portfolio.LINK_pct))
    if portfolio.SNM_pct > 0.0:
        pairs.append("SNM")
        pair_pcts.append(float(portfolio.SNM_pct))
    if portfolio.STORJ_pct > 0.0:
        pairs.append("STORJ")
        pair_pcts.append(float(portfolio.STORJ_pct))
    if portfolio.MAN_pct > 0.0:
        pairs.append("MAN")
        pair_pcts.append(float(portfolio.MAN_pct))
    if portfolio.ICN_pct > 0.0:
        pairs.append("ICN")
        pair_pcts.append(float(portfolio.ICN_pct))
    if portfolio.SALT_pct > 0.0:
        pairs.append("SALT")
        pair_pcts.append(float(portfolio.SALT_pct))
    if portfolio.NEXO_pct > 0.0:
        pairs.append("NEXO")
        pair_pcts.append(float(portfolio.NEXO_pct))
    if portfolio.DATA_pct > 0.0:
        pairs.append("DATA")
        pair_pcts.append(float(portfolio.DATA_pct))
    if portfolio.BTCD_pct > 0.0:
        pairs.append("BTCD")
        pair_pcts.append(float(portfolio.BTCD_pct))
    if portfolio.HOT_pct > 0.0:
        pairs.append("HOT")
        pair_pcts.append(float(portfolio.HOT_pct))
    if portfolio.CVC_pct > 0.0:
        pairs.append("CVC")
        pair_pcts.append(float(portfolio.CVC_pct))
    if portfolio.REQ_pct > 0.0:
        pairs.append("REQ")
        pair_pcts.append(float(portfolio.REQ_pct))
    if portfolio.NCASH_pct > 0.0:
        pairs.append("NCASH")
        pair_pcts.append(float(portfolio.NCASH_pct))
    if portfolio.PAY_pct > 0.0:
        pairs.append("PAY")
        pair_pcts.append(float(portfolio.PAY_pct))
    if portfolio.AGI_pct > 0.0:
        pairs.append("AGI")
        pair_pcts.append(float(portfolio.AGI_pct))
    if portfolio.HPB_pct > 0.0:
        pairs.append("HPB")
        pair_pcts.append(float(portfolio.HPB_pct))
    if portfolio.SKY_pct > 0.0:
        pairs.append("SKY")
        pair_pcts.append(float(portfolio.SKY_pct))
    if portfolio.TNB_pct > 0.0:
        pairs.append("TNB")
        pair_pcts.append(float(portfolio.TNB_pct))
    if portfolio.ACT_pct > 0.0:
        pairs.append("ACT")
        pair_pcts.append(float(portfolio.ACT_pct))
    if portfolio.XAS_pct > 0.0:
        pairs.append("XAS")
        pair_pcts.append(float(portfolio.XAS_pct))
    if portfolio.CVT_pct > 0.0:
        pairs.append("CVT")
        pair_pcts.append(float(portfolio.CVT_pct))
    if portfolio.ANT_pct > 0.0:
        pairs.append("ANT")
        pair_pcts.append(float(portfolio.ANT_pct))
    if portfolio.BCI_pct > 0.0:
        pairs.append("BCI")
        pair_pcts.append(float(portfolio.BCI_pct))
    if portfolio.GNO_pct > 0.0:
        pairs.append("GNO")
        pair_pcts.append(float(portfolio.GNO_pct))
    if portfolio.MDS_pct > 0.0:
        pairs.append("MDS")
        pair_pcts.append(float(portfolio.MDS_pct))
    if portfolio.NEBL_pct > 0.0:
        pairs.append("NEBL")
        pair_pcts.append(float(portfolio.NEBL_pct))
    if portfolio.BTO_pct > 0.0:
        pairs.append("BTO")
        pair_pcts.append(float(portfolio.BTO_pct))
    if portfolio.SAN_pct > 0.0:
        pairs.append("SAN")
        pair_pcts.append(float(portfolio.SAN_pct))
    if portfolio.RUFF_pct > 0.0:
        pairs.append("RUFF")
        pair_pcts.append(float(portfolio.RUFF_pct))
    if portfolio.ABT_pct > 0.0:
        pairs.append("ABT")
        pair_pcts.append(float(portfolio.ABT_pct))
    if portfolio.TRUE_pct > 0.0:
        pairs.append("TRUE")
        pair_pcts.append(float(portfolio.TRUE_pct))
    if portfolio.CND_pct > 0.0:
        pairs.append("CND")
        pair_pcts.append(float(portfolio.CND_pct))
    if portfolio.EKT_pct > 0.0:
        pairs.append("EKT")
        pair_pcts.append(float(portfolio.EKT_pct))
    if portfolio.GAME_pct > 0.0:
        pairs.append("GAME")
        pair_pcts.append(float(portfolio.GAME_pct))
    if portfolio.SMT_pct > 0.0:
        pairs.append("SMT")
        pair_pcts.append(float(portfolio.SMT_pct))
    if portfolio.DENT_pct > 0.0:
        pairs.append("DENT")
        pair_pcts.append(float(portfolio.DENT_pct))
    if portfolio.GRS_pct > 0.0:
        pairs.append("GRS")
        pair_pcts.append(float(portfolio.GRS_pct))
    if portfolio.DTR_pct > 0.0:
        pairs.append("DTR")
        pair_pcts.append(float(portfolio.DTR_pct))
    if portfolio.CRPT_pct > 0.0:
        pairs.append("CRPT")
        pair_pcts.append(float(portfolio.CRPT_pct))
    if portfolio.QSP_pct > 0.0:
        pairs.append("QSP")
        pair_pcts.append(float(portfolio.QSP_pct))
    if portfolio.DAI_pct > 0.0:
        pairs.append("DAI")
        pair_pcts.append(float(portfolio.DAI_pct))
    if portfolio.SOC_pct > 0.0:
        pairs.append("SOC")
        pair_pcts.append(float(portfolio.SOC_pct))
    if portfolio.CS_pct > 0.0:
        pairs.append("CS")
        pair_pcts.append(float(portfolio.CS_pct))
    if portfolio.IGNIS_pct > 0.0:
        pairs.append("IGNIS")
        pair_pcts.append(float(portfolio.IGNIS_pct))
    if portfolio.XDN_pct > 0.0:
        pairs.append("XDN")
        pair_pcts.append(float(portfolio.XDN_pct))
    if portfolio.PLR_pct > 0.0:
        pairs.append("PLR")
        pair_pcts.append(float(portfolio.PLR_pct))
    if portfolio.ENJ_pct > 0.0:
        pairs.append("ENJ")
        pair_pcts.append(float(portfolio.ENJ_pct))
    if portfolio.C20_pct > 0.0:
        pairs.append("C20")
        pair_pcts.append(float(portfolio.C20_pct))
    if portfolio.STQ_pct > 0.0:
        pairs.append("STQ")
        pair_pcts.append(float(portfolio.STQ_pct))
    if portfolio.VTC_pct > 0.0:
        pairs.append("VTC")
        pair_pcts.append(float(portfolio.VTC_pct))
    if portfolio.BLZ_pct > 0.0:
        pairs.append("BLZ")
        pair_pcts.append(float(portfolio.BLZ_pct))
    if portfolio.TKY_pct > 0.0:
        pairs.append("TKY")
        pair_pcts.append(float(portfolio.TKY_pct))
    if portfolio.BOS_pct > 0.0:
        pairs.append("BOS")
        pair_pcts.append(float(portfolio.BOS_pct))
    if portfolio.PART_pct > 0.0:
        pairs.append("PART")
        pair_pcts.append(float(portfolio.PART_pct))
    if portfolio.XSN_pct > 0.0:
        pairs.append("XSN")
        pair_pcts.append(float(portfolio.XSN_pct))
    if portfolio.EDR_pct > 0.0:
        pairs.append("EDR")
        pair_pcts.append(float(portfolio.EDR_pct))
    if portfolio.TPAY_pct > 0.0:
        pairs.append("TPAY")
        pair_pcts.append(float(portfolio.TPAY_pct))
    if portfolio.RDN_pct > 0.0:
        pairs.append("RDN")
        pair_pcts.append(float(portfolio.RDN_pct))
    if portfolio.AMB_pct > 0.0:
        pairs.append("AMB")
        pair_pcts.append(float(portfolio.AMB_pct))
    if portfolio.QKC_pct > 0.0:
        pairs.append("QKC")
        pair_pcts.append(float(portfolio.QKC_pct))
    if portfolio.OCN_pct > 0.0:
        pairs.append("OCN")
        pair_pcts.append(float(portfolio.OCN_pct))
    if portfolio.GNX_pct > 0.0:
        pairs.append("GNX")
        pair_pcts.append(float(portfolio.GNX_pct))
    if portfolio.PPC_pct > 0.0:
        pairs.append("PPC")
        pair_pcts.append(float(portfolio.PPC_pct))
    if portfolio.BRD_pct > 0.0:
        pairs.append("BRD")
        pair_pcts.append(float(portfolio.BRD_pct))
    if portfolio.ODE_pct > 0.0:
        pairs.append("ODE")
        pair_pcts.append(float(portfolio.ODE_pct))
    if portfolio.NKN_pct > 0.0:
        pairs.append("NKN")
        pair_pcts.append(float(portfolio.NKN_pct))
    if portfolio.ZCL_pct > 0.0:
        pairs.append("ZCL")
        pair_pcts.append(float(portfolio.ZCL_pct))
    if portfolio.POA_pct > 0.0:
        pairs.append("POA")
        pair_pcts.append(float(portfolio.POA_pct))
    if portfolio.SRN_pct > 0.0:
        pairs.append("SRN")
        pair_pcts.append(float(portfolio.SRN_pct))
    if portfolio.SPHTX_pct > 0.0:
        pairs.append("SPHTX")
        pair_pcts.append(float(portfolio.SPHTX_pct))
    if portfolio.VEE_pct > 0.0:
        pairs.append("VEE")
        pair_pcts.append(float(portfolio.VEE_pct))
    if portfolio.UBQ_pct > 0.0:
        pairs.append("UBQ")
        pair_pcts.append(float(portfolio.UBQ_pct))
    if portfolio.NANJ_pct > 0.0:
        pairs.append("NANJ")
        pair_pcts.append(float(portfolio.NANJ_pct))
    if portfolio.MTL_pct > 0.0:
        pairs.append("MTL")
        pair_pcts.append(float(portfolio.MTL_pct))
    if portfolio.GVT_pct > 0.0:
        pairs.append("GVT")
        pair_pcts.append(float(portfolio.GVT_pct))
    if portfolio.CPX_pct > 0.0:
        pairs.append("CPX")
        pair_pcts.append(float(portfolio.CPX_pct))
    if portfolio.IOTX_pct > 0.0:
        pairs.append("IOTX")
        pair_pcts.append(float(portfolio.IOTX_pct))
    if portfolio.TIO_pct > 0.0:
        pairs.append("TIO")
        pair_pcts.append(float(portfolio.TIO_pct))
    if portfolio.IHT_pct > 0.0:
        pairs.append("IHT")
        pair_pcts.append(float(portfolio.IHT_pct))
    if portfolio.POE_pct > 0.0:
        pairs.append("POE")
        pair_pcts.append(float(portfolio.POE_pct))
    if portfolio.REN_pct > 0.0:
        pairs.append("REN")
        pair_pcts.append(float(portfolio.REN_pct))
    if portfolio.JNT_pct > 0.0:
        pairs.append("JNT")
        pair_pcts.append(float(portfolio.JNT_pct))
    if portfolio.AUTO_pct > 0.0:
        pairs.append("AUTO")
        pair_pcts.append(float(portfolio.AUTO_pct))
    if portfolio.TEL_pct > 0.0:
        pairs.append("TEL")
        pair_pcts.append(float(portfolio.TEL_pct))
    if portfolio.BTX_pct > 0.0:
        pairs.append("BTX")
        pair_pcts.append(float(portfolio.BTX_pct))
    if portfolio.INT_pct > 0.0:
        pairs.append("INT")
        pair_pcts.append(float(portfolio.INT_pct))
    if portfolio.BURST_pct > 0.0:
        pairs.append("BURST")
        pair_pcts.append(float(portfolio.BURST_pct))
    if portfolio.SAFEX_pct > 0.0:
        pairs.append("SAFEX")
        pair_pcts.append(float(portfolio.SAFEX_pct))
    if portfolio.ITC_pct > 0.0:
        pairs.append("ITC")
        pair_pcts.append(float(portfolio.ITC_pct))
    if portfolio.EDG_pct > 0.0:
        pairs.append("EDG")
        pair_pcts.append(float(portfolio.EDG_pct))
    if portfolio.LINDA_pct > 0.0:
        pairs.append("LINDA")
        pair_pcts.append(float(portfolio.LINDA_pct))
    if portfolio.XPM_pct > 0.0:
        pairs.append("XPM")
        pair_pcts.append(float(portfolio.XPM_pct))
    if portfolio.INK_pct > 0.0:
        pairs.append("INK")
        pair_pcts.append(float(portfolio.INK_pct))
    if portfolio.ECA_pct > 0.0:
        pairs.append("ECA")
        pair_pcts.append(float(portfolio.ECA_pct))
    if portfolio.BITCNY_pct > 0.0:
        pairs.append("BITCNY")
        pair_pcts.append(float(portfolio.BITCNY_pct))
    if portfolio.RKT_pct > 0.0:
        pairs.append("RKT")
        pair_pcts.append(float(portfolio.RKT_pct))
    if portfolio.DAX_pct > 0.0:
        pairs.append("DAX")
        pair_pcts.append(float(portfolio.DAX_pct))
    if portfolio.TEN_pct > 0.0:
        pairs.append("TEN")
        pair_pcts.append(float(portfolio.TEN_pct))
    if portfolio.NAV_pct > 0.0:
        pairs.append("NAV")
        pair_pcts.append(float(portfolio.NAV_pct))
    if portfolio.SPANK_pct > 0.0:
        pairs.append("SPANK")
        pair_pcts.append(float(portfolio.SPANK_pct))
    if portfolio.TRAC_pct > 0.0:
        pairs.append("TRAC")
        pair_pcts.append(float(portfolio.TRAC_pct))
    if portfolio.LCC_pct > 0.0:
        pairs.append("LCC")
        pair_pcts.append(float(portfolio.LCC_pct))
    if portfolio.DTA_pct > 0.0:
        pairs.append("DTA")
        pair_pcts.append(float(portfolio.DTA_pct))
    if portfolio.NLG_pct > 0.0:
        pairs.append("NLG")
        pair_pcts.append(float(portfolio.NLG_pct))
    if portfolio.EDO_pct > 0.0:
        pairs.append("EDO")
        pair_pcts.append(float(portfolio.EDO_pct))
    if portfolio.WGR_pct > 0.0:
        pairs.append("WGR")
        pair_pcts.append(float(portfolio.WGR_pct))
    if portfolio.RPX_pct > 0.0:
        pairs.append("RPX")
        pair_pcts.append(float(portfolio.RPX_pct))
    if portfolio.DPY_pct > 0.0:
        pairs.append("DPY")
        pair_pcts.append(float(portfolio.DPY_pct))
    if portfolio.LEND_pct > 0.0:
        pairs.append("LEND")
        pair_pcts.append(float(portfolio.LEND_pct))
    if portfolio.EXC_pct > 0.0:
        pairs.append("EXC")
        pair_pcts.append(float(portfolio.EXC_pct))
    if portfolio.UNO_pct > 0.0:
        pairs.append("UNO")
        pair_pcts.append(float(portfolio.UNO_pct))
    if portfolio.EMC2_pct > 0.0:
        pairs.append("EMC2")
        pair_pcts.append(float(portfolio.EMC2_pct))
    if portfolio.BAY_pct > 0.0:
        pairs.append("BAY")
        pair_pcts.append(float(portfolio.BAY_pct))
    if portfolio.LYM_pct > 0.0:
        pairs.append("LYM")
        pair_pcts.append(float(portfolio.LYM_pct))
    if portfolio.ADX_pct > 0.0:
        pairs.append("ADX")
        pair_pcts.append(float(portfolio.ADX_pct))
    if portfolio.FTC_pct > 0.0:
        pairs.append("FTC")
        pair_pcts.append(float(portfolio.FTC_pct))
    if portfolio.CPT_pct > 0.0:
        pairs.append("CPT")
        pair_pcts.append(float(portfolio.CPT_pct))
    if portfolio.APIS_pct > 0.0:
        pairs.append("APIS")
        pair_pcts.append(float(portfolio.APIS_pct))
    if portfolio.QRL_pct > 0.0:
        pairs.append("QRL")
        pair_pcts.append(float(portfolio.QRL_pct))
    if portfolio.RVN_pct > 0.0:
        pairs.append("RVN")
        pair_pcts.append(float(portfolio.RVN_pct))
    if portfolio.BAX_pct > 0.0:
        pairs.append("BAX")
        pair_pcts.append(float(portfolio.BAX_pct))
    if portfolio.RNTB_pct > 0.0:
        pairs.append("RNTB")
        pair_pcts.append(float(portfolio.RNTB_pct))
    if portfolio.PPP_pct > 0.0:
        pairs.append("PPP")
        pair_pcts.append(float(portfolio.PPP_pct))
    if portfolio.TKN_pct > 0.0:
        pairs.append("TKN")
        pair_pcts.append(float(portfolio.TKN_pct))
    if portfolio.SLS_pct > 0.0:
        pairs.append("SLS")
        pair_pcts.append(float(portfolio.SLS_pct))
    if portfolio.TOMO_pct > 0.0:
        pairs.append("TOMO")
        pair_pcts.append(float(portfolio.TOMO_pct))
    if portfolio.DATX_pct > 0.0:
        pairs.append("DATX")
        pair_pcts.append(float(portfolio.DATX_pct))
    if portfolio.LGO_pct > 0.0:
        pairs.append("LGO")
        pair_pcts.append(float(portfolio.LGO_pct))
    if portfolio.PZM_pct > 0.0:
        pairs.append("PZM")
        pair_pcts.append(float(portfolio.PZM_pct))
    if portfolio.ETP_pct > 0.0:
        pairs.append("ETP")
        pair_pcts.append(float(portfolio.ETP_pct))
    if portfolio.CLOAK_pct > 0.0:
        pairs.append("CLOAK")
        pair_pcts.append(float(portfolio.CLOAK_pct))
    if portfolio.EVN_pct > 0.0:
        pairs.append("EVN")
        pair_pcts.append(float(portfolio.EVN_pct))
    if portfolio.XCP_pct > 0.0:
        pairs.append("XCP")
        pair_pcts.append(float(portfolio.XCP_pct))
    if portfolio.SWM_pct > 0.0:
        pairs.append("SWM")
        pair_pcts.append(float(portfolio.SWM_pct))
    if portfolio.TNT_pct > 0.0:
        pairs.append("TNT")
        pair_pcts.append(float(portfolio.TNT_pct))
    if portfolio.RCN_pct > 0.0:
        pairs.append("RCN")
        pair_pcts.append(float(portfolio.RCN_pct))
    if portfolio.TCT_pct > 0.0:
        pairs.append("TCT")
        pair_pcts.append(float(portfolio.TCT_pct))
    if portfolio.SWFTC_pct > 0.0:
        pairs.append("SWFTC")
        pair_pcts.append(float(portfolio.SWFTC_pct))
    if portfolio.VIA_pct > 0.0:
        pairs.append("VIA")
        pair_pcts.append(float(portfolio.VIA_pct))
    if portfolio.SNGLS_pct > 0.0:
        pairs.append("SNGLS")
        pair_pcts.append(float(portfolio.SNGLS_pct))
    if portfolio.ZCO_pct > 0.0:
        pairs.append("ZCO")
        pair_pcts.append(float(portfolio.ZCO_pct))
    if portfolio.GIN_pct > 0.0:
        pairs.append("GIN")
        pair_pcts.append(float(portfolio.GIN_pct))
    if portfolio.OST_pct > 0.0:
        pairs.append("OST")
        pair_pcts.append(float(portfolio.OST_pct))
    if portfolio.FXT_pct > 0.0:
        pairs.append("FXT")
        pair_pcts.append(float(portfolio.FXT_pct))
    if portfolio.AST_pct > 0.0:
        pairs.append("AST")
        pair_pcts.append(float(portfolio.AST_pct))
    if portfolio.HAV_pct > 0.0:
        pairs.append("HAV")
        pair_pcts.append(float(portfolio.HAV_pct))
    if portfolio.PAC_pct > 0.0:
        pairs.append("PAC")
        pair_pcts.append(float(portfolio.PAC_pct))
    if portfolio.KICK_pct > 0.0:
        pairs.append("KICK")
        pair_pcts.append(float(portfolio.KICK_pct))
    if portfolio.PRE_pct > 0.0:
        pairs.append("PRE")
        pair_pcts.append(float(portfolio.PRE_pct))
    if portfolio.SXDT_pct > 0.0:
        pairs.append("SXDT")
        pair_pcts.append(float(portfolio.SXDT_pct))
    if portfolio.DNT_pct > 0.0:
        pairs.append("DNT")
        pair_pcts.append(float(portfolio.DNT_pct))
    if portfolio.XWC_pct > 0.0:
        pairs.append("XWC")
        pair_pcts.append(float(portfolio.XWC_pct))
    if portfolio.UTK_pct > 0.0:
        pairs.append("UTK")
        pair_pcts.append(float(portfolio.UTK_pct))
    if portfolio.INS_pct > 0.0:
        pairs.append("INS")
        pair_pcts.append(float(portfolio.INS_pct))
    if portfolio.ATN_pct > 0.0:
        pairs.append("ATN")
        pair_pcts.append(float(portfolio.ATN_pct))
    if portfolio.UTNP_pct > 0.0:
        pairs.append("UTNP")
        pair_pcts.append(float(portfolio.UTNP_pct))
    if portfolio.WINGS_pct > 0.0:
        pairs.append("WINGS")
        pair_pcts.append(float(portfolio.WINGS_pct))
    if portfolio.CPC_pct > 0.0:
        pairs.append("CPC")
        pair_pcts.append(float(portfolio.CPC_pct))
    if portfolio.MGO_pct > 0.0:
        pairs.append("MGO")
        pair_pcts.append(float(portfolio.MGO_pct))
    if portfolio.DAT_pct > 0.0:
        pairs.append("DAT")
        pair_pcts.append(float(portfolio.DAT_pct))
    if portfolio.XP_pct > 0.0:
        pairs.append("XP")
        pair_pcts.append(float(portfolio.XP_pct))
    if portfolio.NGC_pct > 0.0:
        pairs.append("NGC")
        pair_pcts.append(float(portfolio.NGC_pct))
    if portfolio.BCO_pct > 0.0:
        pairs.append("BCO")
        pair_pcts.append(float(portfolio.BCO_pct))
    if portfolio.ZPT_pct > 0.0:
        pairs.append("ZPT")
        pair_pcts.append(float(portfolio.ZPT_pct))
    if portfolio.RNT_pct > 0.0:
        pairs.append("RNT")
        pair_pcts.append(float(portfolio.RNT_pct))
    if portfolio.AEON_pct > 0.0:
        pairs.append("AEON")
        pair_pcts.append(float(portfolio.AEON_pct))
    if portfolio.MSP_pct > 0.0:
        pairs.append("MSP")
        pair_pcts.append(float(portfolio.MSP_pct))
    if portfolio.HTML_pct > 0.0:
        pairs.append("HTML")
        pair_pcts.append(float(portfolio.HTML_pct))
    if portfolio.CDT_pct > 0.0:
        pairs.append("CDT")
        pair_pcts.append(float(portfolio.CDT_pct))
    if portfolio.LYL_pct > 0.0:
        pairs.append("LYL")
        pair_pcts.append(float(portfolio.LYL_pct))
    if portfolio.NMC_pct > 0.0:
        pairs.append("NMC")
        pair_pcts.append(float(portfolio.NMC_pct))
    if portfolio.MOD_pct > 0.0:
        pairs.append("MOD")
        pair_pcts.append(float(portfolio.MOD_pct))
    if portfolio.MNX_pct > 0.0:
        pairs.append("MNX")
        pair_pcts.append(float(portfolio.MNX_pct))
    if portfolio.WPR_pct > 0.0:
        pairs.append("WPR")
        pair_pcts.append(float(portfolio.WPR_pct))
    if portfolio.HST_pct > 0.0:
        pairs.append("HST")
        pair_pcts.append(float(portfolio.HST_pct))
    if portfolio.LBC_pct > 0.0:
        pairs.append("LBC")
        pair_pcts.append(float(portfolio.LBC_pct))
    if portfolio.CREDO_pct > 0.0:
        pairs.append("CREDO")
        pair_pcts.append(float(portfolio.CREDO_pct))
    if portfolio.ION_pct > 0.0:
        pairs.append("ION")
        pair_pcts.append(float(portfolio.ION_pct))
    if portfolio.YOYOW_pct > 0.0:
        pairs.append("YOYOW")
        pair_pcts.append(float(portfolio.YOYOW_pct))
    if portfolio.ART_pct > 0.0:
        pairs.append("ART")
        pair_pcts.append(float(portfolio.ART_pct))
    if portfolio.MLN_pct > 0.0:
        pairs.append("MLN")
        pair_pcts.append(float(portfolio.MLN_pct))
    if portfolio.CMCT_pct > 0.0:
        pairs.append("CMCT")
        pair_pcts.append(float(portfolio.CMCT_pct))
    if portfolio.FUEL_pct > 0.0:
        pairs.append("FUEL")
        pair_pcts.append(float(portfolio.FUEL_pct))
    if portfolio.HVN_pct > 0.0:
        pairs.append("HVN")
        pair_pcts.append(float(portfolio.HVN_pct))
    if portfolio.DCT_pct > 0.0:
        pairs.append("DCT")
        pair_pcts.append(float(portfolio.DCT_pct))
    if portfolio.APPC_pct > 0.0:
        pairs.append("APPC")
        pair_pcts.append(float(portfolio.APPC_pct))
    if portfolio.MED_pct > 0.0:
        pairs.append("MED")
        pair_pcts.append(float(portfolio.MED_pct))
    if portfolio.PHR_pct > 0.0:
        pairs.append("PHR")
        pair_pcts.append(float(portfolio.PHR_pct))
    if portfolio.BANCA_pct > 0.0:
        pairs.append("BANCA")
        pair_pcts.append(float(portfolio.BANCA_pct))
    if portfolio.LET_pct > 0.0:
        pairs.append("LET")
        pair_pcts.append(float(portfolio.LET_pct))
    if portfolio.ECC_pct > 0.0:
        pairs.append("ECC")
        pair_pcts.append(float(portfolio.ECC_pct))
    if portfolio.LUN_pct > 0.0:
        pairs.append("LUN")
        pair_pcts.append(float(portfolio.LUN_pct))
    if portfolio.DAG_pct > 0.0:
        pairs.append("DAG")
        pair_pcts.append(float(portfolio.DAG_pct))
    if portfolio.UUU_pct > 0.0:
        pairs.append("UUU")
        pair_pcts.append(float(portfolio.UUU_pct))
    if portfolio.SBD_pct > 0.0:
        pairs.append("SBD")
        pair_pcts.append(float(portfolio.SBD_pct))
    if portfolio.SENT_pct > 0.0:
        pairs.append("SENT")
        pair_pcts.append(float(portfolio.SENT_pct))
    if portfolio.DBET_pct > 0.0:
        pairs.append("DBET")
        pair_pcts.append(float(portfolio.DBET_pct))
    if portfolio.TAAS_pct > 0.0:
        pairs.append("TAAS")
        pair_pcts.append(float(portfolio.TAAS_pct))
    if portfolio.QLC_pct > 0.0:
        pairs.append("QLC")
        pair_pcts.append(float(portfolio.QLC_pct))
    if portfolio.WABI_pct > 0.0:
        pairs.append("WABI")
        pair_pcts.append(float(portfolio.WABI_pct))
    if portfolio.PCN_pct > 0.0:
        pairs.append("PCN")
        pair_pcts.append(float(portfolio.PCN_pct))
    if portfolio.PURA_pct > 0.0:
        pairs.append("PURA")
        pair_pcts.append(float(portfolio.PURA_pct))
    if portfolio.XDCE_pct > 0.0:
        pairs.append("XDCE")
        pair_pcts.append(float(portfolio.XDCE_pct))
    if portfolio.SSC_pct > 0.0:
        pairs.append("SSC")
        pair_pcts.append(float(portfolio.SSC_pct))
    if portfolio.VIBE_pct > 0.0:
        pairs.append("VIBE")
        pair_pcts.append(float(portfolio.VIBE_pct))
    if portfolio.ELEC_pct > 0.0:
        pairs.append("ELEC")
        pair_pcts.append(float(portfolio.ELEC_pct))
    if portfolio.MEDIC_pct > 0.0:
        pairs.append("MEDIC")
        pair_pcts.append(float(portfolio.MEDIC_pct))
    if portfolio.COSS_pct > 0.0:
        pairs.append("COSS")
        pair_pcts.append(float(portfolio.COSS_pct))
    if portfolio.YEE_pct > 0.0:
        pairs.append("YEE")
        pair_pcts.append(float(portfolio.YEE_pct))
    if portfolio.AURA_pct > 0.0:
        pairs.append("AURA")
        pair_pcts.append(float(portfolio.AURA_pct))
    if portfolio.CSC_pct > 0.0:
        pairs.append("CSC")
        pair_pcts.append(float(portfolio.CSC_pct))
    if portfolio.MOBI_pct > 0.0:
        pairs.append("MOBI")
        pair_pcts.append(float(portfolio.MOBI_pct))
    if portfolio.PRL_pct > 0.0:
        pairs.append("PRL")
        pair_pcts.append(float(portfolio.PRL_pct))
    if portfolio.QUN_pct > 0.0:
        pairs.append("QUN")
        pair_pcts.append(float(portfolio.QUN_pct))
    if portfolio.SHIFT_pct > 0.0:
        pairs.append("SHIFT")
        pair_pcts.append(float(portfolio.SHIFT_pct))
    if portfolio.CAS_pct > 0.0:
        pairs.append("CAS")
        pair_pcts.append(float(portfolio.CAS_pct))
    if portfolio.SOAR_pct > 0.0:
        pairs.append("SOAR")
        pair_pcts.append(float(portfolio.SOAR_pct))
    if portfolio.BITG_pct > 0.0:
        pairs.append("BITG")
        pair_pcts.append(float(portfolio.BITG_pct))
    if portfolio.BKX_pct > 0.0:
        pairs.append("BKX")
        pair_pcts.append(float(portfolio.BKX_pct))
    if portfolio.DOCK_pct > 0.0:
        pairs.append("DOCK")
        pair_pcts.append(float(portfolio.DOCK_pct))
    if portfolio.KEY_pct > 0.0:
        pairs.append("KEY")
        pair_pcts.append(float(portfolio.KEY_pct))
    if portfolio.XES_pct > 0.0:
        pairs.append("XES")
        pair_pcts.append(float(portfolio.XES_pct))
    if portfolio.POT_pct > 0.0:
        pairs.append("POT")
        pair_pcts.append(float(portfolio.POT_pct))
    if portfolio.QBT_pct > 0.0:
        pairs.append("QBT")
        pair_pcts.append(float(portfolio.QBT_pct))
    if portfolio.DXT_pct > 0.0:
        pairs.append("DXT")
        pair_pcts.append(float(portfolio.DXT_pct))
    if portfolio.IXT_pct > 0.0:
        pairs.append("IXT")
        pair_pcts.append(float(portfolio.IXT_pct))
    if portfolio.BMC_pct > 0.0:
        pairs.append("BMC")
        pair_pcts.append(float(portfolio.BMC_pct))
    if portfolio.PEPECASH_pct > 0.0:
        pairs.append("PEPECASH")
        pair_pcts.append(float(portfolio.PEPECASH_pct))
    if portfolio.COB_pct > 0.0:
        pairs.append("COB")
        pair_pcts.append(float(portfolio.COB_pct))
    if portfolio.GRID_pct > 0.0:
        pairs.append("GRID")
        pair_pcts.append(float(portfolio.GRID_pct))
    if portfolio.BITUSD_pct > 0.0:
        pairs.append("BITUSD")
        pair_pcts.append(float(portfolio.BITUSD_pct))
    if portfolio.KRM_pct > 0.0:
        pairs.append("KRM")
        pair_pcts.append(float(portfolio.KRM_pct))
    if portfolio.HMQ_pct > 0.0:
        pairs.append("HMQ")
        pair_pcts.append(float(portfolio.HMQ_pct))
    if portfolio.VIB_pct > 0.0:
        pairs.append("VIB")
        pair_pcts.append(float(portfolio.VIB_pct))
    if portfolio.PPY_pct > 0.0:
        pairs.append("PPY")
        pair_pcts.append(float(portfolio.PPY_pct))
    if portfolio.XEL_pct > 0.0:
        pairs.append("XEL")
        pair_pcts.append(float(portfolio.XEL_pct))
    if portfolio.e_1ST_pct > 0.0:
        pairs.append("1ST")
        pair_pcts.append(float(portfolio.e_1ST_pct))
    if portfolio.NLC2_pct > 0.0:
        pairs.append("NLC2")
        pair_pcts.append(float(portfolio.NLC2_pct))
    if portfolio.MTN_pct > 0.0:
        pairs.append("MTN")
        pair_pcts.append(float(portfolio.MTN_pct))
    if portfolio.THC_pct > 0.0:
        pairs.append("THC")
        pair_pcts.append(float(portfolio.THC_pct))
    if portfolio.TNC_pct > 0.0:
        pairs.append("TNC")
        pair_pcts.append(float(portfolio.TNC_pct))
    if portfolio.NTK_pct > 0.0:
        pairs.append("NTK")
        pair_pcts.append(float(portfolio.NTK_pct))
    if portfolio.COLX_pct > 0.0:
        pairs.append("COLX")
        pair_pcts.append(float(portfolio.COLX_pct))
    if portfolio.COV_pct > 0.0:
        pairs.append("COV")
        pair_pcts.append(float(portfolio.COV_pct))
    if portfolio.DIME_pct > 0.0:
        pairs.append("DIME")
        pair_pcts.append(float(portfolio.DIME_pct))
    if portfolio.FOTA_pct > 0.0:
        pairs.append("FOTA")
        pair_pcts.append(float(portfolio.FOTA_pct))
    if portfolio.LIFE_pct > 0.0:
        pairs.append("LIFE")
        pair_pcts.append(float(portfolio.LIFE_pct))
    if portfolio.XBY_pct > 0.0:
        pairs.append("XBY")
        pair_pcts.append(float(portfolio.XBY_pct))
    if portfolio.MER_pct > 0.0:
        pairs.append("MER")
        pair_pcts.append(float(portfolio.MER_pct))
    if portfolio.RFR_pct > 0.0:
        pairs.append("RFR")
        pair_pcts.append(float(portfolio.RFR_pct))
    if portfolio.PST_pct > 0.0:
        pairs.append("PST")
        pair_pcts.append(float(portfolio.PST_pct))
    if portfolio.ZSC_pct > 0.0:
        pairs.append("ZSC")
        pair_pcts.append(float(portfolio.ZSC_pct))
    if portfolio.PRA_pct > 0.0:
        pairs.append("PRA")
        pair_pcts.append(float(portfolio.PRA_pct))
    if portfolio.CFI_pct > 0.0:
        pairs.append("CFI")
        pair_pcts.append(float(portfolio.CFI_pct))
    if portfolio.BIS_pct > 0.0:
        pairs.append("BIS")
        pair_pcts.append(float(portfolio.BIS_pct))
    if portfolio.QAU_pct > 0.0:
        pairs.append("QAU")
        pair_pcts.append(float(portfolio.QAU_pct))
    if portfolio.LEO_pct > 0.0:
        pairs.append("LEO")
        pair_pcts.append(float(portfolio.LEO_pct))
    if portfolio.BRM_pct > 0.0:
        pairs.append("BRM")
        pair_pcts.append(float(portfolio.BRM_pct))
    if portfolio.BCPT_pct > 0.0:
        pairs.append("BCPT")
        pair_pcts.append(float(portfolio.BCPT_pct))
    if portfolio.AMP_pct > 0.0:
        pairs.append("AMP")
        pair_pcts.append(float(portfolio.AMP_pct))
    if portfolio.TIME_pct > 0.0:
        pairs.append("TIME")
        pair_pcts.append(float(portfolio.TIME_pct))
    if portfolio.BITB_pct > 0.0:
        pairs.append("BITB")
        pair_pcts.append(float(portfolio.BITB_pct))
    if portfolio.BLT_pct > 0.0:
        pairs.append("BLT")
        pair_pcts.append(float(portfolio.BLT_pct))
    if portfolio.LUX_pct > 0.0:
        pairs.append("LUX")
        pair_pcts.append(float(portfolio.LUX_pct))
    if portfolio.SPC_pct > 0.0:
        pairs.append("SPC")
        pair_pcts.append(float(portfolio.SPC_pct))
    if portfolio.ONION_pct > 0.0:
        pairs.append("ONION")
        pair_pcts.append(float(portfolio.ONION_pct))
    if portfolio.RVR_pct > 0.0:
        pairs.append("RVR")
        pair_pcts.append(float(portfolio.RVR_pct))
    if portfolio.CEEK_pct > 0.0:
        pairs.append("CEEK")
        pair_pcts.append(float(portfolio.CEEK_pct))
    if portfolio.TRIG_pct > 0.0:
        pairs.append("TRIG")
        pair_pcts.append(float(portfolio.TRIG_pct))
    if portfolio.LATX_pct > 0.0:
        pairs.append("LATX")
        pair_pcts.append(float(portfolio.LATX_pct))
    if portfolio.ACAT_pct > 0.0:
        pairs.append("ACAT")
        pair_pcts.append(float(portfolio.ACAT_pct))
    if portfolio.ALQO_pct > 0.0:
        pairs.append("ALQO")
        pair_pcts.append(float(portfolio.ALQO_pct))
    if portfolio.MOT_pct > 0.0:
        pairs.append("MOT")
        pair_pcts.append(float(portfolio.MOT_pct))
    if portfolio.XSH_pct > 0.0:
        pairs.append("XSH")
        pair_pcts.append(float(portfolio.XSH_pct))
    if portfolio.EVX_pct > 0.0:
        pairs.append("EVX")
        pair_pcts.append(float(portfolio.EVX_pct))
    if portfolio.DIVX_pct > 0.0:
        pairs.append("DIVX")
        pair_pcts.append(float(portfolio.DIVX_pct))
    if portfolio.DMT_pct > 0.0:
        pairs.append("DMT")
        pair_pcts.append(float(portfolio.DMT_pct))
    if portfolio.CRW_pct > 0.0:
        pairs.append("CRW")
        pair_pcts.append(float(portfolio.CRW_pct))
    if portfolio.MWAT_pct > 0.0:
        pairs.append("MWAT")
        pair_pcts.append(float(portfolio.MWAT_pct))
    if portfolio.UKG_pct > 0.0:
        pairs.append("UKG")
        pair_pcts.append(float(portfolio.UKG_pct))
    if portfolio.PASC_pct > 0.0:
        pairs.append("PASC")
        pair_pcts.append(float(portfolio.PASC_pct))
    if portfolio.TAU_pct > 0.0:
        pairs.append("TAU")
        pair_pcts.append(float(portfolio.TAU_pct))
    if portfolio.OXY_pct > 0.0:
        pairs.append("OXY")
        pair_pcts.append(float(portfolio.OXY_pct))
    if portfolio.OMX_pct > 0.0:
        pairs.append("OMX")
        pair_pcts.append(float(portfolio.OMX_pct))
    if portfolio.BBR_pct > 0.0:
        pairs.append("BBR")
        pair_pcts.append(float(portfolio.BBR_pct))
    if portfolio.TSL_pct > 0.0:
        pairs.append("TSL")
        pair_pcts.append(float(portfolio.TSL_pct))
    if portfolio.DIM_pct > 0.0:
        pairs.append("DIM")
        pair_pcts.append(float(portfolio.DIM_pct))
    if portfolio.PRO_pct > 0.0:
        pairs.append("PRO")
        pair_pcts.append(float(portfolio.PRO_pct))
    if portfolio.PLBT_pct > 0.0:
        pairs.append("PLBT")
        pair_pcts.append(float(portfolio.PLBT_pct))
    if portfolio.DADI_pct > 0.0:
        pairs.append("DADI")
        pair_pcts.append(float(portfolio.DADI_pct))
    if portfolio.UGC_pct > 0.0:
        pairs.append("UGC")
        pair_pcts.append(float(portfolio.UGC_pct))
    if portfolio.DMD_pct > 0.0:
        pairs.append("DMD")
        pair_pcts.append(float(portfolio.DMD_pct))
    if portfolio.BLK_pct > 0.0:
        pairs.append("BLK")
        pair_pcts.append(float(portfolio.BLK_pct))
    if portfolio.SNC_pct > 0.0:
        pairs.append("SNC")
        pair_pcts.append(float(portfolio.SNC_pct))
    if portfolio.BETR_pct > 0.0:
        pairs.append("BETR")
        pair_pcts.append(float(portfolio.BETR_pct))
    if portfolio.GRC_pct > 0.0:
        pairs.append("GRC")
        pair_pcts.append(float(portfolio.GRC_pct))
    if portfolio.BOT_pct > 0.0:
        pairs.append("BOT")
        pair_pcts.append(float(portfolio.BOT_pct))
    if portfolio.FLASH_pct > 0.0:
        pairs.append("FLASH")
        pair_pcts.append(float(portfolio.FLASH_pct))
    if portfolio.TFD_pct > 0.0:
        pairs.append("TFD")
        pair_pcts.append(float(portfolio.TFD_pct))
    if portfolio.DBIX_pct > 0.0:
        pairs.append("DBIX")
        pair_pcts.append(float(portfolio.DBIX_pct))
    if portfolio.UQC_pct > 0.0:
        pairs.append("UQC")
        pair_pcts.append(float(portfolio.UQC_pct))
    if portfolio.SWTH_pct > 0.0:
        pairs.append("SWTH")
        pair_pcts.append(float(portfolio.SWTH_pct))
    if portfolio.SKB_pct > 0.0:
        pairs.append("SKB")
        pair_pcts.append(float(portfolio.SKB_pct))
    if portfolio.BCA_pct > 0.0:
        pairs.append("BCA")
        pair_pcts.append(float(portfolio.BCA_pct))
    if portfolio.SOUL_pct > 0.0:
        pairs.append("SOUL")
        pair_pcts.append(float(portfolio.SOUL_pct))
    if portfolio.GUP_pct > 0.0:
        pairs.append("GUP")
        pair_pcts.append(float(portfolio.GUP_pct))
    if portfolio.MUSE_pct > 0.0:
        pairs.append("MUSE")
        pair_pcts.append(float(portfolio.MUSE_pct))
    if portfolio.SNTR_pct > 0.0:
        pairs.append("SNTR")
        pair_pcts.append(float(portfolio.SNTR_pct))
    if portfolio.GEM_pct > 0.0:
        pairs.append("GEM")
        pair_pcts.append(float(portfolio.GEM_pct))
    if portfolio.LA_pct > 0.0:
        pairs.append("LA")
        pair_pcts.append(float(portfolio.LA_pct))
    if portfolio.NKC_pct > 0.0:
        pairs.append("NKC")
        pair_pcts.append(float(portfolio.NKC_pct))
    if portfolio.MUE_pct > 0.0:
        pairs.append("MUE")
        pair_pcts.append(float(portfolio.MUE_pct))
    if portfolio.BPT_pct > 0.0:
        pairs.append("BPT")
        pair_pcts.append(float(portfolio.BPT_pct))
    if portfolio.STK_pct > 0.0:
        pairs.append("STK")
        pair_pcts.append(float(portfolio.STK_pct))
    if portfolio.NMR_pct > 0.0:
        pairs.append("NMR")
        pair_pcts.append(float(portfolio.NMR_pct))
    if portfolio.CV_pct > 0.0:
        pairs.append("CV")
        pair_pcts.append(float(portfolio.CV_pct))
    if portfolio.OMNI_pct > 0.0:
        pairs.append("OMNI")
        pair_pcts.append(float(portfolio.OMNI_pct))
    if portfolio.REM_pct > 0.0:
        pairs.append("REM")
        pair_pcts.append(float(portfolio.REM_pct))
    if portfolio.HYDRO_pct > 0.0:
        pairs.append("HYDRO")
        pair_pcts.append(float(portfolio.HYDRO_pct))
    if portfolio.RBY_pct > 0.0:
        pairs.append("RBY")
        pair_pcts.append(float(portfolio.RBY_pct))
    if portfolio.ORME_pct > 0.0:
        pairs.append("ORME")
        pair_pcts.append(float(portfolio.ORME_pct))
    if portfolio.SSP_pct > 0.0:
        pairs.append("SSP")
        pair_pcts.append(float(portfolio.SSP_pct))
    if portfolio.EVR_pct > 0.0:
        pairs.append("EVR")
        pair_pcts.append(float(portfolio.EVR_pct))
    if portfolio.MTH_pct > 0.0:
        pairs.append("MTH")
        pair_pcts.append(float(portfolio.MTH_pct))
    if portfolio.SHND_pct > 0.0:
        pairs.append("SHND")
        pair_pcts.append(float(portfolio.SHND_pct))
    if portfolio.NEU_pct > 0.0:
        pairs.append("NEU")
        pair_pcts.append(float(portfolio.NEU_pct))
    if portfolio.RADS_pct > 0.0:
        pairs.append("RADS")
        pair_pcts.append(float(portfolio.RADS_pct))
    if portfolio.CAPP_pct > 0.0:
        pairs.append("CAPP")
        pair_pcts.append(float(portfolio.CAPP_pct))
    if portfolio.STX_pct > 0.0:
        pairs.append("STX")
        pair_pcts.append(float(portfolio.STX_pct))
    if portfolio.MDA_pct > 0.0:
        pairs.append("MDA")
        pair_pcts.append(float(portfolio.MDA_pct))
    if portfolio.RMT_pct > 0.0:
        pairs.append("RMT")
        pair_pcts.append(float(portfolio.RMT_pct))
    if portfolio.TIX_pct > 0.0:
        pairs.append("TIX")
        pair_pcts.append(float(portfolio.TIX_pct))
    if portfolio.MDT_pct > 0.0:
        pairs.append("MDT")
        pair_pcts.append(float(portfolio.MDT_pct))
    if portfolio.SLR_pct > 0.0:
        pairs.append("SLR")
        pair_pcts.append(float(portfolio.SLR_pct))
    if portfolio.OAX_pct > 0.0:
        pairs.append("OAX")
        pair_pcts.append(float(portfolio.OAX_pct))
    if portfolio.ADT_pct > 0.0:
        pairs.append("ADT")
        pair_pcts.append(float(portfolio.ADT_pct))
    if portfolio.FLO_pct > 0.0:
        pairs.append("FLO")
        pair_pcts.append(float(portfolio.FLO_pct))
    if portfolio.ARN_pct > 0.0:
        pairs.append("ARN")
        pair_pcts.append(float(portfolio.ARN_pct))
    if portfolio.BBN_pct > 0.0:
        pairs.append("BBN")
        pair_pcts.append(float(portfolio.BBN_pct))
    if portfolio.MOON_pct > 0.0:
        pairs.append("MOON")
        pair_pcts.append(float(portfolio.MOON_pct))
    if portfolio.CHP_pct > 0.0:
        pairs.append("CHP")
        pair_pcts.append(float(portfolio.CHP_pct))
    if portfolio.AIT_pct > 0.0:
        pairs.append("AIT")
        pair_pcts.append(float(portfolio.AIT_pct))
    if portfolio.CLO_pct > 0.0:
        pairs.append("CLO")
        pair_pcts.append(float(portfolio.CLO_pct))
    if portfolio.AIDOC_pct > 0.0:
        pairs.append("AIDOC")
        pair_pcts.append(float(portfolio.AIDOC_pct))
    if portfolio.FDZ_pct > 0.0:
        pairs.append("FDZ")
        pair_pcts.append(float(portfolio.FDZ_pct))
    if portfolio.LOC_pct > 0.0:
        pairs.append("LOC")
        pair_pcts.append(float(portfolio.LOC_pct))
    if portfolio.PAL_pct > 0.0:
        pairs.append("PAL")
        pair_pcts.append(float(portfolio.PAL_pct))
    if portfolio.IOC_pct > 0.0:
        pairs.append("IOC")
        pair_pcts.append(float(portfolio.IOC_pct))
    if portfolio.PKC_pct > 0.0:
        pairs.append("PKC")
        pair_pcts.append(float(portfolio.PKC_pct))
    if portfolio.HXX_pct > 0.0:
        pairs.append("HXX")
        pair_pcts.append(float(portfolio.HXX_pct))
    if portfolio.UP_pct > 0.0:
        pairs.append("UP")
        pair_pcts.append(float(portfolio.UP_pct))
    if portfolio.SLT_pct > 0.0:
        pairs.append("SLT")
        pair_pcts.append(float(portfolio.SLT_pct))
    if portfolio.PAT_pct > 0.0:
        pairs.append("PAT")
        pair_pcts.append(float(portfolio.PAT_pct))
    if portfolio.DICE_pct > 0.0:
        pairs.append("DICE")
        pair_pcts.append(float(portfolio.DICE_pct))
    if portfolio.EXRN_pct > 0.0:
        pairs.append("EXRN")
        pair_pcts.append(float(portfolio.EXRN_pct))
    if portfolio.HMC_pct > 0.0:
        pairs.append("HMC")
        pair_pcts.append(float(portfolio.HMC_pct))
    if portfolio.SENC_pct > 0.0:
        pairs.append("SENC")
        pair_pcts.append(float(portfolio.SENC_pct))
    if portfolio.DLT_pct > 0.0:
        pairs.append("DLT")
        pair_pcts.append(float(portfolio.DLT_pct))
    if portfolio.GEN_pct > 0.0:
        pairs.append("GEN")
        pair_pcts.append(float(portfolio.GEN_pct))
    if portfolio.CHSB_pct > 0.0:
        pairs.append("CHSB")
        pair_pcts.append(float(portfolio.CHSB_pct))
    if portfolio.ABYSS_pct > 0.0:
        pairs.append("ABYSS")
        pair_pcts.append(float(portfolio.ABYSS_pct))
    if portfolio.BQ_pct > 0.0:
        pairs.append("BQ")
        pair_pcts.append(float(portfolio.BQ_pct))
    if portfolio.EXP_pct > 0.0:
        pairs.append("EXP")
        pair_pcts.append(float(portfolio.EXP_pct))
    if portfolio.EKO_pct > 0.0:
        pairs.append("EKO")
        pair_pcts.append(float(portfolio.EKO_pct))
    if portfolio.ZIPT_pct > 0.0:
        pairs.append("ZIPT")
        pair_pcts.append(float(portfolio.ZIPT_pct))
    if portfolio.CLAM_pct > 0.0:
        pairs.append("CLAM")
        pair_pcts.append(float(portfolio.CLAM_pct))
    if portfolio.IDH_pct > 0.0:
        pairs.append("IDH")
        pair_pcts.append(float(portfolio.IDH_pct))
    if portfolio.SRCOIN_pct > 0.0:
        pairs.append("SRCOIN")
        pair_pcts.append(float(portfolio.SRCOIN_pct))
    if portfolio.ATM_pct > 0.0:
        pairs.append("ATM")
        pair_pcts.append(float(portfolio.ATM_pct))
    if portfolio.NYC_pct > 0.0:
        pairs.append("NYC")
        pair_pcts.append(float(portfolio.NYC_pct))
    if portfolio.DEV_pct > 0.0:
        pairs.append("DEV")
        pair_pcts.append(float(portfolio.DEV_pct))
    if portfolio.GCR_pct > 0.0:
        pairs.append("GCR")
        pair_pcts.append(float(portfolio.GCR_pct))
    if portfolio.NBAI_pct > 0.0:
        pairs.append("NBAI")
        pair_pcts.append(float(portfolio.NBAI_pct))
    if portfolio.POLIS_pct > 0.0:
        pairs.append("POLIS")
        pair_pcts.append(float(portfolio.POLIS_pct))
    if portfolio.DTB_pct > 0.0:
        pairs.append("DTB")
        pair_pcts.append(float(portfolio.DTB_pct))
    if portfolio.CVCOIN_pct > 0.0:
        pairs.append("CVCOIN")
        pair_pcts.append(float(portfolio.CVCOIN_pct))
    if portfolio.MRK_pct > 0.0:
        pairs.append("MRK")
        pair_pcts.append(float(portfolio.MRK_pct))
    if portfolio.SHIP_pct > 0.0:
        pairs.append("SHIP")
        pair_pcts.append(float(portfolio.SHIP_pct))
    if portfolio.INCNT_pct > 0.0:
        pairs.append("INCNT")
        pair_pcts.append(float(portfolio.INCNT_pct))
    if portfolio.HER_pct > 0.0:
        pairs.append("HER")
        pair_pcts.append(float(portfolio.HER_pct))
    if portfolio.AXP_pct > 0.0:
        pairs.append("AXP")
        pair_pcts.append(float(portfolio.AXP_pct))
    if portfolio.LMC_pct > 0.0:
        pairs.append("LMC")
        pair_pcts.append(float(portfolio.LMC_pct))
    if portfolio.REBL_pct > 0.0:
        pairs.append("REBL")
        pair_pcts.append(float(portfolio.REBL_pct))
    if portfolio.APH_pct > 0.0:
        pairs.append("APH")
        pair_pcts.append(float(portfolio.APH_pct))
    if portfolio.DRT_pct > 0.0:
        pairs.append("DRT")
        pair_pcts.append(float(portfolio.DRT_pct))
    if portfolio.HKN_pct > 0.0:
        pairs.append("HKN")
        pair_pcts.append(float(portfolio.HKN_pct))
    if portfolio.UBT_pct > 0.0:
        pairs.append("UBT")
        pair_pcts.append(float(portfolio.UBT_pct))
    if portfolio.XMY_pct > 0.0:
        pairs.append("XMY")
        pair_pcts.append(float(portfolio.XMY_pct))
    if portfolio.RVT_pct > 0.0:
        pairs.append("RVT")
        pair_pcts.append(float(portfolio.RVT_pct))
    if portfolio.SEXC_pct > 0.0:
        pairs.append("SEXC")
        pair_pcts.append(float(portfolio.SEXC_pct))
    if portfolio.ECOB_pct > 0.0:
        pairs.append("ECOB")
        pair_pcts.append(float(portfolio.ECOB_pct))
    if portfolio.SIB_pct > 0.0:
        pairs.append("SIB")
        pair_pcts.append(float(portfolio.SIB_pct))
    if portfolio.RED_pct > 0.0:
        pairs.append("RED")
        pair_pcts.append(float(portfolio.RED_pct))
    if portfolio.ICOS_pct > 0.0:
        pairs.append("ICOS")
        pair_pcts.append(float(portfolio.ICOS_pct))
    if portfolio.SPRTS_pct > 0.0:
        pairs.append("SPRTS")
        pair_pcts.append(float(portfolio.SPRTS_pct))
    if portfolio.GET_pct > 0.0:
        pairs.append("GET")
        pair_pcts.append(float(portfolio.GET_pct))
    if portfolio.PCL_pct > 0.0:
        pairs.append("PCL")
        pair_pcts.append(float(portfolio.PCL_pct))
    if portfolio.NEOS_pct > 0.0:
        pairs.append("NEOS")
        pair_pcts.append(float(portfolio.NEOS_pct))
    if portfolio.BWK_pct > 0.0:
        pairs.append("BWK")
        pair_pcts.append(float(portfolio.BWK_pct))
    if portfolio.NPX_pct > 0.0:
        pairs.append("NPX")
        pair_pcts.append(float(portfolio.NPX_pct))
    if portfolio.DYN_pct > 0.0:
        pairs.append("DYN")
        pair_pcts.append(float(portfolio.DYN_pct))
    if portfolio.BEZ_pct > 0.0:
        pairs.append("BEZ")
        pair_pcts.append(float(portfolio.BEZ_pct))
    if portfolio.XST_pct > 0.0:
        pairs.append("XST")
        pair_pcts.append(float(portfolio.XST_pct))
    if portfolio.IPL_pct > 0.0:
        pairs.append("IPL")
        pair_pcts.append(float(portfolio.IPL_pct))
    if portfolio.VRC_pct > 0.0:
        pairs.append("VRC")
        pair_pcts.append(float(portfolio.VRC_pct))
    if portfolio.IFT_pct > 0.0:
        pairs.append("IFT")
        pair_pcts.append(float(portfolio.IFT_pct))
    if portfolio.MUSIC_pct > 0.0:
        pairs.append("MUSIC")
        pair_pcts.append(float(portfolio.MUSIC_pct))
    if portfolio.CAT_pct > 0.0:
        pairs.append("CAT")
        pair_pcts.append(float(portfolio.CAT_pct))
    if portfolio.LOKI_pct > 0.0:
        pairs.append("LOKI")
        pair_pcts.append(float(portfolio.LOKI_pct))
    if portfolio.UCASH_pct > 0.0:
        pairs.append("UCASH")
        pair_pcts.append(float(portfolio.UCASH_pct))
    if portfolio.BSD_pct > 0.0:
        pairs.append("BSD")
        pair_pcts.append(float(portfolio.BSD_pct))
    if portfolio.PIRL_pct > 0.0:
        pairs.append("PIRL")
        pair_pcts.append(float(portfolio.PIRL_pct))
    if portfolio.DEB_pct > 0.0:
        pairs.append("DEB")
        pair_pcts.append(float(portfolio.DEB_pct))
    if portfolio.HWC_pct > 0.0:
        pairs.append("HWC")
        pair_pcts.append(float(portfolio.HWC_pct))
    if portfolio.NVC_pct > 0.0:
        pairs.append("NVC")
        pair_pcts.append(float(portfolio.NVC_pct))
    if portfolio.XAUR_pct > 0.0:
        pairs.append("XAUR")
        pair_pcts.append(float(portfolio.XAUR_pct))
    if portfolio.FLIXX_pct > 0.0:
        pairs.append("FLIXX")
        pair_pcts.append(float(portfolio.FLIXX_pct))
    if portfolio.RMC_pct > 0.0:
        pairs.append("RMC")
        pair_pcts.append(float(portfolio.RMC_pct))
    if portfolio.PKT_pct > 0.0:
        pairs.append("PKT")
        pair_pcts.append(float(portfolio.PKT_pct))
    if portfolio.GBX_pct > 0.0:
        pairs.append("GBX")
        pair_pcts.append(float(portfolio.GBX_pct))
    if portfolio.NCT_pct > 0.0:
        pairs.append("NCT")
        pair_pcts.append(float(portfolio.NCT_pct))
    if portfolio.GRFT_pct > 0.0:
        pairs.append("GRFT")
        pair_pcts.append(float(portfolio.GRFT_pct))
    if portfolio.EFX_pct > 0.0:
        pairs.append("EFX")
        pair_pcts.append(float(portfolio.EFX_pct))
    if portfolio.NXC_pct > 0.0:
        pairs.append("NXC")
        pair_pcts.append(float(portfolio.NXC_pct))
    if portfolio.XPA_pct > 0.0:
        pairs.append("XPA")
        pair_pcts.append(float(portfolio.XPA_pct))
    if portfolio.AU_pct > 0.0:
        pairs.append("AU")
        pair_pcts.append(float(portfolio.AU_pct))
    if portfolio.SS_pct > 0.0:
        pairs.append("SS")
        pair_pcts.append(float(portfolio.SS_pct))
    if portfolio.APX_pct > 0.0:
        pairs.append("APX")
        pair_pcts.append(float(portfolio.APX_pct))
    if portfolio.PARETO_pct > 0.0:
        pairs.append("PARETO")
        pair_pcts.append(float(portfolio.PARETO_pct))
    if portfolio.AIR_pct > 0.0:
        pairs.append("AIR")
        pair_pcts.append(float(portfolio.AIR_pct))
    if portfolio.PINK_pct > 0.0:
        pairs.append("PINK")
        pair_pcts.append(float(portfolio.PINK_pct))
    if portfolio.GETX_pct > 0.0:
        pairs.append("GETX")
        pair_pcts.append(float(portfolio.GETX_pct))
    if portfolio.ZLA_pct > 0.0:
        pairs.append("ZLA")
        pair_pcts.append(float(portfolio.ZLA_pct))
    if portfolio.LEV_pct > 0.0:
        pairs.append("LEV")
        pair_pcts.append(float(portfolio.LEV_pct))
    if portfolio.SWT_pct > 0.0:
        pairs.append("SWT")
        pair_pcts.append(float(portfolio.SWT_pct))
    if portfolio.AID_pct > 0.0:
        pairs.append("AID")
        pair_pcts.append(float(portfolio.AID_pct))
    if portfolio.TUBE_pct > 0.0:
        pairs.append("TUBE")
        pair_pcts.append(float(portfolio.TUBE_pct))
    if portfolio.OK_pct > 0.0:
        pairs.append("OK")
        pair_pcts.append(float(portfolio.OK_pct))
    if portfolio.DGTX_pct > 0.0:
        pairs.append("DGTX")
        pair_pcts.append(float(portfolio.DGTX_pct))
    if portfolio.BIO_pct > 0.0:
        pairs.append("BIO")
        pair_pcts.append(float(portfolio.BIO_pct))
    if portfolio.AVT_pct > 0.0:
        pairs.append("AVT")
        pair_pcts.append(float(portfolio.AVT_pct))
    if portfolio.MTX_pct > 0.0:
        pairs.append("MTX")
        pair_pcts.append(float(portfolio.MTX_pct))
    if portfolio.CAG_pct > 0.0:
        pairs.append("CAG")
        pair_pcts.append(float(portfolio.CAG_pct))
    if portfolio.FLDC_pct > 0.0:
        pairs.append("FLDC")
        pair_pcts.append(float(portfolio.FLDC_pct))
    if portfolio.SPD_pct > 0.0:
        pairs.append("SPD")
        pair_pcts.append(float(portfolio.SPD_pct))
    if portfolio.CXO_pct > 0.0:
        pairs.append("CXO")
        pair_pcts.append(float(portfolio.CXO_pct))
    if portfolio.PRG_pct > 0.0:
        pairs.append("PRG")
        pair_pcts.append(float(portfolio.PRG_pct))
    if portfolio.CAN_pct > 0.0:
        pairs.append("CAN")
        pair_pcts.append(float(portfolio.CAN_pct))
    if portfolio.HBT_pct > 0.0:
        pairs.append("HBT")
        pair_pcts.append(float(portfolio.HBT_pct))
    if portfolio.PTOY_pct > 0.0:
        pairs.append("PTOY")
        pair_pcts.append(float(portfolio.PTOY_pct))
    if portfolio.ZAP_pct > 0.0:
        pairs.append("ZAP")
        pair_pcts.append(float(portfolio.ZAP_pct))
    if portfolio.LALA_pct > 0.0:
        pairs.append("LALA")
        pair_pcts.append(float(portfolio.LALA_pct))
    if portfolio.HBZ_pct > 0.0:
        pairs.append("HBZ")
        pair_pcts.append(float(portfolio.HBZ_pct))
    if portfolio.ZOI_pct > 0.0:
        pairs.append("ZOI")
        pair_pcts.append(float(portfolio.ZOI_pct))
    if portfolio.PND_pct > 0.0:
        pairs.append("PND")
        pair_pcts.append(float(portfolio.PND_pct))
    if portfolio.ERO_pct > 0.0:
        pairs.append("ERO")
        pair_pcts.append(float(portfolio.ERO_pct))
    if portfolio.BDG_pct > 0.0:
        pairs.append("BDG")
        pair_pcts.append(float(portfolio.BDG_pct))
    if portfolio.ADB_pct > 0.0:
        pairs.append("ADB")
        pair_pcts.append(float(portfolio.ADB_pct))
    if portfolio.ZRC_pct > 0.0:
        pairs.append("ZRC")
        pair_pcts.append(float(portfolio.ZRC_pct))
    if portfolio.GOLOS_pct > 0.0:
        pairs.append("GOLOS")
        pair_pcts.append(float(portfolio.GOLOS_pct))
    if portfolio.DERO_pct > 0.0:
        pairs.append("DERO")
        pair_pcts.append(float(portfolio.DERO_pct))
    if portfolio.MINT_pct > 0.0:
        pairs.append("MINT")
        pair_pcts.append(float(portfolio.MINT_pct))
    if portfolio.LNC_pct > 0.0:
        pairs.append("LNC")
        pair_pcts.append(float(portfolio.LNC_pct))
    if portfolio.LWF_pct > 0.0:
        pairs.append("LWF")
        pair_pcts.append(float(portfolio.LWF_pct))
    if portfolio.DNA_pct > 0.0:
        pairs.append("DNA")
        pair_pcts.append(float(portfolio.DNA_pct))
    if portfolio.BCC_pct > 0.0:
        pairs.append("BCC")
        pair_pcts.append(float(portfolio.BCC_pct))
    if portfolio.ADH_pct > 0.0:
        pairs.append("ADH")
        pair_pcts.append(float(portfolio.ADH_pct))
    if portfolio.PUT_pct > 0.0:
        pairs.append("PUT")
        pair_pcts.append(float(portfolio.PUT_pct))
    if portfolio.DOT_pct > 0.0:
        pairs.append("DOT")
        pair_pcts.append(float(portfolio.DOT_pct))
    if portfolio.XNK_pct > 0.0:
        pairs.append("XNK")
        pair_pcts.append(float(portfolio.XNK_pct))
    if portfolio.SIG_pct > 0.0:
        pairs.append("SIG")
        pair_pcts.append(float(portfolio.SIG_pct))
    if portfolio.SENSE_pct > 0.0:
        pairs.append("SENSE")
        pair_pcts.append(float(portfolio.SENSE_pct))
    if portfolio.MLM_pct > 0.0:
        pairs.append("MLM")
        pair_pcts.append(float(portfolio.MLM_pct))
    if portfolio.IDXM_pct > 0.0:
        pairs.append("IDXM")
        pair_pcts.append(float(portfolio.IDXM_pct))
    if portfolio.FLUZ_pct > 0.0:
        pairs.append("FLUZ")
        pair_pcts.append(float(portfolio.FLUZ_pct))
    if portfolio.BET_pct > 0.0:
        pairs.append("BET")
        pair_pcts.append(float(portfolio.BET_pct))
    if portfolio.NET_pct > 0.0:
        pairs.append("NET")
        pair_pcts.append(float(portfolio.NET_pct))
    if portfolio.BERRY_pct > 0.0:
        pairs.append("BERRY")
        pair_pcts.append(float(portfolio.BERRY_pct))
    if portfolio.ELIX_pct > 0.0:
        pairs.append("ELIX")
        pair_pcts.append(float(portfolio.ELIX_pct))
    if portfolio.TRST_pct > 0.0:
        pairs.append("TRST")
        pair_pcts.append(float(portfolio.TRST_pct))
    if portfolio.SEQ_pct > 0.0:
        pairs.append("SEQ")
        pair_pcts.append(float(portfolio.SEQ_pct))
    if portfolio.YOC_pct > 0.0:
        pairs.append("YOC")
        pair_pcts.append(float(portfolio.YOC_pct))
    if portfolio.ADI_pct > 0.0:
        pairs.append("ADI")
        pair_pcts.append(float(portfolio.ADI_pct))
    if portfolio.BNTY_pct > 0.0:
        pairs.append("BNTY")
        pair_pcts.append(float(portfolio.BNTY_pct))
    if portfolio.HEAT_pct > 0.0:
        pairs.append("HEAT")
        pair_pcts.append(float(portfolio.HEAT_pct))
    if portfolio.ALIS_pct > 0.0:
        pairs.append("ALIS")
        pair_pcts.append(float(portfolio.ALIS_pct))
    if portfolio.B2B_pct > 0.0:
        pairs.append("B2B")
        pair_pcts.append(float(portfolio.B2B_pct))
    if portfolio.TGT_pct > 0.0:
        pairs.append("TGT")
        pair_pcts.append(float(portfolio.TGT_pct))
    if portfolio.ENRG_pct > 0.0:
        pairs.append("ENRG")
        pair_pcts.append(float(portfolio.ENRG_pct))
    if portfolio.ESP_pct > 0.0:
        pairs.append("ESP")
        pair_pcts.append(float(portfolio.ESP_pct))
    if portfolio.APR_pct > 0.0:
        pairs.append("APR")
        pair_pcts.append(float(portfolio.APR_pct))
    if portfolio.MITX_pct > 0.0:
        pairs.append("MITX")
        pair_pcts.append(float(portfolio.MITX_pct))
    if portfolio.e_1WO_pct > 0.0:
        pairs.append("1WO")
        pair_pcts.append(float(portfolio.e_1WO_pct))
    if portfolio.XLR_pct > 0.0:
        pairs.append("XLR")
        pair_pcts.append(float(portfolio.XLR_pct))
    if portfolio.XSPEC_pct > 0.0:
        pairs.append("XSPEC")
        pair_pcts.append(float(portfolio.XSPEC_pct))
    if portfolio.CBT_pct > 0.0:
        pairs.append("CBT")
        pair_pcts.append(float(portfolio.CBT_pct))
    if portfolio.CURE_pct > 0.0:
        pairs.append("CURE")
        pair_pcts.append(float(portfolio.CURE_pct))
    if portfolio.CFUN_pct > 0.0:
        pairs.append("CFUN")
        pair_pcts.append(float(portfolio.CFUN_pct))
    if portfolio.COFI_pct > 0.0:
        pairs.append("COFI")
        pair_pcts.append(float(portfolio.COFI_pct))
    if portfolio.CLN_pct > 0.0:
        pairs.append("CLN")
        pair_pcts.append(float(portfolio.CLN_pct))
    if portfolio.BEE_pct > 0.0:
        pairs.append("BEE")
        pair_pcts.append(float(portfolio.BEE_pct))
    if portfolio.BCY_pct > 0.0:
        pairs.append("BCY")
        pair_pcts.append(float(portfolio.BCY_pct))
    if portfolio.FID_pct > 0.0:
        pairs.append("FID")
        pair_pcts.append(float(portfolio.FID_pct))
    if portfolio.LDC_pct > 0.0:
        pairs.append("LDC")
        pair_pcts.append(float(portfolio.LDC_pct))
    if portfolio.FACE_pct > 0.0:
        pairs.append("FACE")
        pair_pcts.append(float(portfolio.FACE_pct))
    if portfolio.MORPH_pct > 0.0:
        pairs.append("MORPH")
        pair_pcts.append(float(portfolio.MORPH_pct))
    if portfolio.MYST_pct > 0.0:
        pairs.append("MYST")
        pair_pcts.append(float(portfolio.MYST_pct))
    if portfolio.PBT_pct > 0.0:
        pairs.append("PBT")
        pair_pcts.append(float(portfolio.PBT_pct))
    if portfolio.GLD_pct > 0.0:
        pairs.append("GLD")
        pair_pcts.append(float(portfolio.GLD_pct))
    if portfolio.ADST_pct > 0.0:
        pairs.append("ADST")
        pair_pcts.append(float(portfolio.ADST_pct))
    if portfolio.LND_pct > 0.0:
        pairs.append("LND")
        pair_pcts.append(float(portfolio.LND_pct))
    if portfolio.COVAL_pct > 0.0:
        pairs.append("COVAL")
        pair_pcts.append(float(portfolio.COVAL_pct))
    if portfolio.AUR_pct > 0.0:
        pairs.append("AUR")
        pair_pcts.append(float(portfolio.AUR_pct))
    if portfolio.SETH_pct > 0.0:
        pairs.append("SETH")
        pair_pcts.append(float(portfolio.SETH_pct))
    if portfolio.SNOV_pct > 0.0:
        pairs.append("SNOV")
        pair_pcts.append(float(portfolio.SNOV_pct))
    if portfolio.EVE_pct > 0.0:
        pairs.append("EVE")
        pair_pcts.append(float(portfolio.EVE_pct))
    if portfolio.ATB_pct > 0.0:
        pairs.append("ATB")
        pair_pcts.append(float(portfolio.ATB_pct))
    if portfolio.TOA_pct > 0.0:
        pairs.append("TOA")
        pair_pcts.append(float(portfolio.TOA_pct))
    if portfolio.TFL_pct > 0.0:
        pairs.append("TFL")
        pair_pcts.append(float(portfolio.TFL_pct))
    if portfolio.SPHR_pct > 0.0:
        pairs.append("SPHR")
        pair_pcts.append(float(portfolio.SPHR_pct))
    if portfolio.MYB_pct > 0.0:
        pairs.append("MYB")
        pair_pcts.append(float(portfolio.MYB_pct))
    if portfolio.PRIX_pct > 0.0:
        pairs.append("PRIX")
        pair_pcts.append(float(portfolio.PRIX_pct))
    if portfolio.POLL_pct > 0.0:
        pairs.append("POLL")
        pair_pcts.append(float(portfolio.POLL_pct))
    if portfolio.EZT_pct > 0.0:
        pairs.append("EZT")
        pair_pcts.append(float(portfolio.EZT_pct))
    if portfolio.WCT_pct > 0.0:
        pairs.append("WCT")
        pair_pcts.append(float(portfolio.WCT_pct))
    if portfolio.MAX_pct > 0.0:
        pairs.append("MAX")
        pair_pcts.append(float(portfolio.MAX_pct))
    if portfolio.CSNO_pct > 0.0:
        pairs.append("CSNO")
        pair_pcts.append(float(portfolio.CSNO_pct))
    if portfolio.TRF_pct > 0.0:
        pairs.append("TRF")
        pair_pcts.append(float(portfolio.TRF_pct))
    if portfolio.AVA_pct > 0.0:
        pairs.append("AVA")
        pair_pcts.append(float(portfolio.AVA_pct))
    if portfolio.SYNX_pct > 0.0:
        pairs.append("SYNX")
        pair_pcts.append(float(portfolio.SYNX_pct))
    if portfolio.GLA_pct > 0.0:
        pairs.append("GLA")
        pair_pcts.append(float(portfolio.GLA_pct))
    if portfolio.REAL_pct > 0.0:
        pairs.append("REAL")
        pair_pcts.append(float(portfolio.REAL_pct))
    if portfolio.IPSX_pct > 0.0:
        pairs.append("IPSX")
        pair_pcts.append(float(portfolio.IPSX_pct))
    if portfolio.ABY_pct > 0.0:
        pairs.append("ABY")
        pair_pcts.append(float(portfolio.ABY_pct))
    if portfolio.TX_pct > 0.0:
        pairs.append("TX")
        pair_pcts.append(float(portfolio.TX_pct))
    if portfolio.NPER_pct > 0.0:
        pairs.append("NPER")
        pair_pcts.append(float(portfolio.NPER_pct))
    if portfolio.KORE_pct > 0.0:
        pairs.append("KORE")
        pair_pcts.append(float(portfolio.KORE_pct))
    if portfolio.TIPS_pct > 0.0:
        pairs.append("TIPS")
        pair_pcts.append(float(portfolio.TIPS_pct))
    if portfolio.ARY_pct > 0.0:
        pairs.append("ARY")
        pair_pcts.append(float(portfolio.ARY_pct))
    if portfolio.VIT_pct > 0.0:
        pairs.append("VIT")
        pair_pcts.append(float(portfolio.VIT_pct))
    if portfolio.OBITS_pct > 0.0:
        pairs.append("OBITS")
        pair_pcts.append(float(portfolio.OBITS_pct))
    if portfolio.SHL_pct > 0.0:
        pairs.append("SHL")
        pair_pcts.append(float(portfolio.SHL_pct))
    if portfolio.WRC_pct > 0.0:
        pairs.append("WRC")
        pair_pcts.append(float(portfolio.WRC_pct))
    if portfolio.SHP_pct > 0.0:
        pairs.append("SHP")
        pair_pcts.append(float(portfolio.SHP_pct))
    if portfolio.HQX_pct > 0.0:
        pairs.append("HQX")
        pair_pcts.append(float(portfolio.HQX_pct))
    if portfolio.J8T_pct > 0.0:
        pairs.append("J8T")
        pair_pcts.append(float(portfolio.J8T_pct))
    if portfolio.INXT_pct > 0.0:
        pairs.append("INXT")
        pair_pcts.append(float(portfolio.INXT_pct))
    if portfolio.BRX_pct > 0.0:
        pairs.append("BRX")
        pair_pcts.append(float(portfolio.BRX_pct))
    if portfolio.VME_pct > 0.0:
        pairs.append("VME")
        pair_pcts.append(float(portfolio.VME_pct))
    if portfolio.BTCZ_pct > 0.0:
        pairs.append("BTCZ")
        pair_pcts.append(float(portfolio.BTCZ_pct))
    if portfolio.PTC_pct > 0.0:
        pairs.append("PTC")
        pair_pcts.append(float(portfolio.PTC_pct))
    if portfolio.MONK_pct > 0.0:
        pairs.append("MONK")
        pair_pcts.append(float(portfolio.MONK_pct))
    if portfolio.HUR_pct > 0.0:
        pairs.append("HUR")
        pair_pcts.append(float(portfolio.HUR_pct))
    if portfolio.GEO_pct > 0.0:
        pairs.append("GEO")
        pair_pcts.append(float(portfolio.GEO_pct))
    if portfolio.e_2GIVE_pct > 0.0:
        pairs.append("2GIVE")
        pair_pcts.append(float(portfolio.e_2GIVE_pct))
    if portfolio.ASTRO_pct > 0.0:
        pairs.append("ASTRO")
        pair_pcts.append(float(portfolio.ASTRO_pct))
    if portfolio.AUC_pct > 0.0:
        pairs.append("AUC")
        pair_pcts.append(float(portfolio.AUC_pct))
    if portfolio.DTH_pct > 0.0:
        pairs.append("DTH")
        pair_pcts.append(float(portfolio.DTH_pct))
    if portfolio.OTN_pct > 0.0:
        pairs.append("OTN")
        pair_pcts.append(float(portfolio.OTN_pct))
    if portfolio.BLUE_pct > 0.0:
        pairs.append("BLUE")
        pair_pcts.append(float(portfolio.BLUE_pct))
    if portfolio.PLAY_pct > 0.0:
        pairs.append("PLAY")
        pair_pcts.append(float(portfolio.PLAY_pct))
    if portfolio.XBC_pct > 0.0:
        pairs.append("XBC")
        pair_pcts.append(float(portfolio.XBC_pct))
    if portfolio.FND_pct > 0.0:
        pairs.append("FND")
        pair_pcts.append(float(portfolio.FND_pct))
    if portfolio.PFR_pct > 0.0:
        pairs.append("PFR")
        pair_pcts.append(float(portfolio.PFR_pct))
    if portfolio.HYP_pct > 0.0:
        pairs.append("HYP")
        pair_pcts.append(float(portfolio.HYP_pct))
    if portfolio.GCC_pct > 0.0:
        pairs.append("GCC")
        pair_pcts.append(float(portfolio.GCC_pct))
    if portfolio.IOP_pct > 0.0:
        pairs.append("IOP")
        pair_pcts.append(float(portfolio.IOP_pct))
    if portfolio.FDX_pct > 0.0:
        pairs.append("FDX")
        pair_pcts.append(float(portfolio.FDX_pct))
    if portfolio.ATL_pct > 0.0:
        pairs.append("ATL")
        pair_pcts.append(float(portfolio.ATL_pct))
    if portfolio.INSTAR_pct > 0.0:
        pairs.append("INSTAR")
        pair_pcts.append(float(portfolio.INSTAR_pct))
    if portfolio.HGT_pct > 0.0:
        pairs.append("HGT")
        pair_pcts.append(float(portfolio.HGT_pct))
    if portfolio.LEDU_pct > 0.0:
        pairs.append("LEDU")
        pair_pcts.append(float(portfolio.LEDU_pct))
    if portfolio.UNIT_pct > 0.0:
        pairs.append("UNIT")
        pair_pcts.append(float(portfolio.UNIT_pct))
    if portfolio.USNBT_pct > 0.0:
        pairs.append("USNBT")
        pair_pcts.append(float(portfolio.USNBT_pct))
    if portfolio.SUMO_pct > 0.0:
        pairs.append("SUMO")
        pair_pcts.append(float(portfolio.SUMO_pct))
    if portfolio.EXY_pct > 0.0:
        pairs.append("EXY")
        pair_pcts.append(float(portfolio.EXY_pct))
    if portfolio.e_0xBTC_pct > 0.0:
        pairs.append("0xBTC")
        pair_pcts.append(float(portfolio.e_0xBTC_pct))
    if portfolio.SPR_pct > 0.0:
        pairs.append("SPR")
        pair_pcts.append(float(portfolio.SPR_pct))
    if portfolio.ERC_pct > 0.0:
        pairs.append("ERC")
        pair_pcts.append(float(portfolio.ERC_pct))
    if portfolio.XHV_pct > 0.0:
        pairs.append("XHV")
        pair_pcts.append(float(portfolio.XHV_pct))
    if portfolio.INV_pct > 0.0:
        pairs.append("INV")
        pair_pcts.append(float(portfolio.INV_pct))
    if portfolio.CPAY_pct > 0.0:
        pairs.append("CPAY")
        pair_pcts.append(float(portfolio.CPAY_pct))
    if portfolio.IXC_pct > 0.0:
        pairs.append("IXC")
        pair_pcts.append(float(portfolio.IXC_pct))
    if portfolio.BUZZ_pct > 0.0:
        pairs.append("BUZZ")
        pair_pcts.append(float(portfolio.BUZZ_pct))
    if portfolio.BBO_pct > 0.0:
        pairs.append("BBO")
        pair_pcts.append(float(portfolio.BBO_pct))
    if portfolio.HAC_pct > 0.0:
        pairs.append("HAC")
        pair_pcts.append(float(portfolio.HAC_pct))
    if portfolio.BSTN_pct > 0.0:
        pairs.append("BSTN")
        pair_pcts.append(float(portfolio.BSTN_pct))
    if portfolio.NTRN_pct > 0.0:
        pairs.append("NTRN")
        pair_pcts.append(float(portfolio.NTRN_pct))
    if portfolio.XMCC_pct > 0.0:
        pairs.append("XMCC")
        pair_pcts.append(float(portfolio.XMCC_pct))
    if portfolio.SXUT_pct > 0.0:
        pairs.append("SXUT")
        pair_pcts.append(float(portfolio.SXUT_pct))
    if portfolio.UFR_pct > 0.0:
        pairs.append("UFR")
        pair_pcts.append(float(portfolio.UFR_pct))
    if portfolio.SPF_pct > 0.0:
        pairs.append("SPF")
        pair_pcts.append(float(portfolio.SPF_pct))
    if portfolio.GMT_pct > 0.0:
        pairs.append("GMT")
        pair_pcts.append(float(portfolio.GMT_pct))
    if portfolio.SEND_pct > 0.0:
        pairs.append("SEND")
        pair_pcts.append(float(portfolio.SEND_pct))
    if portfolio.AMLT_pct > 0.0:
        pairs.append("AMLT")
        pair_pcts.append(float(portfolio.AMLT_pct))
    if portfolio.SCL_pct > 0.0:
        pairs.append("SCL")
        pair_pcts.append(float(portfolio.SCL_pct))
    if portfolio.QWARK_pct > 0.0:
        pairs.append("QWARK")
        pair_pcts.append(float(portfolio.QWARK_pct))
    if portfolio.DOPE_pct > 0.0:
        pairs.append("DOPE")
        pair_pcts.append(float(portfolio.DOPE_pct))
    if portfolio.TKS_pct > 0.0:
        pairs.append("TKS")
        pair_pcts.append(float(portfolio.TKS_pct))
    if portfolio.MSR_pct > 0.0:
        pairs.append("MSR")
        pair_pcts.append(float(portfolio.MSR_pct))
    if portfolio.FTX_pct > 0.0:
        pairs.append("FTX")
        pair_pcts.append(float(portfolio.FTX_pct))
    if portfolio.TKA_pct > 0.0:
        pairs.append("TKA")
        pair_pcts.append(float(portfolio.TKA_pct))
    if portfolio.VRM_pct > 0.0:
        pairs.append("VRM")
        pair_pcts.append(float(portfolio.VRM_pct))
    if portfolio.RIC_pct > 0.0:
        pairs.append("RIC")
        pair_pcts.append(float(portfolio.RIC_pct))
    if portfolio.PING_pct > 0.0:
        pairs.append("PING")
        pair_pcts.append(float(portfolio.PING_pct))
    if portfolio.PBL_pct > 0.0:
        pairs.append("PBL")
        pair_pcts.append(float(portfolio.PBL_pct))
    if portfolio.RUPX_pct > 0.0:
        pairs.append("RUPX")
        pair_pcts.append(float(portfolio.RUPX_pct))
    if portfolio.GAT_pct > 0.0:
        pairs.append("GAT")
        pair_pcts.append(float(portfolio.GAT_pct))
    if portfolio.ZEIT_pct > 0.0:
        pairs.append("ZEIT")
        pair_pcts.append(float(portfolio.ZEIT_pct))
    if portfolio.VOISE_pct > 0.0:
        pairs.append("VOISE")
        pair_pcts.append(float(portfolio.VOISE_pct))
    if portfolio.ING_pct > 0.0:
        pairs.append("ING")
        pair_pcts.append(float(portfolio.ING_pct))
    if portfolio.EXCL_pct > 0.0:
        pairs.append("EXCL")
        pair_pcts.append(float(portfolio.EXCL_pct))
    if portfolio.HOLD_pct > 0.0:
        pairs.append("HOLD")
        pair_pcts.append(float(portfolio.HOLD_pct))
    if portfolio.WISH_pct > 0.0:
        pairs.append("WISH")
        pair_pcts.append(float(portfolio.WISH_pct))
    if portfolio.IND_pct > 0.0:
        pairs.append("IND")
        pair_pcts.append(float(portfolio.IND_pct))
    if portfolio.MEME_pct > 0.0:
        pairs.append("MEME")
        pair_pcts.append(float(portfolio.MEME_pct))
    if portfolio.ALT_pct > 0.0:
        pairs.append("ALT")
        pair_pcts.append(float(portfolio.ALT_pct))
    if portfolio.BON_pct > 0.0:
        pairs.append("BON")
        pair_pcts.append(float(portfolio.BON_pct))
    if portfolio.BRK_pct > 0.0:
        pairs.append("BRK")
        pair_pcts.append(float(portfolio.BRK_pct))
    if portfolio.EBST_pct > 0.0:
        pairs.append("EBST")
        pair_pcts.append(float(portfolio.EBST_pct))
    if portfolio.BTDX_pct > 0.0:
        pairs.append("BTDX")
        pair_pcts.append(float(portfolio.BTDX_pct))
    if portfolio.I0C_pct > 0.0:
        pairs.append("I0C")
        pair_pcts.append(float(portfolio.I0C_pct))
    if portfolio.TRC_pct > 0.0:
        pairs.append("TRC")
        pair_pcts.append(float(portfolio.TRC_pct))
    if portfolio.KRB_pct > 0.0:
        pairs.append("KRB")
        pair_pcts.append(float(portfolio.KRB_pct))
    if portfolio.SSS_pct > 0.0:
        pairs.append("SSS")
        pair_pcts.append(float(portfolio.SSS_pct))
    if portfolio.PURE_pct > 0.0:
        pairs.append("PURE")
        pair_pcts.append(float(portfolio.PURE_pct))
    if portfolio.XHI_pct > 0.0:
        pairs.append("XHI")
        pair_pcts.append(float(portfolio.XHI_pct))
    if portfolio.CRAVE_pct > 0.0:
        pairs.append("CRAVE")
        pair_pcts.append(float(portfolio.CRAVE_pct))
    if portfolio.ORE_pct > 0.0:
        pairs.append("ORE")
        pair_pcts.append(float(portfolio.ORE_pct))
    if portfolio.HUSH_pct > 0.0:
        pairs.append("HUSH")
        pair_pcts.append(float(portfolio.HUSH_pct))
    if portfolio.VTR_pct > 0.0:
        pairs.append("VTR")
        pair_pcts.append(float(portfolio.VTR_pct))
    if portfolio.ANC_pct > 0.0:
        pairs.append("ANC")
        pair_pcts.append(float(portfolio.ANC_pct))
    if portfolio.CMPCO_pct > 0.0:
        pairs.append("CMPCO")
        pair_pcts.append(float(portfolio.CMPCO_pct))
    if portfolio.ETBS_pct > 0.0:
        pairs.append("ETBS")
        pair_pcts.append(float(portfolio.ETBS_pct))
    if portfolio.REF_pct > 0.0:
        pairs.append("REF")
        pair_pcts.append(float(portfolio.REF_pct))
    if portfolio.DNR_pct > 0.0:
        pairs.append("DNR")
        pair_pcts.append(float(portfolio.DNR_pct))
    if portfolio.XGOX_pct > 0.0:
        pairs.append("XGOX")
        pair_pcts.append(float(portfolio.XGOX_pct))
    if portfolio.CHX_pct > 0.0:
        pairs.append("CHX")
        pair_pcts.append(float(portfolio.CHX_pct))
    if portfolio.MVC_pct > 0.0:
        pairs.append("MVC")
        pair_pcts.append(float(portfolio.MVC_pct))
    if portfolio.FOR_pct > 0.0:
        pairs.append("FOR")
        pair_pcts.append(float(portfolio.FOR_pct))
    if portfolio.CANN_pct > 0.0:
        pairs.append("CANN")
        pair_pcts.append(float(portfolio.CANN_pct))
    if portfolio.VIU_pct > 0.0:
        pairs.append("VIU")
        pair_pcts.append(float(portfolio.VIU_pct))
    if portfolio.NAVI_pct > 0.0:
        pairs.append("NAVI")
        pair_pcts.append(float(portfolio.NAVI_pct))
    if portfolio.FYP_pct > 0.0:
        pairs.append("FYP")
        pair_pcts.append(float(portfolio.FYP_pct))
    if portfolio.CPY_pct > 0.0:
        pairs.append("CPY")
        pair_pcts.append(float(portfolio.CPY_pct))
    if portfolio.STAC_pct > 0.0:
        pairs.append("STAC")
        pair_pcts.append(float(portfolio.STAC_pct))
    if portfolio.GENE_pct > 0.0:
        pairs.append("GENE")
        pair_pcts.append(float(portfolio.GENE_pct))
    if portfolio.SGR_pct > 0.0:
        pairs.append("SGR")
        pair_pcts.append(float(portfolio.SGR_pct))
    if portfolio.NIO_pct > 0.0:
        pairs.append("NIO")
        pair_pcts.append(float(portfolio.NIO_pct))
    if portfolio.PIX_pct > 0.0:
        pairs.append("PIX")
        pair_pcts.append(float(portfolio.PIX_pct))
    if portfolio.MAGE_pct > 0.0:
        pairs.append("MAGE")
        pair_pcts.append(float(portfolio.MAGE_pct))
    if portfolio.NLX_pct > 0.0:
        pairs.append("NLX")
        pair_pcts.append(float(portfolio.NLX_pct))
    if portfolio.EGC_pct > 0.0:
        pairs.append("EGC")
        pair_pcts.append(float(portfolio.EGC_pct))
    if portfolio.CL_pct > 0.0:
        pairs.append("CL")
        pair_pcts.append(float(portfolio.CL_pct))
    if portfolio.ZEPH_pct > 0.0:
        pairs.append("ZEPH")
        pair_pcts.append(float(portfolio.ZEPH_pct))
    if portfolio.MFG_pct > 0.0:
        pairs.append("MFG")
        pair_pcts.append(float(portfolio.MFG_pct))
    if portfolio.BBP_pct > 0.0:
        pairs.append("BBP")
        pair_pcts.append(float(portfolio.BBP_pct))
    if portfolio.BUN_pct > 0.0:
        pairs.append("BUN")
        pair_pcts.append(float(portfolio.BUN_pct))
    if portfolio.PYLNT_pct > 0.0:
        pairs.append("PYLNT")
        pair_pcts.append(float(portfolio.PYLNT_pct))
    if portfolio.CDX_pct > 0.0:
        pairs.append("CDX")
        pair_pcts.append(float(portfolio.CDX_pct))
    if portfolio.DAN_pct > 0.0:
        pairs.append("DAN")
        pair_pcts.append(float(portfolio.DAN_pct))
    if portfolio.TRAK_pct > 0.0:
        pairs.append("TRAK")
        pair_pcts.append(float(portfolio.TRAK_pct))
    if portfolio.LDOGE_pct > 0.0:
        pairs.append("LDOGE")
        pair_pcts.append(float(portfolio.LDOGE_pct))
    if portfolio.TES_pct > 0.0:
        pairs.append("TES")
        pair_pcts.append(float(portfolio.TES_pct))
    if portfolio.FGC_pct > 0.0:
        pairs.append("FGC")
        pair_pcts.append(float(portfolio.FGC_pct))
    if portfolio.AIX_pct > 0.0:
        pairs.append("AIX")
        pair_pcts.append(float(portfolio.AIX_pct))
    if portfolio.WSX_pct > 0.0:
        pairs.append("WSX")
        pair_pcts.append(float(portfolio.WSX_pct))
    if portfolio.MAC_pct > 0.0:
        pairs.append("MAC")
        pair_pcts.append(float(portfolio.MAC_pct))
    if portfolio.NOBL_pct > 0.0:
        pairs.append("NOBL")
        pair_pcts.append(float(portfolio.NOBL_pct))
    if portfolio.DP_pct > 0.0:
        pairs.append("DP")
        pair_pcts.append(float(portfolio.DP_pct))
    if portfolio.LOCI_pct > 0.0:
        pairs.append("LOCI")
        pair_pcts.append(float(portfolio.LOCI_pct))
    if portfolio.HIRE_pct > 0.0:
        pairs.append("HIRE")
        pair_pcts.append(float(portfolio.HIRE_pct))
    if portfolio.OPC_pct > 0.0:
        pairs.append("OPC")
        pair_pcts.append(float(portfolio.OPC_pct))
    if portfolio.GCN_pct > 0.0:
        pairs.append("GCN")
        pair_pcts.append(float(portfolio.GCN_pct))
    if portfolio.IC_pct > 0.0:
        pairs.append("IC")
        pair_pcts.append(float(portfolio.IC_pct))
    if portfolio.ACE_pct > 0.0:
        pairs.append("ACE")
        pair_pcts.append(float(portfolio.ACE_pct))
    if portfolio.BOUTS_pct > 0.0:
        pairs.append("BOUTS")
        pair_pcts.append(float(portfolio.BOUTS_pct))
    if portfolio.XNN_pct > 0.0:
        pairs.append("XNN")
        pair_pcts.append(float(portfolio.XNN_pct))
    if portfolio.CREA_pct > 0.0:
        pairs.append("CREA")
        pair_pcts.append(float(portfolio.CREA_pct))
    if portfolio.EFYT_pct > 0.0:
        pairs.append("EFYT")
        pair_pcts.append(float(portfolio.EFYT_pct))
    if portfolio.XTL_pct > 0.0:
        pairs.append("XTL")
        pair_pcts.append(float(portfolio.XTL_pct))
    if portfolio.TEAM_pct > 0.0:
        pairs.append("TEAM")
        pair_pcts.append(float(portfolio.TEAM_pct))
    if portfolio.XMG_pct > 0.0:
        pairs.append("XMG")
        pair_pcts.append(float(portfolio.XMG_pct))
    if portfolio.HUC_pct > 0.0:
        pairs.append("HUC")
        pair_pcts.append(float(portfolio.HUC_pct))
    if portfolio.RAIN_pct > 0.0:
        pairs.append("RAIN")
        pair_pcts.append(float(portfolio.RAIN_pct))
    if portfolio.MNTP_pct > 0.0:
        pairs.append("MNTP")
        pair_pcts.append(float(portfolio.MNTP_pct))
    if portfolio.TRCT_pct > 0.0:
        pairs.append("TRCT")
        pair_pcts.append(float(portfolio.TRCT_pct))
    if portfolio.EFL_pct > 0.0:
        pairs.append("EFL")
        pair_pcts.append(float(portfolio.EFL_pct))
    if portfolio.XBP_pct > 0.0:
        pairs.append("XBP")
        pair_pcts.append(float(portfolio.XBP_pct))
    if portfolio.BTW_pct > 0.0:
        pairs.append("BTW")
        pair_pcts.append(float(portfolio.BTW_pct))
    if portfolio.TZC_pct > 0.0:
        pairs.append("TZC")
        pair_pcts.append(float(portfolio.TZC_pct))
    if portfolio.DIX_pct > 0.0:
        pairs.append("DIX")
        pair_pcts.append(float(portfolio.DIX_pct))
    if portfolio.ODN_pct > 0.0:
        pairs.append("ODN")
        pair_pcts.append(float(portfolio.ODN_pct))
    if portfolio.STAK_pct > 0.0:
        pairs.append("STAK")
        pair_pcts.append(float(portfolio.STAK_pct))
    if portfolio.FT_pct > 0.0:
        pairs.append("FT")
        pair_pcts.append(float(portfolio.FT_pct))
    if portfolio.CRB_pct > 0.0:
        pairs.append("CRB")
        pair_pcts.append(float(portfolio.CRB_pct))
    if portfolio.HAT_pct > 0.0:
        pairs.append("HAT")
        pair_pcts.append(float(portfolio.HAT_pct))
    if portfolio.SWIFT_pct > 0.0:
        pairs.append("SWIFT")
        pair_pcts.append(float(portfolio.SWIFT_pct))
    if portfolio.ZER_pct > 0.0:
        pairs.append("ZER")
        pair_pcts.append(float(portfolio.ZER_pct))
    if portfolio.BYC_pct > 0.0:
        pairs.append("BYC")
        pair_pcts.append(float(portfolio.BYC_pct))
    if portfolio.AMM_pct > 0.0:
        pairs.append("AMM")
        pair_pcts.append(float(portfolio.AMM_pct))
    if portfolio.EBTC_pct > 0.0:
        pairs.append("EBTC")
        pair_pcts.append(float(portfolio.EBTC_pct))
    if portfolio.FRST_pct > 0.0:
        pairs.append("FRST")
        pair_pcts.append(float(portfolio.FRST_pct))
    if portfolio.ITNS_pct > 0.0:
        pairs.append("ITNS")
        pair_pcts.append(float(portfolio.ITNS_pct))
    if portfolio.ESZ_pct > 0.0:
        pairs.append("ESZ")
        pair_pcts.append(float(portfolio.ESZ_pct))
    if portfolio.BTRN_pct > 0.0:
        pairs.append("BTRN")
        pair_pcts.append(float(portfolio.BTRN_pct))
    if portfolio.UCOM_pct > 0.0:
        pairs.append("UCOM")
        pair_pcts.append(float(portfolio.UCOM_pct))
    if portfolio.SKIN_pct > 0.0:
        pairs.append("SKIN")
        pair_pcts.append(float(portfolio.SKIN_pct))
    if portfolio.MAG_pct > 0.0:
        pairs.append("MAG")
        pair_pcts.append(float(portfolio.MAG_pct))
    if portfolio.DGC_pct > 0.0:
        pairs.append("DGC")
        pair_pcts.append(float(portfolio.DGC_pct))
    if portfolio.VIVO_pct > 0.0:
        pairs.append("VIVO")
        pair_pcts.append(float(portfolio.VIVO_pct))
    if portfolio.PHO_pct > 0.0:
        pairs.append("PHO")
        pair_pcts.append(float(portfolio.PHO_pct))
    if portfolio.FCN_pct > 0.0:
        pairs.append("FCN")
        pair_pcts.append(float(portfolio.FCN_pct))
    if portfolio.MRT_pct > 0.0:
        pairs.append("MRT")
        pair_pcts.append(float(portfolio.MRT_pct))
    if portfolio.RNS_pct > 0.0:
        pairs.append("RNS")
        pair_pcts.append(float(portfolio.RNS_pct))
    if portfolio.SCT_pct > 0.0:
        pairs.append("SCT")
        pair_pcts.append(float(portfolio.SCT_pct))
    if portfolio.DAY_pct > 0.0:
        pairs.append("DAY")
        pair_pcts.append(float(portfolio.DAY_pct))
    if portfolio.JEW_pct > 0.0:
        pairs.append("JEW")
        pair_pcts.append(float(portfolio.JEW_pct))
    if portfolio.JC_pct > 0.0:
        pairs.append("JC")
        pair_pcts.append(float(portfolio.JC_pct))
    if portfolio.SGN_pct > 0.0:
        pairs.append("SGN")
        pair_pcts.append(float(portfolio.SGN_pct))
    if portfolio.ADZ_pct > 0.0:
        pairs.append("ADZ")
        pair_pcts.append(float(portfolio.ADZ_pct))
    if portfolio.HERO_pct > 0.0:
        pairs.append("HERO")
        pair_pcts.append(float(portfolio.HERO_pct))
    if portfolio.TDX_pct > 0.0:
        pairs.append("TDX")
        pair_pcts.append(float(portfolio.TDX_pct))
    if portfolio.ZNY_pct > 0.0:
        pairs.append("ZNY")
        pair_pcts.append(float(portfolio.ZNY_pct))
    if portfolio.e_808_pct > 0.0:
        pairs.append("808")
        pair_pcts.append(float(portfolio.e_808_pct))
    if portfolio.EPY_pct > 0.0:
        pairs.append("EPY")
        pair_pcts.append(float(portfolio.EPY_pct))
    if portfolio.TDS_pct > 0.0:
        pairs.append("TDS")
        pair_pcts.append(float(portfolio.TDS_pct))
    if portfolio.UIS_pct > 0.0:
        pairs.append("UIS")
        pair_pcts.append(float(portfolio.UIS_pct))
    if portfolio.DTRC_pct > 0.0:
        pairs.append("DTRC")
        pair_pcts.append(float(portfolio.DTRC_pct))
    if portfolio.ELLA_pct > 0.0:
        pairs.append("ELLA")
        pair_pcts.append(float(portfolio.ELLA_pct))
    if portfolio.EBCH_pct > 0.0:
        pairs.append("EBCH")
        pair_pcts.append(float(portfolio.EBCH_pct))
    if portfolio.UNB_pct > 0.0:
        pairs.append("UNB")
        pair_pcts.append(float(portfolio.UNB_pct))
    if portfolio.FYN_pct > 0.0:
        pairs.append("FYN")
        pair_pcts.append(float(portfolio.FYN_pct))
    if portfolio.TIG_pct > 0.0:
        pairs.append("TIG")
        pair_pcts.append(float(portfolio.TIG_pct))
    if portfolio.AMN_pct > 0.0:
        pairs.append("AMN")
        pair_pcts.append(float(portfolio.AMN_pct))
    if portfolio.ATS_pct > 0.0:
        pairs.append("ATS")
        pair_pcts.append(float(portfolio.ATS_pct))
    if portfolio.DFT_pct > 0.0:
        pairs.append("DFT")
        pair_pcts.append(float(portfolio.DFT_pct))
    if portfolio.NOX_pct > 0.0:
        pairs.append("NOX")
        pair_pcts.append(float(portfolio.NOX_pct))
    if portfolio.STU_pct > 0.0:
        pairs.append("STU")
        pair_pcts.append(float(portfolio.STU_pct))
    if portfolio.EARTH_pct > 0.0:
        pairs.append("EARTH")
        pair_pcts.append(float(portfolio.EARTH_pct))
    if portfolio.JIYO_pct > 0.0:
        pairs.append("JIYO")
        pair_pcts.append(float(portfolio.JIYO_pct))
    if portfolio.MEC_pct > 0.0:
        pairs.append("MEC")
        pair_pcts.append(float(portfolio.MEC_pct))
    if portfolio.ORI_pct > 0.0:
        pairs.append("ORI")
        pair_pcts.append(float(portfolio.ORI_pct))
    if portfolio.DRPU_pct > 0.0:
        pairs.append("DRPU")
        pair_pcts.append(float(portfolio.DRPU_pct))
    if portfolio.MORE_pct > 0.0:
        pairs.append("MORE")
        pair_pcts.append(float(portfolio.MORE_pct))
    if portfolio.INN_pct > 0.0:
        pairs.append("INN")
        pair_pcts.append(float(portfolio.INN_pct))
    if portfolio.EVC_pct > 0.0:
        pairs.append("EVC")
        pair_pcts.append(float(portfolio.EVC_pct))
    if portfolio.TNS_pct > 0.0:
        pairs.append("TNS")
        pair_pcts.append(float(portfolio.TNS_pct))
    if portfolio.LINX_pct > 0.0:
        pairs.append("LINX")
        pair_pcts.append(float(portfolio.LINX_pct))
    if portfolio.SAGA_pct > 0.0:
        pairs.append("SAGA")
        pair_pcts.append(float(portfolio.SAGA_pct))
    if portfolio.MBI_pct > 0.0:
        pairs.append("MBI")
        pair_pcts.append(float(portfolio.MBI_pct))
    if portfolio.ZET_pct > 0.0:
        pairs.append("ZET")
        pair_pcts.append(float(portfolio.ZET_pct))
    if portfolio.ARC_pct > 0.0:
        pairs.append("ARC")
        pair_pcts.append(float(portfolio.ARC_pct))
    if portfolio.EL_pct > 0.0:
        pairs.append("EL")
        pair_pcts.append(EL_pct(portfolio.EL_pct))
    if portfolio.UNIFY_pct > 0.0:
        pairs.append("UNIFY")
        pair_pcts.append(float(portfolio.UNIFY_pct))
    if portfolio.EQT_pct > 0.0:
        pairs.append("EQT")
        pair_pcts.append(float(portfolio.EQT_pct))
    if portfolio.VULC_pct > 0.0:
        pairs.append("VULC")
        pair_pcts.append(float(portfolio.VULC_pct))
    if portfolio.KLN_pct > 0.0:
        pairs.append("KLN")
        pair_pcts.append(float(portfolio.KLN_pct))
    if portfolio.QVT_pct > 0.0:
        pairs.append("QVT")
        pair_pcts.append(float(portfolio.QVT_pct))
    if portfolio.PLAN_pct > 0.0:
        pairs.append("PLAN")
        pair_pcts.append(float(portfolio.PLAN_pct))
    if portfolio.VRS_pct > 0.0:
        pairs.append("VRS")
        pair_pcts.append(float(portfolio.VRS_pct))
    if portfolio.IFLT_pct > 0.0:
        pairs.append("IFLT")
        pair_pcts.append(float(portfolio.IFLT_pct))
    if portfolio.BTA_pct > 0.0:
        pairs.append("BTA")
        pair_pcts.append(float(portfolio.BTA_pct))
    if portfolio.MCAP_pct > 0.0:
        pairs.append("MCAP")
        pair_pcts.append(float(portfolio.MCAP_pct))
    if portfolio.SUR_pct > 0.0:
        pairs.append("SUR")
        pair_pcts.append(float(portfolio.SUR_pct))
    if portfolio.HPC_pct > 0.0:
        pairs.append("HPC")
        pair_pcts.append(float(portfolio.HPC_pct))
    if portfolio.ELTCOIN_pct > 0.0:
        pairs.append("ELTCOIN")
        pair_pcts.append(float(portfolio.ELTCOIN_pct))
    if portfolio.XPD_pct > 0.0:
        pairs.append("XPD")
        pair_pcts.append(float(portfolio.XPD_pct))
    if portfolio.CRM_pct > 0.0:
        pairs.append("CRM")
        pair_pcts.append(float(portfolio.CRM_pct))
    if portfolio.RLT_pct > 0.0:
        pairs.append("RLT")
        pair_pcts.append(float(portfolio.RLT_pct))
    if portfolio.WILD_pct > 0.0:
        pairs.append("WILD")
        pair_pcts.append(float(portfolio.WILD_pct))
    if portfolio.XTO_pct > 0.0:
        pairs.append("XTO")
        pair_pcts.append(float(portfolio.XTO_pct))
    if portfolio.DGPT_pct > 0.0:
        pairs.append("DGPT")
        pair_pcts.append(float(portfolio.DGPT_pct))
    if portfolio.CJT_pct > 0.0:
        pairs.append("CJT")
        pair_pcts.append(float(portfolio.CJT_pct))
    if portfolio.BTB_pct > 0.0:
        pairs.append("BTB")
        pair_pcts.append(float(portfolio.BTB_pct))
    if portfolio.ZBC_pct > 0.0:
        pairs.append("ZBC")
        pair_pcts.append(float(portfolio.ZBC_pct))
    if portfolio.e_1337_pct > 0.0:
        pairs.append("1337")
        pair_pcts.append(float(portfolio.e_1337_pct))
    if portfolio.e_42_pct > 0.0:
        pairs.append("42")
        pair_pcts.append(float(portfolio.e_42_pct))
    if portfolio.GAM_pct > 0.0:
        pairs.append("GAM")
        pair_pcts.append(float(portfolio.GAM_pct))
    if portfolio.KB3_pct > 0.0:
        pairs.append("KB3")
        pair_pcts.append(float(portfolio.KB3_pct))
    if portfolio.NSR_pct > 0.0:
        pairs.append("NSR")
        pair_pcts.append(float(portfolio.NSR_pct))
    if portfolio.CRC_pct > 0.0:
        pairs.append("CRC")
        pair_pcts.append(float(portfolio.CRC_pct))
    if portfolio.BDL_pct > 0.0:
        pairs.append("BDL")
        pair_pcts.append(float(portfolio.BDL_pct))
    if portfolio.CHC_pct > 0.0:
        pairs.append("CHC")
        pair_pcts.append(float(portfolio.CHC_pct))
    if portfolio.GRMD_pct > 0.0:
        pairs.append("GRMD")
        pair_pcts.append(float(portfolio.GRMD_pct))
    if portfolio.MBRS_pct > 0.0:
        pairs.append("MBRS")
        pair_pcts.append(float(portfolio.MBRS_pct))
    if portfolio.EQL_pct > 0.0:
        pairs.append("EQL")
        pair_pcts.append(float(portfolio.EQL_pct))
    if portfolio.JET_pct > 0.0:
        pairs.append("JET")
        pair_pcts.append(float(portfolio.JET_pct))
    if portfolio.BITSILVER_pct > 0.0:
        pairs.append("BITSILVER")
        pair_pcts.append(float(portfolio.BITSILVER_pct))
    if portfolio.PIPL_pct > 0.0:
        pairs.append("PIPL")
        pair_pcts.append(float(portfolio.PIPL_pct))
    if portfolio.XCN_pct > 0.0:
        pairs.append("XCN")
        pair_pcts.append(float(portfolio.XCN_pct))
    if portfolio.BBI_pct > 0.0:
        pairs.append("BBI")
        pair_pcts.append(float(portfolio.BBI_pct))
    if portfolio.NMS_pct > 0.0:
        pairs.append("NMS")
        pair_pcts.append(float(portfolio.NMS_pct))
    if portfolio.OCT_pct > 0.0:
        pairs.append("OCT")
        pair_pcts.append(float(portfolio.OCT_pct))
    if portfolio.QBIC_pct > 0.0:
        pairs.append("QBIC")
        pair_pcts.append(float(portfolio.QBIC_pct))
    if portfolio.FANS_pct > 0.0:
        pairs.append("FANS")
        pair_pcts.append(float(portfolio.FANS_pct))
    if portfolio.ADC_pct > 0.0:
        pairs.append("ADC")
        pair_pcts.append(float(portfolio.ADC_pct))
    if portfolio.TRUST_pct > 0.0:
        pairs.append("TRUST")
        pair_pcts.append(float(portfolio.TRUST_pct))
    if portfolio.VZT_pct > 0.0:
        pairs.append("VZT")
        pair_pcts.append(float(portfolio.VZT_pct))
    if portfolio.TBX_pct > 0.0:
        pairs.append("TBX")
        pair_pcts.append(float(portfolio.TBX_pct))
    if portfolio.XRL_pct > 0.0:
        pairs.append("XRL")
        pair_pcts.append(float(portfolio.XRL_pct))
    if portfolio.ARG_pct > 0.0:
        pairs.append("ARG")
        pair_pcts.append(float(portfolio.ARG_pct))
    if portfolio.SMS_pct > 0.0:
        pairs.append("SMS")
        pair_pcts.append(float(portfolio.SMS_pct))
    if portfolio.CRED_pct > 0.0:
        pairs.append("CRED")
        pair_pcts.append(float(portfolio.CRED_pct))
    if portfolio.ONG_pct > 0.0:
        pairs.append("ONG")
        pair_pcts.append(float(portfolio.ONG_pct))
    if portfolio.DEW_pct > 0.0:
        pairs.append("DEW")
        pair_pcts.append(float(portfolio.DEW_pct))
    if portfolio.OPT_pct > 0.0:
        pairs.append("OPT")
        pair_pcts.append(float(portfolio.OPT_pct))
    if portfolio.DOVU_pct > 0.0:
        pairs.append("DOVU")
        pair_pcts.append(float(portfolio.DOVU_pct))
    if portfolio.DEM_pct > 0.0:
        pairs.append("DEM")
        pair_pcts.append(float(portfolio.DEM_pct))
    if portfolio.SXC_pct > 0.0:
        pairs.append("SXC")
        pair_pcts.append(float(portfolio.SXC_pct))
    if portfolio.HORSE_pct > 0.0:
        pairs.append("HORSE")
        pair_pcts.append(float(portfolio.HORSE_pct))
    if portfolio.LIVE_pct > 0.0:
        pairs.append("LIVE")
        pair_pcts.append(float(portfolio.LIVE_pct))
    return (pairs, pair_pcts)

def get_all_pairs(portfolio_ids):
    all_pairs = set()
    for i in range(len(portfolio_ids)):
        portfolio_id = portfolio_ids[i]
        # print("portfolio_id", portfolio_id)
        if int(portfolio_id) != -1:
            # print("entered")
            # print("portfolio.id", portfolio.id)
            # p = Portfolio.objects.get(pk = portfolio.id)
            # print("p.BTC_pct", p.BTC_pct)
            (pairs, _) = get_pairs_and_pcts(portfolio_id)
            # print("portfolio_id", portfolio_id, "pairs", pairs)
            # print("inside pairs", pairs)
            all_pairs = all_pairs.union(set(pairs))
    return list(all_pairs)

def get_latest_price_for_shorthand(shorthand):
    pricing_data = PricingData.objects.raw("select * from app_pricingdata where shorthand = '" + shorthand + "' order by created_at desc limit 1")
    return float(pricing_data[0].price)

def fill_investment(investment, portfolio, usd_amt):
    # print("(float(portfolio.BTC_pct) / 100.0)", ((float(portfolio.BTC_pct) / 100.0)))
    if portfolio.BTC_pct > 0.0:
        price = get_latest_price_for_shorthand("BTC")
        investment.BTC_amt = ((float(portfolio.BTC_pct) / 100.0) * usd_amt) / price
    if portfolio.ETH_pct > 0.0:
        price = get_latest_price_for_shorthand("ETH")
        investment.ETH_amt = ((float(portfolio.ETH_pct) / 100.0) * usd_amt) / price
    if portfolio.XRP_pct > 0.0:
        price = get_latest_price_for_shorthand("XRP")
        investment.XRP_amt = ((float(portfolio.XRP_pct) / 100.0) * usd_amt) / price
    if portfolio.BCH_pct > 0.0:
        price = get_latest_price_for_shorthand("BCH")
        investment.BCH_amt = ((float(portfolio.BCH_pct) / 100.0) * usd_amt) / price
    if portfolio.EOS_pct > 0.0:
        price = get_latest_price_for_shorthand("EOS")
        investment.EOS_amt = ((float(portfolio.EOS_pct) / 100.0) * usd_amt) / price
    if portfolio.LTC_pct > 0.0:
        price = get_latest_price_for_shorthand("LTC")
        investment.LTC_amt = ((float(portfolio.LTC_pct) / 100.0) * usd_amt) / price
    if portfolio.XLM_pct > 0.0:
        price = get_latest_price_for_shorthand("XLM")
        investment.XLM_amt = ((float(portfolio.XLM_pct) / 100.0) * usd_amt) / price
    if portfolio.ADA_pct > 0.0:
        price = get_latest_price_for_shorthand("ADA")
        investment.ADA_amt = ((float(portfolio.ADA_pct) / 100.0) * usd_amt) / price
    if portfolio.TRX_pct > 0.0:
        price = get_latest_price_for_shorthand("TRX")
        investment.TRX_amt = ((float(portfolio.TRX_pct) / 100.0) * usd_amt) / price
    if portfolio.MIOTA_pct > 0.0:
        price = get_latest_price_for_shorthand("MIOTA")
        investment.MIOTA_amt = ((float(portfolio.MIOTA_pct) / 100.0) * usd_amt) / price
    if portfolio.USDT_pct > 0.0:
        price = get_latest_price_for_shorthand("USDT")
        investment.USDT_amt = ((float(portfolio.USDT_pct) / 100.0) * usd_amt) / price
    if portfolio.NEO_pct > 0.0:
        price = get_latest_price_for_shorthand("NEO")
        investment.NEO_amt = ((float(portfolio.NEO_pct) / 100.0) * usd_amt) / price
    if portfolio.DASH_pct > 0.0:
        price = get_latest_price_for_shorthand("DASH")
        investment.DASH_amt = ((float(portfolio.DASH_pct) / 100.0) * usd_amt) / price
    if portfolio.XMR_pct > 0.0:
        price = get_latest_price_for_shorthand("XMR")
        investment.XMR_amt = ((float(portfolio.XMR_pct) / 100.0) * usd_amt) / price
    if portfolio.BNB_pct > 0.0:
        price = get_latest_price_for_shorthand("BNB")
        investment.BNB_amt = ((float(portfolio.BNB_pct) / 100.0) * usd_amt) / price
    if portfolio.VEN_pct > 0.0:
        price = get_latest_price_for_shorthand("VEN")
        investment.VEN_amt = ((float(portfolio.VEN_pct) / 100.0) * usd_amt) / price
    if portfolio.ETC_pct > 0.0:
        price = get_latest_price_for_shorthand("ETC")
        investment.ETC_amt = ((float(portfolio.ETC_pct) / 100.0) * usd_amt) / price
    if portfolio.XEM_pct > 0.0:
        price = get_latest_price_for_shorthand("XEM")
        investment.XEM_amt = ((float(portfolio.XEM_pct) / 100.0) * usd_amt) / price
    if portfolio.OMG_pct > 0.0:
        price = get_latest_price_for_shorthand("OMG")
        investment.OMG_amt = ((float(portfolio.OMG_pct) / 100.0) * usd_amt) / price
    if portfolio.QTUM_pct > 0.0:
        price = get_latest_price_for_shorthand("QTUM")
        investment.QTUM_amt = ((float(portfolio.QTUM_pct) / 100.0) * usd_amt) / price
    if portfolio.ONT_pct > 0.0:
        price = get_latest_price_for_shorthand("ONT")
        investment.ONT_amt = ((float(portfolio.ONT_pct) / 100.0) * usd_amt) / price
    if portfolio.ZEC_pct > 0.0:
        price = get_latest_price_for_shorthand("ZEC")
        investment.ZEC_amt = ((float(portfolio.ZEC_pct) / 100.0) * usd_amt) / price
    if portfolio.ICX_pct > 0.0:
        price = get_latest_price_for_shorthand("ICX")
        investment.ICX_amt = ((float(portfolio.ICX_pct) / 100.0) * usd_amt) / price
    if portfolio.LSK_pct > 0.0:
        price = get_latest_price_for_shorthand("LSK")
        investment.LSK_amt = ((float(portfolio.LSK_pct) / 100.0) * usd_amt) / price
    if portfolio.DCR_pct > 0.0:
        price = get_latest_price_for_shorthand("DCR")
        investment.DCR_amt = ((float(portfolio.DCR_pct) / 100.0) * usd_amt) / price
    if portfolio.BCN_pct > 0.0:
        price = get_latest_price_for_shorthand("BCN")
        investment.BCN_amt = ((float(portfolio.BCN_pct) / 100.0) * usd_amt) / price
    if portfolio.ZIL_pct > 0.0:
        price = get_latest_price_for_shorthand("ZIL")
        investment.ZIL_amt = ((float(portfolio.ZIL_pct) / 100.0) * usd_amt) / price
    if portfolio.AE_pct > 0.0:
        price = get_latest_price_for_shorthand("AE")
        investment.AE_amt = ((float(portfolio.AE_pct) / 100.0) * usd_amt) / price
    if portfolio.BTG_pct > 0.0:
        price = get_latest_price_for_shorthand("BTG")
        investment.BTG_amt = ((float(portfolio.BTG_pct) / 100.0) * usd_amt) / price
    if portfolio.BTM_pct > 0.0:
        price = get_latest_price_for_shorthand("BTM")
        investment.BTM_amt = ((float(portfolio.BTM_pct) / 100.0) * usd_amt) / price
    if portfolio.SC_pct > 0.0:
        price = get_latest_price_for_shorthand("SC")
        investment.SC_amt = ((float(portfolio.SC_pct) / 100.0) * usd_amt) / price
    if portfolio.ZRX_pct > 0.0:
        price = get_latest_price_for_shorthand("ZRX")
        investment.ZRX_amt = ((float(portfolio.ZRX_pct) / 100.0) * usd_amt) / price
    if portfolio.XVG_pct > 0.0:
        price = get_latest_price_for_shorthand("XVG")
        investment.XVG_amt = ((float(portfolio.XVG_pct) / 100.0) * usd_amt) / price
    if portfolio.BTS_pct > 0.0:
        price = get_latest_price_for_shorthand("BTS")
        investment.BTS_amt = ((float(portfolio.BTS_pct) / 100.0) * usd_amt) / price
    if portfolio.STEEM_pct > 0.0:
        price = get_latest_price_for_shorthand("STEEM")
        investment.STEEM_amt = ((float(portfolio.STEEM_pct) / 100.0) * usd_amt) / price
    if portfolio.MKR_pct > 0.0:
        price = get_latest_price_for_shorthand("MKR")
        investment.MKR_amt = ((float(portfolio.MKR_pct) / 100.0) * usd_amt) / price
    if portfolio.REP_pct > 0.0:
        price = get_latest_price_for_shorthand("REP")
        investment.REP_amt = ((float(portfolio.REP_pct) / 100.0) * usd_amt) / price
    if portfolio.NANO_pct > 0.0:
        price = get_latest_price_for_shorthand("NANO")
        investment.NANO_amt = ((float(portfolio.NANO_pct) / 100.0) * usd_amt) / price
    if portfolio.DOGE_pct > 0.0:
        price = get_latest_price_for_shorthand("DOGE")
        investment.DOGE_amt = ((float(portfolio.DOGE_pct) / 100.0) * usd_amt) / price
    if portfolio.RHOC_pct > 0.0:
        price = get_latest_price_for_shorthand("RHOC")
        investment.RHOC_amt = ((float(portfolio.RHOC_pct) / 100.0) * usd_amt) / price
    if portfolio.WAVES_pct > 0.0:
        price = get_latest_price_for_shorthand("WAVES")
        investment.WAVES_amt = ((float(portfolio.WAVES_pct) / 100.0) * usd_amt) / price
    if portfolio.BCD_pct > 0.0:
        price = get_latest_price_for_shorthand("BCD")
        investment.BCD_amt = ((float(portfolio.BCD_pct) / 100.0) * usd_amt) / price
    if portfolio.BAT_pct > 0.0:
        price = get_latest_price_for_shorthand("BAT")
        investment.BAT_amt = ((float(portfolio.BAT_pct) / 100.0) * usd_amt) / price
    if portfolio.WAN_pct > 0.0:
        price = get_latest_price_for_shorthand("WAN")
        investment.WAN_amt = ((float(portfolio.WAN_pct) / 100.0) * usd_amt) / price
    if portfolio.GNT_pct > 0.0:
        price = get_latest_price_for_shorthand("GNT")
        investment.GNT_amt = ((float(portfolio.GNT_pct) / 100.0) * usd_amt) / price
    if portfolio.BTCP_pct > 0.0:
        price = get_latest_price_for_shorthand("BTCP")
        investment.BTCP_amt = ((float(portfolio.BTCP_pct) / 100.0) * usd_amt) / price
    if portfolio.STRAT_pct > 0.0:
        price = get_latest_price_for_shorthand("STRAT")
        investment.STRAT_amt = ((float(portfolio.STRAT_pct) / 100.0) * usd_amt) / price
    if portfolio.DGB_pct > 0.0:
        price = get_latest_price_for_shorthand("DGB")
        investment.DGB_amt = ((float(portfolio.DGB_pct) / 100.0) * usd_amt) / price
    if portfolio.KCS_pct > 0.0:
        price = get_latest_price_for_shorthand("KCS")
        investment.KCS_amt = ((float(portfolio.KCS_pct) / 100.0) * usd_amt) / price
    if portfolio.WTC_pct > 0.0:
        price = get_latest_price_for_shorthand("WTC")
        investment.WTC_amt = ((float(portfolio.WTC_pct) / 100.0) * usd_amt) / price
    if portfolio.PPT_pct > 0.0:
        price = get_latest_price_for_shorthand("PPT")
        investment.PPT_amt = ((float(portfolio.PPT_pct) / 100.0) * usd_amt) / price
    if portfolio.SNT_pct > 0.0:
        price = get_latest_price_for_shorthand("SNT")
        investment.SNT_amt = ((float(portfolio.SNT_pct) / 100.0) * usd_amt) / price
    if portfolio.HSR_pct > 0.0:
        price = get_latest_price_for_shorthand("HSR")
        investment.HSR_amt = ((float(portfolio.HSR_pct) / 100.0) * usd_amt) / price
    if portfolio.DGD_pct > 0.0:
        price = get_latest_price_for_shorthand("DGD")
        investment.DGD_amt = ((float(portfolio.DGD_pct) / 100.0) * usd_amt) / price
    if portfolio.NAS_pct > 0.0:
        price = get_latest_price_for_shorthand("NAS")
        investment.NAS_amt = ((float(portfolio.NAS_pct) / 100.0) * usd_amt) / price
    if portfolio.HT_pct > 0.0:
        price = get_latest_price_for_shorthand("HT")
        investment.HT_amt = ((float(portfolio.HT_pct) / 100.0) * usd_amt) / price
    if portfolio.IOST_pct > 0.0:
        price = get_latest_price_for_shorthand("IOST")
        investment.IOST_amt = ((float(portfolio.IOST_pct) / 100.0) * usd_amt) / price
    if portfolio.AION_pct > 0.0:
        price = get_latest_price_for_shorthand("AION")
        investment.AION_amt = ((float(portfolio.AION_pct) / 100.0) * usd_amt) / price
    if portfolio.LRC_pct > 0.0:
        price = get_latest_price_for_shorthand("LRC")
        investment.LRC_amt = ((float(portfolio.LRC_pct) / 100.0) * usd_amt) / price
    if portfolio.KMD_pct > 0.0:
        price = get_latest_price_for_shorthand("KMD")
        investment.KMD_amt = ((float(portfolio.KMD_pct) / 100.0) * usd_amt) / price
    if portfolio.GXS_pct > 0.0:
        price = get_latest_price_for_shorthand("GXS")
        investment.GXS_amt = ((float(portfolio.GXS_pct) / 100.0) * usd_amt) / price
    if portfolio.CNX_pct > 0.0:
        price = get_latest_price_for_shorthand("CNX")
        investment.CNX_amt = ((float(portfolio.CNX_pct) / 100.0) * usd_amt) / price
    if portfolio.RDD_pct > 0.0:
        price = get_latest_price_for_shorthand("RDD")
        investment.RDD_amt = ((float(portfolio.RDD_pct) / 100.0) * usd_amt) / price
    if portfolio.BNT_pct > 0.0:
        price = get_latest_price_for_shorthand("BNT")
        investment.BNT_amt = ((float(portfolio.BNT_pct) / 100.0) * usd_amt) / price
    if portfolio.ARDR_pct > 0.0:
        price = get_latest_price_for_shorthand("ARDR")
        investment.ARDR_amt = ((float(portfolio.ARDR_pct) / 100.0) * usd_amt) / price
    if portfolio.MAID_pct > 0.0:
        price = get_latest_price_for_shorthand("MAID")
        investment.MAID_amt = ((float(portfolio.MAID_pct) / 100.0) * usd_amt) / price
    if portfolio.ARK_pct > 0.0:
        price = get_latest_price_for_shorthand("ARK")
        investment.ARK_amt = ((float(portfolio.ARK_pct) / 100.0) * usd_amt) / price
    if portfolio.MOAC_pct > 0.0:
        price = get_latest_price_for_shorthand("MOAC")
        investment.MOAC_amt = ((float(portfolio.MOAC_pct) / 100.0) * usd_amt) / price
    if portfolio.MONA_pct > 0.0:
        price = get_latest_price_for_shorthand("MONA")
        investment.MONA_amt = ((float(portfolio.MONA_pct) / 100.0) * usd_amt) / price
    if portfolio.ELF_pct > 0.0:
        price = get_latest_price_for_shorthand("ELF")
        investment.ELF_amt = ((float(portfolio.ELF_pct) / 100.0) * usd_amt) / price
    if portfolio.CENNZ_pct > 0.0:
        price = get_latest_price_for_shorthand("CENNZ")
        investment.CENNZ_amt = ((float(portfolio.CENNZ_pct) / 100.0) * usd_amt) / price
    if portfolio.DCN_pct > 0.0:
        price = get_latest_price_for_shorthand("DCN")
        investment.DCN_amt = ((float(portfolio.DCN_pct) / 100.0) * usd_amt) / price
    if portfolio.FUN_pct > 0.0:
        price = get_latest_price_for_shorthand("FUN")
        investment.FUN_amt = ((float(portfolio.FUN_pct) / 100.0) * usd_amt) / price
    if portfolio.BIX_pct > 0.0:
        price = get_latest_price_for_shorthand("BIX")
        investment.BIX_amt = ((float(portfolio.BIX_pct) / 100.0) * usd_amt) / price
    if portfolio.GAS_pct > 0.0:
        price = get_latest_price_for_shorthand("GAS")
        investment.GAS_amt = ((float(portfolio.GAS_pct) / 100.0) * usd_amt) / price
    if portfolio.MITH_pct > 0.0:
        price = get_latest_price_for_shorthand("MITH")
        investment.MITH_amt = ((float(portfolio.MITH_pct) / 100.0) * usd_amt) / price
    if portfolio.ENG_pct > 0.0:
        price = get_latest_price_for_shorthand("ENG")
        investment.ENG_amt = ((float(portfolio.ENG_pct) / 100.0) * usd_amt) / price
    if portfolio.PIVX_pct > 0.0:
        price = get_latest_price_for_shorthand("PIVX")
        investment.PIVX_amt = ((float(portfolio.PIVX_pct) / 100.0) * usd_amt) / price
    if portfolio.VERI_pct > 0.0:
        price = get_latest_price_for_shorthand("VERI")
        investment.VERI_amt = ((float(portfolio.VERI_pct) / 100.0) * usd_amt) / price
    if portfolio.KNC_pct > 0.0:
        price = get_latest_price_for_shorthand("KNC")
        investment.KNC_amt = ((float(portfolio.KNC_pct) / 100.0) * usd_amt) / price
    if portfolio.ELA_pct > 0.0:
        price = get_latest_price_for_shorthand("ELA")
        investment.ELA_amt = ((float(portfolio.ELA_pct) / 100.0) * usd_amt) / price
    if portfolio.EMC_pct > 0.0:
        price = get_latest_price_for_shorthand("EMC")
        investment.EMC_amt = ((float(portfolio.EMC_pct) / 100.0) * usd_amt) / price
    if portfolio.FSN_pct > 0.0:
        price = get_latest_price_for_shorthand("FSN")
        investment.FSN_amt = ((float(portfolio.FSN_pct) / 100.0) * usd_amt) / price
    if portfolio.SYS_pct > 0.0:
        price = get_latest_price_for_shorthand("SYS")
        investment.SYS_amt = ((float(portfolio.SYS_pct) / 100.0) * usd_amt) / price
    if portfolio.DROP_pct > 0.0:
        price = get_latest_price_for_shorthand("DROP")
        investment.DROP_amt = ((float(portfolio.DROP_pct) / 100.0) * usd_amt) / price
    if portfolio.CMT_pct > 0.0:
        price = get_latest_price_for_shorthand("CMT")
        investment.CMT_amt = ((float(portfolio.CMT_pct) / 100.0) * usd_amt) / price
    if portfolio.KIN_pct > 0.0:
        price = get_latest_price_for_shorthand("KIN")
        investment.KIN_amt = ((float(portfolio.KIN_pct) / 100.0) * usd_amt) / price
    if portfolio.MANA_pct > 0.0:
        price = get_latest_price_for_shorthand("MANA")
        investment.MANA_amt = ((float(portfolio.MANA_pct) / 100.0) * usd_amt) / price
    if portfolio.NXT_pct > 0.0:
        price = get_latest_price_for_shorthand("NXT")
        investment.NXT_amt = ((float(portfolio.NXT_pct) / 100.0) * usd_amt) / price
    if portfolio.ETHOS_pct > 0.0:
        price = get_latest_price_for_shorthand("ETHOS")
        investment.ETHOS_amt = ((float(portfolio.ETHOS_pct) / 100.0) * usd_amt) / price
    if portfolio.DDD_pct > 0.0:
        price = get_latest_price_for_shorthand("DDD")
        investment.DDD_amt = ((float(portfolio.DDD_pct) / 100.0) * usd_amt) / price
    if portfolio.QASH_pct > 0.0:
        price = get_latest_price_for_shorthand("QASH")
        investment.QASH_amt = ((float(portfolio.QASH_pct) / 100.0) * usd_amt) / price
    if portfolio.DRGN_pct > 0.0:
        price = get_latest_price_for_shorthand("DRGN")
        investment.DRGN_amt = ((float(portfolio.DRGN_pct) / 100.0) * usd_amt) / price
    if portfolio.FCT_pct > 0.0:
        price = get_latest_price_for_shorthand("FCT")
        investment.FCT_amt = ((float(portfolio.FCT_pct) / 100.0) * usd_amt) / price
    if portfolio.LOOM_pct > 0.0:
        price = get_latest_price_for_shorthand("LOOM")
        investment.LOOM_amt = ((float(portfolio.LOOM_pct) / 100.0) * usd_amt) / price
    if portfolio.MTC_pct > 0.0:
        price = get_latest_price_for_shorthand("MTC")
        investment.MTC_amt = ((float(portfolio.MTC_pct) / 100.0) * usd_amt) / price
    if portfolio.GTC_pct > 0.0:
        price = get_latest_price_for_shorthand("GTC")
        investment.GTC_amt = ((float(portfolio.GTC_pct) / 100.0) * usd_amt) / price
    if portfolio.XZC_pct > 0.0:
        price = get_latest_price_for_shorthand("XZC")
        investment.XZC_amt = ((float(portfolio.XZC_pct) / 100.0) * usd_amt) / price
    if portfolio.POLY_pct > 0.0:
        price = get_latest_price_for_shorthand("POLY")
        investment.POLY_amt = ((float(portfolio.POLY_pct) / 100.0) * usd_amt) / price
    if portfolio.NULS_pct > 0.0:
        price = get_latest_price_for_shorthand("NULS")
        investment.NULS_amt = ((float(portfolio.NULS_pct) / 100.0) * usd_amt) / price
    if portfolio.SMART_pct > 0.0:
        price = get_latest_price_for_shorthand("SMART")
        investment.SMART_amt = ((float(portfolio.SMART_pct) / 100.0) * usd_amt) / price
    if portfolio.SUB_pct > 0.0:
        price = get_latest_price_for_shorthand("SUB")
        investment.SUB_amt = ((float(portfolio.SUB_pct) / 100.0) * usd_amt) / price
    if portfolio.CTXC_pct > 0.0:
        price = get_latest_price_for_shorthand("CTXC")
        investment.CTXC_amt = ((float(portfolio.CTXC_pct) / 100.0) * usd_amt) / price
    if portfolio.THETA_pct > 0.0:
        price = get_latest_price_for_shorthand("THETA")
        investment.THETA_amt = ((float(portfolio.THETA_pct) / 100.0) * usd_amt) / price
    if portfolio.BFT_pct > 0.0:
        price = get_latest_price_for_shorthand("BFT")
        investment.BFT_amt = ((float(portfolio.BFT_pct) / 100.0) * usd_amt) / price
    if portfolio.PAYX_pct > 0.0:
        price = get_latest_price_for_shorthand("PAYX")
        investment.PAYX_amt = ((float(portfolio.PAYX_pct) / 100.0) * usd_amt) / price
    if portfolio.STORM_pct > 0.0:
        price = get_latest_price_for_shorthand("STORM")
        investment.STORM_amt = ((float(portfolio.STORM_pct) / 100.0) * usd_amt) / price
    if portfolio.POWR_pct > 0.0:
        price = get_latest_price_for_shorthand("POWR")
        investment.POWR_amt = ((float(portfolio.POWR_pct) / 100.0) * usd_amt) / price
    if portfolio.BLOCK_pct > 0.0:
        price = get_latest_price_for_shorthand("BLOCK")
        investment.BLOCK_amt = ((float(portfolio.BLOCK_pct) / 100.0) * usd_amt) / price
    if portfolio.NXS_pct > 0.0:
        price = get_latest_price_for_shorthand("NXS")
        investment.NXS_amt = ((float(portfolio.NXS_pct) / 100.0) * usd_amt) / price
    if portfolio.MCO_pct > 0.0:
        price = get_latest_price_for_shorthand("MCO")
        investment.MCO_amt = ((float(portfolio.MCO_pct) / 100.0) * usd_amt) / price
    if portfolio.ETN_pct > 0.0:
        price = get_latest_price_for_shorthand("ETN")
        investment.ETN_amt = ((float(portfolio.ETN_pct) / 100.0) * usd_amt) / price
    if portfolio.GBYTE_pct > 0.0:
        price = get_latest_price_for_shorthand("GBYTE")
        investment.GBYTE_amt = ((float(portfolio.GBYTE_pct) / 100.0) * usd_amt) / price
    if portfolio.WAX_pct > 0.0:
        price = get_latest_price_for_shorthand("WAX")
        investment.WAX_amt = ((float(portfolio.WAX_pct) / 100.0) * usd_amt) / price
    if portfolio.TUSD_pct > 0.0:
        price = get_latest_price_for_shorthand("TUSD")
        investment.TUSD_amt = ((float(portfolio.TUSD_pct) / 100.0) * usd_amt) / price
    if portfolio.ZEN_pct > 0.0:
        price = get_latest_price_for_shorthand("ZEN")
        investment.ZEN_amt = ((float(portfolio.ZEN_pct) / 100.0) * usd_amt) / price
    if portfolio.WICC_pct > 0.0:
        price = get_latest_price_for_shorthand("WICC")
        investment.WICC_amt = ((float(portfolio.WICC_pct) / 100.0) * usd_amt) / price
    if portfolio.EOSDAC_pct > 0.0:
        price = get_latest_price_for_shorthand("EOSDAC")
        investment.EOSDAC_amt = ((float(portfolio.EOSDAC_pct) / 100.0) * usd_amt) / price
    if portfolio.RLC_pct > 0.0:
        price = get_latest_price_for_shorthand("RLC")
        investment.RLC_amt = ((float(portfolio.RLC_pct) / 100.0) * usd_amt) / price
    if portfolio.GTO_pct > 0.0:
        price = get_latest_price_for_shorthand("GTO")
        investment.GTO_amt = ((float(portfolio.GTO_pct) / 100.0) * usd_amt) / price
    if portfolio.R_pct > 0.0:
        price = get_latest_price_for_shorthand("R")
        investment.R_amt = ((float(portfolio.R_pct) / 100.0) * usd_amt) / price
    if portfolio.DBC_pct > 0.0:
        price = get_latest_price_for_shorthand("DBC")
        investment.DBC_amt = ((float(portfolio.DBC_pct) / 100.0) * usd_amt) / price
    if portfolio.LINK_pct > 0.0:
        price = get_latest_price_for_shorthand("LINK")
        investment.LINK_amt = ((float(portfolio.LINK_pct) / 100.0) * usd_amt) / price
    if portfolio.SNM_pct > 0.0:
        price = get_latest_price_for_shorthand("SNM")
        investment.SNM_amt = ((float(portfolio.SNM_pct) / 100.0) * usd_amt) / price
    if portfolio.STORJ_pct > 0.0:
        price = get_latest_price_for_shorthand("STORJ")
        investment.STORJ_amt = ((float(portfolio.STORJ_pct) / 100.0) * usd_amt) / price
    if portfolio.MAN_pct > 0.0:
        price = get_latest_price_for_shorthand("MAN")
        investment.MAN_amt = ((float(portfolio.MAN_pct) / 100.0) * usd_amt) / price
    if portfolio.ICN_pct > 0.0:
        price = get_latest_price_for_shorthand("ICN")
        investment.ICN_amt = ((float(portfolio.ICN_pct) / 100.0) * usd_amt) / price
    if portfolio.SALT_pct > 0.0:
        price = get_latest_price_for_shorthand("SALT")
        investment.SALT_amt = ((float(portfolio.SALT_pct) / 100.0) * usd_amt) / price
    if portfolio.NEXO_pct > 0.0:
        price = get_latest_price_for_shorthand("NEXO")
        investment.NEXO_amt = ((float(portfolio.NEXO_pct) / 100.0) * usd_amt) / price
    if portfolio.DATA_pct > 0.0:
        price = get_latest_price_for_shorthand("DATA")
        investment.DATA_amt = ((float(portfolio.DATA_pct) / 100.0) * usd_amt) / price
    if portfolio.BTCD_pct > 0.0:
        price = get_latest_price_for_shorthand("BTCD")
        investment.BTCD_amt = ((float(portfolio.BTCD_pct) / 100.0) * usd_amt) / price
    if portfolio.HOT_pct > 0.0:
        price = get_latest_price_for_shorthand("HOT")
        investment.HOT_amt = ((float(portfolio.HOT_pct) / 100.0) * usd_amt) / price
    if portfolio.CVC_pct > 0.0:
        price = get_latest_price_for_shorthand("CVC")
        investment.CVC_amt = ((float(portfolio.CVC_pct) / 100.0) * usd_amt) / price
    if portfolio.REQ_pct > 0.0:
        price = get_latest_price_for_shorthand("REQ")
        investment.REQ_amt = ((float(portfolio.REQ_pct) / 100.0) * usd_amt) / price
    if portfolio.NCASH_pct > 0.0:
        price = get_latest_price_for_shorthand("NCASH")
        investment.NCASH_amt = ((float(portfolio.NCASH_pct) / 100.0) * usd_amt) / price
    if portfolio.PAY_pct > 0.0:
        price = get_latest_price_for_shorthand("PAY")
        investment.PAY_amt = ((float(portfolio.PAY_pct) / 100.0) * usd_amt) / price
    if portfolio.AGI_pct > 0.0:
        price = get_latest_price_for_shorthand("AGI")
        investment.AGI_amt = ((float(portfolio.AGI_pct) / 100.0) * usd_amt) / price
    if portfolio.HPB_pct > 0.0:
        price = get_latest_price_for_shorthand("HPB")
        investment.HPB_amt = ((float(portfolio.HPB_pct) / 100.0) * usd_amt) / price
    if portfolio.SKY_pct > 0.0:
        price = get_latest_price_for_shorthand("SKY")
        investment.SKY_amt = ((float(portfolio.SKY_pct) / 100.0) * usd_amt) / price
    if portfolio.TNB_pct > 0.0:
        price = get_latest_price_for_shorthand("TNB")
        investment.TNB_amt = ((float(portfolio.TNB_pct) / 100.0) * usd_amt) / price
    if portfolio.ACT_pct > 0.0:
        price = get_latest_price_for_shorthand("ACT")
        investment.ACT_amt = ((float(portfolio.ACT_pct) / 100.0) * usd_amt) / price
    if portfolio.XAS_pct > 0.0:
        price = get_latest_price_for_shorthand("XAS")
        investment.XAS_amt = ((float(portfolio.XAS_pct) / 100.0) * usd_amt) / price
    if portfolio.CVT_pct > 0.0:
        price = get_latest_price_for_shorthand("CVT")
        investment.CVT_amt = ((float(portfolio.CVT_pct) / 100.0) * usd_amt) / price
    if portfolio.ANT_pct > 0.0:
        price = get_latest_price_for_shorthand("ANT")
        investment.ANT_amt = ((float(portfolio.ANT_pct) / 100.0) * usd_amt) / price
    if portfolio.BCI_pct > 0.0:
        price = get_latest_price_for_shorthand("BCI")
        investment.BCI_amt = ((float(portfolio.BCI_pct) / 100.0) * usd_amt) / price
    if portfolio.GNO_pct > 0.0:
        price = get_latest_price_for_shorthand("GNO")
        investment.GNO_amt = ((float(portfolio.GNO_pct) / 100.0) * usd_amt) / price
    if portfolio.MDS_pct > 0.0:
        price = get_latest_price_for_shorthand("MDS")
        investment.MDS_amt = ((float(portfolio.MDS_pct) / 100.0) * usd_amt) / price
    if portfolio.NEBL_pct > 0.0:
        price = get_latest_price_for_shorthand("NEBL")
        investment.NEBL_amt = ((float(portfolio.NEBL_pct) / 100.0) * usd_amt) / price
    if portfolio.BTO_pct > 0.0:
        price = get_latest_price_for_shorthand("BTO")
        investment.BTO_amt = ((float(portfolio.BTO_pct) / 100.0) * usd_amt) / price
    if portfolio.SAN_pct > 0.0:
        price = get_latest_price_for_shorthand("SAN")
        investment.SAN_amt = ((float(portfolio.SAN_pct) / 100.0) * usd_amt) / price
    if portfolio.RUFF_pct > 0.0:
        price = get_latest_price_for_shorthand("RUFF")
        investment.RUFF_amt = ((float(portfolio.RUFF_pct) / 100.0) * usd_amt) / price
    if portfolio.ABT_pct > 0.0:
        price = get_latest_price_for_shorthand("ABT")
        investment.ABT_amt = ((float(portfolio.ABT_pct) / 100.0) * usd_amt) / price
    if portfolio.TRUE_pct > 0.0:
        price = get_latest_price_for_shorthand("TRUE")
        investment.TRUE_amt = ((float(portfolio.TRUE_pct) / 100.0) * usd_amt) / price
    if portfolio.CND_pct > 0.0:
        price = get_latest_price_for_shorthand("CND")
        investment.CND_amt = ((float(portfolio.CND_pct) / 100.0) * usd_amt) / price
    if portfolio.EKT_pct > 0.0:
        price = get_latest_price_for_shorthand("EKT")
        investment.EKT_amt = ((float(portfolio.EKT_pct) / 100.0) * usd_amt) / price
    if portfolio.GAME_pct > 0.0:
        price = get_latest_price_for_shorthand("GAME")
        investment.GAME_amt = ((float(portfolio.GAME_pct) / 100.0) * usd_amt) / price
    if portfolio.SMT_pct > 0.0:
        price = get_latest_price_for_shorthand("SMT")
        investment.SMT_amt = ((float(portfolio.SMT_pct) / 100.0) * usd_amt) / price
    if portfolio.DENT_pct > 0.0:
        price = get_latest_price_for_shorthand("DENT")
        investment.DENT_amt = ((float(portfolio.DENT_pct) / 100.0) * usd_amt) / price
    if portfolio.GRS_pct > 0.0:
        price = get_latest_price_for_shorthand("GRS")
        investment.GRS_amt = ((float(portfolio.GRS_pct) / 100.0) * usd_amt) / price
    if portfolio.DTR_pct > 0.0:
        price = get_latest_price_for_shorthand("DTR")
        investment.DTR_amt = ((float(portfolio.DTR_pct) / 100.0) * usd_amt) / price
    if portfolio.CRPT_pct > 0.0:
        price = get_latest_price_for_shorthand("CRPT")
        investment.CRPT_amt = ((float(portfolio.CRPT_pct) / 100.0) * usd_amt) / price
    if portfolio.QSP_pct > 0.0:
        price = get_latest_price_for_shorthand("QSP")
        investment.QSP_amt = ((float(portfolio.QSP_pct) / 100.0) * usd_amt) / price
    if portfolio.DAI_pct > 0.0:
        price = get_latest_price_for_shorthand("DAI")
        investment.DAI_amt = ((float(portfolio.DAI_pct) / 100.0) * usd_amt) / price
    if portfolio.SOC_pct > 0.0:
        price = get_latest_price_for_shorthand("SOC")
        investment.SOC_amt = ((float(portfolio.SOC_pct) / 100.0) * usd_amt) / price
    if portfolio.CS_pct > 0.0:
        price = get_latest_price_for_shorthand("CS")
        investment.CS_amt = ((float(portfolio.CS_pct) / 100.0) * usd_amt) / price
    if portfolio.IGNIS_pct > 0.0:
        price = get_latest_price_for_shorthand("IGNIS")
        investment.IGNIS_amt = ((float(portfolio.IGNIS_pct) / 100.0) * usd_amt) / price
    if portfolio.XDN_pct > 0.0:
        price = get_latest_price_for_shorthand("XDN")
        investment.XDN_amt = ((float(portfolio.XDN_pct) / 100.0) * usd_amt) / price
    if portfolio.PLR_pct > 0.0:
        price = get_latest_price_for_shorthand("PLR")
        investment.PLR_amt = ((float(portfolio.PLR_pct) / 100.0) * usd_amt) / price
    if portfolio.ENJ_pct > 0.0:
        price = get_latest_price_for_shorthand("ENJ")
        investment.ENJ_amt = ((float(portfolio.ENJ_pct) / 100.0) * usd_amt) / price
    if portfolio.C20_pct > 0.0:
        price = get_latest_price_for_shorthand("C20")
        investment.C20_amt = ((float(portfolio.C20_pct) / 100.0) * usd_amt) / price
    if portfolio.STQ_pct > 0.0:
        price = get_latest_price_for_shorthand("STQ")
        investment.STQ_amt = ((float(portfolio.STQ_pct) / 100.0) * usd_amt) / price
    if portfolio.VTC_pct > 0.0:
        price = get_latest_price_for_shorthand("VTC")
        investment.VTC_amt = ((float(portfolio.VTC_pct) / 100.0) * usd_amt) / price
    if portfolio.BLZ_pct > 0.0:
        price = get_latest_price_for_shorthand("BLZ")
        investment.BLZ_amt = ((float(portfolio.BLZ_pct) / 100.0) * usd_amt) / price
    if portfolio.TKY_pct > 0.0:
        price = get_latest_price_for_shorthand("TKY")
        investment.TKY_amt = ((float(portfolio.TKY_pct) / 100.0) * usd_amt) / price
    if portfolio.BOS_pct > 0.0:
        price = get_latest_price_for_shorthand("BOS")
        investment.BOS_amt = ((float(portfolio.BOS_pct) / 100.0) * usd_amt) / price
    if portfolio.PART_pct > 0.0:
        price = get_latest_price_for_shorthand("PART")
        investment.PART_amt = ((float(portfolio.PART_pct) / 100.0) * usd_amt) / price
    if portfolio.XSN_pct > 0.0:
        price = get_latest_price_for_shorthand("XSN")
        investment.XSN_amt = ((float(portfolio.XSN_pct) / 100.0) * usd_amt) / price
    if portfolio.EDR_pct > 0.0:
        price = get_latest_price_for_shorthand("EDR")
        investment.EDR_amt = ((float(portfolio.EDR_pct) / 100.0) * usd_amt) / price
    if portfolio.TPAY_pct > 0.0:
        price = get_latest_price_for_shorthand("TPAY")
        investment.TPAY_amt = ((float(portfolio.TPAY_pct) / 100.0) * usd_amt) / price
    if portfolio.RDN_pct > 0.0:
        price = get_latest_price_for_shorthand("RDN")
        investment.RDN_amt = ((float(portfolio.RDN_pct) / 100.0) * usd_amt) / price
    if portfolio.AMB_pct > 0.0:
        price = get_latest_price_for_shorthand("AMB")
        investment.AMB_amt = ((float(portfolio.AMB_pct) / 100.0) * usd_amt) / price
    if portfolio.QKC_pct > 0.0:
        price = get_latest_price_for_shorthand("QKC")
        investment.QKC_amt = ((float(portfolio.QKC_pct) / 100.0) * usd_amt) / price
    if portfolio.OCN_pct > 0.0:
        price = get_latest_price_for_shorthand("OCN")
        investment.OCN_amt = ((float(portfolio.OCN_pct) / 100.0) * usd_amt) / price
    if portfolio.GNX_pct > 0.0:
        price = get_latest_price_for_shorthand("GNX")
        investment.GNX_amt = ((float(portfolio.GNX_pct) / 100.0) * usd_amt) / price
    if portfolio.PPC_pct > 0.0:
        price = get_latest_price_for_shorthand("PPC")
        investment.PPC_amt = ((float(portfolio.PPC_pct) / 100.0) * usd_amt) / price
    if portfolio.BRD_pct > 0.0:
        price = get_latest_price_for_shorthand("BRD")
        investment.BRD_amt = ((float(portfolio.BRD_pct) / 100.0) * usd_amt) / price
    if portfolio.ODE_pct > 0.0:
        price = get_latest_price_for_shorthand("ODE")
        investment.ODE_amt = ((float(portfolio.ODE_pct) / 100.0) * usd_amt) / price
    if portfolio.NKN_pct > 0.0:
        price = get_latest_price_for_shorthand("NKN")
        investment.NKN_amt = ((float(portfolio.NKN_pct) / 100.0) * usd_amt) / price
    if portfolio.ZCL_pct > 0.0:
        price = get_latest_price_for_shorthand("ZCL")
        investment.ZCL_amt = ((float(portfolio.ZCL_pct) / 100.0) * usd_amt) / price
    if portfolio.POA_pct > 0.0:
        price = get_latest_price_for_shorthand("POA")
        investment.POA_amt = ((float(portfolio.POA_pct) / 100.0) * usd_amt) / price
    if portfolio.SRN_pct > 0.0:
        price = get_latest_price_for_shorthand("SRN")
        investment.SRN_amt = ((float(portfolio.SRN_pct) / 100.0) * usd_amt) / price
    if portfolio.SPHTX_pct > 0.0:
        price = get_latest_price_for_shorthand("SPHTX")
        investment.SPHTX_amt = ((float(portfolio.SPHTX_pct) / 100.0) * usd_amt) / price
    if portfolio.VEE_pct > 0.0:
        price = get_latest_price_for_shorthand("VEE")
        investment.VEE_amt = ((float(portfolio.VEE_pct) / 100.0) * usd_amt) / price
    if portfolio.UBQ_pct > 0.0:
        price = get_latest_price_for_shorthand("UBQ")
        investment.UBQ_amt = ((float(portfolio.UBQ_pct) / 100.0) * usd_amt) / price
    if portfolio.NANJ_pct > 0.0:
        price = get_latest_price_for_shorthand("NANJ")
        investment.NANJ_amt = ((float(portfolio.NANJ_pct) / 100.0) * usd_amt) / price
    if portfolio.MTL_pct > 0.0:
        price = get_latest_price_for_shorthand("MTL")
        investment.MTL_amt = ((float(portfolio.MTL_pct) / 100.0) * usd_amt) / price
    if portfolio.GVT_pct > 0.0:
        price = get_latest_price_for_shorthand("GVT")
        investment.GVT_amt = ((float(portfolio.GVT_pct) / 100.0) * usd_amt) / price
    if portfolio.CPX_pct > 0.0:
        price = get_latest_price_for_shorthand("CPX")
        investment.CPX_amt = ((float(portfolio.CPX_pct) / 100.0) * usd_amt) / price
    if portfolio.IOTX_pct > 0.0:
        price = get_latest_price_for_shorthand("IOTX")
        investment.IOTX_amt = ((float(portfolio.IOTX_pct) / 100.0) * usd_amt) / price
    if portfolio.TIO_pct > 0.0:
        price = get_latest_price_for_shorthand("TIO")
        investment.TIO_amt = ((float(portfolio.TIO_pct) / 100.0) * usd_amt) / price
    if portfolio.IHT_pct > 0.0:
        price = get_latest_price_for_shorthand("IHT")
        investment.IHT_amt = ((float(portfolio.IHT_pct) / 100.0) * usd_amt) / price
    if portfolio.POE_pct > 0.0:
        price = get_latest_price_for_shorthand("POE")
        investment.POE_amt = ((float(portfolio.POE_pct) / 100.0) * usd_amt) / price
    if portfolio.REN_pct > 0.0:
        price = get_latest_price_for_shorthand("REN")
        investment.REN_amt = ((float(portfolio.REN_pct) / 100.0) * usd_amt) / price
    if portfolio.JNT_pct > 0.0:
        price = get_latest_price_for_shorthand("JNT")
        investment.JNT_amt = ((float(portfolio.JNT_pct) / 100.0) * usd_amt) / price
    if portfolio.AUTO_pct > 0.0:
        price = get_latest_price_for_shorthand("AUTO")
        investment.AUTO_amt = ((float(portfolio.AUTO_pct) / 100.0) * usd_amt) / price
    if portfolio.TEL_pct > 0.0:
        price = get_latest_price_for_shorthand("TEL")
        investment.TEL_amt = ((float(portfolio.TEL_pct) / 100.0) * usd_amt) / price
    if portfolio.BTX_pct > 0.0:
        price = get_latest_price_for_shorthand("BTX")
        investment.BTX_amt = ((float(portfolio.BTX_pct) / 100.0) * usd_amt) / price
    if portfolio.INT_pct > 0.0:
        price = get_latest_price_for_shorthand("INT")
        investment.INT_amt = ((float(portfolio.INT_pct) / 100.0) * usd_amt) / price
    if portfolio.BURST_pct > 0.0:
        price = get_latest_price_for_shorthand("BURST")
        investment.BURST_amt = ((float(portfolio.BURST_pct) / 100.0) * usd_amt) / price
    if portfolio.SAFEX_pct > 0.0:
        price = get_latest_price_for_shorthand("SAFEX")
        investment.SAFEX_amt = ((float(portfolio.SAFEX_pct) / 100.0) * usd_amt) / price
    if portfolio.ITC_pct > 0.0:
        price = get_latest_price_for_shorthand("ITC")
        investment.ITC_amt = ((float(portfolio.ITC_pct) / 100.0) * usd_amt) / price
    if portfolio.EDG_pct > 0.0:
        price = get_latest_price_for_shorthand("EDG")
        investment.EDG_amt = ((float(portfolio.EDG_pct) / 100.0) * usd_amt) / price
    if portfolio.LINDA_pct > 0.0:
        price = get_latest_price_for_shorthand("LINDA")
        investment.LINDA_amt = ((float(portfolio.LINDA_pct) / 100.0) * usd_amt) / price
    if portfolio.XPM_pct > 0.0:
        price = get_latest_price_for_shorthand("XPM")
        investment.XPM_amt = ((float(portfolio.XPM_pct) / 100.0) * usd_amt) / price
    if portfolio.INK_pct > 0.0:
        price = get_latest_price_for_shorthand("INK")
        investment.INK_amt = ((float(portfolio.INK_pct) / 100.0) * usd_amt) / price
    if portfolio.ECA_pct > 0.0:
        price = get_latest_price_for_shorthand("ECA")
        investment.ECA_amt = ((float(portfolio.ECA_pct) / 100.0) * usd_amt) / price
    if portfolio.BITCNY_pct > 0.0:
        price = get_latest_price_for_shorthand("BITCNY")
        investment.BITCNY_amt = ((float(portfolio.BITCNY_pct) / 100.0) * usd_amt) / price
    if portfolio.RKT_pct > 0.0:
        price = get_latest_price_for_shorthand("RKT")
        investment.RKT_amt = ((float(portfolio.RKT_pct) / 100.0) * usd_amt) / price
    if portfolio.DAX_pct > 0.0:
        price = get_latest_price_for_shorthand("DAX")
        investment.DAX_amt = ((float(portfolio.DAX_pct) / 100.0) * usd_amt) / price
    if portfolio.TEN_pct > 0.0:
        price = get_latest_price_for_shorthand("TEN")
        investment.TEN_amt = ((float(portfolio.TEN_pct) / 100.0) * usd_amt) / price
    if portfolio.NAV_pct > 0.0:
        price = get_latest_price_for_shorthand("NAV")
        investment.NAV_amt = ((float(portfolio.NAV_pct) / 100.0) * usd_amt) / price
    if portfolio.SPANK_pct > 0.0:
        price = get_latest_price_for_shorthand("SPANK")
        investment.SPANK_amt = ((float(portfolio.SPANK_pct) / 100.0) * usd_amt) / price
    if portfolio.TRAC_pct > 0.0:
        price = get_latest_price_for_shorthand("TRAC")
        investment.TRAC_amt = ((float(portfolio.TRAC_pct) / 100.0) * usd_amt) / price
    if portfolio.LCC_pct > 0.0:
        price = get_latest_price_for_shorthand("LCC")
        investment.LCC_amt = ((float(portfolio.LCC_pct) / 100.0) * usd_amt) / price
    if portfolio.DTA_pct > 0.0:
        price = get_latest_price_for_shorthand("DTA")
        investment.DTA_amt = ((float(portfolio.DTA_pct) / 100.0) * usd_amt) / price
    if portfolio.NLG_pct > 0.0:
        price = get_latest_price_for_shorthand("NLG")
        investment.NLG_amt = ((float(portfolio.NLG_pct) / 100.0) * usd_amt) / price
    if portfolio.EDO_pct > 0.0:
        price = get_latest_price_for_shorthand("EDO")
        investment.EDO_amt = ((float(portfolio.EDO_pct) / 100.0) * usd_amt) / price
    if portfolio.WGR_pct > 0.0:
        price = get_latest_price_for_shorthand("WGR")
        investment.WGR_amt = ((float(portfolio.WGR_pct) / 100.0) * usd_amt) / price
    if portfolio.RPX_pct > 0.0:
        price = get_latest_price_for_shorthand("RPX")
        investment.RPX_amt = ((float(portfolio.RPX_pct) / 100.0) * usd_amt) / price
    if portfolio.DPY_pct > 0.0:
        price = get_latest_price_for_shorthand("DPY")
        investment.DPY_amt = ((float(portfolio.DPY_pct) / 100.0) * usd_amt) / price
    if portfolio.LEND_pct > 0.0:
        price = get_latest_price_for_shorthand("LEND")
        investment.LEND_amt = ((float(portfolio.LEND_pct) / 100.0) * usd_amt) / price
    if portfolio.EXC_pct > 0.0:
        price = get_latest_price_for_shorthand("EXC")
        investment.EXC_amt = ((float(portfolio.EXC_pct) / 100.0) * usd_amt) / price
    if portfolio.UNO_pct > 0.0:
        price = get_latest_price_for_shorthand("UNO")
        investment.UNO_amt = ((float(portfolio.UNO_pct) / 100.0) * usd_amt) / price
    if portfolio.EMC2_pct > 0.0:
        price = get_latest_price_for_shorthand("EMC2")
        investment.EMC2_amt = ((float(portfolio.EMC2_pct) / 100.0) * usd_amt) / price
    if portfolio.BAY_pct > 0.0:
        price = get_latest_price_for_shorthand("BAY")
        investment.BAY_amt = ((float(portfolio.BAY_pct) / 100.0) * usd_amt) / price
    if portfolio.LYM_pct > 0.0:
        price = get_latest_price_for_shorthand("LYM")
        investment.LYM_amt = ((float(portfolio.LYM_pct) / 100.0) * usd_amt) / price
    if portfolio.ADX_pct > 0.0:
        price = get_latest_price_for_shorthand("ADX")
        investment.ADX_amt = ((float(portfolio.ADX_pct) / 100.0) * usd_amt) / price
    if portfolio.FTC_pct > 0.0:
        price = get_latest_price_for_shorthand("FTC")
        investment.FTC_amt = ((float(portfolio.FTC_pct) / 100.0) * usd_amt) / price
    if portfolio.CPT_pct > 0.0:
        price = get_latest_price_for_shorthand("CPT")
        investment.CPT_amt = ((float(portfolio.CPT_pct) / 100.0) * usd_amt) / price
    if portfolio.APIS_pct > 0.0:
        price = get_latest_price_for_shorthand("APIS")
        investment.APIS_amt = ((float(portfolio.APIS_pct) / 100.0) * usd_amt) / price
    if portfolio.QRL_pct > 0.0:
        price = get_latest_price_for_shorthand("QRL")
        investment.QRL_amt = ((float(portfolio.QRL_pct) / 100.0) * usd_amt) / price
    if portfolio.RVN_pct > 0.0:
        price = get_latest_price_for_shorthand("RVN")
        investment.RVN_amt = ((float(portfolio.RVN_pct) / 100.0) * usd_amt) / price
    if portfolio.BAX_pct > 0.0:
        price = get_latest_price_for_shorthand("BAX")
        investment.BAX_amt = ((float(portfolio.BAX_pct) / 100.0) * usd_amt) / price
    if portfolio.RNTB_pct > 0.0:
        price = get_latest_price_for_shorthand("RNTB")
        investment.RNTB_amt = ((float(portfolio.RNTB_pct) / 100.0) * usd_amt) / price
    if portfolio.PPP_pct > 0.0:
        price = get_latest_price_for_shorthand("PPP")
        investment.PPP_amt = ((float(portfolio.PPP_pct) / 100.0) * usd_amt) / price
    if portfolio.TKN_pct > 0.0:
        price = get_latest_price_for_shorthand("TKN")
        investment.TKN_amt = ((float(portfolio.TKN_pct) / 100.0) * usd_amt) / price
    if portfolio.SLS_pct > 0.0:
        price = get_latest_price_for_shorthand("SLS")
        investment.SLS_amt = ((float(portfolio.SLS_pct) / 100.0) * usd_amt) / price
    if portfolio.TOMO_pct > 0.0:
        price = get_latest_price_for_shorthand("TOMO")
        investment.TOMO_amt = ((float(portfolio.TOMO_pct) / 100.0) * usd_amt) / price
    if portfolio.DATX_pct > 0.0:
        price = get_latest_price_for_shorthand("DATX")
        investment.DATX_amt = ((float(portfolio.DATX_pct) / 100.0) * usd_amt) / price
    if portfolio.LGO_pct > 0.0:
        price = get_latest_price_for_shorthand("LGO")
        investment.LGO_amt = ((float(portfolio.LGO_pct) / 100.0) * usd_amt) / price
    if portfolio.PZM_pct > 0.0:
        price = get_latest_price_for_shorthand("PZM")
        investment.PZM_amt = ((float(portfolio.PZM_pct) / 100.0) * usd_amt) / price
    if portfolio.ETP_pct > 0.0:
        price = get_latest_price_for_shorthand("ETP")
        investment.ETP_amt = ((float(portfolio.ETP_pct) / 100.0) * usd_amt) / price
    if portfolio.CLOAK_pct > 0.0:
        price = get_latest_price_for_shorthand("CLOAK")
        investment.CLOAK_amt = ((float(portfolio.CLOAK_pct) / 100.0) * usd_amt) / price
    if portfolio.EVN_pct > 0.0:
        price = get_latest_price_for_shorthand("EVN")
        investment.EVN_amt = ((float(portfolio.EVN_pct) / 100.0) * usd_amt) / price
    if portfolio.XCP_pct > 0.0:
        price = get_latest_price_for_shorthand("XCP")
        investment.XCP_amt = ((float(portfolio.XCP_pct) / 100.0) * usd_amt) / price
    if portfolio.SWM_pct > 0.0:
        price = get_latest_price_for_shorthand("SWM")
        investment.SWM_amt = ((float(portfolio.SWM_pct) / 100.0) * usd_amt) / price
    if portfolio.TNT_pct > 0.0:
        price = get_latest_price_for_shorthand("TNT")
        investment.TNT_amt = ((float(portfolio.TNT_pct) / 100.0) * usd_amt) / price
    if portfolio.RCN_pct > 0.0:
        price = get_latest_price_for_shorthand("RCN")
        investment.RCN_amt = ((float(portfolio.RCN_pct) / 100.0) * usd_amt) / price
    if portfolio.TCT_pct > 0.0:
        price = get_latest_price_for_shorthand("TCT")
        investment.TCT_amt = ((float(portfolio.TCT_pct) / 100.0) * usd_amt) / price
    if portfolio.SWFTC_pct > 0.0:
        price = get_latest_price_for_shorthand("SWFTC")
        investment.SWFTC_amt = ((float(portfolio.SWFTC_pct) / 100.0) * usd_amt) / price
    if portfolio.VIA_pct > 0.0:
        price = get_latest_price_for_shorthand("VIA")
        investment.VIA_amt = ((float(portfolio.VIA_pct) / 100.0) * usd_amt) / price
    if portfolio.SNGLS_pct > 0.0:
        price = get_latest_price_for_shorthand("SNGLS")
        investment.SNGLS_amt = ((float(portfolio.SNGLS_pct) / 100.0) * usd_amt) / price
    if portfolio.ZCO_pct > 0.0:
        price = get_latest_price_for_shorthand("ZCO")
        investment.ZCO_amt = ((float(portfolio.ZCO_pct) / 100.0) * usd_amt) / price
    if portfolio.GIN_pct > 0.0:
        price = get_latest_price_for_shorthand("GIN")
        investment.GIN_amt = ((float(portfolio.GIN_pct) / 100.0) * usd_amt) / price
    if portfolio.OST_pct > 0.0:
        price = get_latest_price_for_shorthand("OST")
        investment.OST_amt = ((float(portfolio.OST_pct) / 100.0) * usd_amt) / price
    if portfolio.FXT_pct > 0.0:
        price = get_latest_price_for_shorthand("FXT")
        investment.FXT_amt = ((float(portfolio.FXT_pct) / 100.0) * usd_amt) / price
    if portfolio.AST_pct > 0.0:
        price = get_latest_price_for_shorthand("AST")
        investment.AST_amt = ((float(portfolio.AST_pct) / 100.0) * usd_amt) / price
    if portfolio.HAV_pct > 0.0:
        price = get_latest_price_for_shorthand("HAV")
        investment.HAV_amt = ((float(portfolio.HAV_pct) / 100.0) * usd_amt) / price
    if portfolio.PAC_pct > 0.0:
        price = get_latest_price_for_shorthand("PAC")
        investment.PAC_amt = ((float(portfolio.PAC_pct) / 100.0) * usd_amt) / price
    if portfolio.KICK_pct > 0.0:
        price = get_latest_price_for_shorthand("KICK")
        investment.KICK_amt = ((float(portfolio.KICK_pct) / 100.0) * usd_amt) / price
    if portfolio.PRE_pct > 0.0:
        price = get_latest_price_for_shorthand("PRE")
        investment.PRE_amt = ((float(portfolio.PRE_pct) / 100.0) * usd_amt) / price
    if portfolio.SXDT_pct > 0.0:
        price = get_latest_price_for_shorthand("SXDT")
        investment.SXDT_amt = ((float(portfolio.SXDT_pct) / 100.0) * usd_amt) / price
    if portfolio.DNT_pct > 0.0:
        price = get_latest_price_for_shorthand("DNT")
        investment.DNT_amt = ((float(portfolio.DNT_pct) / 100.0) * usd_amt) / price
    if portfolio.XWC_pct > 0.0:
        price = get_latest_price_for_shorthand("XWC")
        investment.XWC_amt = ((float(portfolio.XWC_pct) / 100.0) * usd_amt) / price
    if portfolio.UTK_pct > 0.0:
        price = get_latest_price_for_shorthand("UTK")
        investment.UTK_amt = ((float(portfolio.UTK_pct) / 100.0) * usd_amt) / price
    if portfolio.INS_pct > 0.0:
        price = get_latest_price_for_shorthand("INS")
        investment.INS_amt = ((float(portfolio.INS_pct) / 100.0) * usd_amt) / price
    if portfolio.ATN_pct > 0.0:
        price = get_latest_price_for_shorthand("ATN")
        investment.ATN_amt = ((float(portfolio.ATN_pct) / 100.0) * usd_amt) / price
    if portfolio.UTNP_pct > 0.0:
        price = get_latest_price_for_shorthand("UTNP")
        investment.UTNP_amt = ((float(portfolio.UTNP_pct) / 100.0) * usd_amt) / price
    if portfolio.WINGS_pct > 0.0:
        price = get_latest_price_for_shorthand("WINGS")
        investment.WINGS_amt = ((float(portfolio.WINGS_pct) / 100.0) * usd_amt) / price
    if portfolio.CPC_pct > 0.0:
        price = get_latest_price_for_shorthand("CPC")
        investment.CPC_amt = ((float(portfolio.CPC_pct) / 100.0) * usd_amt) / price
    if portfolio.MGO_pct > 0.0:
        price = get_latest_price_for_shorthand("MGO")
        investment.MGO_amt = ((float(portfolio.MGO_pct) / 100.0) * usd_amt) / price
    if portfolio.DAT_pct > 0.0:
        price = get_latest_price_for_shorthand("DAT")
        investment.DAT_amt = ((float(portfolio.DAT_pct) / 100.0) * usd_amt) / price
    if portfolio.XP_pct > 0.0:
        price = get_latest_price_for_shorthand("XP")
        investment.XP_amt = ((float(portfolio.XP_pct) / 100.0) * usd_amt) / price
    if portfolio.NGC_pct > 0.0:
        price = get_latest_price_for_shorthand("NGC")
        investment.NGC_amt = ((float(portfolio.NGC_pct) / 100.0) * usd_amt) / price
    if portfolio.BCO_pct > 0.0:
        price = get_latest_price_for_shorthand("BCO")
        investment.BCO_amt = ((float(portfolio.BCO_pct) / 100.0) * usd_amt) / price
    if portfolio.ZPT_pct > 0.0:
        price = get_latest_price_for_shorthand("ZPT")
        investment.ZPT_amt = ((float(portfolio.ZPT_pct) / 100.0) * usd_amt) / price
    if portfolio.RNT_pct > 0.0:
        price = get_latest_price_for_shorthand("RNT")
        investment.RNT_amt = ((float(portfolio.RNT_pct) / 100.0) * usd_amt) / price
    if portfolio.AEON_pct > 0.0:
        price = get_latest_price_for_shorthand("AEON")
        investment.AEON_amt = ((float(portfolio.AEON_pct) / 100.0) * usd_amt) / price
    if portfolio.MSP_pct > 0.0:
        price = get_latest_price_for_shorthand("MSP")
        investment.MSP_amt = ((float(portfolio.MSP_pct) / 100.0) * usd_amt) / price
    if portfolio.HTML_pct > 0.0:
        price = get_latest_price_for_shorthand("HTML")
        investment.HTML_amt = ((float(portfolio.HTML_pct) / 100.0) * usd_amt) / price
    if portfolio.CDT_pct > 0.0:
        price = get_latest_price_for_shorthand("CDT")
        investment.CDT_amt = ((float(portfolio.CDT_pct) / 100.0) * usd_amt) / price
    if portfolio.LYL_pct > 0.0:
        price = get_latest_price_for_shorthand("LYL")
        investment.LYL_amt = ((float(portfolio.LYL_pct) / 100.0) * usd_amt) / price
    if portfolio.NMC_pct > 0.0:
        price = get_latest_price_for_shorthand("NMC")
        investment.NMC_amt = ((float(portfolio.NMC_pct) / 100.0) * usd_amt) / price
    if portfolio.MOD_pct > 0.0:
        price = get_latest_price_for_shorthand("MOD")
        investment.MOD_amt = ((float(portfolio.MOD_pct) / 100.0) * usd_amt) / price
    if portfolio.MNX_pct > 0.0:
        price = get_latest_price_for_shorthand("MNX")
        investment.MNX_amt = ((float(portfolio.MNX_pct) / 100.0) * usd_amt) / price
    if portfolio.WPR_pct > 0.0:
        price = get_latest_price_for_shorthand("WPR")
        investment.WPR_amt = ((float(portfolio.WPR_pct) / 100.0) * usd_amt) / price
    if portfolio.HST_pct > 0.0:
        price = get_latest_price_for_shorthand("HST")
        investment.HST_amt = ((float(portfolio.HST_pct) / 100.0) * usd_amt) / price
    if portfolio.LBC_pct > 0.0:
        price = get_latest_price_for_shorthand("LBC")
        investment.LBC_amt = ((float(portfolio.LBC_pct) / 100.0) * usd_amt) / price
    if portfolio.CREDO_pct > 0.0:
        price = get_latest_price_for_shorthand("CREDO")
        investment.CREDO_amt = ((float(portfolio.CREDO_pct) / 100.0) * usd_amt) / price
    if portfolio.ION_pct > 0.0:
        price = get_latest_price_for_shorthand("ION")
        investment.ION_amt = ((float(portfolio.ION_pct) / 100.0) * usd_amt) / price
    if portfolio.YOYOW_pct > 0.0:
        price = get_latest_price_for_shorthand("YOYOW")
        investment.YOYOW_amt = ((float(portfolio.YOYOW_pct) / 100.0) * usd_amt) / price
    if portfolio.ART_pct > 0.0:
        price = get_latest_price_for_shorthand("ART")
        investment.ART_amt = ((float(portfolio.ART_pct) / 100.0) * usd_amt) / price
    if portfolio.MLN_pct > 0.0:
        price = get_latest_price_for_shorthand("MLN")
        investment.MLN_amt = ((float(portfolio.MLN_pct) / 100.0) * usd_amt) / price
    if portfolio.CMCT_pct > 0.0:
        price = get_latest_price_for_shorthand("CMCT")
        investment.CMCT_amt = ((float(portfolio.CMCT_pct) / 100.0) * usd_amt) / price
    if portfolio.FUEL_pct > 0.0:
        price = get_latest_price_for_shorthand("FUEL")
        investment.FUEL_amt = ((float(portfolio.FUEL_pct) / 100.0) * usd_amt) / price
    if portfolio.HVN_pct > 0.0:
        price = get_latest_price_for_shorthand("HVN")
        investment.HVN_amt = ((float(portfolio.HVN_pct) / 100.0) * usd_amt) / price
    if portfolio.DCT_pct > 0.0:
        price = get_latest_price_for_shorthand("DCT")
        investment.DCT_amt = ((float(portfolio.DCT_pct) / 100.0) * usd_amt) / price
    if portfolio.APPC_pct > 0.0:
        price = get_latest_price_for_shorthand("APPC")
        investment.APPC_amt = ((float(portfolio.APPC_pct) / 100.0) * usd_amt) / price
    if portfolio.MED_pct > 0.0:
        price = get_latest_price_for_shorthand("MED")
        investment.MED_amt = ((float(portfolio.MED_pct) / 100.0) * usd_amt) / price
    if portfolio.PHR_pct > 0.0:
        price = get_latest_price_for_shorthand("PHR")
        investment.PHR_amt = ((float(portfolio.PHR_pct) / 100.0) * usd_amt) / price
    if portfolio.BANCA_pct > 0.0:
        price = get_latest_price_for_shorthand("BANCA")
        investment.BANCA_amt = ((float(portfolio.BANCA_pct) / 100.0) * usd_amt) / price
    if portfolio.LET_pct > 0.0:
        price = get_latest_price_for_shorthand("LET")
        investment.LET_amt = ((float(portfolio.LET_pct) / 100.0) * usd_amt) / price
    if portfolio.ECC_pct > 0.0:
        price = get_latest_price_for_shorthand("ECC")
        investment.ECC_amt = ((float(portfolio.ECC_pct) / 100.0) * usd_amt) / price
    if portfolio.LUN_pct > 0.0:
        price = get_latest_price_for_shorthand("LUN")
        investment.LUN_amt = ((float(portfolio.LUN_pct) / 100.0) * usd_amt) / price
    if portfolio.DAG_pct > 0.0:
        price = get_latest_price_for_shorthand("DAG")
        investment.DAG_amt = ((float(portfolio.DAG_pct) / 100.0) * usd_amt) / price
    if portfolio.UUU_pct > 0.0:
        price = get_latest_price_for_shorthand("UUU")
        investment.UUU_amt = ((float(portfolio.UUU_pct) / 100.0) * usd_amt) / price
    if portfolio.SBD_pct > 0.0:
        price = get_latest_price_for_shorthand("SBD")
        investment.SBD_amt = ((float(portfolio.SBD_pct) / 100.0) * usd_amt) / price
    if portfolio.SENT_pct > 0.0:
        price = get_latest_price_for_shorthand("SENT")
        investment.SENT_amt = ((float(portfolio.SENT_pct) / 100.0) * usd_amt) / price
    if portfolio.DBET_pct > 0.0:
        price = get_latest_price_for_shorthand("DBET")
        investment.DBET_amt = ((float(portfolio.DBET_pct) / 100.0) * usd_amt) / price
    if portfolio.TAAS_pct > 0.0:
        price = get_latest_price_for_shorthand("TAAS")
        investment.TAAS_amt = ((float(portfolio.TAAS_pct) / 100.0) * usd_amt) / price
    if portfolio.QLC_pct > 0.0:
        price = get_latest_price_for_shorthand("QLC")
        investment.QLC_amt = ((float(portfolio.QLC_pct) / 100.0) * usd_amt) / price
    if portfolio.WABI_pct > 0.0:
        price = get_latest_price_for_shorthand("WABI")
        investment.WABI_amt = ((float(portfolio.WABI_pct) / 100.0) * usd_amt) / price
    if portfolio.PCN_pct > 0.0:
        price = get_latest_price_for_shorthand("PCN")
        investment.PCN_amt = ((float(portfolio.PCN_pct) / 100.0) * usd_amt) / price
    if portfolio.PURA_pct > 0.0:
        price = get_latest_price_for_shorthand("PURA")
        investment.PURA_amt = ((float(portfolio.PURA_pct) / 100.0) * usd_amt) / price
    if portfolio.XDCE_pct > 0.0:
        price = get_latest_price_for_shorthand("XDCE")
        investment.XDCE_amt = ((float(portfolio.XDCE_pct) / 100.0) * usd_amt) / price
    if portfolio.SSC_pct > 0.0:
        price = get_latest_price_for_shorthand("SSC")
        investment.SSC_amt = ((float(portfolio.SSC_pct) / 100.0) * usd_amt) / price
    if portfolio.VIBE_pct > 0.0:
        price = get_latest_price_for_shorthand("VIBE")
        investment.VIBE_amt = ((float(portfolio.VIBE_pct) / 100.0) * usd_amt) / price
    if portfolio.ELEC_pct > 0.0:
        price = get_latest_price_for_shorthand("ELEC")
        investment.ELEC_amt = ((float(portfolio.ELEC_pct) / 100.0) * usd_amt) / price
    if portfolio.MEDIC_pct > 0.0:
        price = get_latest_price_for_shorthand("MEDIC")
        investment.MEDIC_amt = ((float(portfolio.MEDIC_pct) / 100.0) * usd_amt) / price
    if portfolio.COSS_pct > 0.0:
        price = get_latest_price_for_shorthand("COSS")
        investment.COSS_amt = ((float(portfolio.COSS_pct) / 100.0) * usd_amt) / price
    if portfolio.YEE_pct > 0.0:
        price = get_latest_price_for_shorthand("YEE")
        investment.YEE_amt = ((float(portfolio.YEE_pct) / 100.0) * usd_amt) / price
    if portfolio.AURA_pct > 0.0:
        price = get_latest_price_for_shorthand("AURA")
        investment.AURA_amt = ((float(portfolio.AURA_pct) / 100.0) * usd_amt) / price
    if portfolio.CSC_pct > 0.0:
        price = get_latest_price_for_shorthand("CSC")
        investment.CSC_amt = ((float(portfolio.CSC_pct) / 100.0) * usd_amt) / price
    if portfolio.MOBI_pct > 0.0:
        price = get_latest_price_for_shorthand("MOBI")
        investment.MOBI_amt = ((float(portfolio.MOBI_pct) / 100.0) * usd_amt) / price
    if portfolio.PRL_pct > 0.0:
        price = get_latest_price_for_shorthand("PRL")
        investment.PRL_amt = ((float(portfolio.PRL_pct) / 100.0) * usd_amt) / price
    if portfolio.QUN_pct > 0.0:
        price = get_latest_price_for_shorthand("QUN")
        investment.QUN_amt = ((float(portfolio.QUN_pct) / 100.0) * usd_amt) / price
    if portfolio.SHIFT_pct > 0.0:
        price = get_latest_price_for_shorthand("SHIFT")
        investment.SHIFT_amt = ((float(portfolio.SHIFT_pct) / 100.0) * usd_amt) / price
    if portfolio.CAS_pct > 0.0:
        price = get_latest_price_for_shorthand("CAS")
        investment.CAS_amt = ((float(portfolio.CAS_pct) / 100.0) * usd_amt) / price
    if portfolio.SOAR_pct > 0.0:
        price = get_latest_price_for_shorthand("SOAR")
        investment.SOAR_amt = ((float(portfolio.SOAR_pct) / 100.0) * usd_amt) / price
    if portfolio.BITG_pct > 0.0:
        price = get_latest_price_for_shorthand("BITG")
        investment.BITG_amt = ((float(portfolio.BITG_pct) / 100.0) * usd_amt) / price
    if portfolio.BKX_pct > 0.0:
        price = get_latest_price_for_shorthand("BKX")
        investment.BKX_amt = ((float(portfolio.BKX_pct) / 100.0) * usd_amt) / price
    if portfolio.DOCK_pct > 0.0:
        price = get_latest_price_for_shorthand("DOCK")
        investment.DOCK_amt = ((float(portfolio.DOCK_pct) / 100.0) * usd_amt) / price
    if portfolio.KEY_pct > 0.0:
        price = get_latest_price_for_shorthand("KEY")
        investment.KEY_amt = ((float(portfolio.KEY_pct) / 100.0) * usd_amt) / price
    if portfolio.XES_pct > 0.0:
        price = get_latest_price_for_shorthand("XES")
        investment.XES_amt = ((float(portfolio.XES_pct) / 100.0) * usd_amt) / price
    if portfolio.POT_pct > 0.0:
        price = get_latest_price_for_shorthand("POT")
        investment.POT_amt = ((float(portfolio.POT_pct) / 100.0) * usd_amt) / price
    if portfolio.QBT_pct > 0.0:
        price = get_latest_price_for_shorthand("QBT")
        investment.QBT_amt = ((float(portfolio.QBT_pct) / 100.0) * usd_amt) / price
    if portfolio.DXT_pct > 0.0:
        price = get_latest_price_for_shorthand("DXT")
        investment.DXT_amt = ((float(portfolio.DXT_pct) / 100.0) * usd_amt) / price
    if portfolio.IXT_pct > 0.0:
        price = get_latest_price_for_shorthand("IXT")
        investment.IXT_amt = ((float(portfolio.IXT_pct) / 100.0) * usd_amt) / price
    if portfolio.BMC_pct > 0.0:
        price = get_latest_price_for_shorthand("BMC")
        investment.BMC_amt = ((float(portfolio.BMC_pct) / 100.0) * usd_amt) / price
    if portfolio.PEPECASH_pct > 0.0:
        price = get_latest_price_for_shorthand("PEPECASH")
        investment.PEPECASH_amt = ((float(portfolio.PEPECASH_pct) / 100.0) * usd_amt) / price
    if portfolio.COB_pct > 0.0:
        price = get_latest_price_for_shorthand("COB")
        investment.COB_amt = ((float(portfolio.COB_pct) / 100.0) * usd_amt) / price
    if portfolio.GRID_pct > 0.0:
        price = get_latest_price_for_shorthand("GRID")
        investment.GRID_amt = ((float(portfolio.GRID_pct) / 100.0) * usd_amt) / price
    if portfolio.BITUSD_pct > 0.0:
        price = get_latest_price_for_shorthand("BITUSD")
        investment.BITUSD_amt = ((float(portfolio.BITUSD_pct) / 100.0) * usd_amt) / price
    if portfolio.KRM_pct > 0.0:
        price = get_latest_price_for_shorthand("KRM")
        investment.KRM_amt = ((float(portfolio.KRM_pct) / 100.0) * usd_amt) / price
    if portfolio.HMQ_pct > 0.0:
        price = get_latest_price_for_shorthand("HMQ")
        investment.HMQ_amt = ((float(portfolio.HMQ_pct) / 100.0) * usd_amt) / price
    if portfolio.VIB_pct > 0.0:
        price = get_latest_price_for_shorthand("VIB")
        investment.VIB_amt = ((float(portfolio.VIB_pct) / 100.0) * usd_amt) / price
    if portfolio.PPY_pct > 0.0:
        price = get_latest_price_for_shorthand("PPY")
        investment.PPY_amt = ((float(portfolio.PPY_pct) / 100.0) * usd_amt) / price
    if portfolio.XEL_pct > 0.0:
        price = get_latest_price_for_shorthand("XEL")
        investment.XEL_amt = ((float(portfolio.XEL_pct) / 100.0) * usd_amt) / price
    if portfolio.e_1ST_pct > 0.0:
        price = get_latest_price_for_shorthand("1ST")
        investment.e_1ST_amt = ((float(portfolio.e_1ST_pct) / 100.0) * usd_amt) / price
    if portfolio.NLC2_pct > 0.0:
        price = get_latest_price_for_shorthand("NLC2")
        investment.NLC2_amt = ((float(portfolio.NLC2_pct) / 100.0) * usd_amt) / price
    if portfolio.MTN_pct > 0.0:
        price = get_latest_price_for_shorthand("MTN")
        investment.MTN_amt = ((float(portfolio.MTN_pct) / 100.0) * usd_amt) / price
    if portfolio.THC_pct > 0.0:
        price = get_latest_price_for_shorthand("THC")
        investment.THC_amt = ((float(portfolio.THC_pct) / 100.0) * usd_amt) / price
    if portfolio.TNC_pct > 0.0:
        price = get_latest_price_for_shorthand("TNC")
        investment.TNC_amt = ((float(portfolio.TNC_pct) / 100.0) * usd_amt) / price
    if portfolio.NTK_pct > 0.0:
        price = get_latest_price_for_shorthand("NTK")
        investment.NTK_amt = ((float(portfolio.NTK_pct) / 100.0) * usd_amt) / price
    if portfolio.COLX_pct > 0.0:
        price = get_latest_price_for_shorthand("COLX")
        investment.COLX_amt = ((float(portfolio.COLX_pct) / 100.0) * usd_amt) / price
    if portfolio.COV_pct > 0.0:
        price = get_latest_price_for_shorthand("COV")
        investment.COV_amt = ((float(portfolio.COV_pct) / 100.0) * usd_amt) / price
    if portfolio.DIME_pct > 0.0:
        price = get_latest_price_for_shorthand("DIME")
        investment.DIME_amt = ((float(portfolio.DIME_pct) / 100.0) * usd_amt) / price
    if portfolio.FOTA_pct > 0.0:
        price = get_latest_price_for_shorthand("FOTA")
        investment.FOTA_amt = ((float(portfolio.FOTA_pct) / 100.0) * usd_amt) / price
    if portfolio.LIFE_pct > 0.0:
        price = get_latest_price_for_shorthand("LIFE")
        investment.LIFE_amt = ((float(portfolio.LIFE_pct) / 100.0) * usd_amt) / price
    if portfolio.XBY_pct > 0.0:
        price = get_latest_price_for_shorthand("XBY")
        investment.XBY_amt = ((float(portfolio.XBY_pct) / 100.0) * usd_amt) / price
    if portfolio.MER_pct > 0.0:
        price = get_latest_price_for_shorthand("MER")
        investment.MER_amt = ((float(portfolio.MER_pct) / 100.0) * usd_amt) / price
    if portfolio.RFR_pct > 0.0:
        price = get_latest_price_for_shorthand("RFR")
        investment.RFR_amt = ((float(portfolio.RFR_pct) / 100.0) * usd_amt) / price
    if portfolio.PST_pct > 0.0:
        price = get_latest_price_for_shorthand("PST")
        investment.PST_amt = ((float(portfolio.PST_pct) / 100.0) * usd_amt) / price
    if portfolio.ZSC_pct > 0.0:
        price = get_latest_price_for_shorthand("ZSC")
        investment.ZSC_amt = ((float(portfolio.ZSC_pct) / 100.0) * usd_amt) / price
    if portfolio.PRA_pct > 0.0:
        price = get_latest_price_for_shorthand("PRA")
        investment.PRA_amt = ((float(portfolio.PRA_pct) / 100.0) * usd_amt) / price
    if portfolio.CFI_pct > 0.0:
        price = get_latest_price_for_shorthand("CFI")
        investment.CFI_amt = ((float(portfolio.CFI_pct) / 100.0) * usd_amt) / price
    if portfolio.BIS_pct > 0.0:
        price = get_latest_price_for_shorthand("BIS")
        investment.BIS_amt = ((float(portfolio.BIS_pct) / 100.0) * usd_amt) / price
    if portfolio.QAU_pct > 0.0:
        price = get_latest_price_for_shorthand("QAU")
        investment.QAU_amt = ((float(portfolio.QAU_pct) / 100.0) * usd_amt) / price
    if portfolio.LEO_pct > 0.0:
        price = get_latest_price_for_shorthand("LEO")
        investment.LEO_amt = ((float(portfolio.LEO_pct) / 100.0) * usd_amt) / price
    if portfolio.BRM_pct > 0.0:
        price = get_latest_price_for_shorthand("BRM")
        investment.BRM_amt = ((float(portfolio.BRM_pct) / 100.0) * usd_amt) / price
    if portfolio.BCPT_pct > 0.0:
        price = get_latest_price_for_shorthand("BCPT")
        investment.BCPT_amt = ((float(portfolio.BCPT_pct) / 100.0) * usd_amt) / price
    if portfolio.AMP_pct > 0.0:
        price = get_latest_price_for_shorthand("AMP")
        investment.AMP_amt = ((float(portfolio.AMP_pct) / 100.0) * usd_amt) / price
    if portfolio.TIME_pct > 0.0:
        price = get_latest_price_for_shorthand("TIME")
        investment.TIME_amt = ((float(portfolio.TIME_pct) / 100.0) * usd_amt) / price
    if portfolio.BITB_pct > 0.0:
        price = get_latest_price_for_shorthand("BITB")
        investment.BITB_amt = ((float(portfolio.BITB_pct) / 100.0) * usd_amt) / price
    if portfolio.BLT_pct > 0.0:
        price = get_latest_price_for_shorthand("BLT")
        investment.BLT_amt = ((float(portfolio.BLT_pct) / 100.0) * usd_amt) / price
    if portfolio.LUX_pct > 0.0:
        price = get_latest_price_for_shorthand("LUX")
        investment.LUX_amt = ((float(portfolio.LUX_pct) / 100.0) * usd_amt) / price
    if portfolio.SPC_pct > 0.0:
        price = get_latest_price_for_shorthand("SPC")
        investment.SPC_amt = ((float(portfolio.SPC_pct) / 100.0) * usd_amt) / price
    if portfolio.ONION_pct > 0.0:
        price = get_latest_price_for_shorthand("ONION")
        investment.ONION_amt = ((float(portfolio.ONION_pct) / 100.0) * usd_amt) / price
    if portfolio.RVR_pct > 0.0:
        price = get_latest_price_for_shorthand("RVR")
        investment.RVR_amt = ((float(portfolio.RVR_pct) / 100.0) * usd_amt) / price
    if portfolio.CEEK_pct > 0.0:
        price = get_latest_price_for_shorthand("CEEK")
        investment.CEEK_amt = ((float(portfolio.CEEK_pct) / 100.0) * usd_amt) / price
    if portfolio.TRIG_pct > 0.0:
        price = get_latest_price_for_shorthand("TRIG")
        investment.TRIG_amt = ((float(portfolio.TRIG_pct) / 100.0) * usd_amt) / price
    if portfolio.LATX_pct > 0.0:
        price = get_latest_price_for_shorthand("LATX")
        investment.LATX_amt = ((float(portfolio.LATX_pct) / 100.0) * usd_amt) / price
    if portfolio.ACAT_pct > 0.0:
        price = get_latest_price_for_shorthand("ACAT")
        investment.ACAT_amt = ((float(portfolio.ACAT_pct) / 100.0) * usd_amt) / price
    if portfolio.ALQO_pct > 0.0:
        price = get_latest_price_for_shorthand("ALQO")
        investment.ALQO_amt = ((float(portfolio.ALQO_pct) / 100.0) * usd_amt) / price
    if portfolio.MOT_pct > 0.0:
        price = get_latest_price_for_shorthand("MOT")
        investment.MOT_amt = ((float(portfolio.MOT_pct) / 100.0) * usd_amt) / price
    if portfolio.XSH_pct > 0.0:
        price = get_latest_price_for_shorthand("XSH")
        investment.XSH_amt = ((float(portfolio.XSH_pct) / 100.0) * usd_amt) / price
    if portfolio.EVX_pct > 0.0:
        price = get_latest_price_for_shorthand("EVX")
        investment.EVX_amt = ((float(portfolio.EVX_pct) / 100.0) * usd_amt) / price
    if portfolio.DIVX_pct > 0.0:
        price = get_latest_price_for_shorthand("DIVX")
        investment.DIVX_amt = ((float(portfolio.DIVX_pct) / 100.0) * usd_amt) / price
    if portfolio.DMT_pct > 0.0:
        price = get_latest_price_for_shorthand("DMT")
        investment.DMT_amt = ((float(portfolio.DMT_pct) / 100.0) * usd_amt) / price
    if portfolio.CRW_pct > 0.0:
        price = get_latest_price_for_shorthand("CRW")
        investment.CRW_amt = ((float(portfolio.CRW_pct) / 100.0) * usd_amt) / price
    if portfolio.MWAT_pct > 0.0:
        price = get_latest_price_for_shorthand("MWAT")
        investment.MWAT_amt = ((float(portfolio.MWAT_pct) / 100.0) * usd_amt) / price
    if portfolio.UKG_pct > 0.0:
        price = get_latest_price_for_shorthand("UKG")
        investment.UKG_amt = ((float(portfolio.UKG_pct) / 100.0) * usd_amt) / price
    if portfolio.PASC_pct > 0.0:
        price = get_latest_price_for_shorthand("PASC")
        investment.PASC_amt = ((float(portfolio.PASC_pct) / 100.0) * usd_amt) / price
    if portfolio.TAU_pct > 0.0:
        price = get_latest_price_for_shorthand("TAU")
        investment.TAU_amt = ((float(portfolio.TAU_pct) / 100.0) * usd_amt) / price
    if portfolio.OXY_pct > 0.0:
        price = get_latest_price_for_shorthand("OXY")
        investment.OXY_amt = ((float(portfolio.OXY_pct) / 100.0) * usd_amt) / price
    if portfolio.OMX_pct > 0.0:
        price = get_latest_price_for_shorthand("OMX")
        investment.OMX_amt = ((float(portfolio.OMX_pct) / 100.0) * usd_amt) / price
    if portfolio.BBR_pct > 0.0:
        price = get_latest_price_for_shorthand("BBR")
        investment.BBR_amt = ((float(portfolio.BBR_pct) / 100.0) * usd_amt) / price
    if portfolio.TSL_pct > 0.0:
        price = get_latest_price_for_shorthand("TSL")
        investment.TSL_amt = ((float(portfolio.TSL_pct) / 100.0) * usd_amt) / price
    if portfolio.DIM_pct > 0.0:
        price = get_latest_price_for_shorthand("DIM")
        investment.DIM_amt = ((float(portfolio.DIM_pct) / 100.0) * usd_amt) / price
    if portfolio.PRO_pct > 0.0:
        price = get_latest_price_for_shorthand("PRO")
        investment.PRO_amt = ((float(portfolio.PRO_pct) / 100.0) * usd_amt) / price
    if portfolio.PLBT_pct > 0.0:
        price = get_latest_price_for_shorthand("PLBT")
        investment.PLBT_amt = ((float(portfolio.PLBT_pct) / 100.0) * usd_amt) / price
    if portfolio.DADI_pct > 0.0:
        price = get_latest_price_for_shorthand("DADI")
        investment.DADI_amt = ((float(portfolio.DADI_pct) / 100.0) * usd_amt) / price
    if portfolio.UGC_pct > 0.0:
        price = get_latest_price_for_shorthand("UGC")
        investment.UGC_amt = ((float(portfolio.UGC_pct) / 100.0) * usd_amt) / price
    if portfolio.DMD_pct > 0.0:
        price = get_latest_price_for_shorthand("DMD")
        investment.DMD_amt = ((float(portfolio.DMD_pct) / 100.0) * usd_amt) / price
    if portfolio.BLK_pct > 0.0:
        price = get_latest_price_for_shorthand("BLK")
        investment.BLK_amt = ((float(portfolio.BLK_pct) / 100.0) * usd_amt) / price
    if portfolio.SNC_pct > 0.0:
        price = get_latest_price_for_shorthand("SNC")
        investment.SNC_amt = ((float(portfolio.SNC_pct) / 100.0) * usd_amt) / price
    if portfolio.BETR_pct > 0.0:
        price = get_latest_price_for_shorthand("BETR")
        investment.BETR_amt = ((float(portfolio.BETR_pct) / 100.0) * usd_amt) / price
    if portfolio.GRC_pct > 0.0:
        price = get_latest_price_for_shorthand("GRC")
        investment.GRC_amt = ((float(portfolio.GRC_pct) / 100.0) * usd_amt) / price
    if portfolio.BOT_pct > 0.0:
        price = get_latest_price_for_shorthand("BOT")
        investment.BOT_amt = ((float(portfolio.BOT_pct) / 100.0) * usd_amt) / price
    if portfolio.FLASH_pct > 0.0:
        price = get_latest_price_for_shorthand("FLASH")
        investment.FLASH_amt = ((float(portfolio.FLASH_pct) / 100.0) * usd_amt) / price
    if portfolio.TFD_pct > 0.0:
        price = get_latest_price_for_shorthand("TFD")
        investment.TFD_amt = ((float(portfolio.TFD_pct) / 100.0) * usd_amt) / price
    if portfolio.DBIX_pct > 0.0:
        price = get_latest_price_for_shorthand("DBIX")
        investment.DBIX_amt = ((float(portfolio.DBIX_pct) / 100.0) * usd_amt) / price
    if portfolio.UQC_pct > 0.0:
        price = get_latest_price_for_shorthand("UQC")
        investment.UQC_amt = ((float(portfolio.UQC_pct) / 100.0) * usd_amt) / price
    if portfolio.SWTH_pct > 0.0:
        price = get_latest_price_for_shorthand("SWTH")
        investment.SWTH_amt = ((float(portfolio.SWTH_pct) / 100.0) * usd_amt) / price
    if portfolio.SKB_pct > 0.0:
        price = get_latest_price_for_shorthand("SKB")
        investment.SKB_amt = ((float(portfolio.SKB_pct) / 100.0) * usd_amt) / price
    if portfolio.BCA_pct > 0.0:
        price = get_latest_price_for_shorthand("BCA")
        investment.BCA_amt = ((float(portfolio.BCA_pct) / 100.0) * usd_amt) / price
    if portfolio.SOUL_pct > 0.0:
        price = get_latest_price_for_shorthand("SOUL")
        investment.SOUL_amt = ((float(portfolio.SOUL_pct) / 100.0) * usd_amt) / price
    if portfolio.GUP_pct > 0.0:
        price = get_latest_price_for_shorthand("GUP")
        investment.GUP_amt = ((float(portfolio.GUP_pct) / 100.0) * usd_amt) / price
    if portfolio.MUSE_pct > 0.0:
        price = get_latest_price_for_shorthand("MUSE")
        investment.MUSE_amt = ((float(portfolio.MUSE_pct) / 100.0) * usd_amt) / price
    if portfolio.SNTR_pct > 0.0:
        price = get_latest_price_for_shorthand("SNTR")
        investment.SNTR_amt = ((float(portfolio.SNTR_pct) / 100.0) * usd_amt) / price
    if portfolio.GEM_pct > 0.0:
        price = get_latest_price_for_shorthand("GEM")
        investment.GEM_amt = ((float(portfolio.GEM_pct) / 100.0) * usd_amt) / price
    if portfolio.LA_pct > 0.0:
        price = get_latest_price_for_shorthand("LA")
        investment.LA_amt = ((float(portfolio.LA_pct) / 100.0) * usd_amt) / price
    if portfolio.NKC_pct > 0.0:
        price = get_latest_price_for_shorthand("NKC")
        investment.NKC_amt = ((float(portfolio.NKC_pct) / 100.0) * usd_amt) / price
    if portfolio.MUE_pct > 0.0:
        price = get_latest_price_for_shorthand("MUE")
        investment.MUE_amt = ((float(portfolio.MUE_pct) / 100.0) * usd_amt) / price
    if portfolio.BPT_pct > 0.0:
        price = get_latest_price_for_shorthand("BPT")
        investment.BPT_amt = ((float(portfolio.BPT_pct) / 100.0) * usd_amt) / price
    if portfolio.STK_pct > 0.0:
        price = get_latest_price_for_shorthand("STK")
        investment.STK_amt = ((float(portfolio.STK_pct) / 100.0) * usd_amt) / price
    if portfolio.NMR_pct > 0.0:
        price = get_latest_price_for_shorthand("NMR")
        investment.NMR_amt = ((float(portfolio.NMR_pct) / 100.0) * usd_amt) / price
    if portfolio.CV_pct > 0.0:
        price = get_latest_price_for_shorthand("CV")
        investment.CV_amt = ((float(portfolio.CV_pct) / 100.0) * usd_amt) / price
    if portfolio.OMNI_pct > 0.0:
        price = get_latest_price_for_shorthand("OMNI")
        investment.OMNI_amt = ((float(portfolio.OMNI_pct) / 100.0) * usd_amt) / price
    if portfolio.REM_pct > 0.0:
        price = get_latest_price_for_shorthand("REM")
        investment.REM_amt = ((float(portfolio.REM_pct) / 100.0) * usd_amt) / price
    if portfolio.HYDRO_pct > 0.0:
        price = get_latest_price_for_shorthand("HYDRO")
        investment.HYDRO_amt = ((float(portfolio.HYDRO_pct) / 100.0) * usd_amt) / price
    if portfolio.RBY_pct > 0.0:
        price = get_latest_price_for_shorthand("RBY")
        investment.RBY_amt = ((float(portfolio.RBY_pct) / 100.0) * usd_amt) / price
    if portfolio.ORME_pct > 0.0:
        price = get_latest_price_for_shorthand("ORME")
        investment.ORME_amt = ((float(portfolio.ORME_pct) / 100.0) * usd_amt) / price
    if portfolio.SSP_pct > 0.0:
        price = get_latest_price_for_shorthand("SSP")
        investment.SSP_amt = ((float(portfolio.SSP_pct) / 100.0) * usd_amt) / price
    if portfolio.EVR_pct > 0.0:
        price = get_latest_price_for_shorthand("EVR")
        investment.EVR_amt = ((float(portfolio.EVR_pct) / 100.0) * usd_amt) / price
    if portfolio.MTH_pct > 0.0:
        price = get_latest_price_for_shorthand("MTH")
        investment.MTH_amt = ((float(portfolio.MTH_pct) / 100.0) * usd_amt) / price
    if portfolio.SHND_pct > 0.0:
        price = get_latest_price_for_shorthand("SHND")
        investment.SHND_amt = ((float(portfolio.SHND_pct) / 100.0) * usd_amt) / price
    if portfolio.NEU_pct > 0.0:
        price = get_latest_price_for_shorthand("NEU")
        investment.NEU_amt = ((float(portfolio.NEU_pct) / 100.0) * usd_amt) / price
    if portfolio.RADS_pct > 0.0:
        price = get_latest_price_for_shorthand("RADS")
        investment.RADS_amt = ((float(portfolio.RADS_pct) / 100.0) * usd_amt) / price
    if portfolio.CAPP_pct > 0.0:
        price = get_latest_price_for_shorthand("CAPP")
        investment.CAPP_amt = ((float(portfolio.CAPP_pct) / 100.0) * usd_amt) / price
    if portfolio.STX_pct > 0.0:
        price = get_latest_price_for_shorthand("STX")
        investment.STX_amt = ((float(portfolio.STX_pct) / 100.0) * usd_amt) / price
    if portfolio.MDA_pct > 0.0:
        price = get_latest_price_for_shorthand("MDA")
        investment.MDA_amt = ((float(portfolio.MDA_pct) / 100.0) * usd_amt) / price
    if portfolio.RMT_pct > 0.0:
        price = get_latest_price_for_shorthand("RMT")
        investment.RMT_amt = ((float(portfolio.RMT_pct) / 100.0) * usd_amt) / price
    if portfolio.TIX_pct > 0.0:
        price = get_latest_price_for_shorthand("TIX")
        investment.TIX_amt = ((float(portfolio.TIX_pct) / 100.0) * usd_amt) / price
    if portfolio.MDT_pct > 0.0:
        price = get_latest_price_for_shorthand("MDT")
        investment.MDT_amt = ((float(portfolio.MDT_pct) / 100.0) * usd_amt) / price
    if portfolio.SLR_pct > 0.0:
        price = get_latest_price_for_shorthand("SLR")
        investment.SLR_amt = ((float(portfolio.SLR_pct) / 100.0) * usd_amt) / price
    if portfolio.OAX_pct > 0.0:
        price = get_latest_price_for_shorthand("OAX")
        investment.OAX_amt = ((float(portfolio.OAX_pct) / 100.0) * usd_amt) / price
    if portfolio.ADT_pct > 0.0:
        price = get_latest_price_for_shorthand("ADT")
        investment.ADT_amt = ((float(portfolio.ADT_pct) / 100.0) * usd_amt) / price
    if portfolio.FLO_pct > 0.0:
        price = get_latest_price_for_shorthand("FLO")
        investment.FLO_amt = ((float(portfolio.FLO_pct) / 100.0) * usd_amt) / price
    if portfolio.ARN_pct > 0.0:
        price = get_latest_price_for_shorthand("ARN")
        investment.ARN_amt = ((float(portfolio.ARN_pct) / 100.0) * usd_amt) / price
    if portfolio.BBN_pct > 0.0:
        price = get_latest_price_for_shorthand("BBN")
        investment.BBN_amt = ((float(portfolio.BBN_pct) / 100.0) * usd_amt) / price
    if portfolio.MOON_pct > 0.0:
        price = get_latest_price_for_shorthand("MOON")
        investment.MOON_amt = ((float(portfolio.MOON_pct) / 100.0) * usd_amt) / price
    if portfolio.CHP_pct > 0.0:
        price = get_latest_price_for_shorthand("CHP")
        investment.CHP_amt = ((float(portfolio.CHP_pct) / 100.0) * usd_amt) / price
    if portfolio.AIT_pct > 0.0:
        price = get_latest_price_for_shorthand("AIT")
        investment.AIT_amt = ((float(portfolio.AIT_pct) / 100.0) * usd_amt) / price
    if portfolio.CLO_pct > 0.0:
        price = get_latest_price_for_shorthand("CLO")
        investment.CLO_amt = ((float(portfolio.CLO_pct) / 100.0) * usd_amt) / price
    if portfolio.AIDOC_pct > 0.0:
        price = get_latest_price_for_shorthand("AIDOC")
        investment.AIDOC_amt = ((float(portfolio.AIDOC_pct) / 100.0) * usd_amt) / price
    if portfolio.FDZ_pct > 0.0:
        price = get_latest_price_for_shorthand("FDZ")
        investment.FDZ_amt = ((float(portfolio.FDZ_pct) / 100.0) * usd_amt) / price
    if portfolio.LOC_pct > 0.0:
        price = get_latest_price_for_shorthand("LOC")
        investment.LOC_amt = ((float(portfolio.LOC_pct) / 100.0) * usd_amt) / price
    if portfolio.PAL_pct > 0.0:
        price = get_latest_price_for_shorthand("PAL")
        investment.PAL_amt = ((float(portfolio.PAL_pct) / 100.0) * usd_amt) / price
    if portfolio.IOC_pct > 0.0:
        price = get_latest_price_for_shorthand("IOC")
        investment.IOC_amt = ((float(portfolio.IOC_pct) / 100.0) * usd_amt) / price
    if portfolio.PKC_pct > 0.0:
        price = get_latest_price_for_shorthand("PKC")
        investment.PKC_amt = ((float(portfolio.PKC_pct) / 100.0) * usd_amt) / price
    if portfolio.HXX_pct > 0.0:
        price = get_latest_price_for_shorthand("HXX")
        investment.HXX_amt = ((float(portfolio.HXX_pct) / 100.0) * usd_amt) / price
    if portfolio.UP_pct > 0.0:
        price = get_latest_price_for_shorthand("UP")
        investment.UP_amt = ((float(portfolio.UP_pct) / 100.0) * usd_amt) / price
    if portfolio.SLT_pct > 0.0:
        price = get_latest_price_for_shorthand("SLT")
        investment.SLT_amt = ((float(portfolio.SLT_pct) / 100.0) * usd_amt) / price
    if portfolio.PAT_pct > 0.0:
        price = get_latest_price_for_shorthand("PAT")
        investment.PAT_amt = ((float(portfolio.PAT_pct) / 100.0) * usd_amt) / price
    if portfolio.DICE_pct > 0.0:
        price = get_latest_price_for_shorthand("DICE")
        investment.DICE_amt = ((float(portfolio.DICE_pct) / 100.0) * usd_amt) / price
    if portfolio.EXRN_pct > 0.0:
        price = get_latest_price_for_shorthand("EXRN")
        investment.EXRN_amt = ((float(portfolio.EXRN_pct) / 100.0) * usd_amt) / price
    if portfolio.HMC_pct > 0.0:
        price = get_latest_price_for_shorthand("HMC")
        investment.HMC_amt = ((float(portfolio.HMC_pct) / 100.0) * usd_amt) / price
    if portfolio.SENC_pct > 0.0:
        price = get_latest_price_for_shorthand("SENC")
        investment.SENC_amt = ((float(portfolio.SENC_pct) / 100.0) * usd_amt) / price
    if portfolio.DLT_pct > 0.0:
        price = get_latest_price_for_shorthand("DLT")
        investment.DLT_amt = ((float(portfolio.DLT_pct) / 100.0) * usd_amt) / price
    if portfolio.GEN_pct > 0.0:
        price = get_latest_price_for_shorthand("GEN")
        investment.GEN_amt = ((float(portfolio.GEN_pct) / 100.0) * usd_amt) / price
    if portfolio.CHSB_pct > 0.0:
        price = get_latest_price_for_shorthand("CHSB")
        investment.CHSB_amt = ((float(portfolio.CHSB_pct) / 100.0) * usd_amt) / price
    if portfolio.ABYSS_pct > 0.0:
        price = get_latest_price_for_shorthand("ABYSS")
        investment.ABYSS_amt = ((float(portfolio.ABYSS_pct) / 100.0) * usd_amt) / price
    if portfolio.BQ_pct > 0.0:
        price = get_latest_price_for_shorthand("BQ")
        investment.BQ_amt = ((float(portfolio.BQ_pct) / 100.0) * usd_amt) / price
    if portfolio.EXP_pct > 0.0:
        price = get_latest_price_for_shorthand("EXP")
        investment.EXP_amt = ((float(portfolio.EXP_pct) / 100.0) * usd_amt) / price
    if portfolio.EKO_pct > 0.0:
        price = get_latest_price_for_shorthand("EKO")
        investment.EKO_amt = ((float(portfolio.EKO_pct) / 100.0) * usd_amt) / price
    if portfolio.ZIPT_pct > 0.0:
        price = get_latest_price_for_shorthand("ZIPT")
        investment.ZIPT_amt = ((float(portfolio.ZIPT_pct) / 100.0) * usd_amt) / price
    if portfolio.CLAM_pct > 0.0:
        price = get_latest_price_for_shorthand("CLAM")
        investment.CLAM_amt = ((float(portfolio.CLAM_pct) / 100.0) * usd_amt) / price
    if portfolio.IDH_pct > 0.0:
        price = get_latest_price_for_shorthand("IDH")
        investment.IDH_amt = ((float(portfolio.IDH_pct) / 100.0) * usd_amt) / price
    if portfolio.SRCOIN_pct > 0.0:
        price = get_latest_price_for_shorthand("SRCOIN")
        investment.SRCOIN_amt = ((float(portfolio.SRCOIN_pct) / 100.0) * usd_amt) / price
    if portfolio.ATM_pct > 0.0:
        price = get_latest_price_for_shorthand("ATM")
        investment.ATM_amt = ((float(portfolio.ATM_pct) / 100.0) * usd_amt) / price
    if portfolio.NYC_pct > 0.0:
        price = get_latest_price_for_shorthand("NYC")
        investment.NYC_amt = ((float(portfolio.NYC_pct) / 100.0) * usd_amt) / price
    if portfolio.DEV_pct > 0.0:
        price = get_latest_price_for_shorthand("DEV")
        investment.DEV_amt = ((float(portfolio.DEV_pct) / 100.0) * usd_amt) / price
    if portfolio.GCR_pct > 0.0:
        price = get_latest_price_for_shorthand("GCR")
        investment.GCR_amt = ((float(portfolio.GCR_pct) / 100.0) * usd_amt) / price
    if portfolio.NBAI_pct > 0.0:
        price = get_latest_price_for_shorthand("NBAI")
        investment.NBAI_amt = ((float(portfolio.NBAI_pct) / 100.0) * usd_amt) / price
    if portfolio.POLIS_pct > 0.0:
        price = get_latest_price_for_shorthand("POLIS")
        investment.POLIS_amt = ((float(portfolio.POLIS_pct) / 100.0) * usd_amt) / price
    if portfolio.DTB_pct > 0.0:
        price = get_latest_price_for_shorthand("DTB")
        investment.DTB_amt = ((float(portfolio.DTB_pct) / 100.0) * usd_amt) / price
    if portfolio.CVCOIN_pct > 0.0:
        price = get_latest_price_for_shorthand("CVCOIN")
        investment.CVCOIN_amt = ((float(portfolio.CVCOIN_pct) / 100.0) * usd_amt) / price
    if portfolio.MRK_pct > 0.0:
        price = get_latest_price_for_shorthand("MRK")
        investment.MRK_amt = ((float(portfolio.MRK_pct) / 100.0) * usd_amt) / price
    if portfolio.SHIP_pct > 0.0:
        price = get_latest_price_for_shorthand("SHIP")
        investment.SHIP_amt = ((float(portfolio.SHIP_pct) / 100.0) * usd_amt) / price
    if portfolio.INCNT_pct > 0.0:
        price = get_latest_price_for_shorthand("INCNT")
        investment.INCNT_amt = ((float(portfolio.INCNT_pct) / 100.0) * usd_amt) / price
    if portfolio.HER_pct > 0.0:
        price = get_latest_price_for_shorthand("HER")
        investment.HER_amt = ((float(portfolio.HER_pct) / 100.0) * usd_amt) / price
    if portfolio.AXP_pct > 0.0:
        price = get_latest_price_for_shorthand("AXP")
        investment.AXP_amt = ((float(portfolio.AXP_pct) / 100.0) * usd_amt) / price
    if portfolio.LMC_pct > 0.0:
        price = get_latest_price_for_shorthand("LMC")
        investment.LMC_amt = ((float(portfolio.LMC_pct) / 100.0) * usd_amt) / price
    if portfolio.REBL_pct > 0.0:
        price = get_latest_price_for_shorthand("REBL")
        investment.REBL_amt = ((float(portfolio.REBL_pct) / 100.0) * usd_amt) / price
    if portfolio.APH_pct > 0.0:
        price = get_latest_price_for_shorthand("APH")
        investment.APH_amt = ((float(portfolio.APH_pct) / 100.0) * usd_amt) / price
    if portfolio.DRT_pct > 0.0:
        price = get_latest_price_for_shorthand("DRT")
        investment.DRT_amt = ((float(portfolio.DRT_pct) / 100.0) * usd_amt) / price
    if portfolio.HKN_pct > 0.0:
        price = get_latest_price_for_shorthand("HKN")
        investment.HKN_amt = ((float(portfolio.HKN_pct) / 100.0) * usd_amt) / price
    if portfolio.UBT_pct > 0.0:
        price = get_latest_price_for_shorthand("UBT")
        investment.UBT_amt = ((float(portfolio.UBT_pct) / 100.0) * usd_amt) / price
    if portfolio.XMY_pct > 0.0:
        price = get_latest_price_for_shorthand("XMY")
        investment.XMY_amt = ((float(portfolio.XMY_pct) / 100.0) * usd_amt) / price
    if portfolio.RVT_pct > 0.0:
        price = get_latest_price_for_shorthand("RVT")
        investment.RVT_amt = ((float(portfolio.RVT_pct) / 100.0) * usd_amt) / price
    if portfolio.SEXC_pct > 0.0:
        price = get_latest_price_for_shorthand("SEXC")
        investment.SEXC_amt = ((float(portfolio.SEXC_pct) / 100.0) * usd_amt) / price
    if portfolio.ECOB_pct > 0.0:
        price = get_latest_price_for_shorthand("ECOB")
        investment.ECOB_amt = ((float(portfolio.ECOB_pct) / 100.0) * usd_amt) / price
    if portfolio.SIB_pct > 0.0:
        price = get_latest_price_for_shorthand("SIB")
        investment.SIB_amt = ((float(portfolio.SIB_pct) / 100.0) * usd_amt) / price
    if portfolio.RED_pct > 0.0:
        price = get_latest_price_for_shorthand("RED")
        investment.RED_amt = ((float(portfolio.RED_pct) / 100.0) * usd_amt) / price
    if portfolio.ICOS_pct > 0.0:
        price = get_latest_price_for_shorthand("ICOS")
        investment.ICOS_amt = ((float(portfolio.ICOS_pct) / 100.0) * usd_amt) / price
    if portfolio.SPRTS_pct > 0.0:
        price = get_latest_price_for_shorthand("SPRTS")
        investment.SPRTS_amt = ((float(portfolio.SPRTS_pct) / 100.0) * usd_amt) / price
    if portfolio.GET_pct > 0.0:
        price = get_latest_price_for_shorthand("GET")
        investment.GET_amt = ((float(portfolio.GET_pct) / 100.0) * usd_amt) / price
    if portfolio.PCL_pct > 0.0:
        price = get_latest_price_for_shorthand("PCL")
        investment.PCL_amt = ((float(portfolio.PCL_pct) / 100.0) * usd_amt) / price
    if portfolio.NEOS_pct > 0.0:
        price = get_latest_price_for_shorthand("NEOS")
        investment.NEOS_amt = ((float(portfolio.NEOS_pct) / 100.0) * usd_amt) / price
    if portfolio.BWK_pct > 0.0:
        price = get_latest_price_for_shorthand("BWK")
        investment.BWK_amt = ((float(portfolio.BWK_pct) / 100.0) * usd_amt) / price
    if portfolio.NPX_pct > 0.0:
        price = get_latest_price_for_shorthand("NPX")
        investment.NPX_amt = ((float(portfolio.NPX_pct) / 100.0) * usd_amt) / price
    if portfolio.DYN_pct > 0.0:
        price = get_latest_price_for_shorthand("DYN")
        investment.DYN_amt = ((float(portfolio.DYN_pct) / 100.0) * usd_amt) / price
    if portfolio.BEZ_pct > 0.0:
        price = get_latest_price_for_shorthand("BEZ")
        investment.BEZ_amt = ((float(portfolio.BEZ_pct) / 100.0) * usd_amt) / price
    if portfolio.XST_pct > 0.0:
        price = get_latest_price_for_shorthand("XST")
        investment.XST_amt = ((float(portfolio.XST_pct) / 100.0) * usd_amt) / price
    if portfolio.IPL_pct > 0.0:
        price = get_latest_price_for_shorthand("IPL")
        investment.IPL_amt = ((float(portfolio.IPL_pct) / 100.0) * usd_amt) / price
    if portfolio.VRC_pct > 0.0:
        price = get_latest_price_for_shorthand("VRC")
        investment.VRC_amt = ((float(portfolio.VRC_pct) / 100.0) * usd_amt) / price
    if portfolio.IFT_pct > 0.0:
        price = get_latest_price_for_shorthand("IFT")
        investment.IFT_amt = ((float(portfolio.IFT_pct) / 100.0) * usd_amt) / price
    if portfolio.MUSIC_pct > 0.0:
        price = get_latest_price_for_shorthand("MUSIC")
        investment.MUSIC_amt = ((float(portfolio.MUSIC_pct) / 100.0) * usd_amt) / price
    if portfolio.CAT_pct > 0.0:
        price = get_latest_price_for_shorthand("CAT")
        investment.CAT_amt = ((float(portfolio.CAT_pct) / 100.0) * usd_amt) / price
    if portfolio.LOKI_pct > 0.0:
        price = get_latest_price_for_shorthand("LOKI")
        investment.LOKI_amt = ((float(portfolio.LOKI_pct) / 100.0) * usd_amt) / price
    if portfolio.UCASH_pct > 0.0:
        price = get_latest_price_for_shorthand("UCASH")
        investment.UCASH_amt = ((float(portfolio.UCASH_pct) / 100.0) * usd_amt) / price
    if portfolio.BSD_pct > 0.0:
        price = get_latest_price_for_shorthand("BSD")
        investment.BSD_amt = ((float(portfolio.BSD_pct) / 100.0) * usd_amt) / price
    if portfolio.PIRL_pct > 0.0:
        price = get_latest_price_for_shorthand("PIRL")
        investment.PIRL_amt = ((float(portfolio.PIRL_pct) / 100.0) * usd_amt) / price
    if portfolio.DEB_pct > 0.0:
        price = get_latest_price_for_shorthand("DEB")
        investment.DEB_amt = ((float(portfolio.DEB_pct) / 100.0) * usd_amt) / price
    if portfolio.HWC_pct > 0.0:
        price = get_latest_price_for_shorthand("HWC")
        investment.HWC_amt = ((float(portfolio.HWC_pct) / 100.0) * usd_amt) / price
    if portfolio.NVC_pct > 0.0:
        price = get_latest_price_for_shorthand("NVC")
        investment.NVC_amt = ((float(portfolio.NVC_pct) / 100.0) * usd_amt) / price
    if portfolio.XAUR_pct > 0.0:
        price = get_latest_price_for_shorthand("XAUR")
        investment.XAUR_amt = ((float(portfolio.XAUR_pct) / 100.0) * usd_amt) / price
    if portfolio.FLIXX_pct > 0.0:
        price = get_latest_price_for_shorthand("FLIXX")
        investment.FLIXX_amt = ((float(portfolio.FLIXX_pct) / 100.0) * usd_amt) / price
    if portfolio.RMC_pct > 0.0:
        price = get_latest_price_for_shorthand("RMC")
        investment.RMC_amt = ((float(portfolio.RMC_pct) / 100.0) * usd_amt) / price
    if portfolio.PKT_pct > 0.0:
        price = get_latest_price_for_shorthand("PKT")
        investment.PKT_amt = ((float(portfolio.PKT_pct) / 100.0) * usd_amt) / price
    if portfolio.GBX_pct > 0.0:
        price = get_latest_price_for_shorthand("GBX")
        investment.GBX_amt = ((float(portfolio.GBX_pct) / 100.0) * usd_amt) / price
    if portfolio.NCT_pct > 0.0:
        price = get_latest_price_for_shorthand("NCT")
        investment.NCT_amt = ((float(portfolio.NCT_pct) / 100.0) * usd_amt) / price
    if portfolio.GRFT_pct > 0.0:
        price = get_latest_price_for_shorthand("GRFT")
        investment.GRFT_amt = ((float(portfolio.GRFT_pct) / 100.0) * usd_amt) / price
    if portfolio.EFX_pct > 0.0:
        price = get_latest_price_for_shorthand("EFX")
        investment.EFX_amt = ((float(portfolio.EFX_pct) / 100.0) * usd_amt) / price
    if portfolio.NXC_pct > 0.0:
        price = get_latest_price_for_shorthand("NXC")
        investment.NXC_amt = ((float(portfolio.NXC_pct) / 100.0) * usd_amt) / price
    if portfolio.XPA_pct > 0.0:
        price = get_latest_price_for_shorthand("XPA")
        investment.XPA_amt = ((float(portfolio.XPA_pct) / 100.0) * usd_amt) / price
    if portfolio.AU_pct > 0.0:
        price = get_latest_price_for_shorthand("AU")
        investment.AU_amt = ((float(portfolio.AU_pct) / 100.0) * usd_amt) / price
    if portfolio.SS_pct > 0.0:
        price = get_latest_price_for_shorthand("SS")
        investment.SS_amt = ((float(portfolio.SS_pct) / 100.0) * usd_amt) / price
    if portfolio.APX_pct > 0.0:
        price = get_latest_price_for_shorthand("APX")
        investment.APX_amt = ((float(portfolio.APX_pct) / 100.0) * usd_amt) / price
    if portfolio.PARETO_pct > 0.0:
        price = get_latest_price_for_shorthand("PARETO")
        investment.PARETO_amt = ((float(portfolio.PARETO_pct) / 100.0) * usd_amt) / price
    if portfolio.AIR_pct > 0.0:
        price = get_latest_price_for_shorthand("AIR")
        investment.AIR_amt = ((float(portfolio.AIR_pct) / 100.0) * usd_amt) / price
    if portfolio.PINK_pct > 0.0:
        price = get_latest_price_for_shorthand("PINK")
        investment.PINK_amt = ((float(portfolio.PINK_pct) / 100.0) * usd_amt) / price
    if portfolio.GETX_pct > 0.0:
        price = get_latest_price_for_shorthand("GETX")
        investment.GETX_amt = ((float(portfolio.GETX_pct) / 100.0) * usd_amt) / price
    if portfolio.ZLA_pct > 0.0:
        price = get_latest_price_for_shorthand("ZLA")
        investment.ZLA_amt = ((float(portfolio.ZLA_pct) / 100.0) * usd_amt) / price
    if portfolio.LEV_pct > 0.0:
        price = get_latest_price_for_shorthand("LEV")
        investment.LEV_amt = ((float(portfolio.LEV_pct) / 100.0) * usd_amt) / price
    if portfolio.SWT_pct > 0.0:
        price = get_latest_price_for_shorthand("SWT")
        investment.SWT_amt = ((float(portfolio.SWT_pct) / 100.0) * usd_amt) / price
    if portfolio.AID_pct > 0.0:
        price = get_latest_price_for_shorthand("AID")
        investment.AID_amt = ((float(portfolio.AID_pct) / 100.0) * usd_amt) / price
    if portfolio.TUBE_pct > 0.0:
        price = get_latest_price_for_shorthand("TUBE")
        investment.TUBE_amt = ((float(portfolio.TUBE_pct) / 100.0) * usd_amt) / price
    if portfolio.OK_pct > 0.0:
        price = get_latest_price_for_shorthand("OK")
        investment.OK_amt = ((float(portfolio.OK_pct) / 100.0) * usd_amt) / price
    if portfolio.DGTX_pct > 0.0:
        price = get_latest_price_for_shorthand("DGTX")
        investment.DGTX_amt = ((float(portfolio.DGTX_pct) / 100.0) * usd_amt) / price
    if portfolio.BIO_pct > 0.0:
        price = get_latest_price_for_shorthand("BIO")
        investment.BIO_amt = ((float(portfolio.BIO_pct) / 100.0) * usd_amt) / price
    if portfolio.AVT_pct > 0.0:
        price = get_latest_price_for_shorthand("AVT")
        investment.AVT_amt = ((float(portfolio.AVT_pct) / 100.0) * usd_amt) / price
    if portfolio.MTX_pct > 0.0:
        price = get_latest_price_for_shorthand("MTX")
        investment.MTX_amt = ((float(portfolio.MTX_pct) / 100.0) * usd_amt) / price
    if portfolio.CAG_pct > 0.0:
        price = get_latest_price_for_shorthand("CAG")
        investment.CAG_amt = ((float(portfolio.CAG_pct) / 100.0) * usd_amt) / price
    if portfolio.FLDC_pct > 0.0:
        price = get_latest_price_for_shorthand("FLDC")
        investment.FLDC_amt = ((float(portfolio.FLDC_pct) / 100.0) * usd_amt) / price
    if portfolio.SPD_pct > 0.0:
        price = get_latest_price_for_shorthand("SPD")
        investment.SPD_amt = ((float(portfolio.SPD_pct) / 100.0) * usd_amt) / price
    if portfolio.CXO_pct > 0.0:
        price = get_latest_price_for_shorthand("CXO")
        investment.CXO_amt = ((float(portfolio.CXO_pct) / 100.0) * usd_amt) / price
    if portfolio.PRG_pct > 0.0:
        price = get_latest_price_for_shorthand("PRG")
        investment.PRG_amt = ((float(portfolio.PRG_pct) / 100.0) * usd_amt) / price
    if portfolio.CAN_pct > 0.0:
        price = get_latest_price_for_shorthand("CAN")
        investment.CAN_amt = ((float(portfolio.CAN_pct) / 100.0) * usd_amt) / price
    if portfolio.HBT_pct > 0.0:
        price = get_latest_price_for_shorthand("HBT")
        investment.HBT_amt = ((float(portfolio.HBT_pct) / 100.0) * usd_amt) / price
    if portfolio.PTOY_pct > 0.0:
        price = get_latest_price_for_shorthand("PTOY")
        investment.PTOY_amt = ((float(portfolio.PTOY_pct) / 100.0) * usd_amt) / price
    if portfolio.ZAP_pct > 0.0:
        price = get_latest_price_for_shorthand("ZAP")
        investment.ZAP_amt = ((float(portfolio.ZAP_pct) / 100.0) * usd_amt) / price
    if portfolio.LALA_pct > 0.0:
        price = get_latest_price_for_shorthand("LALA")
        investment.LALA_amt = ((float(portfolio.LALA_pct) / 100.0) * usd_amt) / price
    if portfolio.HBZ_pct > 0.0:
        price = get_latest_price_for_shorthand("HBZ")
        investment.HBZ_amt = ((float(portfolio.HBZ_pct) / 100.0) * usd_amt) / price
    if portfolio.ZOI_pct > 0.0:
        price = get_latest_price_for_shorthand("ZOI")
        investment.ZOI_amt = ((float(portfolio.ZOI_pct) / 100.0) * usd_amt) / price
    if portfolio.PND_pct > 0.0:
        price = get_latest_price_for_shorthand("PND")
        investment.PND_amt = ((float(portfolio.PND_pct) / 100.0) * usd_amt) / price
    if portfolio.ERO_pct > 0.0:
        price = get_latest_price_for_shorthand("ERO")
        investment.ERO_amt = ((float(portfolio.ERO_pct) / 100.0) * usd_amt) / price
    if portfolio.BDG_pct > 0.0:
        price = get_latest_price_for_shorthand("BDG")
        investment.BDG_amt = ((float(portfolio.BDG_pct) / 100.0) * usd_amt) / price
    if portfolio.ADB_pct > 0.0:
        price = get_latest_price_for_shorthand("ADB")
        investment.ADB_amt = ((float(portfolio.ADB_pct) / 100.0) * usd_amt) / price
    if portfolio.ZRC_pct > 0.0:
        price = get_latest_price_for_shorthand("ZRC")
        investment.ZRC_amt = ((float(portfolio.ZRC_pct) / 100.0) * usd_amt) / price
    if portfolio.GOLOS_pct > 0.0:
        price = get_latest_price_for_shorthand("GOLOS")
        investment.GOLOS_amt = ((float(portfolio.GOLOS_pct) / 100.0) * usd_amt) / price
    if portfolio.DERO_pct > 0.0:
        price = get_latest_price_for_shorthand("DERO")
        investment.DERO_amt = ((float(portfolio.DERO_pct) / 100.0) * usd_amt) / price
    if portfolio.MINT_pct > 0.0:
        price = get_latest_price_for_shorthand("MINT")
        investment.MINT_amt = ((float(portfolio.MINT_pct) / 100.0) * usd_amt) / price
    if portfolio.LNC_pct > 0.0:
        price = get_latest_price_for_shorthand("LNC")
        investment.LNC_amt = ((float(portfolio.LNC_pct) / 100.0) * usd_amt) / price
    if portfolio.LWF_pct > 0.0:
        price = get_latest_price_for_shorthand("LWF")
        investment.LWF_amt = ((float(portfolio.LWF_pct) / 100.0) * usd_amt) / price
    if portfolio.DNA_pct > 0.0:
        price = get_latest_price_for_shorthand("DNA")
        investment.DNA_amt = ((float(portfolio.DNA_pct) / 100.0) * usd_amt) / price
    if portfolio.BCC_pct > 0.0:
        price = get_latest_price_for_shorthand("BCC")
        investment.BCC_amt = ((float(portfolio.BCC_pct) / 100.0) * usd_amt) / price
    if portfolio.ADH_pct > 0.0:
        price = get_latest_price_for_shorthand("ADH")
        investment.ADH_amt = ((float(portfolio.ADH_pct) / 100.0) * usd_amt) / price
    if portfolio.PUT_pct > 0.0:
        price = get_latest_price_for_shorthand("PUT")
        investment.PUT_amt = ((float(portfolio.PUT_pct) / 100.0) * usd_amt) / price
    if portfolio.DOT_pct > 0.0:
        price = get_latest_price_for_shorthand("DOT")
        investment.DOT_amt = ((float(portfolio.DOT_pct) / 100.0) * usd_amt) / price
    if portfolio.XNK_pct > 0.0:
        price = get_latest_price_for_shorthand("XNK")
        investment.XNK_amt = ((float(portfolio.XNK_pct) / 100.0) * usd_amt) / price
    if portfolio.SIG_pct > 0.0:
        price = get_latest_price_for_shorthand("SIG")
        investment.SIG_amt = ((float(portfolio.SIG_pct) / 100.0) * usd_amt) / price
    if portfolio.SENSE_pct > 0.0:
        price = get_latest_price_for_shorthand("SENSE")
        investment.SENSE_amt = ((float(portfolio.SENSE_pct) / 100.0) * usd_amt) / price
    if portfolio.MLM_pct > 0.0:
        price = get_latest_price_for_shorthand("MLM")
        investment.MLM_amt = ((float(portfolio.MLM_pct) / 100.0) * usd_amt) / price
    if portfolio.IDXM_pct > 0.0:
        price = get_latest_price_for_shorthand("IDXM")
        investment.IDXM_amt = ((float(portfolio.IDXM_pct) / 100.0) * usd_amt) / price
    if portfolio.FLUZ_pct > 0.0:
        price = get_latest_price_for_shorthand("FLUZ")
        investment.FLUZ_amt = ((float(portfolio.FLUZ_pct) / 100.0) * usd_amt) / price
    if portfolio.BET_pct > 0.0:
        price = get_latest_price_for_shorthand("BET")
        investment.BET_amt = ((float(portfolio.BET_pct) / 100.0) * usd_amt) / price
    if portfolio.NET_pct > 0.0:
        price = get_latest_price_for_shorthand("NET")
        investment.NET_amt = ((float(portfolio.NET_pct) / 100.0) * usd_amt) / price
    if portfolio.BERRY_pct > 0.0:
        price = get_latest_price_for_shorthand("BERRY")
        investment.BERRY_amt = ((float(portfolio.BERRY_pct) / 100.0) * usd_amt) / price
    if portfolio.ELIX_pct > 0.0:
        price = get_latest_price_for_shorthand("ELIX")
        investment.ELIX_amt = ((float(portfolio.ELIX_pct) / 100.0) * usd_amt) / price
    if portfolio.TRST_pct > 0.0:
        price = get_latest_price_for_shorthand("TRST")
        investment.TRST_amt = ((float(portfolio.TRST_pct) / 100.0) * usd_amt) / price
    if portfolio.SEQ_pct > 0.0:
        price = get_latest_price_for_shorthand("SEQ")
        investment.SEQ_amt = ((float(portfolio.SEQ_pct) / 100.0) * usd_amt) / price
    if portfolio.YOC_pct > 0.0:
        price = get_latest_price_for_shorthand("YOC")
        investment.YOC_amt = ((float(portfolio.YOC_pct) / 100.0) * usd_amt) / price
    if portfolio.ADI_pct > 0.0:
        price = get_latest_price_for_shorthand("ADI")
        investment.ADI_amt = ((float(portfolio.ADI_pct) / 100.0) * usd_amt) / price
    if portfolio.BNTY_pct > 0.0:
        price = get_latest_price_for_shorthand("BNTY")
        investment.BNTY_amt = ((float(portfolio.BNTY_pct) / 100.0) * usd_amt) / price
    if portfolio.HEAT_pct > 0.0:
        price = get_latest_price_for_shorthand("HEAT")
        investment.HEAT_amt = ((float(portfolio.HEAT_pct) / 100.0) * usd_amt) / price
    if portfolio.ALIS_pct > 0.0:
        price = get_latest_price_for_shorthand("ALIS")
        investment.ALIS_amt = ((float(portfolio.ALIS_pct) / 100.0) * usd_amt) / price
    if portfolio.B2B_pct > 0.0:
        price = get_latest_price_for_shorthand("B2B")
        investment.B2B_amt = ((float(portfolio.B2B_pct) / 100.0) * usd_amt) / price
    if portfolio.TGT_pct > 0.0:
        price = get_latest_price_for_shorthand("TGT")
        investment.TGT_amt = ((float(portfolio.TGT_pct) / 100.0) * usd_amt) / price
    if portfolio.ENRG_pct > 0.0:
        price = get_latest_price_for_shorthand("ENRG")
        investment.ENRG_amt = ((float(portfolio.ENRG_pct) / 100.0) * usd_amt) / price
    if portfolio.ESP_pct > 0.0:
        price = get_latest_price_for_shorthand("ESP")
        investment.ESP_amt = ((float(portfolio.ESP_pct) / 100.0) * usd_amt) / price
    if portfolio.APR_pct > 0.0:
        price = get_latest_price_for_shorthand("APR")
        investment.APR_amt = ((float(portfolio.APR_pct) / 100.0) * usd_amt) / price
    if portfolio.MITX_pct > 0.0:
        price = get_latest_price_for_shorthand("MITX")
        investment.MITX_amt = ((float(portfolio.MITX_pct) / 100.0) * usd_amt) / price
    if portfolio.e_1WO_pct > 0.0:
        price = get_latest_price_for_shorthand("1WO")
        investment.e_1WO_amt = ((float(portfolio.e_1WO_pct) / 100.0) * usd_amt) / price
    if portfolio.XLR_pct > 0.0:
        price = get_latest_price_for_shorthand("XLR")
        investment.XLR_amt = ((float(portfolio.XLR_pct) / 100.0) * usd_amt) / price
    if portfolio.XSPEC_pct > 0.0:
        price = get_latest_price_for_shorthand("XSPEC")
        investment.XSPEC_amt = ((float(portfolio.XSPEC_pct) / 100.0) * usd_amt) / price
    if portfolio.CBT_pct > 0.0:
        price = get_latest_price_for_shorthand("CBT")
        investment.CBT_amt = ((float(portfolio.CBT_pct) / 100.0) * usd_amt) / price
    if portfolio.CURE_pct > 0.0:
        price = get_latest_price_for_shorthand("CURE")
        investment.CURE_amt = ((float(portfolio.CURE_pct) / 100.0) * usd_amt) / price
    if portfolio.CFUN_pct > 0.0:
        price = get_latest_price_for_shorthand("CFUN")
        investment.CFUN_amt = ((float(portfolio.CFUN_pct) / 100.0) * usd_amt) / price
    if portfolio.COFI_pct > 0.0:
        price = get_latest_price_for_shorthand("COFI")
        investment.COFI_amt = ((float(portfolio.COFI_pct) / 100.0) * usd_amt) / price
    if portfolio.CLN_pct > 0.0:
        price = get_latest_price_for_shorthand("CLN")
        investment.CLN_amt = ((float(portfolio.CLN_pct) / 100.0) * usd_amt) / price
    if portfolio.BEE_pct > 0.0:
        price = get_latest_price_for_shorthand("BEE")
        investment.BEE_amt = ((float(portfolio.BEE_pct) / 100.0) * usd_amt) / price
    if portfolio.BCY_pct > 0.0:
        price = get_latest_price_for_shorthand("BCY")
        investment.BCY_amt = ((float(portfolio.BCY_pct) / 100.0) * usd_amt) / price
    if portfolio.FID_pct > 0.0:
        price = get_latest_price_for_shorthand("FID")
        investment.FID_amt = ((float(portfolio.FID_pct) / 100.0) * usd_amt) / price
    if portfolio.LDC_pct > 0.0:
        price = get_latest_price_for_shorthand("LDC")
        investment.LDC_amt = ((float(portfolio.LDC_pct) / 100.0) * usd_amt) / price
    if portfolio.FACE_pct > 0.0:
        price = get_latest_price_for_shorthand("FACE")
        investment.FACE_amt = ((float(portfolio.FACE_pct) / 100.0) * usd_amt) / price
    if portfolio.MORPH_pct > 0.0:
        price = get_latest_price_for_shorthand("MORPH")
        investment.MORPH_amt = ((float(portfolio.MORPH_pct) / 100.0) * usd_amt) / price
    if portfolio.MYST_pct > 0.0:
        price = get_latest_price_for_shorthand("MYST")
        investment.MYST_amt = ((float(portfolio.MYST_pct) / 100.0) * usd_amt) / price
    if portfolio.PBT_pct > 0.0:
        price = get_latest_price_for_shorthand("PBT")
        investment.PBT_amt = ((float(portfolio.PBT_pct) / 100.0) * usd_amt) / price
    if portfolio.GLD_pct > 0.0:
        price = get_latest_price_for_shorthand("GLD")
        investment.GLD_amt = ((float(portfolio.GLD_pct) / 100.0) * usd_amt) / price
    if portfolio.ADST_pct > 0.0:
        price = get_latest_price_for_shorthand("ADST")
        investment.ADST_amt = ((float(portfolio.ADST_pct) / 100.0) * usd_amt) / price
    if portfolio.LND_pct > 0.0:
        price = get_latest_price_for_shorthand("LND")
        investment.LND_amt = ((float(portfolio.LND_pct) / 100.0) * usd_amt) / price
    if portfolio.COVAL_pct > 0.0:
        price = get_latest_price_for_shorthand("COVAL")
        investment.COVAL_amt = ((float(portfolio.COVAL_pct) / 100.0) * usd_amt) / price
    if portfolio.AUR_pct > 0.0:
        price = get_latest_price_for_shorthand("AUR")
        investment.AUR_amt = ((float(portfolio.AUR_pct) / 100.0) * usd_amt) / price
    if portfolio.SETH_pct > 0.0:
        price = get_latest_price_for_shorthand("SETH")
        investment.SETH_amt = ((float(portfolio.SETH_pct) / 100.0) * usd_amt) / price
    if portfolio.SNOV_pct > 0.0:
        price = get_latest_price_for_shorthand("SNOV")
        investment.SNOV_amt = ((float(portfolio.SNOV_pct) / 100.0) * usd_amt) / price
    if portfolio.EVE_pct > 0.0:
        price = get_latest_price_for_shorthand("EVE")
        investment.EVE_amt = ((float(portfolio.EVE_pct) / 100.0) * usd_amt) / price
    if portfolio.ATB_pct > 0.0:
        price = get_latest_price_for_shorthand("ATB")
        investment.ATB_amt = ((float(portfolio.ATB_pct) / 100.0) * usd_amt) / price
    if portfolio.TOA_pct > 0.0:
        price = get_latest_price_for_shorthand("TOA")
        investment.TOA_amt = ((float(portfolio.TOA_pct) / 100.0) * usd_amt) / price
    if portfolio.TFL_pct > 0.0:
        price = get_latest_price_for_shorthand("TFL")
        investment.TFL_amt = ((float(portfolio.TFL_pct) / 100.0) * usd_amt) / price
    if portfolio.SPHR_pct > 0.0:
        price = get_latest_price_for_shorthand("SPHR")
        investment.SPHR_amt = ((float(portfolio.SPHR_pct) / 100.0) * usd_amt) / price
    if portfolio.MYB_pct > 0.0:
        price = get_latest_price_for_shorthand("MYB")
        investment.MYB_amt = ((float(portfolio.MYB_pct) / 100.0) * usd_amt) / price
    if portfolio.PRIX_pct > 0.0:
        price = get_latest_price_for_shorthand("PRIX")
        investment.PRIX_amt = ((float(portfolio.PRIX_pct) / 100.0) * usd_amt) / price
    if portfolio.POLL_pct > 0.0:
        price = get_latest_price_for_shorthand("POLL")
        investment.POLL_amt = ((float(portfolio.POLL_pct) / 100.0) * usd_amt) / price
    if portfolio.EZT_pct > 0.0:
        price = get_latest_price_for_shorthand("EZT")
        investment.EZT_amt = ((float(portfolio.EZT_pct) / 100.0) * usd_amt) / price
    if portfolio.WCT_pct > 0.0:
        price = get_latest_price_for_shorthand("WCT")
        investment.WCT_amt = ((float(portfolio.WCT_pct) / 100.0) * usd_amt) / price
    if portfolio.MAX_pct > 0.0:
        price = get_latest_price_for_shorthand("MAX")
        investment.MAX_amt = ((float(portfolio.MAX_pct) / 100.0) * usd_amt) / price
    if portfolio.CSNO_pct > 0.0:
        price = get_latest_price_for_shorthand("CSNO")
        investment.CSNO_amt = ((float(portfolio.CSNO_pct) / 100.0) * usd_amt) / price
    if portfolio.TRF_pct > 0.0:
        price = get_latest_price_for_shorthand("TRF")
        investment.TRF_amt = ((float(portfolio.TRF_pct) / 100.0) * usd_amt) / price
    if portfolio.AVA_pct > 0.0:
        price = get_latest_price_for_shorthand("AVA")
        investment.AVA_amt = ((float(portfolio.AVA_pct) / 100.0) * usd_amt) / price
    if portfolio.SYNX_pct > 0.0:
        price = get_latest_price_for_shorthand("SYNX")
        investment.SYNX_amt = ((float(portfolio.SYNX_pct) / 100.0) * usd_amt) / price
    if portfolio.GLA_pct > 0.0:
        price = get_latest_price_for_shorthand("GLA")
        investment.GLA_amt = ((float(portfolio.GLA_pct) / 100.0) * usd_amt) / price
    if portfolio.REAL_pct > 0.0:
        price = get_latest_price_for_shorthand("REAL")
        investment.REAL_amt = ((float(portfolio.REAL_pct) / 100.0) * usd_amt) / price
    if portfolio.IPSX_pct > 0.0:
        price = get_latest_price_for_shorthand("IPSX")
        investment.IPSX_amt = ((float(portfolio.IPSX_pct) / 100.0) * usd_amt) / price
    if portfolio.ABY_pct > 0.0:
        price = get_latest_price_for_shorthand("ABY")
        investment.ABY_amt = ((float(portfolio.ABY_pct) / 100.0) * usd_amt) / price
    if portfolio.TX_pct > 0.0:
        price = get_latest_price_for_shorthand("TX")
        investment.TX_amt = ((float(portfolio.TX_pct) / 100.0) * usd_amt) / price
    if portfolio.NPER_pct > 0.0:
        price = get_latest_price_for_shorthand("NPER")
        investment.NPER_amt = ((float(portfolio.NPER_pct) / 100.0) * usd_amt) / price
    if portfolio.KORE_pct > 0.0:
        price = get_latest_price_for_shorthand("KORE")
        investment.KORE_amt = ((float(portfolio.KORE_pct) / 100.0) * usd_amt) / price
    if portfolio.TIPS_pct > 0.0:
        price = get_latest_price_for_shorthand("TIPS")
        investment.TIPS_amt = ((float(portfolio.TIPS_pct) / 100.0) * usd_amt) / price
    if portfolio.ARY_pct > 0.0:
        price = get_latest_price_for_shorthand("ARY")
        investment.ARY_amt = ((float(portfolio.ARY_pct) / 100.0) * usd_amt) / price
    if portfolio.VIT_pct > 0.0:
        price = get_latest_price_for_shorthand("VIT")
        investment.VIT_amt = ((float(portfolio.VIT_pct) / 100.0) * usd_amt) / price
    if portfolio.OBITS_pct > 0.0:
        price = get_latest_price_for_shorthand("OBITS")
        investment.OBITS_amt = ((float(portfolio.OBITS_pct) / 100.0) * usd_amt) / price
    if portfolio.SHL_pct > 0.0:
        price = get_latest_price_for_shorthand("SHL")
        investment.SHL_amt = ((float(portfolio.SHL_pct) / 100.0) * usd_amt) / price
    if portfolio.WRC_pct > 0.0:
        price = get_latest_price_for_shorthand("WRC")
        investment.WRC_amt = ((float(portfolio.WRC_pct) / 100.0) * usd_amt) / price
    if portfolio.SHP_pct > 0.0:
        price = get_latest_price_for_shorthand("SHP")
        investment.SHP_amt = ((float(portfolio.SHP_pct) / 100.0) * usd_amt) / price
    if portfolio.HQX_pct > 0.0:
        price = get_latest_price_for_shorthand("HQX")
        investment.HQX_amt = ((float(portfolio.HQX_pct) / 100.0) * usd_amt) / price
    if portfolio.J8T_pct > 0.0:
        price = get_latest_price_for_shorthand("J8T")
        investment.J8T_amt = ((float(portfolio.J8T_pct) / 100.0) * usd_amt) / price
    if portfolio.INXT_pct > 0.0:
        price = get_latest_price_for_shorthand("INXT")
        investment.INXT_amt = ((float(portfolio.INXT_pct) / 100.0) * usd_amt) / price
    if portfolio.BRX_pct > 0.0:
        price = get_latest_price_for_shorthand("BRX")
        investment.BRX_amt = ((float(portfolio.BRX_pct) / 100.0) * usd_amt) / price
    if portfolio.VME_pct > 0.0:
        price = get_latest_price_for_shorthand("VME")
        investment.VME_amt = ((float(portfolio.VME_pct) / 100.0) * usd_amt) / price
    if portfolio.BTCZ_pct > 0.0:
        price = get_latest_price_for_shorthand("BTCZ")
        investment.BTCZ_amt = ((float(portfolio.BTCZ_pct) / 100.0) * usd_amt) / price
    if portfolio.PTC_pct > 0.0:
        price = get_latest_price_for_shorthand("PTC")
        investment.PTC_amt = ((float(portfolio.PTC_pct) / 100.0) * usd_amt) / price
    if portfolio.MONK_pct > 0.0:
        price = get_latest_price_for_shorthand("MONK")
        investment.MONK_amt = ((float(portfolio.MONK_pct) / 100.0) * usd_amt) / price
    if portfolio.HUR_pct > 0.0:
        price = get_latest_price_for_shorthand("HUR")
        investment.HUR_amt = ((float(portfolio.HUR_pct) / 100.0) * usd_amt) / price
    if portfolio.GEO_pct > 0.0:
        price = get_latest_price_for_shorthand("GEO")
        investment.GEO_amt = ((float(portfolio.GEO_pct) / 100.0) * usd_amt) / price
    if portfolio.e_2GIVE_pct > 0.0:
        price = get_latest_price_for_shorthand("2GIVE")
        investment.e_2GIVE_amt = ((float(portfolio.e_2GIVE_pct) / 100.0) * usd_amt) / price
    if portfolio.ASTRO_pct > 0.0:
        price = get_latest_price_for_shorthand("ASTRO")
        investment.ASTRO_amt = ((float(portfolio.ASTRO_pct) / 100.0) * usd_amt) / price
    if portfolio.AUC_pct > 0.0:
        price = get_latest_price_for_shorthand("AUC")
        investment.AUC_amt = ((float(portfolio.AUC_pct) / 100.0) * usd_amt) / price
    if portfolio.DTH_pct > 0.0:
        price = get_latest_price_for_shorthand("DTH")
        investment.DTH_amt = ((float(portfolio.DTH_pct) / 100.0) * usd_amt) / price
    if portfolio.OTN_pct > 0.0:
        price = get_latest_price_for_shorthand("OTN")
        investment.OTN_amt = ((float(portfolio.OTN_pct) / 100.0) * usd_amt) / price
    if portfolio.BLUE_pct > 0.0:
        price = get_latest_price_for_shorthand("BLUE")
        investment.BLUE_amt = ((float(portfolio.BLUE_pct) / 100.0) * usd_amt) / price
    if portfolio.PLAY_pct > 0.0:
        price = get_latest_price_for_shorthand("PLAY")
        investment.PLAY_amt = ((float(portfolio.PLAY_pct) / 100.0) * usd_amt) / price
    if portfolio.XBC_pct > 0.0:
        price = get_latest_price_for_shorthand("XBC")
        investment.XBC_amt = ((float(portfolio.XBC_pct) / 100.0) * usd_amt) / price
    if portfolio.FND_pct > 0.0:
        price = get_latest_price_for_shorthand("FND")
        investment.FND_amt = ((float(portfolio.FND_pct) / 100.0) * usd_amt) / price
    if portfolio.PFR_pct > 0.0:
        price = get_latest_price_for_shorthand("PFR")
        investment.PFR_amt = ((float(portfolio.PFR_pct) / 100.0) * usd_amt) / price
    if portfolio.HYP_pct > 0.0:
        price = get_latest_price_for_shorthand("HYP")
        investment.HYP_amt = ((float(portfolio.HYP_pct) / 100.0) * usd_amt) / price
    if portfolio.GCC_pct > 0.0:
        price = get_latest_price_for_shorthand("GCC")
        investment.GCC_amt = ((float(portfolio.GCC_pct) / 100.0) * usd_amt) / price
    if portfolio.IOP_pct > 0.0:
        price = get_latest_price_for_shorthand("IOP")
        investment.IOP_amt = ((float(portfolio.IOP_pct) / 100.0) * usd_amt) / price
    if portfolio.FDX_pct > 0.0:
        price = get_latest_price_for_shorthand("FDX")
        investment.FDX_amt = ((float(portfolio.FDX_pct) / 100.0) * usd_amt) / price
    if portfolio.ATL_pct > 0.0:
        price = get_latest_price_for_shorthand("ATL")
        investment.ATL_amt = ((float(portfolio.ATL_pct) / 100.0) * usd_amt) / price
    if portfolio.INSTAR_pct > 0.0:
        price = get_latest_price_for_shorthand("INSTAR")
        investment.INSTAR_amt = ((float(portfolio.INSTAR_pct) / 100.0) * usd_amt) / price
    if portfolio.HGT_pct > 0.0:
        price = get_latest_price_for_shorthand("HGT")
        investment.HGT_amt = ((float(portfolio.HGT_pct) / 100.0) * usd_amt) / price
    if portfolio.LEDU_pct > 0.0:
        price = get_latest_price_for_shorthand("LEDU")
        investment.LEDU_amt = ((float(portfolio.LEDU_pct) / 100.0) * usd_amt) / price
    if portfolio.UNIT_pct > 0.0:
        price = get_latest_price_for_shorthand("UNIT")
        investment.UNIT_amt = ((float(portfolio.UNIT_pct) / 100.0) * usd_amt) / price
    if portfolio.USNBT_pct > 0.0:
        price = get_latest_price_for_shorthand("USNBT")
        investment.USNBT_amt = ((float(portfolio.USNBT_pct) / 100.0) * usd_amt) / price
    if portfolio.SUMO_pct > 0.0:
        price = get_latest_price_for_shorthand("SUMO")
        investment.SUMO_amt = ((float(portfolio.SUMO_pct) / 100.0) * usd_amt) / price
    if portfolio.EXY_pct > 0.0:
        price = get_latest_price_for_shorthand("EXY")
        investment.EXY_amt = ((float(portfolio.EXY_pct) / 100.0) * usd_amt) / price
    if portfolio.e_0xBTC_pct > 0.0:
        price = get_latest_price_for_shorthand("0xBTC")
        investment.e_0xBTC_amt = ((float(portfolio.e_0xBTC_pct) / 100.0) * usd_amt) / price
    if portfolio.SPR_pct > 0.0:
        price = get_latest_price_for_shorthand("SPR")
        investment.SPR_amt = ((float(portfolio.SPR_pct) / 100.0) * usd_amt) / price
    if portfolio.ERC_pct > 0.0:
        price = get_latest_price_for_shorthand("ERC")
        investment.ERC_amt = ((float(portfolio.ERC_pct) / 100.0) * usd_amt) / price
    if portfolio.XHV_pct > 0.0:
        price = get_latest_price_for_shorthand("XHV")
        investment.XHV_amt = ((float(portfolio.XHV_pct) / 100.0) * usd_amt) / price
    if portfolio.INV_pct > 0.0:
        price = get_latest_price_for_shorthand("INV")
        investment.INV_amt = ((float(portfolio.INV_pct) / 100.0) * usd_amt) / price
    if portfolio.CPAY_pct > 0.0:
        price = get_latest_price_for_shorthand("CPAY")
        investment.CPAY_amt = ((float(portfolio.CPAY_pct) / 100.0) * usd_amt) / price
    if portfolio.IXC_pct > 0.0:
        price = get_latest_price_for_shorthand("IXC")
        investment.IXC_amt = ((float(portfolio.IXC_pct) / 100.0) * usd_amt) / price
    if portfolio.BUZZ_pct > 0.0:
        price = get_latest_price_for_shorthand("BUZZ")
        investment.BUZZ_amt = ((float(portfolio.BUZZ_pct) / 100.0) * usd_amt) / price
    if portfolio.BBO_pct > 0.0:
        price = get_latest_price_for_shorthand("BBO")
        investment.BBO_amt = ((float(portfolio.BBO_pct) / 100.0) * usd_amt) / price
    if portfolio.HAC_pct > 0.0:
        price = get_latest_price_for_shorthand("HAC")
        investment.HAC_amt = ((float(portfolio.HAC_pct) / 100.0) * usd_amt) / price
    if portfolio.BSTN_pct > 0.0:
        price = get_latest_price_for_shorthand("BSTN")
        investment.BSTN_amt = ((float(portfolio.BSTN_pct) / 100.0) * usd_amt) / price
    if portfolio.NTRN_pct > 0.0:
        price = get_latest_price_for_shorthand("NTRN")
        investment.NTRN_amt = ((float(portfolio.NTRN_pct) / 100.0) * usd_amt) / price
    if portfolio.XMCC_pct > 0.0:
        price = get_latest_price_for_shorthand("XMCC")
        investment.XMCC_amt = ((float(portfolio.XMCC_pct) / 100.0) * usd_amt) / price
    if portfolio.SXUT_pct > 0.0:
        price = get_latest_price_for_shorthand("SXUT")
        investment.SXUT_amt = ((float(portfolio.SXUT_pct) / 100.0) * usd_amt) / price
    if portfolio.UFR_pct > 0.0:
        price = get_latest_price_for_shorthand("UFR")
        investment.UFR_amt = ((float(portfolio.UFR_pct) / 100.0) * usd_amt) / price
    if portfolio.SPF_pct > 0.0:
        price = get_latest_price_for_shorthand("SPF")
        investment.SPF_amt = ((float(portfolio.SPF_pct) / 100.0) * usd_amt) / price
    if portfolio.GMT_pct > 0.0:
        price = get_latest_price_for_shorthand("GMT")
        investment.GMT_amt = ((float(portfolio.GMT_pct) / 100.0) * usd_amt) / price
    if portfolio.SEND_pct > 0.0:
        price = get_latest_price_for_shorthand("SEND")
        investment.SEND_amt = ((float(portfolio.SEND_pct) / 100.0) * usd_amt) / price
    if portfolio.AMLT_pct > 0.0:
        price = get_latest_price_for_shorthand("AMLT")
        investment.AMLT_amt = ((float(portfolio.AMLT_pct) / 100.0) * usd_amt) / price
    if portfolio.SCL_pct > 0.0:
        price = get_latest_price_for_shorthand("SCL")
        investment.SCL_amt = ((float(portfolio.SCL_pct) / 100.0) * usd_amt) / price
    if portfolio.QWARK_pct > 0.0:
        price = get_latest_price_for_shorthand("QWARK")
        investment.QWARK_amt = ((float(portfolio.QWARK_pct) / 100.0) * usd_amt) / price
    if portfolio.DOPE_pct > 0.0:
        price = get_latest_price_for_shorthand("DOPE")
        investment.DOPE_amt = ((float(portfolio.DOPE_pct) / 100.0) * usd_amt) / price
    if portfolio.TKS_pct > 0.0:
        price = get_latest_price_for_shorthand("TKS")
        investment.TKS_amt = ((float(portfolio.TKS_pct) / 100.0) * usd_amt) / price
    if portfolio.MSR_pct > 0.0:
        price = get_latest_price_for_shorthand("MSR")
        investment.MSR_amt = ((float(portfolio.MSR_pct) / 100.0) * usd_amt) / price
    if portfolio.FTX_pct > 0.0:
        price = get_latest_price_for_shorthand("FTX")
        investment.FTX_amt = ((float(portfolio.FTX_pct) / 100.0) * usd_amt) / price
    if portfolio.TKA_pct > 0.0:
        price = get_latest_price_for_shorthand("TKA")
        investment.TKA_amt = ((float(portfolio.TKA_pct) / 100.0) * usd_amt) / price
    if portfolio.VRM_pct > 0.0:
        price = get_latest_price_for_shorthand("VRM")
        investment.VRM_amt = ((float(portfolio.VRM_pct) / 100.0) * usd_amt) / price
    if portfolio.RIC_pct > 0.0:
        price = get_latest_price_for_shorthand("RIC")
        investment.RIC_amt = ((float(portfolio.RIC_pct) / 100.0) * usd_amt) / price
    if portfolio.PING_pct > 0.0:
        price = get_latest_price_for_shorthand("PING")
        investment.PING_amt = ((float(portfolio.PING_pct) / 100.0) * usd_amt) / price
    if portfolio.PBL_pct > 0.0:
        price = get_latest_price_for_shorthand("PBL")
        investment.PBL_amt = ((float(portfolio.PBL_pct) / 100.0) * usd_amt) / price
    if portfolio.RUPX_pct > 0.0:
        price = get_latest_price_for_shorthand("RUPX")
        investment.RUPX_amt = ((float(portfolio.RUPX_pct) / 100.0) * usd_amt) / price
    if portfolio.GAT_pct > 0.0:
        price = get_latest_price_for_shorthand("GAT")
        investment.GAT_amt = ((float(portfolio.GAT_pct) / 100.0) * usd_amt) / price
    if portfolio.ZEIT_pct > 0.0:
        price = get_latest_price_for_shorthand("ZEIT")
        investment.ZEIT_amt = ((float(portfolio.ZEIT_pct) / 100.0) * usd_amt) / price
    if portfolio.VOISE_pct > 0.0:
        price = get_latest_price_for_shorthand("VOISE")
        investment.VOISE_amt = ((float(portfolio.VOISE_pct) / 100.0) * usd_amt) / price
    if portfolio.ING_pct > 0.0:
        price = get_latest_price_for_shorthand("ING")
        investment.ING_amt = ((float(portfolio.ING_pct) / 100.0) * usd_amt) / price
    if portfolio.EXCL_pct > 0.0:
        price = get_latest_price_for_shorthand("EXCL")
        investment.EXCL_amt = ((float(portfolio.EXCL_pct) / 100.0) * usd_amt) / price
    if portfolio.HOLD_pct > 0.0:
        price = get_latest_price_for_shorthand("HOLD")
        investment.HOLD_amt = ((float(portfolio.HOLD_pct) / 100.0) * usd_amt) / price
    if portfolio.WISH_pct > 0.0:
        price = get_latest_price_for_shorthand("WISH")
        investment.WISH_amt = ((float(portfolio.WISH_pct) / 100.0) * usd_amt) / price
    if portfolio.IND_pct > 0.0:
        price = get_latest_price_for_shorthand("IND")
        investment.IND_amt = ((float(portfolio.IND_pct) / 100.0) * usd_amt) / price
    if portfolio.MEME_pct > 0.0:
        price = get_latest_price_for_shorthand("MEME")
        investment.MEME_amt = ((float(portfolio.MEME_pct) / 100.0) * usd_amt) / price
    if portfolio.ALT_pct > 0.0:
        price = get_latest_price_for_shorthand("ALT")
        investment.ALT_amt = ((float(portfolio.ALT_pct) / 100.0) * usd_amt) / price
    if portfolio.BON_pct > 0.0:
        price = get_latest_price_for_shorthand("BON")
        investment.BON_amt = ((float(portfolio.BON_pct) / 100.0) * usd_amt) / price
    if portfolio.BRK_pct > 0.0:
        price = get_latest_price_for_shorthand("BRK")
        investment.BRK_amt = ((float(portfolio.BRK_pct) / 100.0) * usd_amt) / price
    if portfolio.EBST_pct > 0.0:
        price = get_latest_price_for_shorthand("EBST")
        investment.EBST_amt = ((float(portfolio.EBST_pct) / 100.0) * usd_amt) / price
    if portfolio.BTDX_pct > 0.0:
        price = get_latest_price_for_shorthand("BTDX")
        investment.BTDX_amt = ((float(portfolio.BTDX_pct) / 100.0) * usd_amt) / price
    if portfolio.I0C_pct > 0.0:
        price = get_latest_price_for_shorthand("I0C")
        investment.I0C_amt = ((float(portfolio.I0C_pct) / 100.0) * usd_amt) / price
    if portfolio.TRC_pct > 0.0:
        price = get_latest_price_for_shorthand("TRC")
        investment.TRC_amt = ((float(portfolio.TRC_pct) / 100.0) * usd_amt) / price
    if portfolio.KRB_pct > 0.0:
        price = get_latest_price_for_shorthand("KRB")
        investment.KRB_amt = ((float(portfolio.KRB_pct) / 100.0) * usd_amt) / price
    if portfolio.SSS_pct > 0.0:
        price = get_latest_price_for_shorthand("SSS")
        investment.SSS_amt = ((float(portfolio.SSS_pct) / 100.0) * usd_amt) / price
    if portfolio.PURE_pct > 0.0:
        price = get_latest_price_for_shorthand("PURE")
        investment.PURE_amt = ((float(portfolio.PURE_pct) / 100.0) * usd_amt) / price
    if portfolio.XHI_pct > 0.0:
        price = get_latest_price_for_shorthand("XHI")
        investment.XHI_amt = ((float(portfolio.XHI_pct) / 100.0) * usd_amt) / price
    if portfolio.CRAVE_pct > 0.0:
        price = get_latest_price_for_shorthand("CRAVE")
        investment.CRAVE_amt = ((float(portfolio.CRAVE_pct) / 100.0) * usd_amt) / price
    if portfolio.ORE_pct > 0.0:
        price = get_latest_price_for_shorthand("ORE")
        investment.ORE_amt = ((float(portfolio.ORE_pct) / 100.0) * usd_amt) / price
    if portfolio.HUSH_pct > 0.0:
        price = get_latest_price_for_shorthand("HUSH")
        investment.HUSH_amt = ((float(portfolio.HUSH_pct) / 100.0) * usd_amt) / price
    if portfolio.VTR_pct > 0.0:
        price = get_latest_price_for_shorthand("VTR")
        investment.VTR_amt = ((float(portfolio.VTR_pct) / 100.0) * usd_amt) / price
    if portfolio.ANC_pct > 0.0:
        price = get_latest_price_for_shorthand("ANC")
        investment.ANC_amt = ((float(portfolio.ANC_pct) / 100.0) * usd_amt) / price
    if portfolio.CMPCO_pct > 0.0:
        price = get_latest_price_for_shorthand("CMPCO")
        investment.CMPCO_amt = ((float(portfolio.CMPCO_pct) / 100.0) * usd_amt) / price
    if portfolio.ETBS_pct > 0.0:
        price = get_latest_price_for_shorthand("ETBS")
        investment.ETBS_amt = ((float(portfolio.ETBS_pct) / 100.0) * usd_amt) / price
    if portfolio.REF_pct > 0.0:
        price = get_latest_price_for_shorthand("REF")
        investment.REF_amt = ((float(portfolio.REF_pct) / 100.0) * usd_amt) / price
    if portfolio.DNR_pct > 0.0:
        price = get_latest_price_for_shorthand("DNR")
        investment.DNR_amt = ((float(portfolio.DNR_pct) / 100.0) * usd_amt) / price
    if portfolio.XGOX_pct > 0.0:
        price = get_latest_price_for_shorthand("XGOX")
        investment.XGOX_amt = ((float(portfolio.XGOX_pct) / 100.0) * usd_amt) / price
    if portfolio.CHX_pct > 0.0:
        price = get_latest_price_for_shorthand("CHX")
        investment.CHX_amt = ((float(portfolio.CHX_pct) / 100.0) * usd_amt) / price
    if portfolio.MVC_pct > 0.0:
        price = get_latest_price_for_shorthand("MVC")
        investment.MVC_amt = ((float(portfolio.MVC_pct) / 100.0) * usd_amt) / price
    if portfolio.FOR_pct > 0.0:
        price = get_latest_price_for_shorthand("FOR")
        investment.FOR_amt = ((float(portfolio.FOR_pct) / 100.0) * usd_amt) / price
    if portfolio.CANN_pct > 0.0:
        price = get_latest_price_for_shorthand("CANN")
        investment.CANN_amt = ((float(portfolio.CANN_pct) / 100.0) * usd_amt) / price
    if portfolio.VIU_pct > 0.0:
        price = get_latest_price_for_shorthand("VIU")
        investment.VIU_amt = ((float(portfolio.VIU_pct) / 100.0) * usd_amt) / price
    if portfolio.NAVI_pct > 0.0:
        price = get_latest_price_for_shorthand("NAVI")
        investment.NAVI_amt = ((float(portfolio.NAVI_pct) / 100.0) * usd_amt) / price
    if portfolio.FYP_pct > 0.0:
        price = get_latest_price_for_shorthand("FYP")
        investment.FYP_amt = ((float(portfolio.FYP_pct) / 100.0) * usd_amt) / price
    if portfolio.CPY_pct > 0.0:
        price = get_latest_price_for_shorthand("CPY")
        investment.CPY_amt = ((float(portfolio.CPY_pct) / 100.0) * usd_amt) / price
    if portfolio.STAC_pct > 0.0:
        price = get_latest_price_for_shorthand("STAC")
        investment.STAC_amt = ((float(portfolio.STAC_pct) / 100.0) * usd_amt) / price
    if portfolio.GENE_pct > 0.0:
        price = get_latest_price_for_shorthand("GENE")
        investment.GENE_amt = ((float(portfolio.GENE_pct) / 100.0) * usd_amt) / price
    if portfolio.SGR_pct > 0.0:
        price = get_latest_price_for_shorthand("SGR")
        investment.SGR_amt = ((float(portfolio.SGR_pct) / 100.0) * usd_amt) / price
    if portfolio.NIO_pct > 0.0:
        price = get_latest_price_for_shorthand("NIO")
        investment.NIO_amt = ((float(portfolio.NIO_pct) / 100.0) * usd_amt) / price
    if portfolio.PIX_pct > 0.0:
        price = get_latest_price_for_shorthand("PIX")
        investment.PIX_amt = ((float(portfolio.PIX_pct) / 100.0) * usd_amt) / price
    if portfolio.MAGE_pct > 0.0:
        price = get_latest_price_for_shorthand("MAGE")
        investment.MAGE_amt = ((float(portfolio.MAGE_pct) / 100.0) * usd_amt) / price
    if portfolio.NLX_pct > 0.0:
        price = get_latest_price_for_shorthand("NLX")
        investment.NLX_amt = ((float(portfolio.NLX_pct) / 100.0) * usd_amt) / price
    if portfolio.EGC_pct > 0.0:
        price = get_latest_price_for_shorthand("EGC")
        investment.EGC_amt = ((float(portfolio.EGC_pct) / 100.0) * usd_amt) / price
    if portfolio.CL_pct > 0.0:
        price = get_latest_price_for_shorthand("CL")
        investment.CL_amt = ((float(portfolio.CL_pct) / 100.0) * usd_amt) / price
    if portfolio.ZEPH_pct > 0.0:
        price = get_latest_price_for_shorthand("ZEPH")
        investment.ZEPH_amt = ((float(portfolio.ZEPH_pct) / 100.0) * usd_amt) / price
    if portfolio.MFG_pct > 0.0:
        price = get_latest_price_for_shorthand("MFG")
        investment.MFG_amt = ((float(portfolio.MFG_pct) / 100.0) * usd_amt) / price
    if portfolio.BBP_pct > 0.0:
        price = get_latest_price_for_shorthand("BBP")
        investment.BBP_amt = ((float(portfolio.BBP_pct) / 100.0) * usd_amt) / price
    if portfolio.BUN_pct > 0.0:
        price = get_latest_price_for_shorthand("BUN")
        investment.BUN_amt = ((float(portfolio.BUN_pct) / 100.0) * usd_amt) / price
    if portfolio.PYLNT_pct > 0.0:
        price = get_latest_price_for_shorthand("PYLNT")
        investment.PYLNT_amt = ((float(portfolio.PYLNT_pct) / 100.0) * usd_amt) / price
    if portfolio.CDX_pct > 0.0:
        price = get_latest_price_for_shorthand("CDX")
        investment.CDX_amt = ((float(portfolio.CDX_pct) / 100.0) * usd_amt) / price
    if portfolio.DAN_pct > 0.0:
        price = get_latest_price_for_shorthand("DAN")
        investment.DAN_amt = ((float(portfolio.DAN_pct) / 100.0) * usd_amt) / price
    if portfolio.TRAK_pct > 0.0:
        price = get_latest_price_for_shorthand("TRAK")
        investment.TRAK_amt = ((float(portfolio.TRAK_pct) / 100.0) * usd_amt) / price
    if portfolio.LDOGE_pct > 0.0:
        price = get_latest_price_for_shorthand("LDOGE")
        investment.LDOGE_amt = ((float(portfolio.LDOGE_pct) / 100.0) * usd_amt) / price
    if portfolio.TES_pct > 0.0:
        price = get_latest_price_for_shorthand("TES")
        investment.TES_amt = ((float(portfolio.TES_pct) / 100.0) * usd_amt) / price
    if portfolio.FGC_pct > 0.0:
        price = get_latest_price_for_shorthand("FGC")
        investment.FGC_amt = ((float(portfolio.FGC_pct) / 100.0) * usd_amt) / price
    if portfolio.AIX_pct > 0.0:
        price = get_latest_price_for_shorthand("AIX")
        investment.AIX_amt = ((float(portfolio.AIX_pct) / 100.0) * usd_amt) / price
    if portfolio.WSX_pct > 0.0:
        price = get_latest_price_for_shorthand("WSX")
        investment.WSX_amt = ((float(portfolio.WSX_pct) / 100.0) * usd_amt) / price
    if portfolio.MAC_pct > 0.0:
        price = get_latest_price_for_shorthand("MAC")
        investment.MAC_amt = ((float(portfolio.MAC_pct) / 100.0) * usd_amt) / price
    if portfolio.NOBL_pct > 0.0:
        price = get_latest_price_for_shorthand("NOBL")
        investment.NOBL_amt = ((float(portfolio.NOBL_pct) / 100.0) * usd_amt) / price
    if portfolio.DP_pct > 0.0:
        price = get_latest_price_for_shorthand("DP")
        investment.DP_amt = ((float(portfolio.DP_pct) / 100.0) * usd_amt) / price
    if portfolio.LOCI_pct > 0.0:
        price = get_latest_price_for_shorthand("LOCI")
        investment.LOCI_amt = ((float(portfolio.LOCI_pct) / 100.0) * usd_amt) / price
    if portfolio.HIRE_pct > 0.0:
        price = get_latest_price_for_shorthand("HIRE")
        investment.HIRE_amt = ((float(portfolio.HIRE_pct) / 100.0) * usd_amt) / price
    if portfolio.OPC_pct > 0.0:
        price = get_latest_price_for_shorthand("OPC")
        investment.OPC_amt = ((float(portfolio.OPC_pct) / 100.0) * usd_amt) / price
    if portfolio.GCN_pct > 0.0:
        price = get_latest_price_for_shorthand("GCN")
        investment.GCN_amt = ((float(portfolio.GCN_pct) / 100.0) * usd_amt) / price
    if portfolio.IC_pct > 0.0:
        price = get_latest_price_for_shorthand("IC")
        investment.IC_amt = ((float(portfolio.IC_pct) / 100.0) * usd_amt) / price
    if portfolio.ACE_pct > 0.0:
        price = get_latest_price_for_shorthand("ACE")
        investment.ACE_amt = ((float(portfolio.ACE_pct) / 100.0) * usd_amt) / price
    if portfolio.BOUTS_pct > 0.0:
        price = get_latest_price_for_shorthand("BOUTS")
        investment.BOUTS_amt = ((float(portfolio.BOUTS_pct) / 100.0) * usd_amt) / price
    if portfolio.XNN_pct > 0.0:
        price = get_latest_price_for_shorthand("XNN")
        investment.XNN_amt = ((float(portfolio.XNN_pct) / 100.0) * usd_amt) / price
    if portfolio.CREA_pct > 0.0:
        price = get_latest_price_for_shorthand("CREA")
        investment.CREA_amt = ((float(portfolio.CREA_pct) / 100.0) * usd_amt) / price
    if portfolio.EFYT_pct > 0.0:
        price = get_latest_price_for_shorthand("EFYT")
        investment.EFYT_amt = ((float(portfolio.EFYT_pct) / 100.0) * usd_amt) / price
    if portfolio.XTL_pct > 0.0:
        price = get_latest_price_for_shorthand("XTL")
        investment.XTL_amt = ((float(portfolio.XTL_pct) / 100.0) * usd_amt) / price
    if portfolio.TEAM_pct > 0.0:
        price = get_latest_price_for_shorthand("TEAM")
        investment.TEAM_amt = ((float(portfolio.TEAM_pct) / 100.0) * usd_amt) / price
    if portfolio.XMG_pct > 0.0:
        price = get_latest_price_for_shorthand("XMG")
        investment.XMG_amt = ((float(portfolio.XMG_pct) / 100.0) * usd_amt) / price
    if portfolio.HUC_pct > 0.0:
        price = get_latest_price_for_shorthand("HUC")
        investment.HUC_amt = ((float(portfolio.HUC_pct) / 100.0) * usd_amt) / price
    if portfolio.RAIN_pct > 0.0:
        price = get_latest_price_for_shorthand("RAIN")
        investment.RAIN_amt = ((float(portfolio.RAIN_pct) / 100.0) * usd_amt) / price
    if portfolio.MNTP_pct > 0.0:
        price = get_latest_price_for_shorthand("MNTP")
        investment.MNTP_amt = ((float(portfolio.MNTP_pct) / 100.0) * usd_amt) / price
    if portfolio.TRCT_pct > 0.0:
        price = get_latest_price_for_shorthand("TRCT")
        investment.TRCT_amt = ((float(portfolio.TRCT_pct) / 100.0) * usd_amt) / price
    if portfolio.EFL_pct > 0.0:
        price = get_latest_price_for_shorthand("EFL")
        investment.EFL_amt = ((float(portfolio.EFL_pct) / 100.0) * usd_amt) / price
    if portfolio.XBP_pct > 0.0:
        price = get_latest_price_for_shorthand("XBP")
        investment.XBP_amt = ((float(portfolio.XBP_pct) / 100.0) * usd_amt) / price
    if portfolio.BTW_pct > 0.0:
        price = get_latest_price_for_shorthand("BTW")
        investment.BTW_amt = ((float(portfolio.BTW_pct) / 100.0) * usd_amt) / price
    if portfolio.TZC_pct > 0.0:
        price = get_latest_price_for_shorthand("TZC")
        investment.TZC_amt = ((float(portfolio.TZC_pct) / 100.0) * usd_amt) / price
    if portfolio.DIX_pct > 0.0:
        price = get_latest_price_for_shorthand("DIX")
        investment.DIX_amt = ((float(portfolio.DIX_pct) / 100.0) * usd_amt) / price
    if portfolio.ODN_pct > 0.0:
        price = get_latest_price_for_shorthand("ODN")
        investment.ODN_amt = ((float(portfolio.ODN_pct) / 100.0) * usd_amt) / price
    if portfolio.STAK_pct > 0.0:
        price = get_latest_price_for_shorthand("STAK")
        investment.STAK_amt = ((float(portfolio.STAK_pct) / 100.0) * usd_amt) / price
    if portfolio.FT_pct > 0.0:
        price = get_latest_price_for_shorthand("FT")
        investment.FT_amt = ((float(portfolio.FT_pct) / 100.0) * usd_amt) / price
    if portfolio.CRB_pct > 0.0:
        price = get_latest_price_for_shorthand("CRB")
        investment.CRB_amt = ((float(portfolio.CRB_pct) / 100.0) * usd_amt) / price
    if portfolio.HAT_pct > 0.0:
        price = get_latest_price_for_shorthand("HAT")
        investment.HAT_amt = ((float(portfolio.HAT_pct) / 100.0) * usd_amt) / price
    if portfolio.SWIFT_pct > 0.0:
        price = get_latest_price_for_shorthand("SWIFT")
        investment.SWIFT_amt = ((float(portfolio.SWIFT_pct) / 100.0) * usd_amt) / price
    if portfolio.ZER_pct > 0.0:
        price = get_latest_price_for_shorthand("ZER")
        investment.ZER_amt = ((float(portfolio.ZER_pct) / 100.0) * usd_amt) / price
    if portfolio.BYC_pct > 0.0:
        price = get_latest_price_for_shorthand("BYC")
        investment.BYC_amt = ((float(portfolio.BYC_pct) / 100.0) * usd_amt) / price
    if portfolio.AMM_pct > 0.0:
        price = get_latest_price_for_shorthand("AMM")
        investment.AMM_amt = ((float(portfolio.AMM_pct) / 100.0) * usd_amt) / price
    if portfolio.EBTC_pct > 0.0:
        price = get_latest_price_for_shorthand("EBTC")
        investment.EBTC_amt = ((float(portfolio.EBTC_pct) / 100.0) * usd_amt) / price
    if portfolio.FRST_pct > 0.0:
        price = get_latest_price_for_shorthand("FRST")
        investment.FRST_amt = ((float(portfolio.FRST_pct) / 100.0) * usd_amt) / price
    if portfolio.ITNS_pct > 0.0:
        price = get_latest_price_for_shorthand("ITNS")
        investment.ITNS_amt = ((float(portfolio.ITNS_pct) / 100.0) * usd_amt) / price
    if portfolio.ESZ_pct > 0.0:
        price = get_latest_price_for_shorthand("ESZ")
        investment.ESZ_amt = ((float(portfolio.ESZ_pct) / 100.0) * usd_amt) / price
    if portfolio.BTRN_pct > 0.0:
        price = get_latest_price_for_shorthand("BTRN")
        investment.BTRN_amt = ((float(portfolio.BTRN_pct) / 100.0) * usd_amt) / price
    if portfolio.UCOM_pct > 0.0:
        price = get_latest_price_for_shorthand("UCOM")
        investment.UCOM_amt = ((float(portfolio.UCOM_pct) / 100.0) * usd_amt) / price
    if portfolio.SKIN_pct > 0.0:
        price = get_latest_price_for_shorthand("SKIN")
        investment.SKIN_amt = ((float(portfolio.SKIN_pct) / 100.0) * usd_amt) / price
    if portfolio.MAG_pct > 0.0:
        price = get_latest_price_for_shorthand("MAG")
        investment.MAG_amt = ((float(portfolio.MAG_pct) / 100.0) * usd_amt) / price
    if portfolio.DGC_pct > 0.0:
        price = get_latest_price_for_shorthand("DGC")
        investment.DGC_amt = ((float(portfolio.DGC_pct) / 100.0) * usd_amt) / price
    if portfolio.VIVO_pct > 0.0:
        price = get_latest_price_for_shorthand("VIVO")
        investment.VIVO_amt = ((float(portfolio.VIVO_pct) / 100.0) * usd_amt) / price
    if portfolio.PHO_pct > 0.0:
        price = get_latest_price_for_shorthand("PHO")
        investment.PHO_amt = ((float(portfolio.PHO_pct) / 100.0) * usd_amt) / price
    if portfolio.FCN_pct > 0.0:
        price = get_latest_price_for_shorthand("FCN")
        investment.FCN_amt = ((float(portfolio.FCN_pct) / 100.0) * usd_amt) / price
    if portfolio.MRT_pct > 0.0:
        price = get_latest_price_for_shorthand("MRT")
        investment.MRT_amt = ((float(portfolio.MRT_pct) / 100.0) * usd_amt) / price
    if portfolio.RNS_pct > 0.0:
        price = get_latest_price_for_shorthand("RNS")
        investment.RNS_amt = ((float(portfolio.RNS_pct) / 100.0) * usd_amt) / price
    if portfolio.SCT_pct > 0.0:
        price = get_latest_price_for_shorthand("SCT")
        investment.SCT_amt = ((float(portfolio.SCT_pct) / 100.0) * usd_amt) / price
    if portfolio.DAY_pct > 0.0:
        price = get_latest_price_for_shorthand("DAY")
        investment.DAY_amt = ((float(portfolio.DAY_pct) / 100.0) * usd_amt) / price
    if portfolio.JEW_pct > 0.0:
        price = get_latest_price_for_shorthand("JEW")
        investment.JEW_amt = ((float(portfolio.JEW_pct) / 100.0) * usd_amt) / price
    if portfolio.JC_pct > 0.0:
        price = get_latest_price_for_shorthand("JC")
        investment.JC_amt = ((float(portfolio.JC_pct) / 100.0) * usd_amt) / price
    if portfolio.SGN_pct > 0.0:
        price = get_latest_price_for_shorthand("SGN")
        investment.SGN_amt = ((float(portfolio.SGN_pct) / 100.0) * usd_amt) / price
    if portfolio.ADZ_pct > 0.0:
        price = get_latest_price_for_shorthand("ADZ")
        investment.ADZ_amt = ((float(portfolio.ADZ_pct) / 100.0) * usd_amt) / price
    if portfolio.HERO_pct > 0.0:
        price = get_latest_price_for_shorthand("HERO")
        investment.HERO_amt = ((float(portfolio.HERO_pct) / 100.0) * usd_amt) / price
    if portfolio.TDX_pct > 0.0:
        price = get_latest_price_for_shorthand("TDX")
        investment.TDX_amt = ((float(portfolio.TDX_pct) / 100.0) * usd_amt) / price
    if portfolio.ZNY_pct > 0.0:
        price = get_latest_price_for_shorthand("ZNY")
        investment.ZNY_amt = ((float(portfolio.ZNY_pct) / 100.0) * usd_amt) / price
    if portfolio.e_808_pct > 0.0:
        price = get_latest_price_for_shorthand("808")
        investment.e_808_amt = ((float(portfolio.e_808_pct) / 100.0) * usd_amt) / price
    if portfolio.EPY_pct > 0.0:
        price = get_latest_price_for_shorthand("EPY")
        investment.EPY_amt = ((float(portfolio.EPY_pct) / 100.0) * usd_amt) / price
    if portfolio.TDS_pct > 0.0:
        price = get_latest_price_for_shorthand("TDS")
        investment.TDS_amt = ((float(portfolio.TDS_pct) / 100.0) * usd_amt) / price
    if portfolio.UIS_pct > 0.0:
        price = get_latest_price_for_shorthand("UIS")
        investment.UIS_amt = ((float(portfolio.UIS_pct) / 100.0) * usd_amt) / price
    if portfolio.DTRC_pct > 0.0:
        price = get_latest_price_for_shorthand("DTRC")
        investment.DTRC_amt = ((float(portfolio.DTRC_pct) / 100.0) * usd_amt) / price
    if portfolio.ELLA_pct > 0.0:
        price = get_latest_price_for_shorthand("ELLA")
        investment.ELLA_amt = ((float(portfolio.ELLA_pct) / 100.0) * usd_amt) / price
    if portfolio.EBCH_pct > 0.0:
        price = get_latest_price_for_shorthand("EBCH")
        investment.EBCH_amt = ((float(portfolio.EBCH_pct) / 100.0) * usd_amt) / price
    if portfolio.UNB_pct > 0.0:
        price = get_latest_price_for_shorthand("UNB")
        investment.UNB_amt = ((float(portfolio.UNB_pct) / 100.0) * usd_amt) / price
    if portfolio.FYN_pct > 0.0:
        price = get_latest_price_for_shorthand("FYN")
        investment.FYN_amt = ((float(portfolio.FYN_pct) / 100.0) * usd_amt) / price
    if portfolio.TIG_pct > 0.0:
        price = get_latest_price_for_shorthand("TIG")
        investment.TIG_amt = ((float(portfolio.TIG_pct) / 100.0) * usd_amt) / price
    if portfolio.AMN_pct > 0.0:
        price = get_latest_price_for_shorthand("AMN")
        investment.AMN_amt = ((float(portfolio.AMN_pct) / 100.0) * usd_amt) / price
    if portfolio.ATS_pct > 0.0:
        price = get_latest_price_for_shorthand("ATS")
        investment.ATS_amt = ((float(portfolio.ATS_pct) / 100.0) * usd_amt) / price
    if portfolio.DFT_pct > 0.0:
        price = get_latest_price_for_shorthand("DFT")
        investment.DFT_amt = ((float(portfolio.DFT_pct) / 100.0) * usd_amt) / price
    if portfolio.NOX_pct > 0.0:
        price = get_latest_price_for_shorthand("NOX")
        investment.NOX_amt = ((float(portfolio.NOX_pct) / 100.0) * usd_amt) / price
    if portfolio.STU_pct > 0.0:
        price = get_latest_price_for_shorthand("STU")
        investment.STU_amt = ((float(portfolio.STU_pct) / 100.0) * usd_amt) / price
    if portfolio.EARTH_pct > 0.0:
        price = get_latest_price_for_shorthand("EARTH")
        investment.EARTH_amt = ((float(portfolio.EARTH_pct) / 100.0) * usd_amt) / price
    if portfolio.JIYO_pct > 0.0:
        price = get_latest_price_for_shorthand("JIYO")
        investment.JIYO_amt = ((float(portfolio.JIYO_pct) / 100.0) * usd_amt) / price
    if portfolio.MEC_pct > 0.0:
        price = get_latest_price_for_shorthand("MEC")
        investment.MEC_amt = ((float(portfolio.MEC_pct) / 100.0) * usd_amt) / price
    if portfolio.ORI_pct > 0.0:
        price = get_latest_price_for_shorthand("ORI")
        investment.ORI_amt = ((float(portfolio.ORI_pct) / 100.0) * usd_amt) / price
    if portfolio.DRPU_pct > 0.0:
        price = get_latest_price_for_shorthand("DRPU")
        investment.DRPU_amt = ((float(portfolio.DRPU_pct) / 100.0) * usd_amt) / price
    if portfolio.MORE_pct > 0.0:
        price = get_latest_price_for_shorthand("MORE")
        investment.MORE_amt = ((float(portfolio.MORE_pct) / 100.0) * usd_amt) / price
    if portfolio.INN_pct > 0.0:
        price = get_latest_price_for_shorthand("INN")
        investment.INN_amt = ((float(portfolio.INN_pct) / 100.0) * usd_amt) / price
    if portfolio.EVC_pct > 0.0:
        price = get_latest_price_for_shorthand("EVC")
        investment.EVC_amt = ((float(portfolio.EVC_pct) / 100.0) * usd_amt) / price
    if portfolio.TNS_pct > 0.0:
        price = get_latest_price_for_shorthand("TNS")
        investment.TNS_amt = ((float(portfolio.TNS_pct) / 100.0) * usd_amt) / price
    if portfolio.LINX_pct > 0.0:
        price = get_latest_price_for_shorthand("LINX")
        investment.LINX_amt = ((float(portfolio.LINX_pct) / 100.0) * usd_amt) / price
    if portfolio.SAGA_pct > 0.0:
        price = get_latest_price_for_shorthand("SAGA")
        investment.SAGA_amt = ((float(portfolio.SAGA_pct) / 100.0) * usd_amt) / price
    if portfolio.MBI_pct > 0.0:
        price = get_latest_price_for_shorthand("MBI")
        investment.MBI_amt = ((float(portfolio.MBI_pct) / 100.0) * usd_amt) / price
    if portfolio.ZET_pct > 0.0:
        price = get_latest_price_for_shorthand("ZET")
        investment.ZET_amt = ((float(portfolio.ZET_pct) / 100.0) * usd_amt) / price
    if portfolio.ARC_pct > 0.0:
        price = get_latest_price_for_shorthand("ARC")
        investment.ARC_amt = ((float(portfolio.ARC_pct) / 100.0) * usd_amt) / price
    if portfolio.EL_pct > 0.0:
        price = get_latest_price_for_shorthand("EL")
        investment.EL_amt = ((float(portfolio.EL_pct) / 100.0) * usd_amt) / price
    if portfolio.UNIFY_pct > 0.0:
        price = get_latest_price_for_shorthand("UNIFY")
        investment.UNIFY_amt = ((float(portfolio.UNIFY_pct) / 100.0) * usd_amt) / price
    if portfolio.EQT_pct > 0.0:
        price = get_latest_price_for_shorthand("EQT")
        investment.EQT_amt = ((float(portfolio.EQT_pct) / 100.0) * usd_amt) / price
    if portfolio.VULC_pct > 0.0:
        price = get_latest_price_for_shorthand("VULC")
        investment.VULC_amt = ((float(portfolio.VULC_pct) / 100.0) * usd_amt) / price
    if portfolio.KLN_pct > 0.0:
        price = get_latest_price_for_shorthand("KLN")
        investment.KLN_amt = ((float(portfolio.KLN_pct) / 100.0) * usd_amt) / price
    if portfolio.QVT_pct > 0.0:
        price = get_latest_price_for_shorthand("QVT")
        investment.QVT_amt = ((float(portfolio.QVT_pct) / 100.0) * usd_amt) / price
    if portfolio.PLAN_pct > 0.0:
        price = get_latest_price_for_shorthand("PLAN")
        investment.PLAN_amt = ((float(portfolio.PLAN_pct) / 100.0) * usd_amt) / price
    if portfolio.VRS_pct > 0.0:
        price = get_latest_price_for_shorthand("VRS")
        investment.VRS_amt = ((float(portfolio.VRS_pct) / 100.0) * usd_amt) / price
    if portfolio.IFLT_pct > 0.0:
        price = get_latest_price_for_shorthand("IFLT")
        investment.IFLT_amt = ((float(portfolio.IFLT_pct) / 100.0) * usd_amt) / price
    if portfolio.BTA_pct > 0.0:
        price = get_latest_price_for_shorthand("BTA")
        investment.BTA_amt = ((float(portfolio.BTA_pct) / 100.0) * usd_amt) / price
    if portfolio.MCAP_pct > 0.0:
        price = get_latest_price_for_shorthand("MCAP")
        investment.MCAP_amt = ((float(portfolio.MCAP_pct) / 100.0) * usd_amt) / price
    if portfolio.SUR_pct > 0.0:
        price = get_latest_price_for_shorthand("SUR")
        investment.SUR_amt = ((float(portfolio.SUR_pct) / 100.0) * usd_amt) / price
    if portfolio.HPC_pct > 0.0:
        price = get_latest_price_for_shorthand("HPC")
        investment.HPC_amt = ((float(portfolio.HPC_pct) / 100.0) * usd_amt) / price
    if portfolio.ELTCOIN_pct > 0.0:
        price = get_latest_price_for_shorthand("ELTCOIN")
        investment.ELTCOIN_amt = ((float(portfolio.ELTCOIN_pct) / 100.0) * usd_amt) / price
    if portfolio.XPD_pct > 0.0:
        price = get_latest_price_for_shorthand("XPD")
        investment.XPD_amt = ((float(portfolio.XPD_pct) / 100.0) * usd_amt) / price
    if portfolio.CRM_pct > 0.0:
        price = get_latest_price_for_shorthand("CRM")
        investment.CRM_amt = ((float(portfolio.CRM_pct) / 100.0) * usd_amt) / price
    if portfolio.RLT_pct > 0.0:
        price = get_latest_price_for_shorthand("RLT")
        investment.RLT_amt = ((float(portfolio.RLT_pct) / 100.0) * usd_amt) / price
    if portfolio.WILD_pct > 0.0:
        price = get_latest_price_for_shorthand("WILD")
        investment.WILD_amt = ((float(portfolio.WILD_pct) / 100.0) * usd_amt) / price
    if portfolio.XTO_pct > 0.0:
        price = get_latest_price_for_shorthand("XTO")
        investment.XTO_amt = ((float(portfolio.XTO_pct) / 100.0) * usd_amt) / price
    if portfolio.DGPT_pct > 0.0:
        price = get_latest_price_for_shorthand("DGPT")
        investment.DGPT_amt = ((float(portfolio.DGPT_pct) / 100.0) * usd_amt) / price
    if portfolio.CJT_pct > 0.0:
        price = get_latest_price_for_shorthand("CJT")
        investment.CJT_amt = ((float(portfolio.CJT_pct) / 100.0) * usd_amt) / price
    if portfolio.BTB_pct > 0.0:
        price = get_latest_price_for_shorthand("BTB")
        investment.BTB_amt = ((float(portfolio.BTB_pct) / 100.0) * usd_amt) / price
    if portfolio.ZBC_pct > 0.0:
        price = get_latest_price_for_shorthand("ZBC")
        investment.ZBC_amt = ((float(portfolio.ZBC_pct) / 100.0) * usd_amt) / price
    if portfolio.e_1337_pct > 0.0:
        price = get_latest_price_for_shorthand("1337")
        investment.e_1337_amt = ((float(portfolio.e_1337_pct) / 100.0) * usd_amt) / price
    if portfolio.e_42_pct > 0.0:
        price = get_latest_price_for_shorthand("42")
        investment.e_42_amt = ((float(portfolio.e_42_pct) / 100.0) * usd_amt) / price
    if portfolio.GAM_pct > 0.0:
        price = get_latest_price_for_shorthand("GAM")
        investment.GAM_amt = ((float(portfolio.GAM_pct) / 100.0) * usd_amt) / price
    if portfolio.KB3_pct > 0.0:
        price = get_latest_price_for_shorthand("KB3")
        investment.KB3_amt = ((float(portfolio.KB3_pct) / 100.0) * usd_amt) / price
    if portfolio.NSR_pct > 0.0:
        price = get_latest_price_for_shorthand("NSR")
        investment.NSR_amt = ((float(portfolio.NSR_pct) / 100.0) * usd_amt) / price
    if portfolio.CRC_pct > 0.0:
        price = get_latest_price_for_shorthand("CRC")
        investment.CRC_amt = ((float(portfolio.CRC_pct) / 100.0) * usd_amt) / price
    if portfolio.BDL_pct > 0.0:
        price = get_latest_price_for_shorthand("BDL")
        investment.BDL_amt = ((float(portfolio.BDL_pct) / 100.0) * usd_amt) / price
    if portfolio.CHC_pct > 0.0:
        price = get_latest_price_for_shorthand("CHC")
        investment.CHC_amt = ((float(portfolio.CHC_pct) / 100.0) * usd_amt) / price
    if portfolio.GRMD_pct > 0.0:
        price = get_latest_price_for_shorthand("GRMD")
        investment.GRMD_amt = ((float(portfolio.GRMD_pct) / 100.0) * usd_amt) / price
    if portfolio.MBRS_pct > 0.0:
        price = get_latest_price_for_shorthand("MBRS")
        investment.MBRS_amt = ((float(portfolio.MBRS_pct) / 100.0) * usd_amt) / price
    if portfolio.EQL_pct > 0.0:
        price = get_latest_price_for_shorthand("EQL")
        investment.EQL_amt = ((float(portfolio.EQL_pct) / 100.0) * usd_amt) / price
    if portfolio.JET_pct > 0.0:
        price = get_latest_price_for_shorthand("JET")
        investment.JET_amt = ((float(portfolio.JET_pct) / 100.0) * usd_amt) / price
    if portfolio.BITSILVER_pct > 0.0:
        price = get_latest_price_for_shorthand("BITSILVER")
        investment.BITSILVER_amt = ((float(portfolio.BITSILVER_pct) / 100.0) * usd_amt) / price
    if portfolio.PIPL_pct > 0.0:
        price = get_latest_price_for_shorthand("PIPL")
        investment.PIPL_amt = ((float(portfolio.PIPL_pct) / 100.0) * usd_amt) / price
    if portfolio.XCN_pct > 0.0:
        price = get_latest_price_for_shorthand("XCN")
        investment.XCN_amt = ((float(portfolio.XCN_pct) / 100.0) * usd_amt) / price
    if portfolio.BBI_pct > 0.0:
        price = get_latest_price_for_shorthand("BBI")
        investment.BBI_amt = ((float(portfolio.BBI_pct) / 100.0) * usd_amt) / price
    if portfolio.NMS_pct > 0.0:
        price = get_latest_price_for_shorthand("NMS")
        investment.NMS_amt = ((float(portfolio.NMS_pct) / 100.0) * usd_amt) / price
    if portfolio.OCT_pct > 0.0:
        price = get_latest_price_for_shorthand("OCT")
        investment.OCT_amt = ((float(portfolio.OCT_pct) / 100.0) * usd_amt) / price
    if portfolio.QBIC_pct > 0.0:
        price = get_latest_price_for_shorthand("QBIC")
        investment.QBIC_amt = ((float(portfolio.QBIC_pct) / 100.0) * usd_amt) / price
    if portfolio.FANS_pct > 0.0:
        price = get_latest_price_for_shorthand("FANS")
        investment.FANS_amt = ((float(portfolio.FANS_pct) / 100.0) * usd_amt) / price
    if portfolio.ADC_pct > 0.0:
        price = get_latest_price_for_shorthand("ADC")
        investment.ADC_amt = ((float(portfolio.ADC_pct) / 100.0) * usd_amt) / price
    if portfolio.TRUST_pct > 0.0:
        price = get_latest_price_for_shorthand("TRUST")
        investment.TRUST_amt = ((float(portfolio.TRUST_pct) / 100.0) * usd_amt) / price
    if portfolio.VZT_pct > 0.0:
        price = get_latest_price_for_shorthand("VZT")
        investment.VZT_amt = ((float(portfolio.VZT_pct) / 100.0) * usd_amt) / price
    if portfolio.TBX_pct > 0.0:
        price = get_latest_price_for_shorthand("TBX")
        investment.TBX_amt = ((float(portfolio.TBX_pct) / 100.0) * usd_amt) / price
    if portfolio.XRL_pct > 0.0:
        price = get_latest_price_for_shorthand("XRL")
        investment.XRL_amt = ((float(portfolio.XRL_pct) / 100.0) * usd_amt) / price
    if portfolio.ARG_pct > 0.0:
        price = get_latest_price_for_shorthand("ARG")
        investment.ARG_amt = ((float(portfolio.ARG_pct) / 100.0) * usd_amt) / price
    if portfolio.SMS_pct > 0.0:
        price = get_latest_price_for_shorthand("SMS")
        investment.SMS_amt = ((float(portfolio.SMS_pct) / 100.0) * usd_amt) / price
    if portfolio.CRED_pct > 0.0:
        price = get_latest_price_for_shorthand("CRED")
        investment.CRED_amt = ((float(portfolio.CRED_pct) / 100.0) * usd_amt) / price
    if portfolio.ONG_pct > 0.0:
        price = get_latest_price_for_shorthand("ONG")
        investment.ONG_amt = ((float(portfolio.ONG_pct) / 100.0) * usd_amt) / price
    if portfolio.DEW_pct > 0.0:
        price = get_latest_price_for_shorthand("DEW")
        investment.DEW_amt = ((float(portfolio.DEW_pct) / 100.0) * usd_amt) / price
    if portfolio.OPT_pct > 0.0:
        price = get_latest_price_for_shorthand("OPT")
        investment.OPT_amt = ((float(portfolio.OPT_pct) / 100.0) * usd_amt) / price
    if portfolio.DOVU_pct > 0.0:
        price = get_latest_price_for_shorthand("DOVU")
        investment.DOVU_amt = ((float(portfolio.DOVU_pct) / 100.0) * usd_amt) / price
    if portfolio.DEM_pct > 0.0:
        price = get_latest_price_for_shorthand("DEM")
        investment.DEM_amt = ((float(portfolio.DEM_pct) / 100.0) * usd_amt) / price
    if portfolio.SXC_pct > 0.0:
        price = get_latest_price_for_shorthand("SXC")
        investment.SXC_amt = ((float(portfolio.SXC_pct) / 100.0) * usd_amt) / price
    if portfolio.HORSE_pct > 0.0:
        price = get_latest_price_for_shorthand("HORSE")
        investment.HORSE_amt = ((float(portfolio.HORSE_pct) / 100.0) * usd_amt) / price
    if portfolio.LIVE_pct > 0.0:
        price = get_latest_price_for_shorthand("LIVE")
        investment.LIVE_amt = ((float(portfolio.LIVE_pct) / 100.0) * usd_amt) / price
    investment.save()

def get_investment_array(investment):
    return [investment.BTC_amt, investment.ETH_amt, investment.XRP_amt, investment.BCH_amt, investment.EOS_amt, investment.LTC_amt, investment.XLM_amt, investment.ADA_amt, investment.TRX_amt, investment.MIOTA_amt, investment.USDT_amt, investment.NEO_amt, investment.DASH_amt, investment.XMR_amt, investment.BNB_amt, investment.VEN_amt, investment.ETC_amt, investment.XEM_amt, investment.OMG_amt, investment.QTUM_amt, investment.ONT_amt, investment.ZEC_amt, investment.ICX_amt, investment.LSK_amt, investment.DCR_amt, investment.BCN_amt, investment.ZIL_amt, investment.AE_amt, investment.BTG_amt, investment.BTM_amt, investment.SC_amt, investment.ZRX_amt, investment.XVG_amt, investment.BTS_amt, investment.STEEM_amt, investment.MKR_amt, investment.REP_amt, investment.NANO_amt, investment.DOGE_amt, investment.RHOC_amt, investment.WAVES_amt, investment.BCD_amt, investment.BAT_amt, investment.WAN_amt, investment.GNT_amt, investment.BTCP_amt, investment.STRAT_amt, investment.DGB_amt, investment.KCS_amt, investment.WTC_amt, investment.PPT_amt, investment.SNT_amt, investment.HSR_amt, investment.DGD_amt, investment.NAS_amt, investment.HT_amt, investment.IOST_amt, investment.AION_amt, investment.LRC_amt, investment.KMD_amt, investment.GXS_amt, investment.CNX_amt, investment.RDD_amt, investment.BNT_amt, investment.ARDR_amt, investment.MAID_amt, investment.ARK_amt, investment.MOAC_amt, investment.MONA_amt, investment.ELF_amt, investment.CENNZ_amt, investment.DCN_amt, investment.FUN_amt, investment.BIX_amt, investment.GAS_amt, investment.MITH_amt, investment.ENG_amt, investment.PIVX_amt, investment.VERI_amt, investment.KNC_amt, investment.ELA_amt, investment.EMC_amt, investment.FSN_amt, investment.SYS_amt, investment.DROP_amt, investment.CMT_amt, investment.KIN_amt, investment.MANA_amt, investment.NXT_amt, investment.ETHOS_amt, investment.DDD_amt, investment.QASH_amt, investment.DRGN_amt, investment.FCT_amt, investment.LOOM_amt, investment.MTC_amt, investment.GTC_amt, investment.XZC_amt, investment.POLY_amt, investment.NULS_amt, investment.SMART_amt, investment.SUB_amt, investment.CTXC_amt, investment.THETA_amt, investment.BFT_amt, investment.PAYX_amt, investment.STORM_amt, investment.POWR_amt, investment.BLOCK_amt, investment.NXS_amt, investment.MCO_amt, investment.ETN_amt, investment.GBYTE_amt, investment.WAX_amt, investment.TUSD_amt, investment.ZEN_amt, investment.WICC_amt, investment.EOSDAC_amt, investment.RLC_amt, investment.GTO_amt, investment.R_amt, investment.DBC_amt, investment.LINK_amt, investment.SNM_amt, investment.STORJ_amt, investment.MAN_amt, investment.ICN_amt, investment.SALT_amt, investment.NEXO_amt, investment.DATA_amt, investment.BTCD_amt, investment.HOT_amt, investment.CVC_amt, investment.REQ_amt, investment.NCASH_amt, investment.PAY_amt, investment.AGI_amt, investment.HPB_amt, investment.SKY_amt, investment.TNB_amt, investment.ACT_amt, investment.XAS_amt, investment.CVT_amt, investment.ANT_amt, investment.BCI_amt, investment.GNO_amt, investment.MDS_amt, investment.NEBL_amt, investment.BTO_amt, investment.SAN_amt, investment.RUFF_amt, investment.ABT_amt, investment.TRUE_amt, investment.CND_amt, investment.EKT_amt, investment.GAME_amt, investment.SMT_amt, investment.DENT_amt, investment.GRS_amt, investment.DTR_amt, investment.CRPT_amt, investment.QSP_amt, investment.DAI_amt, investment.SOC_amt, investment.CS_amt, investment.IGNIS_amt, investment.XDN_amt, investment.PLR_amt, investment.ENJ_amt, investment.C20_amt, investment.STQ_amt, investment.VTC_amt, investment.BLZ_amt, investment.TKY_amt, investment.BOS_amt, investment.PART_amt, investment.XSN_amt, investment.EDR_amt, investment.TPAY_amt, investment.RDN_amt, investment.AMB_amt, investment.QKC_amt, investment.OCN_amt, investment.GNX_amt, investment.PPC_amt, investment.BRD_amt, investment.ODE_amt, investment.NKN_amt, investment.ZCL_amt, investment.POA_amt, investment.SRN_amt, investment.SPHTX_amt, investment.VEE_amt, investment.UBQ_amt, investment.NANJ_amt, investment.MTL_amt, investment.GVT_amt, investment.CPX_amt, investment.IOTX_amt, investment.TIO_amt, investment.IHT_amt, investment.POE_amt, investment.REN_amt, investment.JNT_amt, investment.AUTO_amt, investment.TEL_amt, investment.BTX_amt, investment.INT_amt, investment.BURST_amt, investment.SAFEX_amt, investment.ITC_amt, investment.EDG_amt, investment.LINDA_amt, investment.XPM_amt, investment.INK_amt, investment.ECA_amt, investment.BITCNY_amt, investment.RKT_amt, investment.DAX_amt, investment.TEN_amt, investment.NAV_amt, investment.SPANK_amt, investment.TRAC_amt, investment.LCC_amt, investment.DTA_amt, investment.NLG_amt, investment.EDO_amt, investment.WGR_amt, investment.RPX_amt, investment.DPY_amt, investment.LEND_amt, investment.EXC_amt, investment.UNO_amt, investment.EMC2_amt, investment.BAY_amt, investment.LYM_amt, investment.ADX_amt, investment.FTC_amt, investment.CPT_amt, investment.APIS_amt, investment.QRL_amt, investment.RVN_amt, investment.BAX_amt, investment.RNTB_amt, investment.PPP_amt, investment.TKN_amt, investment.SLS_amt, investment.TOMO_amt, investment.DATX_amt, investment.LGO_amt, investment.PZM_amt, investment.ETP_amt, investment.CLOAK_amt, investment.EVN_amt, investment.XCP_amt, investment.SWM_amt, investment.TNT_amt, investment.RCN_amt, investment.TCT_amt, investment.SWFTC_amt, investment.VIA_amt, investment.SNGLS_amt, investment.ZCO_amt, investment.GIN_amt, investment.OST_amt, investment.FXT_amt, investment.AST_amt, investment.HAV_amt, investment.PAC_amt, investment.KICK_amt, investment.PRE_amt, investment.SXDT_amt, investment.DNT_amt, investment.XWC_amt, investment.UTK_amt, investment.INS_amt, investment.ATN_amt, investment.UTNP_amt, investment.WINGS_amt, investment.CPC_amt, investment.MGO_amt, investment.DAT_amt, investment.XP_amt, investment.NGC_amt, investment.BCO_amt, investment.ZPT_amt, investment.RNT_amt, investment.AEON_amt, investment.MSP_amt, investment.HTML_amt, investment.CDT_amt, investment.LYL_amt, investment.NMC_amt, investment.MOD_amt, investment.MNX_amt, investment.WPR_amt, investment.HST_amt, investment.LBC_amt, investment.CREDO_amt, investment.ION_amt, investment.YOYOW_amt, investment.ART_amt, investment.MLN_amt, investment.CMCT_amt, investment.FUEL_amt, investment.HVN_amt, investment.DCT_amt, investment.APPC_amt, investment.MED_amt, investment.PHR_amt, investment.BANCA_amt, investment.LET_amt, investment.ECC_amt, investment.LUN_amt, investment.DAG_amt, investment.UUU_amt, investment.SBD_amt, investment.SENT_amt, investment.DBET_amt, investment.TAAS_amt, investment.QLC_amt, investment.WABI_amt, investment.PCN_amt, investment.PURA_amt, investment.XDCE_amt, investment.SSC_amt, investment.VIBE_amt, investment.ELEC_amt, investment.MEDIC_amt, investment.COSS_amt, investment.YEE_amt, investment.AURA_amt, investment.CSC_amt, investment.MOBI_amt, investment.PRL_amt, investment.QUN_amt, investment.SHIFT_amt, investment.CAS_amt, investment.SOAR_amt, investment.BITG_amt, investment.BKX_amt, investment.DOCK_amt, investment.KEY_amt, investment.XES_amt, investment.POT_amt, investment.QBT_amt, investment.DXT_amt, investment.IXT_amt, investment.BMC_amt, investment.PEPECASH_amt, investment.COB_amt, investment.GRID_amt, investment.BITUSD_amt, investment.KRM_amt, investment.HMQ_amt, investment.VIB_amt, investment.PPY_amt, investment.XEL_amt, investment.e_1ST_amt, investment.NLC2_amt, investment.MTN_amt, investment.THC_amt, investment.TNC_amt, investment.NTK_amt, investment.COLX_amt, investment.COV_amt, investment.DIME_amt, investment.FOTA_amt, investment.LIFE_amt, investment.XBY_amt, investment.MER_amt, investment.RFR_amt, investment.PST_amt, investment.ZSC_amt, investment.PRA_amt, investment.CFI_amt, investment.BIS_amt, investment.QAU_amt, investment.LEO_amt, investment.BRM_amt, investment.BCPT_amt, investment.AMP_amt, investment.TIME_amt, investment.BITB_amt, investment.BLT_amt, investment.LUX_amt, investment.SPC_amt, investment.ONION_amt, investment.RVR_amt, investment.CEEK_amt, investment.TRIG_amt, investment.LATX_amt, investment.ACAT_amt, investment.ALQO_amt, investment.MOT_amt, investment.XSH_amt, investment.EVX_amt, investment.DIVX_amt, investment.DMT_amt, investment.CRW_amt, investment.MWAT_amt, investment.UKG_amt, investment.PASC_amt, investment.TAU_amt, investment.OXY_amt, investment.OMX_amt, investment.BBR_amt, investment.TSL_amt, investment.DIM_amt, investment.PRO_amt, investment.PLBT_amt, investment.DADI_amt, investment.UGC_amt, investment.DMD_amt, investment.BLK_amt, investment.SNC_amt, investment.BETR_amt, investment.GRC_amt, investment.BOT_amt, investment.FLASH_amt, investment.TFD_amt, investment.DBIX_amt, investment.UQC_amt, investment.SWTH_amt, investment.SKB_amt, investment.BCA_amt, investment.SOUL_amt, investment.GUP_amt, investment.MUSE_amt, investment.SNTR_amt, investment.GEM_amt, investment.LA_amt, investment.NKC_amt, investment.MUE_amt, investment.BPT_amt, investment.STK_amt, investment.NMR_amt, investment.CV_amt, investment.OMNI_amt, investment.REM_amt, investment.HYDRO_amt, investment.RBY_amt, investment.ORME_amt, investment.SSP_amt, investment.EVR_amt, investment.MTH_amt, investment.SHND_amt, investment.NEU_amt, investment.RADS_amt, investment.CAPP_amt, investment.STX_amt, investment.MDA_amt, investment.RMT_amt, investment.TIX_amt, investment.MDT_amt, investment.SLR_amt, investment.OAX_amt, investment.ADT_amt, investment.FLO_amt, investment.ARN_amt, investment.BBN_amt, investment.MOON_amt, investment.CHP_amt, investment.AIT_amt, investment.CLO_amt, investment.AIDOC_amt, investment.FDZ_amt, investment.LOC_amt, investment.PAL_amt, investment.IOC_amt, investment.PKC_amt, investment.HXX_amt, investment.UP_amt, investment.SLT_amt, investment.PAT_amt, investment.DICE_amt, investment.EXRN_amt, investment.HMC_amt, investment.SENC_amt, investment.DLT_amt, investment.GEN_amt, investment.CHSB_amt, investment.ABYSS_amt, investment.BQ_amt, investment.EXP_amt, investment.EKO_amt, investment.ZIPT_amt, investment.CLAM_amt, investment.IDH_amt, investment.SRCOIN_amt, investment.ATM_amt, investment.NYC_amt, investment.DEV_amt, investment.GCR_amt, investment.NBAI_amt, investment.POLIS_amt, investment.DTB_amt, investment.CVCOIN_amt, investment.MRK_amt, investment.SHIP_amt, investment.INCNT_amt, investment.HER_amt, investment.AXP_amt, investment.LMC_amt, investment.REBL_amt, investment.APH_amt, investment.DRT_amt, investment.HKN_amt, investment.UBT_amt, investment.XMY_amt, investment.RVT_amt, investment.SEXC_amt, investment.ECOB_amt, investment.SIB_amt, investment.RED_amt, investment.ICOS_amt, investment.SPRTS_amt, investment.GET_amt, investment.PCL_amt, investment.NEOS_amt, investment.BWK_amt, investment.NPX_amt, investment.DYN_amt, investment.BEZ_amt, investment.XST_amt, investment.IPL_amt, investment.VRC_amt, investment.IFT_amt, investment.MUSIC_amt, investment.CAT_amt, investment.LOKI_amt, investment.UCASH_amt, investment.BSD_amt, investment.PIRL_amt, investment.DEB_amt, investment.HWC_amt, investment.NVC_amt, investment.XAUR_amt, investment.FLIXX_amt, investment.RMC_amt, investment.PKT_amt, investment.GBX_amt, investment.NCT_amt, investment.GRFT_amt, investment.EFX_amt, investment.NXC_amt, investment.XPA_amt, investment.AU_amt, investment.SS_amt, investment.APX_amt, investment.PARETO_amt, investment.AIR_amt, investment.PINK_amt, investment.GETX_amt, investment.ZLA_amt, investment.LEV_amt, investment.SWT_amt, investment.AID_amt, investment.TUBE_amt, investment.OK_amt, investment.DGTX_amt, investment.BIO_amt, investment.AVT_amt, investment.MTX_amt, investment.CAG_amt, investment.FLDC_amt, investment.SPD_amt, investment.CXO_amt, investment.PRG_amt, investment.CAN_amt, investment.HBT_amt, investment.PTOY_amt, investment.ZAP_amt, investment.LALA_amt, investment.HBZ_amt, investment.ZOI_amt, investment.PND_amt, investment.ERO_amt, investment.BDG_amt, investment.ADB_amt, investment.ZRC_amt, investment.GOLOS_amt, investment.DERO_amt, investment.MINT_amt, investment.LNC_amt, investment.LWF_amt, investment.DNA_amt, investment.BCC_amt, investment.ADH_amt, investment.PUT_amt, investment.DOT_amt, investment.XNK_amt, investment.SIG_amt, investment.SENSE_amt, investment.MLM_amt, investment.IDXM_amt, investment.FLUZ_amt, investment.BET_amt, investment.NET_amt, investment.BERRY_amt, investment.ELIX_amt, investment.TRST_amt, investment.SEQ_amt, investment.YOC_amt, investment.ADI_amt, investment.BNTY_amt, investment.HEAT_amt, investment.ALIS_amt, investment.B2B_amt, investment.TGT_amt, investment.ENRG_amt, investment.ESP_amt, investment.APR_amt, investment.MITX_amt, investment.e_1WO_amt, investment.XLR_amt, investment.XSPEC_amt, investment.CBT_amt, investment.CURE_amt, investment.CFUN_amt, investment.COFI_amt, investment.CLN_amt, investment.BEE_amt, investment.BCY_amt, investment.FID_amt, investment.LDC_amt, investment.FACE_amt, investment.MORPH_amt, investment.MYST_amt, investment.PBT_amt, investment.GLD_amt, investment.ADST_amt, investment.LND_amt, investment.COVAL_amt, investment.AUR_amt, investment.SETH_amt, investment.SNOV_amt, investment.EVE_amt, investment.ATB_amt, investment.TOA_amt, investment.TFL_amt, investment.SPHR_amt, investment.MYB_amt, investment.PRIX_amt, investment.POLL_amt, investment.EZT_amt, investment.WCT_amt, investment.MAX_amt, investment.CSNO_amt, investment.TRF_amt, investment.AVA_amt, investment.SYNX_amt, investment.GLA_amt, investment.REAL_amt, investment.IPSX_amt, investment.ABY_amt, investment.TX_amt, investment.NPER_amt, investment.KORE_amt, investment.TIPS_amt, investment.ARY_amt, investment.VIT_amt, investment.OBITS_amt, investment.SHL_amt, investment.WRC_amt, investment.SHP_amt, investment.HQX_amt, investment.J8T_amt, investment.INXT_amt, investment.BRX_amt, investment.VME_amt, investment.BTCZ_amt, investment.PTC_amt, investment.MONK_amt, investment.HUR_amt, investment.GEO_amt, investment.e_2GIVE_amt, investment.ASTRO_amt, investment.AUC_amt, investment.DTH_amt, investment.OTN_amt, investment.BLUE_amt, investment.PLAY_amt, investment.XBC_amt, investment.FND_amt, investment.PFR_amt, investment.HYP_amt, investment.GCC_amt, investment.IOP_amt, investment.FDX_amt, investment.ATL_amt, investment.INSTAR_amt, investment.HGT_amt, investment.LEDU_amt, investment.UNIT_amt, investment.USNBT_amt, investment.SUMO_amt, investment.EXY_amt, investment.e_0xBTC_amt, investment.SPR_amt, investment.ERC_amt, investment.XHV_amt, investment.INV_amt, investment.CPAY_amt, investment.IXC_amt, investment.BUZZ_amt, investment.BBO_amt, investment.HAC_amt, investment.BSTN_amt, investment.NTRN_amt, investment.XMCC_amt, investment.SXUT_amt, investment.UFR_amt, investment.SPF_amt, investment.GMT_amt, investment.SEND_amt, investment.AMLT_amt, investment.SCL_amt, investment.QWARK_amt, investment.DOPE_amt, investment.TKS_amt, investment.MSR_amt, investment.FTX_amt, investment.TKA_amt, investment.VRM_amt, investment.RIC_amt, investment.PING_amt, investment.PBL_amt, investment.RUPX_amt, investment.GAT_amt, investment.ZEIT_amt, investment.VOISE_amt, investment.ING_amt, investment.EXCL_amt, investment.HOLD_amt, investment.WISH_amt, investment.IND_amt, investment.MEME_amt, investment.ALT_amt, investment.BON_amt, investment.BRK_amt, investment.EBST_amt, investment.BTDX_amt, investment.I0C_amt, investment.TRC_amt, investment.KRB_amt, investment.SSS_amt, investment.PURE_amt, investment.XHI_amt, investment.CRAVE_amt, investment.ORE_amt, investment.HUSH_amt, investment.VTR_amt, investment.ANC_amt, investment.CMPCO_amt, investment.ETBS_amt, investment.REF_amt, investment.DNR_amt, investment.XGOX_amt, investment.CHX_amt, investment.MVC_amt, investment.FOR_amt, investment.CANN_amt, investment.VIU_amt, investment.NAVI_amt, investment.FYP_amt, investment.CPY_amt, investment.STAC_amt, investment.GENE_amt, investment.SGR_amt, investment.NIO_amt, investment.PIX_amt, investment.MAGE_amt, investment.NLX_amt, investment.EGC_amt, investment.CL_amt, investment.ZEPH_amt, investment.MFG_amt, investment.BBP_amt, investment.BUN_amt, investment.PYLNT_amt, investment.CDX_amt, investment.DAN_amt, investment.TRAK_amt, investment.LDOGE_amt, investment.TES_amt, investment.FGC_amt, investment.AIX_amt, investment.WSX_amt, investment.MAC_amt, investment.NOBL_amt, investment.DP_amt, investment.LOCI_amt, investment.HIRE_amt, investment.OPC_amt, investment.GCN_amt, investment.IC_amt, investment.ACE_amt, investment.BOUTS_amt, investment.XNN_amt, investment.CREA_amt, investment.EFYT_amt, investment.XTL_amt, investment.TEAM_amt, investment.XMG_amt, investment.HUC_amt, investment.RAIN_amt, investment.MNTP_amt, investment.TRCT_amt, investment.EFL_amt, investment.XBP_amt, investment.BTW_amt, investment.TZC_amt, investment.DIX_amt, investment.ODN_amt, investment.STAK_amt, investment.FT_amt, investment.CRB_amt, investment.HAT_amt, investment.SWIFT_amt, investment.ZER_amt, investment.BYC_amt, investment.AMM_amt, investment.EBTC_amt, investment.FRST_amt, investment.ITNS_amt, investment.ESZ_amt, investment.BTRN_amt, investment.UCOM_amt, investment.SKIN_amt, investment.MAG_amt, investment.DGC_amt, investment.VIVO_amt, investment.PHO_amt, investment.FCN_amt, investment.MRT_amt, investment.RNS_amt, investment.SCT_amt, investment.DAY_amt, investment.JEW_amt, investment.JC_amt, investment.SGN_amt, investment.ADZ_amt, investment.HERO_amt, investment.TDX_amt, investment.ZNY_amt, investment.e_808_amt, investment.EPY_amt, investment.TDS_amt, investment.UIS_amt, investment.DTRC_amt, investment.ELLA_amt, investment.EBCH_amt, investment.UNB_amt, investment.FYN_amt, investment.TIG_amt, investment.AMN_amt, investment.ATS_amt, investment.DFT_amt, investment.NOX_amt, investment.STU_amt, investment.EARTH_amt, investment.JIYO_amt, investment.MEC_amt, investment.ORI_amt, investment.DRPU_amt, investment.MORE_amt, investment.INN_amt, investment.EVC_amt, investment.TNS_amt, investment.LINX_amt, investment.SAGA_amt, investment.MBI_amt, investment.ZET_amt, investment.ARC_amt, investment.EL_amt, investment.UNIFY_amt, investment.EQT_amt, investment.VULC_amt, investment.KLN_amt, investment.QVT_amt, investment.PLAN_amt, investment.VRS_amt, investment.IFLT_amt, investment.BTA_amt, investment.MCAP_amt, investment.SUR_amt, investment.HPC_amt, investment.ELTCOIN_amt, investment.XPD_amt, investment.CRM_amt, investment.RLT_amt, investment.WILD_amt, investment.XTO_amt, investment.DGPT_amt, investment.CJT_amt, investment.BTB_amt, investment.ZBC_amt, investment.e_1337_amt, investment.e_42_amt, investment.GAM_amt, investment.KB3_amt, investment.NSR_amt, investment.CRC_amt, investment.BDL_amt, investment.CHC_amt, investment.GRMD_amt, investment.MBRS_amt, investment.EQL_amt, investment.JET_amt, investment.BITSILVER_amt, investment.PIPL_amt, investment.XCN_amt, investment.BBI_amt, investment.NMS_amt, investment.OCT_amt, investment.QBIC_amt, investment.FANS_amt, investment.ADC_amt, investment.TRUST_amt, investment.VZT_amt, investment.TBX_amt, investment.XRL_amt, investment.ARG_amt, investment.SMS_amt, investment.CRED_amt, investment.ONG_amt, investment.DEW_amt, investment.OPT_amt, investment.DOVU_amt, investment.DEM_amt, investment.SXC_amt, investment.HORSE_amt, investment.LIVE_amt]

# returns investment_array like array with latest valuations of applicable coins
def get_latest_prices_arr(portfolio_ids):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password="01990199",#settings.SPREADS_DB_PASSWD,
                                 db="coiniumweb",#settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    latest_prices_arr = [0.0 for i in range(934)]
    try:
        with connection.cursor() as cursor:
            # print("portfolio_ids", portfolio_ids)
            pairs = get_all_pairs(portfolio_ids)
            #print("pairs", pairs)
            spreads_for_pair = dict()
            for i in range(len(pairs)):
                pair = pairs[i]
                #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                sql = "select * from app_pricingdata where shorthand = %s order by created_at desc limit 1"
                cursor.execute(sql, (pair,))
                spreads = cursor.fetchall()
                spreads_for_pair[pair] = spreads
                if len(spreads):
                    latest_prices_arr[pair_reverse_idx[pair]] = float(spreads[0]["price"])
                else:
                    latest_prices_arr[pair_reverse_idx[pair]] = 0
                #print("for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

    finally:
        connection.close()

    return latest_prices_arr

def get_portfolio_appreciation_since_inception(portfolio):
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
            (pairs, pair_pcts) = get_pairs_and_pcts(portfolio.id)
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
                sql = "select round(avg(price),6) as price, convert((min(created_at) div 1000)*1000, datetime) as time \
from app_pricingdata where shorthand = %s and created_at >= '" + str(portfolio.created_date) + "' \
 group by created_at div 1000;"
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
            for i in range(ln-1, ln):
                appreciation = 0.0
                k = i
                for j in range(len(pairs)):
                    k = len(spreads_for_pair[pairs[j]])-1
                    if k < 0:
                        px = 0
                    else:
                        px = float(spreads_for_pair[pairs[j]][k]["price"])
                    # print ("i", i, "px", px)
                    initial_px = float(spreads_for_pair[pairs[j]][0]["price"])
                    if not initial_px:
                        initial_px = px
                    appreciation += pair_pcts[j] * (px / initial_px)
                tm = spreads_for_pair[pairs[0]][i]["time"]
                tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                appreciations.append(appreciation - 100.0)
            connection.close()
            return appreciations[len(appreciations) - 1]
    finally:
        pass
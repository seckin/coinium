def get_pairs_and_pcts(portfolio):
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
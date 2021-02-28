import datetime
from binance.client import Client as c

# test
test_api_key = "AibX2zigFqfEHTCmuV0pIXtM5rCCk6c2SUnBeF5Hxn78yF40V29n0imCRgV7V5Hq"
test_api_secret = "kLO5DN3Nv38W2uYzBkJrrTpnLfzjCUu8qHhi0gDlkxjk4AsqSHyyrAXxzaUkiS3N"

# crypto
# api_key = "xCTmpTB1thBdiHpLhtHGLbWwE3FBM9f8DeSls1ZOssHnGgh18a2Rustu1aElc41k"
# api_secret = "sFq09v9KbFjjGr7QdzwYL56ZoKZmuL3R0adVttTnEUl3AbZPfi0ijo9XDwYi2YPh"

# binance_api
api_key = "kzWnN0vx3IN4ZJ66vbYZ6ZU8zjoe1cZjNGbFcYni5pQ6eB3O5DID2KRpJdCjNx7g"
api_secret = "lYd3mAcnHZqQmpL6Z8cKcrYGjmGw6rxA1uaOmNERf342rK0VnasRxKV7RzCmLh2R"

timestamp_base_time = datetime.datetime(year=1970, month=1, day=1)

api_coin_base_list = ['BTC', 'ETH', 'BNB', 'USDT', 'TRX', 'XRP']

api_interval_list = [c.KLINE_INTERVAL_1MINUTE,
                     c.KLINE_INTERVAL_3MINUTE,
                     c.KLINE_INTERVAL_5MINUTE,
                     c.KLINE_INTERVAL_15MINUTE,
                     c.KLINE_INTERVAL_30MINUTE,
                     c.KLINE_INTERVAL_1HOUR,
                     c.KLINE_INTERVAL_2HOUR,
                     c.KLINE_INTERVAL_4HOUR,
                     c.KLINE_INTERVAL_6HOUR,
                     c.KLINE_INTERVAL_8HOUR,
                     c.KLINE_INTERVAL_12HOUR,
                     c.KLINE_INTERVAL_1DAY,
                     c.KLINE_INTERVAL_3DAY,
                     c.KLINE_INTERVAL_1WEEK,
                     c.KLINE_INTERVAL_1MONTH]

api_interval_dict = {c.KLINE_INTERVAL_1MINUTE: 0,
                     c.KLINE_INTERVAL_3MINUTE: 1,
                     c.KLINE_INTERVAL_5MINUTE: 2,
                     c.KLINE_INTERVAL_15MINUTE: 3,
                     c.KLINE_INTERVAL_30MINUTE: 4,
                     c.KLINE_INTERVAL_1HOUR: 5,
                     c.KLINE_INTERVAL_2HOUR: 6,
                     c.KLINE_INTERVAL_4HOUR: 7,
                     c.KLINE_INTERVAL_6HOUR: 8,
                     c.KLINE_INTERVAL_8HOUR: 9,
                     c.KLINE_INTERVAL_12HOUR: 10,
                     c.KLINE_INTERVAL_1DAY: 11,
                     c.KLINE_INTERVAL_3DAY: 12,
                     c.KLINE_INTERVAL_1WEEK: 13,
                     c.KLINE_INTERVAL_1MONTH: 14}


symbol_BTC_list = [['1INCHBTC', '2020-12-25 05:00:00'], ['AAVEBTC', '2020-10-15 03:00:00'], ['ADABTC', '2017-11-30 12:29:00'], ['ADXBTC', '2017-11-29 03:10:00'], ['AERGOBTC', '2020-10-21 10:00:00'], ['AGIBTC', '2018-06-05 10:00:00'], ['AIONBTC', '2017-12-21 08:51:00'], ['AKROBTC', '2020-11-02 07:00:00'], ['ALGOBTC', '2019-06-22 00:00:00'], ['ALPHABTC', '2020-10-10 05:00:00'], ['AMBBTC', '2017-11-10 16:14:00'], ['ANKRBTC', '2019-07-23 14:00:00'], ['ANTBTC', '2020-08-13 02:30:00'], ['APPCBTC', '2018-01-05 16:14:00'], ['ARDRBTC', '2018-07-18 11:00:00'], ['ARKBTC', '2017-11-01 09:22:00'], ['ARPABTC', '2019-11-06 14:00:00'], ['ASRBTC', '2020-12-30 06:00:00'], ['ASTBTC', '2017-10-19 04:15:00'], ['ATMBTC', '2020-12-30 06:00:00'], ['ATOMBTC', '2019-04-29 04:00:00'], ['AUDIOBTC', '2020-10-23 19:00:00'], ['AVABTC', '2020-08-05 15:00:00'], ['AVAXBTC', '2020-09-22 06:30:00'], ['AXSBTC', '2020-11-04 13:00:00'], ['BALBTC', '2020-08-06 14:00:00'], ['BANDBTC', '2019-09-18 12:00:00'], ['BATBTC', '2017-11-13 11:10:00'], ['BCDBTC', '2017-11-24 14:26:00'], ['BCHBTC', '2019-11-28 10:00:00'], ['BCPTBTC', '2017-11-14 11:25:00'], ['BEAMBTC', '2019-09-21 12:00:00'], ['BELBTC', '2020-09-15 08:00:00'], ['BLZBTC', '2018-02-06 10:50:00'], ['BNBBTC', '2017-07-14 04:00:00'], ['BNTBTC', '2017-10-17 04:01:00'], ['BOTBTC', '2020-10-29 08:00:00'], ['BQXBTC', '2017-09-22 10:01:00'], ['BRDBTC', '2017-12-24 04:40:00'], ['BTCSTBTC', '2021-01-13 06:00:00'], ['BTGBTC', '2017-10-24 06:21:00'], ['BTSBTC', '2017-11-21 06:51:00'], ['BZRXBTC', '2020-08-29 07:00:00'], ['CDTBTC', '2017-11-16 11:53:00'], ['CELOBTC', '2021-01-05 08:30:00'], ['CELRBTC', '2019-03-25 04:00:00'], ['CHRBTC', '2020-05-07 14:00:00'], ['CHZBTC', '2019-09-06 04:00:00'], ['CKBBTC', '2021-01-26 12:00:00'], ['CNDBTC', '2017-12-11 03:00:00'], ['COMPBTC', '2020-06-25 06:00:00'], ['COSBTC', '2019-08-03 10:00:00'], ['COTIBTC', '2020-02-26 14:00:00'], ['CRVBTC', '2020-08-15 04:00:00'], ['CTKBTC', '2020-10-27 08:00:00'], ['CTSIBTC', '2020-04-23 02:00:00'], ['CTXCBTC', '2019-11-22 14:00:00'], ['CVCBTC', '2018-05-28 09:00:00'], ['DASHBTC', '2017-10-20 04:20:00'], ['DATABTC', '2018-06-08 04:45:00'], ['DCRBTC', '2018-10-24 04:00:00'], ['DGBBTC', '2020-06-22 14:00:00'], ['DIABTC', '2020-09-02 13:00:00'], ['DLTBTC', '2017-11-10 10:04:00'], ['DNTBTC', '2017-10-16 04:06:00'], ['DOCKBTC', '2018-07-30 10:00:00'], ['DOGEBTC', '2019-07-05 12:00:00'], ['DOTBTC', '2020-08-18 23:00:00'], ['DREPBTC', '2020-01-16 14:00:00'], ['DUSKBTC', '2019-07-22 10:00:00'], ['EGLDBTC', '2020-09-03 03:00:00'], ['ELFBTC', '2017-12-21 03:51:00'], ['ENJBTC', '2017-11-03 03:42:00'], ['EOSBTC', '2017-10-11 07:04:00'], ['ETCBTC', '2017-10-12 09:32:00'], ['ETHBTC', '2017-07-14 04:00:00'], ['EVXBTC', '2017-10-26 13:23:00'], ['FETBTC', '2019-02-28 10:00:00'], ['FILBTC', '2020-10-15 17:00:00'], ['FIOBTC', '2020-07-31 09:00:00'], ['FIROBTC', '2021-01-29 02:00:00'], ['FLMBTC', '2020-09-28 07:00:00'], ['FORBTC', '2020-11-17 12:30:00'], ['FTMBTC', '2019-06-11 04:00:00'], ['FTTBTC', '2019-12-20 03:00:00'], ['FUNBTC', '2017-09-28 04:01:00'], ['GASBTC', '2017-08-07 04:00:00'], ['GLMBTC', '2020-12-10 04:00:00'], ['GOBTC', '2018-09-12 04:01:00'], ['GRSBTC', '2018-04-04 09:40:00'], ['GRTBTC', '2020-12-17 20:30:00'], ['GTOBTC', '2017-12-18 08:11:00'], ['GVTBTC', '2017-11-16 09:51:00'], ['GXSBTC', '2017-11-17 02:59:00'], ['HARDBTC', '2020-11-06 06:00:00'], ['HBARBTC', '2019-09-29 04:00:00'], ['HIVEBTC', '2020-04-27 05:00:00'], ['HNTBTC', '2020-09-24 09:00:00'], ['ICXBTC', '2017-12-18 05:10:00'], ['IDEXBTC', '2020-08-22 07:00:00'], ['INJBTC', '2020-10-21 04:00:00'], ['IOSTBTC', '2018-01-24 06:02:00'], ['IOTABTC', '2017-09-30 09:00:00'], ['IOTXBTC', '2018-06-01 05:00:00'], ['IRISBTC', '2020-07-21 13:00:00'], ['JSTBTC', '2020-08-11 06:00:00'], ['JUVBTC', '2020-12-21 06:00:00'], ['KAVABTC', '2019-10-25 02:00:00'], ['KMDBTC', '2017-11-07 08:22:00'], ['KNCBTC', '2017-09-26 04:00:00'], ['KSMBTC', '2020-09-02 11:00:00'], ['LINKBTC', '2017-09-28 08:38:00'], ['LOOMBTC', '2018-05-02 06:45:00'], ['LRCBTC', '2017-09-01 04:00:00'], ['LSKBTC', '2017-11-22 09:42:00'], ['LTCBTC', '2017-07-14 04:09:00'], ['LTOBTC', '2020-02-07 14:00:00'], ['LUNABTC', '2020-08-19 10:00:00'], ['MANABTC', '2017-11-24 02:34:00'], ['MATICBTC', '2019-04-26 15:00:00'], ['MDABTC', '2017-10-05 04:01:00'], ['MDTBTC', '2020-06-05 14:00:00'], ['MITHBTC', '2018-11-15 14:00:00'], ['MKRBTC', '2020-07-23 14:00:00'], ['MTHBTC', '2017-10-13 03:44:00'], ['MTLBTC', '2017-10-09 08:14:00'], ['NANOBTC', '2018-02-02 19:55:00'], ['NASBTC', '2018-06-28 08:00:00'], ['NAVBTC', '2017-12-27 08:56:00'], ['NBSBTC', '2020-09-21 10:00:00'], ['NEARBTC', '2020-10-14 05:00:00'], ['NEBLBTC', '2017-12-22 06:40:00'], ['NEOBTC', '2017-07-14 04:00:00'], ['NKNBTC', '2019-10-11 14:00:00'], ['NMRBTC', '2020-08-17 12:02:00'], ['NULSBTC', '2017-11-09 02:30:00'], ['NXSBTC', '2018-06-06 10:00:00'], ['OAXBTC', '2017-10-23 10:01:00'], ['OCEANBTC', '2020-08-17 08:00:00'], ['OGBTC', '2020-12-30 06:00:00'], ['OGNBTC', '2020-01-09 03:00:00'], ['OMGBTC', '2017-09-12 04:00:00'], ['ONEBTC', '2019-06-01 04:00:00'], ['ONGBTC', '2019-02-16 10:04:00'], ['ONTBTC', '2018-03-08 06:27:00'], ['ORNBTC', '2020-09-30 06:00:00'], ['OSTBTC', '2017-12-19 05:58:00'], ['OXTBTC', '2020-09-21 08:15:00'], ['PAXGBTC', '2020-08-26 12:00:00'], ['PERLBTC', '2019-08-26 12:00:00'], ['PHBBTC', '2019-05-24 04:00:00'], ['PIVXBTC', '2018-01-23 03:29:00'], ['PNTBTC', '2020-06-22 04:00:00'], ['POABTC', '2018-02-28 07:24:00'], ['POLYBTC', '2018-07-31 10:00:00'], ['POWRBTC', '2017-11-01 03:42:00'], ['PPTBTC', '2017-12-01 03:46:00'], ['PSGBTC', '2020-12-21 06:00:00'], ['QKCBTC', '2018-06-05 04:00:00'], ['QLCBTC', '2018-03-26 09:07:00'], ['QSPBTC', '2017-11-21 02:18:00'], ['QTUMBTC', '2017-09-04 04:02:00'], ['RCNBTC', '2017-11-08 05:18:00'], ['RDNBTC', '2017-11-09 11:16:00'], ['REEFBTC', '2020-12-29 06:00:00'], ['RENBTC', '2018-12-06 10:00:00'], ['RENBTCBTC', '2020-11-09 13:00:00'], ['REPBTC', '2018-05-11 07:34:00'], ['REQBTC', '2017-10-27 02:23:00'], ['RIFBTC', '2021-01-07 13:00:00'], ['RLCBTC', '2018-01-12 06:44:00'], ['ROSEBTC', '2020-11-19 08:00:00'], ['RSRBTC', '2020-08-25 07:00:00'], ['RUNEBTC', '2020-07-24 11:00:00'], ['RVNBTC', '2018-10-12 04:00:00'], ['SANDBTC', '2020-08-14 13:00:00'], ['SCBTC', '2018-06-14 11:00:00'], ['SCRTBTC', '2020-09-30 04:00:00'], ['SKLBTC', '2020-12-01 01:00:00'], ['SKYBTC', '2018-05-24 09:00:00'], ['SNGLSBTC', '2017-09-19 10:00:00'], ['SNMBTC', '2017-09-27 07:31:00'], ['SNTBTC', '2017-10-12 08:01:00'], ['SNXBTC', '2020-07-09 12:00:00'], ['SOLBTC', '2020-04-10 04:00:00'], ['SRMBTC', '2020-08-11 13:30:00'], ['STEEMBTC', '2018-02-01 09:36:00'], ['STMXBTC', '2020-06-11 03:00:00'], ['STORJBTC', '2017-11-03 09:25:00'], ['STPTBTC', '2020-03-25 14:00:00'], ['STRAXBTC', '2020-11-18 03:00:00'], ['STXBTC', '2019-10-25 04:00:00'], ['SUNBTC', '2020-09-21 14:00:00'], ['SUSDBTC', '2020-12-04 11:00:00'], ['SUSHIBTC', '2020-09-01 11:00:00'], ['SXPBTC', '2020-07-07 14:00:00'], ['SYSBTC', '2018-03-28 08:37:00'], ['TCTBTC', '2020-01-21 14:00:00'], ['TFUELBTC', '2019-05-24 10:00:00'], ['THETABTC', '2018-05-29 07:30:00'], ['TNBBTC', '2017-12-15 06:29:00'], ['TOMOBTC', '2019-08-24 13:00:00'], ['TRBBTC', '2020-08-27 07:00:00'], ['TROYBTC', '2019-12-05 02:00:00'], ['TRUBTC', '2021-01-19 07:00:00'], ['TRXBTC', '2017-10-31 04:01:00'], ['TWTBTC', '2021-01-27 08:00:00'], ['UMABTC', '2020-09-09 09:00:00'], ['UNFIBTC', '2020-11-19 06:00:00'], ['UNIBTC', '2020-09-17 03:00:00'], ['UTKBTC', '2020-10-02 06:00:00'], ['VETBTC', '2018-07-25 04:00:00'], ['VIABTC', '2018-02-05 07:58:00'], ['VIBBTC', '2017-10-30 07:56:00'], ['VIBEBTC', '2018-01-10 06:31:00'], ['VIDTBTC', '2020-10-09 14:00:00'], ['VITEBTC', '2019-12-13 14:00:00'], ['WABIBTC', '2017-12-12 13:18:00'], ['WANBTC', '2018-03-23 06:00:00'], ['WAVESBTC', '2017-12-15 12:29:00'], ['WBTCBTC', '2020-08-31 08:00:00'], ['WINGBTC', '2020-09-16 02:00:00'], ['WNXMBTC', '2020-08-26 07:00:00'], ['WPRBTC', '2018-03-29 06:24:00'], ['WRXBTC', '2020-02-05 02:00:00'], ['WTCBTC', '2017-08-27 04:00:00'], ['XEMBTC', '2018-03-20 11:46:00'], ['XLMBTC', '2017-12-08 06:01:00'], ['XMRBTC', '2017-11-10 06:12:00'], ['XRPBTC', '2017-11-02 07:58:00'], ['XTZBTC', '2019-09-24 11:00:00'], ['XVGBTC', '2017-10-02 04:00:00'], ['XVSBTC', '2020-10-06 05:00:00'], ['XZCBTC', '2017-11-22 06:05:00'], ['YFIBTC', '2020-08-10 12:00:00'], ['YFIIBTC', '2020-09-01 11:00:00'], ['YOYOBTC', '2017-09-03 04:00:00'], ['ZECBTC', '2017-11-14 03:46:00'], ['ZENBTC', '2018-05-23 07:30:00'], ['ZILBTC', '2018-03-05 06:09:00'], ['ZRXBTC', '2017-09-13 04:00:00']]

symbol_ETH_list = [['AAVEETH', '2020-10-15 03:00:00'], ['ADAETH', '2017-11-30 12:30:00'], ['ADXETH', '2017-11-29 03:11:00'], ['AIONETH', '2017-12-21 08:54:00'], ['BATETH', '2017-11-13 11:11:00'], ['BETHETH', '2021-01-29 12:00:00'], ['BLZETH', '2018-02-06 10:50:00'], ['BNBETH', '2017-08-09 09:00:00'], ['BNTETH', '2017-07-27 00:02:00'], ['BQXETH', '2017-09-22 10:38:00'], ['BRDETH', '2017-12-24 04:40:00'], ['CDTETH', '2017-11-16 11:55:00'], ['CMTETH', '2017-12-05 12:09:00'], ['COVERETH', '2020-12-05 05:00:00'], ['CVCETH', '2018-05-28 09:00:00'], ['CVPETH', '2020-11-16 06:00:00'], ['DASHETH', '2017-10-20 04:19:00'], ['DATAETH', '2018-06-08 04:46:00'], ['DENTETH', '2018-07-06 07:00:00'], ['DEXEETH', '2021-01-21 08:00:00'], ['DFETH', '2020-12-11 10:00:00'], ['EASYETH', '2020-10-23 09:00:00'], ['ELFETH', '2017-12-21 03:51:00'], ['ENJETH', '2017-11-03 03:43:00'], ['EOSETH', '2017-07-27 00:02:00'], ['ETCETH', '2017-10-12 09:33:00'], ['FIROETH', '2021-01-29 02:00:00'], ['FRONTETH', '2020-11-18 08:00:00'], ['FUNETH', '2017-09-28 04:01:00'], ['GHSTETH', '2020-12-08 05:30:00'], ['GLMETH', '2020-12-10 04:00:00'], ['GRTETH', '2020-12-17 20:30:00'], ['GXSETH', '2017-11-17 02:59:00'], ['HEGICETH', '2020-11-25 09:30:00'], ['HOTETH', '2018-07-24 04:00:00'], ['ICXETH', '2017-12-18 05:10:00'], ['IOSTETH', '2018-01-24 06:02:00'], ['IOTAETH', '2017-09-30 09:03:00'], ['IOTXETH', '2018-06-01 05:00:00'], ['KEYETH', '2018-06-27 06:00:00'], ['KMDETH', '2017-11-07 08:23:00'], ['KNCETH', '2017-09-26 04:00:00'], ['LINKETH', '2017-09-28 08:36:00'], ['LOOMETH', '2018-05-02 06:46:00'], ['LRCETH', '2017-09-01 04:00:00'], ['LSKETH', '2017-11-22 09:43:00'], ['LTCETH', '2017-12-13 03:29:00'], ['MANAETH', '2017-11-24 02:35:00'], ['MFTETH', '2018-07-05 09:00:00'], ['MTLETH', '2017-10-09 08:14:00'], ['NANOETH', '2018-02-02 19:56:00'], ['NASETH', '2018-06-28 08:00:00'], ['NCASHETH', '2018-02-26 10:32:00'], ['NEBLETH', '2017-12-22 06:41:00'], ['NEOETH', '2017-09-28 06:31:00'], ['NPXSETH', '2018-06-21 02:01:00'], ['NULSETH', '2017-11-09 02:32:00'], ['OMGETH', '2017-09-12 04:00:00'], ['ONTETH', '2018-03-08 06:28:00'], ['OSTETH', '2017-12-19 05:59:00'], ['PIVXETH', '2018-01-23 03:29:00'], ['POWRETH', '2017-11-01 03:42:00'], ['QKCETH', '2018-06-05 04:00:00'], ['QLCETH', '2018-03-26 09:08:00'], ['QSPETH', '2017-11-21 02:17:00'], ['QTUMETH', '2017-07-27 00:03:00'], ['RENBTCETH', '2020-11-09 13:00:00'], ['REPETH', '2018-05-11 07:34:00'], ['RLCETH', '2018-01-12 06:45:00'], ['SCETH', '2018-06-14 11:00:00'], ['SCRTETH', '2020-09-30 04:00:00'], ['SLPETH', '2020-11-10 09:00:00'], ['SNTETH', '2017-07-27 00:03:00'], ['STEEMETH', '2018-02-01 09:37:00'], ['STMXETH', '2020-06-11 03:00:00'], ['STRAXETH', '2020-11-18 03:00:00'], ['SUSDETH', '2020-12-04 11:00:00'], ['THETAETH', '2018-05-29 07:30:00'], ['TRXETH', '2017-10-31 04:01:00'], ['VETETH', '2018-07-25 04:00:00'], ['VIBETH', '2017-10-30 07:57:00'], ['WANETH', '2018-03-23 06:00:00'], ['WAVESETH', '2017-12-15 12:30:00'], ['WBTCETH', '2020-08-31 08:00:00'], ['XEMETH', '2018-03-20 11:47:00'], ['XLMETH', '2017-12-08 06:03:00'], ['XMRETH', '2017-11-10 06:13:00'], ['XRPETH', '2017-11-02 07:59:00'], ['XVGETH', '2017-10-02 04:00:00'], ['XZCETH', '2017-11-22 06:07:00'], ['ZECETH', '2017-11-14 03:49:00'], ['ZENETH', '2018-05-23 07:30:00'], ['ZILETH', '2018-03-05 06:09:00'], ['ZRXETH', '2017-09-13 04:05:00']]

symbol_BNB_list = [['AAVEBNB', '2020-10-15 03:00:00'], ['ADABNB', '2018-04-17 04:02:00'], ['ALGOBNB', '2019-06-22 00:00:00'], ['ALPHABNB', '2020-10-10 05:00:00'], ['ANKRBNB', '2019-07-23 14:00:00'], ['ANTBNB', '2020-08-13 02:30:00'], ['ARPABNB', '2019-11-06 14:00:00'], ['ATOMBNB', '2019-04-29 04:00:00'], ['AVABNB', '2020-08-05 15:00:00'], ['AVAXBNB', '2020-09-22 06:30:00'], ['AXSBNB', '2020-11-04 13:00:00'], ['BAKEBNB', '2020-09-24 11:00:00'], ['BANDBNB', '2019-09-18 12:00:00'], ['BATBNB', '2017-11-13 11:12:00'], ['BCHBNB', '2019-11-28 10:00:00'], ['BELBNB', '2020-09-15 08:00:00'], ['BLZBNB', '2018-02-06 10:50:00'], ['BTTBNB', '2019-01-31 10:00:00'], ['BURGERBNB', '2020-09-24 11:00:00'], ['CAKEBNB', '2020-09-29 08:00:00'], ['CELRBNB', '2019-03-25 04:00:00'], ['CHRBNB', '2020-05-07 14:00:00'], ['CHZBNB', '2019-09-06 04:00:00'], ['COCOSBNB', '2019-08-21 11:00:00'], ['COSBNB', '2019-08-03 10:00:00'], ['COTIBNB', '2020-02-26 14:00:00'], ['CREAMBNB', '2020-09-16 13:00:00'], ['CRVBNB', '2020-08-15 04:00:00'], ['CTKBNB', '2020-10-27 08:00:00'], ['CTSIBNB', '2020-04-23 02:00:00'], ['DASHBNB', '2019-03-28 04:00:00'], ['DGBBNB', '2020-06-22 14:00:00'], ['DIABNB', '2020-09-02 13:00:00'], ['DOTBNB', '2020-08-18 23:00:00'], ['EGLDBNB', '2020-09-03 03:00:00'], ['ENJBNB', '2018-06-07 08:30:00'], ['EOSBNB', '2018-05-28 05:00:00'], ['ETCBNB', '2018-06-12 02:30:00'], ['FETBNB', '2019-02-28 10:00:00'], ['FILBNB', '2020-10-15 17:00:00'], ['FIOBNB', '2020-07-31 09:00:00'], ['FTMBNB', '2019-06-11 04:00:00'], ['FTTBNB', '2019-12-20 03:00:00'], ['HARDBNB', '2020-11-06 06:00:00'], ['HBARBNB', '2019-09-29 04:00:00'], ['HOTBNB', '2019-02-18 10:00:00'], ['ICXBNB', '2017-12-18 05:12:00'], ['INJBNB', '2020-10-21 04:00:00'], ['IOSTBNB', '2019-03-22 04:08:00'], ['IOTABNB', '2017-11-28 07:47:00'], ['IQBNB', '2020-06-18 10:00:00'], ['JSTBNB', '2020-08-11 06:00:00'], ['KAVABNB', '2019-10-25 02:00:00'], ['KP3RBNB', '2020-11-03 12:00:00'], ['KSMBNB', '2020-09-02 11:00:00'], ['LTCBNB', '2017-12-13 03:31:00'], ['LUNABNB', '2020-08-19 10:00:00'], ['MATICBNB', '2019-04-26 15:00:00'], ['MBLBNB', '2020-02-21 14:00:00'], ['MFTBNB', '2018-07-05 09:00:00'], ['MITHBNB', '2018-11-15 14:00:00'], ['MKRBNB', '2020-07-23 14:00:00'], ['NEARBNB', '2020-10-14 05:00:00'], ['NEOBNB', '2017-11-20 03:41:00'], ['NMRBNB', '2020-08-17 12:02:00'], ['OCEANBNB', '2020-08-17 08:00:00'], ['OGNBNB', '2020-01-09 03:00:00'], ['ONEBNB', '2019-06-01 04:00:00'], ['ONTBNB', '2018-03-08 06:28:00'], ['PAXGBNB', '2020-08-26 12:00:00'], ['PERLBNB', '2019-08-26 12:00:00'], ['PROMBNB', '2020-11-26 07:00:00'], ['RSRBNB', '2020-08-25 07:00:00'], ['RUNEBNB', '2020-07-24 11:00:00'], ['RVNBNB', '2018-10-12 04:00:00'], ['SANDBNB', '2020-08-14 13:00:00'], ['SCBNB', '2018-06-14 11:00:00'], ['SNXBNB', '2020-07-09 12:00:00'], ['SOLBNB', '2020-04-10 04:00:00'], ['SPARTABNB', '2020-09-29 08:00:00'], ['SRMBNB', '2020-08-11 13:30:00'], ['STMXBNB', '2020-06-11 03:00:00'], ['STXBNB', '2019-10-25 04:00:00'], ['SUSHIBNB', '2020-09-01 11:00:00'], ['SWRVBNB', '2020-09-15 06:00:00'], ['SXPBNB', '2020-07-07 14:00:00'], ['THETABNB', '2018-05-29 07:30:00'], ['TROYBNB', '2019-12-05 02:00:00'], ['TRXBNB', '2018-06-12 07:59:00'], ['UNFIBNB', '2020-11-19 06:00:00'], ['UNIBNB', '2020-09-17 03:00:00'], ['VETBNB', '2018-07-25 04:00:00'], ['VTHOBNB', '2020-07-17 09:00:00'], ['WABIBNB', '2017-12-12 13:26:00'], ['WANBNB', '2018-03-23 06:00:00'], ['WAVESBNB', '2017-12-15 12:32:00'], ['WINBNB', '2019-08-01 10:00:00'], ['WINGBNB', '2020-09-16 02:00:00'], ['WNXMBNB', '2020-08-26 07:00:00'], ['WRXBNB', '2020-02-05 02:00:00'], ['WTCBNB', '2017-11-10 09:40:00'], ['XLMBNB', '2017-12-08 06:04:00'], ['XMRBNB', '2019-03-15 04:00:00'], ['XRPBNB', '2018-05-31 09:30:00'], ['XTZBNB', '2019-09-24 11:00:00'], ['XVSBNB', '2020-10-06 05:00:00'], ['YFIBNB', '2020-08-10 12:00:00'], ['YFIIBNB', '2020-09-01 11:00:00'], ['ZECBNB', '2019-03-21 04:00:00'], ['ZENBNB', '2018-05-23 07:30:00'], ['ZILBNB', '2018-03-05 06:11:00']]

symbol_USDT_list =[['1INCHUSDT', '2020-12-25 05:00:00'], ['AAVEUSDT', '2020-10-15 03:00:00'], ['ADAUSDT', '2018-04-17 04:02:00'], ['AIONUSDT', '2020-02-19 09:00:00'], ['AKROUSDT', '2020-11-02 07:00:00'], ['ALGOUSDT', '2019-06-22 00:00:00'], ['ALPHAUSDT', '2020-10-10 05:00:00'], ['ANKRUSDT', '2019-07-23 14:00:00'], ['ANTUSDT', '2020-08-13 02:30:00'], ['ARDRUSDT', '2020-05-15 08:00:00'], ['ARPAUSDT', '2019-11-06 14:00:00'], ['ASRUSDT', '2020-12-30 06:00:00'], ['ATMUSDT', '2020-12-30 06:00:00'], ['ATOMUSDT', '2019-04-29 04:00:00'], ['AUDIOUSDT', '2020-10-23 19:00:00'], ['AUDUSDT', '2020-08-07 02:00:00'], ['AVAUSDT', '2020-11-24 13:00:00'], ['AVAXUSDT', '2020-09-22 06:30:00'], ['AXSUSDT', '2020-11-04 13:00:00'], ['BALUSDT', '2020-08-11 06:00:00'], ['BANDUSDT', '2019-09-18 12:00:00'], ['BATUSDT', '2019-03-04 10:00:00'], ['BCHUSDT', '2019-11-28 10:00:00'], ['BEAMUSDT', '2019-09-21 12:00:00'], ['BELUSDT', '2020-09-15 08:00:00'], ['BLZUSDT', '2020-08-11 06:00:00'], ['BNBUSDT', '2017-11-06 03:54:00'], ['BNTUSDT', '2020-02-06 10:00:00'], ['BTCSTUSDT', '2021-01-13 06:00:00'], ['BTCUSDT', '2017-08-17 04:00:00'], ['BTSUSDT', '2020-02-06 10:00:00'], ['BTTUSDT', '2019-01-31 10:00:00'], ['BUSDUSDT', '2019-09-20 08:00:00'], ['BZRXUSDT', '2020-08-31 07:00:00'], ['CELOUSDT', '2021-01-05 08:30:00'], ['CELRUSDT', '2019-03-25 04:00:00'], ['CHRUSDT', '2020-05-07 14:00:00'], ['CHZUSDT', '2019-09-06 04:00:00'], ['CKBUSDT', '2021-01-26 12:00:00'], ['COCOSUSDT', '2019-08-21 11:00:00'], ['COMPUSDT', '2020-06-25 06:00:00'], ['COSUSDT', '2019-08-03 10:00:00'], ['COTIUSDT', '2020-02-26 14:00:00'], ['CRVUSDT', '2020-08-15 04:00:00'], ['CTKUSDT', '2020-10-27 08:00:00'], ['CTSIUSDT', '2020-04-23 02:00:00'], ['CTXCUSDT', '2019-11-22 14:00:00'], ['CVCUSDT', '2019-08-27 04:00:00'], ['DASHUSDT', '2019-03-28 04:00:00'], ['DATAUSDT', '2020-04-07 13:00:00'], ['DCRUSDT', '2020-07-30 05:00:00'], ['DENTUSDT', '2019-08-27 04:00:00'], ['DGBUSDT', '2020-07-20 12:00:00'], ['DIAUSDT', '2020-09-04 13:00:00'], ['DNTUSDT', '2020-11-10 06:00:00'], ['DOCKUSDT', '2019-08-27 04:00:00'], ['DOGEUSDT', '2019-07-05 12:00:00'], ['DOTUSDT', '2020-08-18 23:00:00'], ['DREPUSDT', '2020-01-16 14:00:00'], ['DUSKUSDT', '2019-07-22 10:00:00'], ['EGLDUSDT', '2020-09-03 03:00:00'], ['ENJUSDT', '2019-04-18 04:00:00'], ['EOSUSDT', '2018-05-28 05:00:00'], ['ETCUSDT', '2018-06-12 02:30:00'], ['ETHUSDT', '2017-08-17 04:00:00'], ['EURUSDT', '2020-01-03 08:00:00'], ['FETUSDT', '2019-02-28 10:00:00'], ['FILUSDT', '2020-10-15 17:00:00'], ['FIOUSDT', '2020-09-04 06:50:00'], ['FIROUSDT', '2021-01-29 02:00:00'], ['FLMUSDT', '2020-09-28 07:00:00'], ['FTMUSDT', '2019-06-11 04:00:00'], ['FTTUSDT', '2019-12-20 03:00:00'], ['FUNUSDT', '2019-08-27 04:00:00'], ['GBPUSDT', '2020-07-20 12:00:00'], ['GRTUSDT', '2020-12-17 20:30:00'], ['GTOUSDT', '2019-07-01 11:00:00'], ['GXSUSDT', '2020-05-13 14:00:00'], ['HARDUSDT', '2020-11-06 06:00:00'], ['HBARUSDT', '2019-09-29 04:00:00'], ['HIVEUSDT', '2020-04-27 05:00:00'], ['HNTUSDT', '2020-09-24 09:00:00'], ['HOTUSDT', '2019-02-18 10:00:00'], ['ICXUSDT', '2018-06-13 08:01:00'], ['INJUSDT', '2020-10-21 04:00:00'], ['IOSTUSDT', '2019-03-22 04:08:00'], ['IOTAUSDT', '2018-05-31 09:30:00'], ['IOTXUSDT', '2019-11-14 03:00:00'], ['IRISUSDT', '2020-08-11 06:00:00'], ['JSTUSDT', '2020-08-11 06:00:00'], ['JUVUSDT', '2020-12-21 06:00:00'], ['KAVAUSDT', '2019-10-25 02:00:00'], ['KEYUSDT', '2019-08-27 04:00:00'], ['KMDUSDT', '2020-08-11 06:00:00'], ['KNCUSDT', '2020-06-12 08:00:00'], ['KSMUSDT', '2020-09-04 11:00:00'], ['LINKUSDT', '2019-01-16 10:00:00'], ['LRCUSDT', '2020-06-12 08:00:00'], ['LSKUSDT', '2020-02-06 10:00:00'], ['LTCUSDT', '2017-12-13 03:32:00'], ['LTOUSDT', '2020-02-07 14:00:00'], ['LUNAUSDT', '2020-08-21 10:00:00'], ['MANAUSDT', '2020-08-06 10:00:00'], ['MATICUSDT', '2019-04-26 15:00:00'], ['MBLUSDT', '2020-02-21 14:00:00'], ['MDTUSDT', '2020-06-05 14:00:00'], ['MFTUSDT', '2019-08-27 04:00:00'], ['MITHUSDT', '2019-04-19 10:00:00'], ['MKRUSDT', '2020-07-23 14:00:00'], ['MTLUSDT', '2019-08-23 10:00:00'], ['NANOUSDT', '2019-04-03 04:00:00'], ['NBSUSDT', '2020-09-21 10:00:00'], ['NEARUSDT', '2020-10-14 05:00:00'], ['NEOUSDT', '2017-11-20 03:42:00'], ['NKNUSDT', '2019-10-11 14:00:00'], ['NMRUSDT', '2020-08-19 12:00:00'], ['NPXSUSDT', '2019-08-13 11:00:00'], ['NULSUSDT', '2018-07-23 04:02:00'], ['OCEANUSDT', '2020-08-19 08:00:00'], ['OGNUSDT', '2020-01-09 03:00:00'], ['OGUSDT', '2020-12-30 06:00:00'], ['OMGUSDT', '2019-04-03 04:00:00'], ['ONEUSDT', '2019-06-01 04:00:00'], ['ONGUSDT', '2019-02-16 10:04:00'], ['ONTUSDT', '2018-06-08 07:00:00'], ['ORNUSDT', '2020-09-30 06:00:00'], ['OXTUSDT', '2020-09-21 08:15:00'], ['PAXGUSDT', '2020-08-28 12:00:00'], ['PAXUSDT', '2018-10-04 10:00:00'], ['PERLUSDT', '2019-08-26 12:00:00'], ['PNTUSDT', '2020-06-22 04:00:00'], ['PSGUSDT', '2020-12-21 06:00:00'], ['QTUMUSDT', '2018-03-19 08:48:00'], ['REEFUSDT', '2020-12-29 06:00:00'], ['RENUSDT', '2019-09-25 12:00:00'], ['REPUSDT', '2020-06-12 08:00:00'], ['RIFUSDT', '2021-01-07 13:00:00'], ['RLCUSDT', '2019-11-14 03:00:00'], ['ROSEUSDT', '2020-11-19 08:00:00'], ['RSRUSDT', '2020-08-27 07:00:00'], ['RUNEUSDT', '2020-09-04 06:50:00'], ['RVNUSDT', '2019-09-25 12:00:00'], ['SANDUSDT', '2020-08-14 13:00:00'], ['SCUSDT', '2020-07-06 05:00:00'], ['SKLUSDT', '2020-12-01 01:00:00'], ['SNXUSDT', '2020-07-09 12:00:00'], ['SOLUSDT', '2020-08-11 06:00:00'], ['SRMUSDT', '2020-08-11 13:30:00'], ['STMXUSDT', '2020-06-11 03:00:00'], ['STORJUSDT', '2020-07-30 05:00:00'], ['STPTUSDT', '2020-03-25 14:00:00'], ['STRAXUSDT', '2020-11-18 03:00:00'], ['STXUSDT', '2019-10-25 04:00:00'], ['SUNUSDT', '2020-09-21 14:00:00'], ['SUSDUSDT', '2020-12-04 11:00:00'], ['SUSHIUSDT', '2020-09-01 11:00:00'], ['SXPUSDT', '2020-07-20 12:00:00'], ['TCTUSDT', '2020-01-21 14:00:00'], ['TFUELUSDT', '2019-05-24 10:00:00'], ['THETAUSDT', '2019-04-10 04:00:00'], ['TOMOUSDT', '2019-08-24 13:00:00'], ['TRBUSDT', '2020-08-29 07:00:00'], ['TROYUSDT', '2019-12-05 02:00:00'], ['TRUUSDT', '2021-01-19 07:00:00'], ['TRXUSDT', '2018-06-11 11:30:00'], ['TUSDUSDT', '2018-05-31 09:32:00'], ['TWTUSDT', '2021-01-27 08:00:00'], ['UMAUSDT', '2020-09-09 09:00:00'], ['UNFIUSDT', '2020-11-19 06:00:00'], ['UNIUSDT', '2020-09-17 03:00:00'], ['USDCUSDT', '2018-12-15 03:12:00'], ['UTKUSDT', '2020-10-02 06:00:00'], ['VETUSDT', '2018-07-25 04:00:00'], ['VITEUSDT', '2019-12-13 14:00:00'], ['VTHOUSDT', '2020-07-17 09:00:00'], ['WANUSDT', '2019-08-27 04:00:00'], ['WAVESUSDT', '2019-01-18 10:00:00'], ['WINGUSDT', '2020-09-16 02:00:00'], ['WINUSDT', '2019-08-01 10:00:00'], ['WNXMUSDT', '2020-08-28 07:00:00'], ['WRXUSDT', '2020-02-05 02:00:00'], ['WTCUSDT', '2020-04-07 13:00:00'], ['XEMUSDT', '2020-11-24 13:00:00'], ['XLMUSDT', '2018-05-31 09:30:00'], ['XMRUSDT', '2019-03-15 04:00:00'], ['XRPUSDT', '2018-05-04 08:11:00'], ['XTZUSDT', '2019-09-24 11:00:00'], ['XZCUSDT', '2020-04-07 13:00:00'], ['YFIIUSDT', '2020-09-01 11:00:00'], ['YFIUSDT', '2020-08-10 12:00:00'], ['ZECUSDT', '2019-03-21 04:00:00'], ['ZENUSDT', '2020-07-06 05:00:00'], ['XVSUSDT', '2020-10-06 05:00:00'], ['ZILUSDT', '2019-02-19 11:04:00'], ['ZRXUSDT', '2019-02-28 04:00:00']]

symbol_TRX_list = [['BTTTRX', '2019-09-04 10:00:00'], ['WINTRX', '2019-09-04 10:00:00']]

symbol_XRP_list = [['TRXXRP', '2018-12-24 11:02:00']]


# symbol_ETH_list = ['AAVEETH', 'ADAETH', 'ADXETH', 'AIONETH', 'BATETH', 'BETHETH', 'BLZETH', 'BNBETH', 'BNTETH', 'BQXETH', 'BRDETH', 'CDTETH', 'CMTETH', 'COVERETH', 'CVCETH', 'CVPETH', 'DASHETH', 'DATAETH', 'DENTETH', 'DEXEETH', 'DFETH', 'EASYETH', 'ELFETH', 'ENJETH', 'EOSETH', 'ETCETH', 'FIROETH', 'FRONTETH', 'FUNETH', 'GHSTETH', 'GLMETH', 'GRTETH', 'GXSETH', 'HEGICETH', 'HOTETH', 'ICXETH', 'IOSTETH', 'IOTAETH', 'IOTXETH', 'KEYETH', 'KMDETH', 'KNCETH', 'LINKETH', 'LOOMETH', 'LRCETH', 'LSKETH', 'LTCETH', 'MANAETH', 'MFTETH', 'MTLETH', 'NANOETH', 'NASETH', 'NCASHETH', 'NEBLETH', 'NEOETH', 'NPXSETH', 'NULSETH', 'OMGETH', 'ONTETH', 'OSTETH', 'PIVXETH', 'POWRETH', 'QKCETH', 'QLCETH', 'QSPETH', 'QTUMETH', 'RENBTCETH', 'REPETH', 'RLCETH', 'SCETH', 'SCRTETH', 'SLPETH', 'SNTETH', 'STEEMETH', 'STMXETH', 'STRAXETH', 'SUSDETH', 'THETAETH', 'TRXETH', 'VETETH', 'VIBETH', 'WANETH', 'WAVESETH', 'WBTCETH', 'XEMETH', 'XLMETH', 'XMRETH', 'XRPETH', 'XVGETH', 'XZCETH', 'ZECETH', 'ZENETH', 'ZILETH', 'ZRXETH']
# symbol_BNB_list = ['AAVEBNB', 'ADABNB', 'ALGOBNB', 'ALPHABNB', 'ANKRBNB', 'ANTBNB', 'ARPABNB', 'ATOMBNB', 'AVABNB', 'AVAXBNB', 'AXSBNB', 'BAKEBNB', 'BANDBNB', 'BATBNB', 'BCHBNB', 'BELBNB', 'BLZBNB', 'BTTBNB', 'BURGERBNB', 'CAKEBNB', 'CELRBNB', 'CHRBNB', 'CHZBNB', 'COCOSBNB', 'COSBNB', 'COTIBNB', 'CREAMBNB', 'CRVBNB', 'CTKBNB', 'CTSIBNB', 'DASHBNB', 'DGBBNB', 'DIABNB', 'DOTBNB', 'EGLDBNB', 'ENJBNB', 'EOSBNB', 'ETCBNB', 'FETBNB', 'FILBNB', 'FIOBNB', 'FTMBNB', 'FTTBNB', 'HARDBNB', 'HBARBNB', 'HOTBNB', 'ICXBNB', 'INJBNB', 'IOSTBNB', 'IOTABNB', 'IQBNB', 'JSTBNB', 'KAVABNB', 'KP3RBNB', 'KSMBNB', 'LTCBNB', 'LUNABNB', 'MATICBNB', 'MBLBNB', 'MFTBNB', 'MITHBNB', 'MKRBNB', 'NEARBNB', 'NEOBNB', 'NMRBNB', 'OCEANBNB', 'OGNBNB', 'ONEBNB', 'ONTBNB', 'PAXGBNB', 'PERLBNB', 'PROMBNB', 'RSRBNB', 'RUNEBNB', 'RVNBNB', 'SANDBNB', 'SCBNB', 'SNXBNB', 'SOLBNB', 'SPARTABNB', 'SRMBNB', 'STMXBNB', 'STXBNB', 'SUSHIBNB', 'SWRVBNB', 'SXPBNB', 'THETABNB', 'TROYBNB', 'TRXBNB', 'UNFIBNB', 'UNIBNB', 'VETBNB', 'VTHOBNB', 'WABIBNB', 'WANBNB', 'WAVESBNB', 'WINBNB', 'WINGBNB', 'WNXMBNB', 'WRXBNB', 'WTCBNB', 'XLMBNB', 'XMRBNB', 'XRPBNB', 'XTZBNB', 'XVSBNB', 'YFIBNB', 'YFIIBNB', 'ZECBNB', 'ZENBNB', 'ZILBNB']
# symbol_BTC_list = ['1INCHBTC', 'AAVEBTC', 'ADABTC', 'ADXBTC', 'AERGOBTC', 'AGIBTC', 'AIONBTC', 'AKROBTC', 'ALGOBTC', 'ALPHABTC', 'AMBBTC', 'ANKRBTC', 'ANTBTC', 'APPCBTC', 'ARDRBTC', 'ARKBTC', 'ARPABTC', 'ASRBTC', 'ASTBTC', 'ATMBTC', 'ATOMBTC', 'AUDIOBTC', 'AVABTC', 'AVAXBTC', 'AXSBTC', 'BALBTC', 'BANDBTC', 'BATBTC', 'BCDBTC', 'BCHBTC', 'BCPTBTC', 'BEAMBTC', 'BELBTC', 'BLZBTC', 'BNBBTC', 'BNTBTC', 'BOTBTC', 'BQXBTC', 'BRDBTC', 'BTCSTBTC', 'BTGBTC', 'BTSBTC', 'BZRXBTC', 'CDTBTC', 'CELOBTC', 'CELRBTC', 'CHRBTC', 'CHZBTC', 'CKBBTC', 'CNDBTC', 'COMPBTC', 'COSBTC', 'COTIBTC', 'CRVBTC', 'CTKBTC', 'CTSIBTC', 'CTXCBTC', 'CVCBTC', 'DASHBTC', 'DATABTC', 'DCRBTC', 'DGBBTC', 'DIABTC', 'DLTBTC', 'DNTBTC', 'DOCKBTC', 'DOGEBTC', 'DOTBTC', 'DREPBTC', 'DUSKBTC', 'EGLDBTC', 'ELFBTC', 'ENJBTC', 'EOSBTC', 'ETCBTC', 'ETHBTC', 'EVXBTC', 'FETBTC', 'FILBTC', 'FIOBTC', 'FIROBTC', 'FLMBTC', 'FORBTC', 'FTMBTC', 'FTTBTC', 'FUNBTC', 'GASBTC', 'GLMBTC', 'GOBTC', 'GRSBTC', 'GRTBTC', 'GTOBTC', 'GVTBTC', 'GXSBTC', 'HARDBTC', 'HBARBTC', 'HIVEBTC', 'HNTBTC', 'ICXBTC', 'IDEXBTC', 'INJBTC', 'IOSTBTC', 'IOTABTC', 'IOTXBTC', 'IRISBTC', 'JSTBTC', 'JUVBTC', 'KAVABTC', 'KMDBTC', 'KNCBTC', 'KSMBTC', 'LINKBTC', 'LOOMBTC', 'LRCBTC', 'LSKBTC', 'LTCBTC', 'LTOBTC', 'LUNABTC', 'MANABTC', 'MATICBTC', 'MDABTC', 'MDTBTC', 'MITHBTC', 'MKRBTC', 'MTHBTC', 'MTLBTC', 'NANOBTC', 'NASBTC', 'NAVBTC', 'NBSBTC', 'NEARBTC', 'NEBLBTC', 'NEOBTC', 'NKNBTC', 'NMRBTC', 'NULSBTC', 'NXSBTC', 'OAXBTC', 'OCEANBTC', 'OGBTC', 'OGNBTC', 'OMGBTC', 'ONEBTC', 'ONGBTC', 'ONTBTC', 'ORNBTC', 'OSTBTC', 'OXTBTC', 'PAXGBTC', 'PERLBTC', 'PHBBTC', 'PIVXBTC', 'PNTBTC', 'POABTC', 'POLYBTC', 'POWRBTC', 'PPTBTC', 'PSGBTC', 'QKCBTC', 'QLCBTC', 'QSPBTC', 'QTUMBTC', 'RCNBTC', 'RDNBTC', 'REEFBTC', 'RENBTC', 'RENBTCBTC', 'REPBTC', 'REQBTC', 'RIFBTC', 'RLCBTC', 'ROSEBTC', 'RSRBTC', 'RUNEBTC', 'RVNBTC', 'SANDBTC', 'SCBTC', 'SCRTBTC', 'SKLBTC', 'SKYBTC', 'SNGLSBTC', 'SNMBTC', 'SNTBTC', 'SNXBTC', 'SOLBTC', 'SRMBTC', 'STEEMBTC', 'STMXBTC', 'STORJBTC', 'STPTBTC', 'STRAXBTC', 'STXBTC', 'SUNBTC', 'SUSDBTC', 'SUSHIBTC', 'SXPBTC', 'SYSBTC', 'TCTBTC', 'TFUELBTC', 'THETABTC', 'TNBBTC', 'TOMOBTC', 'TRBBTC', 'TROYBTC', 'TRUBTC', 'TRXBTC', 'TWTBTC', 'UMABTC', 'UNFIBTC', 'UNIBTC', 'UTKBTC', 'VETBTC', 'VIABTC', 'VIBBTC', 'VIBEBTC', 'VIDTBTC', 'VITEBTC', 'WABIBTC', 'WANBTC', 'WAVESBTC', 'WBTCBTC', 'WINGBTC', 'WNXMBTC', 'WPRBTC', 'WRXBTC', 'WTCBTC', 'XEMBTC', 'XLMBTC', 'XMRBTC', 'XRPBTC', 'XTZBTC', 'XVGBTC', 'XVSBTC', 'XZCBTC', 'YFIBTC', 'YFIIBTC', 'YOYOBTC', 'ZECBTC', 'ZENBTC', 'ZILBTC', 'ZRXBTC']
# symbol_USDT_list = ['1INCHUSDT', 'AAVEUSDT', 'ADAUSDT', 'AIONUSDT', 'AKROUSDT', 'ALGOUSDT', 'ALPHAUSDT', 'ANKRUSDT', 'ANTUSDT', 'ARDRUSDT', 'ARPAUSDT', 'ASRUSDT', 'ATMUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'AUDUSDT', 'AVAUSDT', 'AVAXUSDT', 'AXSUSDT', 'BALUSDT', 'BANDUSDT', 'BATUSDT', 'BCHUSDT', 'BEAMUSDT', 'BELUSDT', 'BLZUSDT', 'BNBUSDT', 'BNTUSDT', 'BTCSTUSDT', 'BTCUSDT', 'BTSUSDT', 'BTTUSDT', 'BUSDUSDT', 'BZRXUSDT', 'CELOUSDT', 'CELRUSDT', 'CHRUSDT', 'CHZUSDT', 'CKBUSDT', 'COCOSUSDT', 'COMPUSDT', 'COSUSDT', 'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CTXCUSDT', 'CVCUSDT', 'DASHUSDT', 'DATAUSDT', 'DCRUSDT', 'DENTUSDT', 'DGBUSDT', 'DIAUSDT', 'DNTUSDT', 'DOCKUSDT', 'DOGEUSDT', 'DOTUSDT', 'DREPUSDT', 'DUSKUSDT', 'EGLDUSDT', 'ENJUSDT', 'EOSUSDT', 'ETCUSDT', 'ETHUSDT', 'EURUSDT', 'FETUSDT', 'FILUSDT', 'FIOUSDT', 'FIROUSDT', 'FLMUSDT', 'FTMUSDT', 'FTTUSDT', 'FUNUSDT', 'GBPUSDT', 'GRTUSDT', 'GTOUSDT', 'GXSUSDT', 'HARDUSDT', 'HBARUSDT', 'HIVEUSDT', 'HNTUSDT', 'HOTUSDT', 'ICXUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IRISUSDT', 'JSTUSDT', 'JUVUSDT', 'KAVAUSDT', 'KEYUSDT', 'KMDUSDT', 'KNCUSDT', 'KSMUSDT', 'LINKUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCUSDT', 'LTOUSDT', 'LUNAUSDT', 'MANAUSDT', 'MATICUSDT', 'MBLUSDT', 'MDTUSDT', 'MFTUSDT', 'MITHUSDT', 'MKRUSDT', 'MTLUSDT', 'NANOUSDT', 'NBSUSDT', 'NEARUSDT', 'NEOUSDT', 'NKNUSDT', 'NMRUSDT', 'NPXSUSDT', 'NULSUSDT', 'OCEANUSDT', 'OGNUSDT', 'OGUSDT', 'OMGUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'ORNUSDT', 'OXTUSDT', 'PAXGUSDT', 'PAXUSDT', 'PERLUSDT', 'PNTUSDT', 'PSGUSDT', 'QTUMUSDT', 'REEFUSDT', 'RENUSDT', 'REPUSDT', 'RIFUSDT', 'RLCUSDT', 'ROSEUSDT', 'RSRUSDT', 'RUNEUSDT', 'RVNUSDT', 'SANDUSDT', 'SCUSDT', 'SKLUSDT', 'SNXUSDT', 'SOLUSDT', 'SRMUSDT', 'STMXUSDT', 'STORJUSDT', 'STPTUSDT', 'STRAXUSDT', 'STXUSDT', 'SUNUSDT', 'SUSDUSDT', 'SUSHIUSDT', 'SXPUSDT', 'TCTUSDT', 'TFUELUSDT', 'THETAUSDT', 'TOMOUSDT', 'TRBUSDT', 'TROYUSDT', 'TRUUSDT', 'TRXUSDT', 'TUSDUSDT', 'TWTUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIUSDT', 'USDCUSDT', 'UTKUSDT', 'VETUSDT', 'VITEUSDT', 'VTHOUSDT', 'WANUSDT', 'WAVESUSDT', 'WINGUSDT', 'WINUSDT', 'WNXMUSDT', 'WRXUSDT', 'WTCUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPUSDT', 'XTZUSDT', 'XZCUSDT', 'YFIIUSDT', 'YFIUSDT', 'ZECUSDT', 'ZENUSDT', 'XVSUSDT', 'ZILUSDT', 'ZRXUSDT']
# symbol_TRX_list = ['BTTTRX', 'WINTRX']
# symbol_XRP_list = ['TRXXRP']
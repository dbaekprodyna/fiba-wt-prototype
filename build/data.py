# -*- coding: utf-8 -*-
"""Every figure below is read off the live 2026 World Tour site
   (worldtour.fiba3x3.com/2026) or fiba3x3.com's individual world
   ranking, both read on 3 September 2026."""

# ---- the season, in order. Zadar is tonight. --------------------
STOPS = [
    ("Utsunomiya Opener", "utsunomiya", "past"),
    ("Chengdu",           "chengdu",    "past"),
    ("Zadar",             "zadar",      "live"),
    ("Shanghai",          "shanghai",   "next"),
    ("Vienna",            "vienna",     "next"),
    ("Amsterdam",         "amsterdam",  "next"),
    ("Ulaanbaatar",       "ulaanbaatar","next"),
    ("Marseille",         "marseille",  "next"),
    ("Lausanne",          "lausanne",   "next"),
    ("Debrecen",          "debrecen",   "next"),
    ("Deqing",            "deqing",     "next"),
    ("Málaga",            "malaga",     "next"),
    ("Macau",             "macau",      "next"),
    ("Zaisan",            "zaisan",     "next"),
    ("Manama",            "manama",     "next"),
    ("Hong Kong",         "hongkong",   "next"),
    ("Rio de Janeiro Final", "rio",     "next"),
]

CLD = "https://res.cloudinary.com/ddsbdyeyj/image/upload/ar_16:9,c_lfill,g_auto/w_%d,c_lfill/q_auto/v%s/%s"
def cld(ver, ident, w=1200):
    return CLD % (w, ver, ident)

# ---- Latest news: the five items the World Tour news index leads
#      with on 3 Sep 2026, with the site's own photographs. -------
NEWS = [
    dict(t="Baskets Bonn set the pace: All we learned from World Tour Debrecen",
         d="Bonn's breakthrough proved just how unpredictable the 2026 season remains — and the Germans have now turned an outside shout into a title run.",
         tag="Report", date="Mon 31 Aug", ver="1788122591", img="qirgmjtvki6mf6gtrk2c",
         href="https://worldtour.fiba3x3.com/2026/news/baskets-bonn-set-the-pace-all-we-learned-from-world-tour-debrecen"),
    dict(t="FIBA 3x3 World Tour Utsunomiya Opener 2026 strengthens commitment to sustainable event delivery",
         tag="Announcement", date="Wed 2 Sep", ver="1777114256", img="zhltqbltb9eilmxmjoqx",
         href="https://worldtour.fiba3x3.com/2026/news/fiba-3x3-world-tour-utsunomiya-opener-2026-strengthens-commitment-to-sustainable-event-delivery"),
    dict(t="Debrecen delivers another landmark chapter in its 3x3 basketball story",
         tag="Event", date="Mon 31 Aug", ver="1788041840", img="uaq3r7u19wxmmhu1tpll",
         href="https://worldtour.fiba3x3.com/2026/news/debrecen-delivers-another-landmark-chapter-in-its-3x3-story"),
    dict(t="Baskets Bonn win FIBA 3x3 World Tour Debrecen 2026",
         tag="Result", date="Sun 30 Aug", ver="1788119709", img="qzs5dulvesu6jmxtiq4u",
         href="https://worldtour.fiba3x3.com/2026/news/baskets-bonn-win-fiba-3x3-world-tour-debrecen-2026"),
    dict(t="Fabian Giessmann named FIBA 3x3 World Tour Debrecen 2026 MVP",
         tag="Award", date="Sun 30 Aug", ver="1788119692", img="k9unbkizop9uzs6iafr6",
         href="https://worldtour.fiba3x3.com/2026/news/fabian-giessmann-named-fiba-3x3-world-tour-debrecen-2026-mvp"),
]

# ---- Tour standings, top 16, read off /2026/standings -----------
STANDINGS = [
    (1,  "Ub",                     "SRB", 575, "72%", "19.3"),
    (2,  "Liman",                  "SRB", 535, "61%", "17.9"),
    (3,  "Amsterdam RABOBANK",     "NED", 430, "76%", "19.3"),
    (4,  "Baskets Bonn",           "GER", 428, "75%", "18.1"),
    (5,  "Skyliners",              "GER", 303, "57%", "16.9"),
    (6,  "Antwerp",                "BEL", 300, "50%", "17.7"),
    (7,  "Miami",                  "USA", 295, "61%", "18.8"),
    (8,  "Ulaanbaatar MMC Energy", "MGL", 293, "52%", "17.2"),
    (9,  "Raudondvaris Hoptrans",  "LTU", 260, "55%", "17.2"),
    (10, "Shanghai",               "CHN", 253, "47%", "17.4"),
    (11, "Vienna",                 "AUT", 188, "35%", "17.4"),
    (12, "Toulouse",               "FRA", 184, "42%", "17.2"),
    (13, "DeQing",                 "CHN", 180, "58%", "18.4"),
    (14, "Toronto",                "CAN", 130, "40%", "15.9"),
    (15, "Hangzhou Jingwei",       "CHN", 129, "50%", "17.0"),
    (16, "Cibona Ph.Classic",      "CRO", 115, "44%", "16.6"),
    (17, "Fuengirola",             "ESP", 104, "41%", "16.4"),
    (18, "Crvena Zvezda",          "SRB",  86, "38%", "16.1"),
    (19, "Barcelona",              "ESP",  72, "33%", "15.8"),
    (20, "Phoenix",                "USA",  69, "31%", "16.0"),
]

# ---- Zadar: the twelve-team main draw, with the pools drawn for
#      the event and each team's seed. Three more teams contest the
#      qualifying draw, so the field on site is fifteen. ----------
ZADAR_FIELD = [
    ("A", "Ub",                 "SRB", 1,  575),
    ("A", "Toronto",            "CAN", 8,  130),
    ("A", "Baskets Bonn",       "GER", 5,  428),
    ("B", "Miami",              "USA", 2,  295),
    ("B", "Vienna",             "AUT", 7,  188),
    ("B", "Fuengirola",         "ESP", 11, 104),
    ("C", "Liman",              "SRB", 3,  535),
    ("C", "Antwerp",            "BEL", 9,  300),
    ("C", "Cibona Ph.Classic",  "CRO", 10, 115),
    ("D", "Amsterdam RABOBANK", "NED", 4,  430),
    ("D", "Shanghai",           "CHN", 6,  253),
    ("D", "Los Angeles",        "USA", 12, None),
]

# ---- Individual world ranking, men, updated 3 Sept 2026 ---------
def photo(uuid):
    a, b, c, d = uuid[0], uuid[1], uuid[2], uuid[3]
    return ("https://assets.fiba3x3.com/images/Member/%s/%s/%s/%s/%s/profile.original.png"
            % (a, b, c, d, uuid))

PLAYERS = [
    dict(rk=1, first="Strahinja", last="Stojacic",   ioc="SRB", team="Ub",
         pts="992,519", uuid="89829610-bfa8-4694-8399-3eb4812743d6"),
    dict(rk=2, first="Worthy",    last="de Jong",    ioc="NED", team="Amsterdam RABOBANK",
         pts="869,394", uuid="3322b794-03c3-4b20-8417-f373865e7397"),
    dict(rk=3, first="Fabian",    last="Giessmann",  ioc="GER", team="Baskets Bonn",
         pts="833,076", uuid="1fd4d5e1-b6bd-4774-88f3-b3f3dd28efc5"),
    dict(rk=4, first="Nenad",     last="Nerandžić",  ioc="SRB", team="Ub",
         pts="817,559", uuid="2110dfaf-3a92-4172-b809-d9744eabf837"),
    dict(rk=5, first="Henry",     last="Caruso",     ioc="USA", team="Miami",
         pts="791,508", uuid="1ea253b4-8a85-4b62-9af2-61a4870e78e2"),
    dict(rk=6, first="Stefan",    last="Milivojevic", ioc="SRB", team="Liman",
         pts="735,840", uuid="d714b0db-ae7d-4ab0-a064-79aed594132e"),
]

# ---- Ub's roster, as the team page lists it ---------------------
UB_ROSTER = [
    dict(rk="1",  first="Strahinja", last="Stojacic",     ioc="SRB", pts="992,519",
         uuid="89829610-bfa8-4694-8399-3eb4812743d6"),
    dict(rk="4",  first="Nenad",     last="Nerandžić",    ioc="SRB", pts="817,559",
         uuid="2110dfaf-3a92-4172-b809-d9744eabf837"),
    dict(rk="7",  first="Filip",     last="Kaluđerović",  ioc="SRB", pts="725,759",
         uuid="25284026-e3ad-4d38-851b-b0335be7b95d"),
    dict(rk="9",  first="Marko",     last="Brankovic",    ioc="SRB", pts="713,826",
         uuid="9bb57539-de5c-44df-ac47-5225fc04f868"),
    dict(rk="11", first="Nemanja",   last="Barać",        ioc="SRB", pts="708,845",
         uuid="479e3046-b44d-441f-b24c-f43fecb02560"),
    dict(rk="—",  first="Dejan",     last="Majstorovic",  ioc="SRB", pts="—",
         uuid="e5a1a5fc-c06d-4239-b73f-e321185737f8"),
]

# ---- Ub's season, as the team page lists it ---------------------
UB_SEASON = [
    ("Shibuya City Challenger", "Challenger", "18–19 Apr", "5th",  "—",   "Ranking (automatic)"),
    ("Utsunomiya Opener",       "Masters",    "25–26 Apr", "3rd",  "70",  "Ranking (hard seed)"),
    ("Chengdu",                 "Masters",    "2–3 May",   "1st",  "100", "Ranking (hard seed)"),
    ("Zadar",                   "Masters",    "15–16 May", "3rd",  "70",  "Performance slot"),
    ("Vienna",                  "Masters",    "12–14 Jun", "4th",  "60",  "Ranking (hard seed)"),
    ("Amsterdam",               "Masters",    "19–21 Jun", "3rd",  "70",  "Ranking (hard seed)"),
    ("Ulaanbaatar",             "Masters",    "27–28 Jun", "6th",  "45",  "Performance slot"),
    ("Marseille",               "Masters",    "4–5 Jul",   "1st",  "100", "Performance slot"),
    ("Cáceres Challenger",      "Challenger", "11–12 Jul", "1st",  "—",   "Ranking (automatic)"),
    ("Novi Sad Challenger",     "Challenger", "18–19 Jul", "1st",  "—",   "Ranking (automatic)"),
    ("Batam City Challenger",   "Challenger", "25–26 Jul", "5th",  "—",   "Ranking (automatic)"),
    ("Athens Challenger",       "Challenger", "31 Jul–1 Aug", "1st", "—",  "Ranking (automatic)"),
    ("Bordeaux Challenger",     "Challenger", "21–22 Aug", "1st",  "—",   "Ranking (automatic)"),
    ("Debrecen",                "Masters",    "29–30 Aug", "4th",  "60",  "From Cáceres"),
    ("Hongcheon Challenger",    "Challenger", "18–19 Sep", "—",    "—",   "Ranking (automatic)"),
    ("Deqing",                  "Masters",    "26–27 Sep", "—",    "—",   "From SBA Pro Tour Final"),
    ("Madrid Challenger",       "Challenger", "3–4 Oct",   "—",    "—",   "Ranking (automatic)"),
    ("Málaga",                  "Masters",    "10–11 Oct", "—",    "—",   "From Novi Sad"),
    ("Zaisan",                  "Masters",    "14–15 Nov", "—",    "—",   "From Antwerp Quest"),
]

UB_SELECTIONS = ["Utsunomiya Opener", "Chengdu", "Vienna", "Amsterdam"]

# ---- Six Shorts from youtube.com/@FIBA3x3, all men's World Tour -
SHORTS = [
    ("XU9ZmHnOg2U", "Pap put on a SHOW for the home crowd! 🇭🇺 #3x3WTDebrecen"),
    ("hQSJcY989Oc", "Nenad with the HAMMER! 🇷🇸 #3x3WTDebrecen"),
    ("BoruQZUaY7I", "Air Parrott got up to THROW DOWN! 🇺🇸 #3x3WTDebrecen"),
    ("V_Snhw2fMHA", "AIR MATTIA! 🇮🇹 #3x3WTDebrecen"),
    ("fbLVORINsrc", "Baskets Bonn 🇩🇪 connect UP HIGH! #3x3WTDebrecen"),
    ("wcO30cXC3nk", "ICE-COLD GIESSMANN FTW! Baskets Bonn \U0001F1E9\U0001F1EA emerge victorious at #3x3WTDebrecen"),
]

# ---- Photo galleries, with the counts the site publishes --------
PHOTOS_HOME = [
    ("Debrecen — Games, 30 Aug",   "277", "1788030641", "xywisvauxmbsu2kcpvtt"),
    ("Debrecen — Prize ceremony",  "43",  "1788119709", "qzs5dulvesu6jmxtiq4u"),
    ("Bordeaux Challenger",        "172", "1787430627", "skktvhv1ugrcfowljs7a"),
    ("Beijing — Dunk contest",     "78",  "1787488631", "q7g9ybmtekhkmu0ijmar"),
]
PHOTOS_TEAM = [
    ("Ub at Bordeaux Challenger",  "172", "1787430627", "skktvhv1ugrcfowljs7a"),
    ("Ub at Debrecen",             "277", "1788030641", "xywisvauxmbsu2kcpvtt"),
    ("Majstorović returns",        "24",  "1750010596", "gv3olfjuoaxmfzybpkix"),
    ("Zadar — player and team",    "197", "1782207898", "i9h1pepa8klscoo51a4x"),
]

import streamlit as st

st.set_page_config(
    page_title="PracticeLink — Physician Matching",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
    box-sizing: border-box;
}
.main { background: #F0F2F5; }
.block-container {
    padding: 0 80px 60px 80px !important;
    max-width: 1320px !important;
    margin: 0 auto !important;
}

/* ── NAV ── */
.nav {
    background: #fff;
    border-bottom: 1.5px solid #E2E6EE;
    padding: 0 80px;
    display: flex; align-items: center;
    height: 68px; gap: 40px;
    margin-bottom: 36px;
}
.logo-wrap { display: flex; align-items: center; gap: 12px; }
.logo-mark {
    width: 42px; height: 42px; background: #1251A3;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
}
.logo-text { font-size: 22px; font-weight: 700; color: #1251A3; letter-spacing: -0.5px; }
.nav-right { margin-left: auto; display: flex; align-items: center; gap: 8px; }
.nav-item { font-size: 14px; color: #5A6278; font-weight: 500; padding: 6px 16px; border-radius: 8px; cursor: pointer; }
.nav-item-active { font-size: 14px; color: #1251A3; font-weight: 600; background: #EEF3FC; border-radius: 8px; padding: 6px 16px; }
.nav-btn { background: #1251A3; color: white; font-size: 14px; font-weight: 600; padding: 10px 24px; border-radius: 24px; cursor: pointer; }

/* ── VIEW TOGGLE TABS ── */
.tab-bar-wrap {
    margin-bottom: 28px;
}
.tab-bar-wrap > div[data-testid="stHorizontalBlock"] {
    background: white;
    border: 1.5px solid #E2E6EE;
    border-radius: 14px;
    padding: 6px;
    gap: 4px !important;
}
.tab-bar-wrap .stButton > button {
    border-radius: 10px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 13px 20px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    letter-spacing: -0.1px !important;
}
.tab-bar-wrap .stButton > button[kind="primary"] {
    background: #1251A3 !important;
    color: white !important;
    box-shadow: 0 2px 10px rgba(18,81,163,0.22) !important;
}
.tab-bar-wrap .stButton > button[kind="secondary"] {
    background: transparent !important;
    color: #8A93A8 !important;
    box-shadow: none !important;
}

/* ── LIST HEADER ── */
.list-header { display: flex; align-items: baseline; gap: 12px; margin-bottom: 20px; }
.list-title { font-size: 22px; font-weight: 700; color: #111827; }
.list-sub { font-size: 14px; color: #8A93A8; }

/* ── RESULT CARDS ── */
.rcard {
    background: white;
    border: 1.5px solid #E2E6EE;
    border-radius: 16px;
    padding: 24px 26px;
    margin-bottom: 14px;
    position: relative;
    transition: box-shadow 0.15s, border-color 0.15s;
}
.rcard:hover { box-shadow: 0 4px 18px rgba(0,0,0,0.07); border-color: #BFC9DA; }
.rcard-active { border: 2px solid #1251A3 !important; background: #FAFBFF; }
.rcard-top { display: flex; align-items: flex-start; gap: 16px; }
.rcard-logo {
    width: 56px; height: 56px; border-radius: 12px;
    border: 1.5px solid #E2E6EE;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 16px; flex-shrink: 0;
}
.rcard-info { flex: 1; padding-right: 100px; }
.rcard-title { font-size: 17px; font-weight: 700; color: #1251A3; margin: 0 0 5px; }
.rcard-org { font-size: 15px; font-weight: 600; color: #1F2937; margin: 0 0 4px; }
.rcard-meta { font-size: 13px; color: #6B7280; margin: 0; line-height: 1.6; }
.rcard-badge { position: absolute; top: 24px; right: 26px; text-align: right; }
.rb-pct { font-size: 38px; font-weight: 700; line-height: 1; }
.rb-lbl { font-size: 11px; font-weight: 600; color: #8A93A8; text-transform: uppercase; letter-spacing: 0.06em; margin-top: 2px; }
.tag-row { display: flex; flex-wrap: wrap; gap: 7px; margin: 16px 0 14px; }
.tag { font-size: 12px; font-weight: 600; padding: 5px 13px; border-radius: 7px; }
.tag-blue { background: #EEF3FC; color: #1251A3; }
.tag-green { background: #EDFAF3; color: #1A7A52; }
.tag-gray { background: #F1F3F6; color: #5A6278; }
.rcard-reason {
    font-size: 13px; color: #5A6278; font-weight: 500;
    border-top: 1px solid #F1F3F6; padding-top: 14px;
    display: flex; align-items: center; gap: 9px;
}
.rdot { width: 7px; height: 7px; border-radius: 50%; background: #1251A3; flex-shrink: 0; }

/* ── PROFILE COMPLETENESS ── */
.pcomp {
    background: #FFFBEB; border: 1.5px solid #FDE68A;
    border-radius: 12px; padding: 16px 20px; margin-bottom: 20px;
}
.pcomp-title { font-size: 13px; font-weight: 700; color: #92400E; margin-bottom: 5px; }
.pcomp-text { font-size: 13px; color: #78350F; line-height: 1.6; }
.pcomp-bar-bg { height: 6px; background: #FEF3C7; border-radius: 99px; margin-top: 10px; overflow: hidden; }
.pcomp-bar { height: 100%; background: #F59E0B; border-radius: 99px; width: 72%; }

/* ── DETAIL CARD ── */
.dcard {
    background: white; border: 1.5px solid #E2E6EE;
    border-radius: 18px; padding: 36px 34px;
    position: sticky; top: 24px;
}
.dcard-logo {
    width: 72px; height: 72px; border-radius: 14px;
    border: 1.5px solid #E2E6EE;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 24px; margin-bottom: 20px;
}
.dcard-title { font-size: 21px; font-weight: 700; color: #111827; margin: 0 0 7px; line-height: 1.3; }
.dcard-org { font-size: 15px; font-weight: 600; color: #374151; margin: 0 0 4px; }
.dcard-meta { font-size: 14px; color: #6B7280; margin: 0 0 4px; }
.dcard-comp { font-size: 16px; font-weight: 700; color: #1A7A52; margin: 10px 0 20px; }

/* ── OUTREACH STATUS ── */
.status-pill {
    display: inline-flex; align-items: center; gap: 8px;
    border-radius: 24px; padding: 7px 16px;
    font-size: 13px; font-weight: 600; margin-bottom: 24px;
}
.status-new { background: #EDFAF3; color: #1A7A52; border: 1.5px solid #A7E3C5; }
.status-contacted { background: #FEF3E8; color: #C05621; border: 1.5px solid #F6C79E; }
.status-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }

/* ── MATCH RING ── */
.mring {
    background: #F7F8FA; border: 1.5px solid #E2E6EE;
    border-radius: 14px; padding: 22px 26px;
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 30px;
}
.mring-pct { font-size: 56px; font-weight: 700; line-height: 1; }
.mring-lbl { font-size: 12px; font-weight: 600; color: #8A93A8; text-transform: uppercase; letter-spacing: 0.07em; margin-top: 6px; }
.mring-right { font-size: 14px; color: #6B7280; text-align: right; line-height: 2; }

/* ── BREAKDOWN ── */
.bd-title { font-size: 12px; font-weight: 700; color: #8A93A8; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 20px; }
.bd-item { margin-bottom: 20px; }
.bd-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
.bd-name { font-size: 15px; font-weight: 600; color: #111827; }
.bd-right { display: flex; align-items: center; gap: 10px; }
.bd-val { font-size: 16px; font-weight: 700; }
.bd-bar-bg { height: 9px; background: #ECEEF3; border-radius: 99px; overflow: hidden; margin-bottom: 8px; }
.bd-bar { height: 100%; border-radius: 99px; }
.match-status {
    display: inline-flex; align-items: center; gap: 5px;
    font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 6px;
}
.ms-strong { background: #EDFAF3; color: #1A7A52; }
.ms-partial { background: #EEF3FC; color: #1251A3; }
.ms-gap { background: #FEF3E8; color: #C05621; }
.bd-explain { font-size: 13px; color: #6B7280; line-height: 1.65; }

/* ── MATCH SUMMARY ── */
.match-summary {
    background: #EEF3FC; border-left: 4px solid #1251A3;
    border-radius: 0 12px 12px 0; padding: 18px 20px; margin: 28px 0;
}
.ms-title { font-size: 12px; font-weight: 700; color: #1251A3; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
.ms-text { font-size: 14px; color: #1F2937; line-height: 1.8; }

/* streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stButton > button {
    font-family: 'Sora', sans-serif !important;
    font-size: 14px !important; font-weight: 600 !important;
    border-radius: 10px !important; padding: 12px 20px !important;
    width: 100% !important; transition: all 0.15s !important;
}
div[data-testid="stProgress"] > div {
    background: #ECEEF3 !important; height: 9px !important; border-radius: 99px !important;
}
div[data-testid="stProgress"] > div > div { border-radius: 99px !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
def ms(level, explain):
    cls  = {"Strong":"ms-strong","Partial":"ms-partial","Gap":"ms-gap"}[level]
    icon = {"Strong":"&#10003;","Partial":"&#8776;","Gap":"&#33;"}[level]
    return {"level":level,"cls":cls,"icon":icon,"explain":explain}

JOBS = [
    {
        "id":0,"pct":91,"pct_color":"#1251A3",
        "title":"Director of Interventional Cardiology",
        "org":"UCSF Medical Center","location":"San Francisco, CA",
        "comp":"$480,000 to $520,000 per year",
        "type":"Full-time · Academic Medical Center",
        "initials":"UC","bg":"#003366","fg":"white",
        "tags":[("Interventional Cardiology","blue"),("Academic","blue"),("Research","green"),("West Coast","gray")],
        "reason":"Matches 5 of your 6 stated preferences",
        "scores":[
            ("Specialty fit",98,"#1251A3",ms("Strong","Your interventional cardiology subspecialty is an exact match for this role. No scope adjustment required.")),
            ("Compensation",92,"#1251A3",ms("Strong","The offer range of $480k to $520k exceeds your stated target. You are positioned in the upper half of their band.")),
            ("Location",95,"#1251A3",ms("Strong","This position is in San Francisco, your first-choice metro. No relocation required.")),
            ("Setting type",90,"#1251A3",ms("Strong","UCSF is a leading academic medical center with active research programs, matching your stated preference.")),
            ("Employer reputation",88,"#2E7D9E",ms("Strong","Rated 4.4 out of 5.0 by 62 physicians. Scores are particularly high for research support and collegial culture.")),
            ("Recruiter responsiveness",85,"#2E7D9E",ms("Partial","This recruiter typically responds within 24 hours. Engagement quality is above average based on platform history.")),
        ],
        "summary":"This position aligns with your core clinical focus, compensation expectations, and geographic preference. UCSF's reputation for academic medicine makes it a strong long-term fit based on the career goals in your profile.",
    },
    {
        "id":1,"pct":81,"pct_color":"#1251A3",
        "title":"Attending Cardiologist",
        "org":"Stanford Health","location":"Palo Alto, CA",
        "comp":"$460,000 to $490,000 per year",
        "type":"Full-time · Academic Health System",
        "initials":"SH","bg":"#8C1515","fg":"white",
        "tags":[("Cardiology","blue"),("Academic","blue"),("Research","green"),("Bay Area","gray")],
        "reason":"Highest employer rating in this specialty",
        "scores":[
            ("Specialty fit",85,"#1251A3",ms("Partial","Listed as general cardiology with interventional opportunities. Partial scope match but the primary focus is broader than your subspecialty.")),
            ("Compensation",82,"#2E7D9E",ms("Partial","Median offer here is approximately $472k, slightly below your stated target. Negotiation room exists based on your experience level.")),
            ("Location",88,"#1251A3",ms("Strong","Palo Alto is 35 miles from San Francisco and falls within the Bay Area region you have indicated as acceptable.")),
            ("Setting type",90,"#1251A3",ms("Strong","Stanford has a well-established research infrastructure and strong academic culture aligned with your profile preferences.")),
            ("Employer reputation",94,"#1251A3",ms("Strong","Rated 4.7 out of 5.0, the highest employer rating among cardiology positions in this region. High satisfaction scores for mentorship and work-life balance.")),
            ("Recruiter responsiveness",76,"#2E7D9E",ms("Partial","Average reply time is approximately 48 hours. Response rate is above average for this institution type.")),
        ],
        "summary":"Stanford offers the strongest employer reputation in your specialty with a research environment that fits your academic interest. The primary considerations are a partial specialty scope mismatch and compensation that may require negotiation.",
    },
    {
        "id":2,"pct":70,"pct_color":"#D97706",
        "title":"Cardiology Hospitalist",
        "org":"Kaiser Permanente","location":"Oakland, CA",
        "comp":"$390,000 to $420,000 per year",
        "type":"Full-time · Integrated Health System",
        "initials":"KP","bg":"#003865","fg":"white",
        "tags":[("Cardiology","blue"),("Hospitalist","gray"),("Oakland","gray")],
        "reason":"Strong location match with compensation below your target",
        "scores":[
            ("Specialty fit",78,"#2E7D9E",ms("Partial","This is a hospitalist role with general cardiology scope. Interventional procedures are not part of this position, which represents a meaningful clinical scope reduction.")),
            ("Compensation",58,"#D97706",ms("Gap","The compensation range falls approximately $55,000 below your stated floor. This gap is unlikely to be bridged through negotiation given Kaiser's standardized pay structure.")),
            ("Location",90,"#1251A3",ms("Strong","Oakland is directly adjacent to San Francisco and offers an easy commute. This is your strongest geographic match across all three results.")),
            ("Setting type",68,"#2E7D9E",ms("Partial","Kaiser operates as an integrated health system, not an academic institution. Research and teaching opportunities are limited in this role type.")),
            ("Employer reputation",80,"#2E7D9E",ms("Partial","Rated 4.0 out of 5.0 from 44 verified reviews. Physicians note strong administrative support but limited academic development.")),
            ("Recruiter responsiveness",72,"#2E7D9E",ms("Partial","Average reply time is approximately 72 hours. Response consistency is moderate based on platform history.")),
        ],
        "summary":"Location is the clearest strength here, but two significant gaps exist: compensation falls well below your target and the clinical scope is narrower than your subspecialty training. Consider this position only if schedule predictability outweighs compensation and academic goals.",
    },
]

CANDIDATES = [
    {
        "id":0,"pct":91,"pct_color":"#1251A3",
        "name":"Dr. Sam Smith, MD",
        "specialty":"Interventional Cardiology",
        "location":"San Francisco, CA",
        "status":"Passive, open to opportunities",
        "comp":"Target $450,000 or above",
        "outreach":"new","outreach_label":"Not yet contacted",
        "initials":"SS","bg":"#1a4a6b","fg":"white",
        "tags":[("Interventional Cardiology","blue"),("Academic preferred","blue"),("West Coast","gray"),("$450k+","green")],
        "reason":"Direct subspecialty match with full location and compensation alignment",
        "scores":[
            ("Specialty match",98,"#1251A3",ms("Strong","Dr. Smith holds an active interventional cardiology subspecialty, an exact clinical match for your open role. No scope adjustment required.")),
            ("Compensation fit",90,"#1251A3",ms("Strong","Stated target is $450k or above. Your offer range of $480k to $520k falls comfortably within what this candidate would consider.")),
            ("Location fit",95,"#1251A3",ms("Strong","Dr. Smith is currently based in San Francisco and has indicated no interest in relocation, eliminating one of the most common friction points in physician recruitment.")),
            ("Setting fit",92,"#1251A3",ms("Strong","Profile indicates a strong preference for academic medical centers. UCSF aligns directly with this stated career priority.")),
            ("Platform engagement",88,"#2E7D9E",ms("Strong","Profile was updated 3 weeks ago with recent search activity. Engagement patterns suggest this candidate is actively evaluating options despite passive status.")),
            ("Outreach receptivity",80,"#2E7D9E",ms("Partial","Responded to 2 of 3 outreach attempts in the past 6 months. Response probability is above average for passive candidates in this specialty.")),
        ],
        "summary":"Dr. Smith represents your highest-confidence match. Subspecialty, location, compensation, and setting preferences align across all primary dimensions. Recent platform activity suggests an active evaluation window, making this the optimal time for outreach.",
    },
    {
        "id":1,"pct":83,"pct_color":"#1251A3",
        "name":"Dr. Priya Nair, MD",
        "specialty":"Interventional Cardiology",
        "location":"Seattle, WA, open to Bay Area",
        "status":"Active, currently interviewing",
        "comp":"Target $440,000 or above",
        "outreach":"new","outreach_label":"Not yet contacted",
        "initials":"PN","bg":"#2d5a3d","fg":"white",
        "tags":[("Interventional Cardiology","blue"),("Academic","blue"),("Open to relocation","green"),("$440k+","green")],
        "reason":"Strong specialty fit, actively seeking with high response rate",
        "scores":[
            ("Specialty match",95,"#1251A3",ms("Strong","Direct interventional cardiology subspecialty match. Clinical scope and training level are aligned with the requirements of your open role.")),
            ("Compensation fit",85,"#1251A3",ms("Strong","Stated target of $440k or above is within your offer range, with approximately $40k to $80k of room above her floor.")),
            ("Location fit",72,"#2E7D9E",ms("Partial","Currently based in Seattle. Dr. Nair has explicitly flagged Bay Area as an acceptable relocation destination. Relocation support may increase conversion probability.")),
            ("Setting fit",88,"#1251A3",ms("Strong","Has expressed a strong preference for academic health systems throughout her career history, consistent with UCSF's profile.")),
            ("Platform engagement",94,"#1251A3",ms("Strong","Applied to 4 positions in the past 30 days. This candidate is in active job-search mode, which increases likelihood of a timely response.")),
            ("Outreach receptivity",86,"#1251A3",ms("Strong","Responded to all 3 outreach attempts in the past 3 months, one of the highest response rates among active candidates in this specialty.")),
        ],
        "summary":"Dr. Nair is a strong active candidate with direct subspecialty alignment and a high response rate. The only meaningful gap is location, which she has indicated is not a barrier. Recommend initiating outreach this week given her active search status.",
    },
    {
        "id":2,"pct":71,"pct_color":"#D97706",
        "name":"Dr. Marcus Lee, MD",
        "specialty":"General Cardiology",
        "location":"Los Angeles, CA, open to NorCal",
        "status":"Passive, not actively searching",
        "comp":"Target $430,000 or above",
        "outreach":"contacted","outreach_label":"Outreach sent 6 weeks ago, no response",
        "initials":"ML","bg":"#5a3d1a","fg":"white",
        "tags":[("General Cardiology","gray"),("Some interventional","gray"),("LA-based","gray"),("$430k+","green")],
        "reason":"Compensation match with subspecialty gap and low platform engagement",
        "scores":[
            ("Specialty match",72,"#D97706",ms("Partial","Dr. Lee is a general cardiologist with some interventional experience. Additional training or supervision may be required for full interventional duties.")),
            ("Compensation fit",88,"#1251A3",ms("Strong","Compensation expectations of $430k to $460k fall within your offer range. There is meaningful budget flexibility if this candidate is prioritized.")),
            ("Location fit",80,"#2E7D9E",ms("Partial","Currently based in Los Angeles but has indicated openness to Northern California. Relocation would be required and may be a friction point.")),
            ("Setting fit",78,"#2E7D9E",ms("Partial","Career history includes both community and academic positions. Setting preference is not as clearly defined as your top-ranked candidates.")),
            ("Platform engagement",60,"#D97706",ms("Gap","Last active on the platform 6 weeks ago. Low recent engagement suggests this candidate is not currently evaluating opportunities.")),
            ("Outreach receptivity",55,"#D97706",ms("Gap","Historically responded to 1 of 4 outreach attempts. Previous outreach from your organization 6 weeks ago did not receive a reply.")),
        ],
        "summary":"Dr. Lee offers compensation flexibility and geographic openness but presents two meaningful gaps: subspecialty alignment is partial and platform engagement is currently low. Prior outreach from your team went unanswered. Recommended as a backup once primary outreach is complete.",
    },
]

def tag_cls(t):
    return {"blue":"tag tag-blue","green":"tag tag-green","gray":"tag tag-gray"}.get(t,"tag tag-gray")

# ─── SESSION STATE ────────────────────────────────────────────────────────────
for k,v in [("mode","physician"),("sel_job",0),("sel_cand",0)]:
    if k not in st.session_state:
        st.session_state[k] = v

mode = st.session_state.mode

# ─── NAV ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav">
  <div class="logo-wrap">
    <div class="logo-mark">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="8.5" r="4" stroke="white" stroke-width="2.2"/>
        <path d="M4 21c0-4.418 3.582-8 8-8s8 3.582 8 8" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M17 5l3 3-3 3" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <span class="logo-text">PracticeLink</span>
  </div>
  <div class="nav-right">
    <span class="nav-item-active">Job Matching</span>
    <span class="nav-item">My Profile</span>
    <span class="nav-item">Saved</span>
    <span class="nav-btn">Post a Job</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── TAB TOGGLE ──────────────────────────────────────────────────────────────
st.markdown('<div class="tab-bar-wrap">', unsafe_allow_html=True)
tc1, tc2 = st.columns(2)
with tc1:
    if st.button(
        "Physician   —   Find Jobs",
        key="tab_physician",
        use_container_width=True,
        type="primary" if mode == "physician" else "secondary",
    ):
        st.session_state.mode = "physician"
        st.session_state.sel_job = st.session_state.get("sel_job", 0)
        st.rerun()
with tc2:
    if st.button(
        "Recruiter   —   Find Candidates",
        key="tab_recruiter",
        use_container_width=True,
        type="primary" if mode == "recruiter" else "secondary",
    ):
        st.session_state.mode = "recruiter"
        st.session_state.sel_cand = st.session_state.get("sel_cand", 0)
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

mode = st.session_state.mode

# ─── MAIN LAYOUT ─────────────────────────────────────────────────────────────
items   = JOBS if mode=="physician" else CANDIDATES
sel_key = "sel_job" if mode=="physician" else "sel_cand"
header  = "Recommended Positions" if mode=="physician" else "Matching Candidates"
count   = "3 of 47 matched positions" if mode=="physician" else "3 of 12,400 physicians in database"

left, right = st.columns([1.05, 1], gap="large")

# ─── LEFT ────────────────────────────────────────────────────────────────────
with left:
    st.markdown(f"""
    <div class="list-header">
      <span class="list-title">{header}</span>
      <span class="list-sub">{count}</span>
    </div>
    """, unsafe_allow_html=True)

    if mode == "physician":
        st.markdown("""
        <div class="pcomp">
          <div class="pcomp-title">Complete your profile to improve match accuracy</div>
          <div class="pcomp-text">Adding your preferred schedule type and practice setting will help us surface more relevant positions. Your profile is 72% complete.</div>
          <div class="pcomp-bar-bg"><div class="pcomp-bar"></div></div>
        </div>
        """, unsafe_allow_html=True)

    sel = st.session_state[sel_key]

    for item in items:
        is_sel = sel == item["id"]
        card_cls = "rcard rcard-active" if is_sel else "rcard"
        c = item["pct_color"]
        tags_html = "".join(f'<span class="{tag_cls(t[1])}">{t[0]}</span>' for t in item["tags"])

        if mode == "physician":
            l1,l2 = item["title"], item["org"]
            l3 = f"{item['location']}  ·  {item['type']}"
            l4 = item["comp"]
        else:
            l1,l2 = item["name"], item["specialty"]
            l3 = f"{item['location']}  ·  {item['status']}"
            l4 = item["comp"]

        st.markdown(f"""
        <div class="{card_cls}">
          <div class="rcard-badge">
            <div class="rb-pct" style="color:{c}">{item['pct']}%</div>
            <div class="rb-lbl">AI Match</div>
          </div>
          <div class="rcard-top">
            <div class="rcard-logo" style="background:{item['bg']};color:{item['fg']}">{item['initials']}</div>
            <div class="rcard-info">
              <p class="rcard-title">{l1}</p>
              <p class="rcard-org">{l2}</p>
              <p class="rcard-meta">{l3}</p>
              <p class="rcard-meta" style="font-weight:600;color:#1A7A52;margin-top:3px">{l4}</p>
            </div>
          </div>
          <div class="tag-row">{tags_html}</div>
          <div class="rcard-reason"><div class="rdot"></div>{item['reason']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("View details", key=f"btn_{mode}_{item['id']}"):
            st.session_state[sel_key] = item["id"]
            st.rerun()

# ─── RIGHT ───────────────────────────────────────────────────────────────────
with right:
    item = items[st.session_state[sel_key]]
    c    = item["pct_color"]

    if mode == "physician":
        d_title,d_org = item["title"],item["org"]
        d_loc,d_type  = item["location"],item["type"]
        d_comp        = item["comp"]
        b1,b2         = "Apply Now","Save Job"
    else:
        d_title,d_org = item["name"],item["specialty"]
        d_loc,d_type  = item["location"],item["status"]
        d_comp        = item["comp"]
        b1,b2         = "Send Outreach","Save to Shortlist"

    # header block
    st.markdown(f"""
    <div class="dcard">
      <div class="dcard-logo" style="background:{item['bg']};color:{item['fg']}">{item['initials']}</div>
      <p class="dcard-title">{d_title}</p>
      <p class="dcard-org">{d_org}</p>
      <p class="dcard-meta">{d_loc}  ·  {d_type}</p>
      <p class="dcard-comp">{d_comp}</p>
    """, unsafe_allow_html=True)

    # outreach pill — recruiter only, rendered separately so HTML works
    if mode == "recruiter":
        if item["outreach"] == "new":
            st.markdown(f"""
            <div class="status-pill status-new">
              <div class="status-dot" style="background:#1A7A52"></div>
              {item['outreach_label']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="status-pill status-contacted">
              <div class="status-dot" style="background:#C05621"></div>
              {item['outreach_label']}
            </div>
            """, unsafe_allow_html=True)

    # match ring
    st.markdown(f"""
      <div class="mring">
        <div>
          <div class="mring-pct" style="color:{c}">{item['pct']}%</div>
          <div class="mring-lbl">Overall Match</div>
        </div>
        <div class="mring-right">Analyzed across<br>6 profile dimensions</div>
      </div>
      <div class="bd-title">Match Analysis</div>
    """, unsafe_allow_html=True)

    # score breakdown
    for label, val, bar_color, ms_data in item["scores"]:
        st.markdown(f"""
        <div class="bd-item">
          <div class="bd-top">
            <span class="bd-name">{label}</span>
            <div class="bd-right">
              <span class="match-status {ms_data['cls']}">{ms_data['icon']} {ms_data['level']}</span>
              <span class="bd-val" style="color:{bar_color}">{val}%</span>
            </div>
          </div>
          <div class="bd-bar-bg">
            <div class="bd-bar" style="width:{val}%;background:{bar_color}"></div>
          </div>
          <div class="bd-explain">{ms_data['explain']}</div>
        </div>
        """, unsafe_allow_html=True)

    # summary + close dcard
    st.markdown(f"""
      <div class="match-summary">
        <div class="ms-title">Match Summary</div>
        <div class="ms-text">{item['summary']}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.button(b1, key="d_b1", type="primary")
    with col_b:
        st.button(b2, key="d_b2")

st.markdown("""
<div style="text-align:center;font-size:12px;color:#B0B8CC;padding:48px 0 24px;">
  PracticeLink &nbsp;·&nbsp; JHU IT Consulting Lab &nbsp;·&nbsp; AI Matching Demo
</div>
""", unsafe_allow_html=True)

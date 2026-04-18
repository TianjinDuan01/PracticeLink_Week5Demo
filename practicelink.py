import streamlit as st

st.set_page_config(
    page_title="PracticeLink AI — AI-Driven Physician Matching & Decision Assistant",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.main { background: #F8FAFC; }
.block-container { padding: 2rem 2.5rem 2rem 2.5rem; max-width: 1200px; }

/* ── Topbar ── */
.topbar {
    display: flex; align-items: center; gap: 14px;
    background: #1B2A4A; border-radius: 12px;
    padding: 1rem 1.5rem; margin-bottom: 1.5rem;
}
.topbar-logo {
    width: 38px; height: 38px; border-radius: 8px;
    background: #0F6E56; display: flex; align-items: center;
    justify-content: center; font-weight: 600; color: white;
    font-size: 14px; flex-shrink: 0;
}
.topbar-title { color: white; font-size: 17px; font-weight: 600; margin: 0; }
.topbar-sub { color: #7FB3D3; font-size: 12px; margin: 0; }
.sf-badge {
    margin-left: auto; display: flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.08); border-radius: 20px;
    padding: 4px 12px;
}
.sf-dot { width: 8px; height: 8px; border-radius: 50%; background: #0070D2; display: inline-block; }
.sf-text { color: #94A3B8; font-size: 11px; }

/* ── Flow steps ── */
.flow-container {
    display: flex; align-items: stretch; gap: 0;
    margin-bottom: 1.5rem;
}
.flow-card {
    flex: 1; background: white; border: 0.5px solid #E2E8F0;
    border-radius: 10px; padding: 1rem 1.1rem;
}
.flow-arrow { display: flex; align-items: center; padding: 0 8px; color: #94A3B8; font-size: 20px; }
.flow-num {
    font-size: 10px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; margin-bottom: 5px;
}
.flow-title { font-size: 13px; font-weight: 600; color: #1E293B; margin-bottom: 3px; }
.flow-desc { font-size: 11px; color: #64748B; line-height: 1.5; }

/* ── Profile section ── */
.profile-card {
    background: white; border: 0.5px solid #E2E8F0;
    border-radius: 12px; padding: 1.2rem 1.3rem; margin-bottom: 1rem;
}
.avatar-circle {
    width: 44px; height: 44px; border-radius: 50%;
    background: #E1F5EE; display: inline-flex; align-items: center;
    justify-content: center; font-weight: 600; font-size: 14px;
    color: #085041; vertical-align: middle; margin-right: 12px;
}
.profile-name { font-size: 15px; font-weight: 600; color: #1E293B; margin: 0; }
.profile-sub { font-size: 12px; color: #64748B; margin: 0; }
.tag {
    display: inline-block; font-size: 11px; padding: 3px 10px;
    border-radius: 99px; margin: 3px 3px 3px 0;
}
.tag-teal { background: #E1F5EE; color: #085041; border: 0.5px solid #5DCAA5; }
.tag-gray { background: #F1F5F9; color: #475569; border: 0.5px solid #CBD5E1; }

/* ── Job cards ── */
.job-card {
    background: white; border: 0.5px solid #E2E8F0;
    border-radius: 10px; padding: 0.9rem 1rem;
    margin-bottom: 8px; cursor: pointer;
    transition: border-color 0.15s;
}
.job-card-selected { border: 1.5px solid #1D9E75 !important; background: #FAFFFE; }
.job-card:hover { border-color: #94A3B8; }
.job-title { font-size: 13px; font-weight: 600; color: #1E293B; margin-bottom: 2px; }
.job-org { font-size: 11px; color: #64748B; margin-bottom: 6px; }
.job-reason { font-size: 11px; color: #0F6E56; background: #E1F5EE; border-radius: 5px; padding: 3px 8px; display: inline-block; }
.match-big { font-size: 26px; font-weight: 700; }

/* ── Detail panel ── */
.detail-card {
    background: white; border: 0.5px solid #E2E8F0;
    border-radius: 12px; padding: 1.3rem 1.4rem; height: 100%;
}
.detail-title { font-size: 15px; font-weight: 600; color: #1E293B; margin-bottom: 3px; }
.detail-sub { font-size: 12px; color: #64748B; margin-bottom: 1.1rem; }
.score-label { font-size: 11px; color: #64748B; }
.score-val { font-size: 12px; font-weight: 600; color: #1E293B; text-align: right; }
.ai-reason {
    font-size: 12px; color: #475569; line-height: 1.7;
    background: #F0FFF8; border-left: 3px solid #1D9E75;
    border-radius: 0 6px 6px 0; padding: 0.75rem 1rem;
    margin-top: 1rem;
}
.ai-reason strong { color: #534AB7; }

/* ── Section labels ── */
.section-label {
    font-size: 11px; font-weight: 600; color: #94A3B8;
    letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ── Job data ──
JOBS = [
    {
        "id": 0,
        "pct": 91,
        "title": "Dir. of Interventional Cardiology",
        "org": "UCSF Medical Center · San Francisco, CA",
        "comp": "$480k – $520k · Full-time",
        "reason": "Matches 5 of your top preferences",
        "scores": {
            "Specialty fit": 98,
            "Location": 95,
            "Compensation": 90,
            "Setting type": 92,
            "Employer rating": 88,
        },
        "ai_why": "This role is an exact specialty match (interventional cardiology) at an academic medical center — aligning with your preference for research-adjacent work. Compensation is within your stated target range, and 3 physicians with similar profiles accepted offers here in the last 18 months.",
        "color": "#1D9E75",
    },
    {
        "id": 1,
        "pct": 81,
        "title": "Attending Cardiologist",
        "org": "Stanford Health · Palo Alto, CA",
        "comp": "$460k – $490k · Full-time",
        "reason": "Strong comp + academic research fit",
        "scores": {
            "Specialty fit": 85,
            "Location": 90,
            "Compensation": 82,
            "Setting type": 88,
            "Employer rating": 92,
        },
        "ai_why": "Stanford's research program is a strong match for your academic interest. Compensation is slightly below your top range, but the employer rating and placement success rate are both high. Location is 35 miles from SF.",
        "color": "#1D9E75",
    },
    {
        "id": 2,
        "pct": 70,
        "title": "Cardiology Hospitalist",
        "org": "Kaiser Permanente · Oakland, CA",
        "comp": "$390k – $420k · Full-time",
        "reason": "Location match, comp below target",
        "scores": {
            "Specialty fit": 78,
            "Location": 88,
            "Compensation": 62,
            "Setting type": 70,
            "Employer rating": 80,
        },
        "ai_why": "Location is a strong match, but compensation is below your $450k target. This role is non-academic, which may not align with your stated preference. Consider if stability and work-life balance tradeoffs are priorities for you.",
        "color": "#5DCAA5",
    },
]

def pct_color(p):
    if p >= 85: return "#1D9E75"
    if p >= 75: return "#5DCAA5"
    return "#F59E0B"

# ── Session state ──
if "selected" not in st.session_state:
    st.session_state.selected = 0

# ── Topbar ──
st.markdown("""
<div class="topbar">
  <div class="topbar-logo">PL</div>
  <div>
    <p class="topbar-title">PracticeLink AI — Job Matching</p>
    <p class="topbar-sub">AI-Driven Job Matching & Decision Assistant</p>
  </div>
  <div class="sf-badge">
    <span class="sf-dot"></span>
    <span class="sf-text">Salesforce synced · 2h ago</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Flow steps ──
cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
steps = [
    ("#0F6E56", "Step 1 — User", "Physician profile", "Specialty, location, compensation preferences"),
    ("#185FA5", "Step 2 — AI model", "AI Match engine", "Preference-based scoring (location, comp, specialty), Historical placement learning, Explainable ranking logic"),
    ("#854F0B", "Step 3 — Salesforce", "Live job data", "Openings, placement history, employer ratings"),
    ("#534AB7", "Step 4 — Output", "Ranked results", 'Match % + "why this fits you" explanation'),
]
idxs = [0, 2, 4, 6]
for i, (color, lbl, title, desc) in enumerate(steps):
    with cols[idxs[i]]:
        st.markdown(f"""
        <div class="flow-card">
          <div class="flow-num" style="color:{color}">{lbl}</div>
          <div class="flow-title">{title}</div>
          <div class="flow-desc">{desc}</div>
        </div>""", unsafe_allow_html=True)
    if i < 3:
        with cols[idxs[i]+1]:
            st.markdown('<div class="flow-arrow">→</div>', unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:0.5px solid #E2E8F0;margin:1.2rem 0'>", unsafe_allow_html=True)

# ── Main two-column layout ──
left, right = st.columns([1, 1], gap="large")

with left:
    # Physician profile
    st.markdown("""
    <div class="profile-card">
      <div style="display:flex;align-items:center;margin-bottom:10px">
        <div class="avatar-circle">DR</div>
        <div>
          <p class="profile-name">Dr. Sam Smith</p>
          <p class="profile-sub">Cardiology · San Francisco, CA</p>
        </div>
      </div>
      <div>
        <span class="tag tag-teal">Cardiology</span>
        <span class="tag tag-teal">Interventional</span>
        <span class="tag tag-gray">Academic setting</span>
        <span class="tag tag-gray">$450k+ comp</span>
        <span class="tag tag-gray">West Coast</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Top matches &nbsp;·&nbsp; 3 of 47 results</div>', unsafe_allow_html=True)

    for job in JOBS:
        selected = st.session_state.selected == job["id"]
        card_class = "job-card job-card-selected" if selected else "job-card"
        c_pct = pct_color(job["pct"])

        col_a, col_b = st.columns([0.18, 0.82])
        with col_a:
            st.markdown(f"""
            <div style="text-align:center;padding-top:6px">
              <div class="match-big" style="color:{c_pct}">{job['pct']}%</div>
              <div style="font-size:10px;color:#94A3B8">match</div>
            </div>""", unsafe_allow_html=True)
        with col_b:
            st.markdown(f"""
            <div class="{card_class}">
              <div class="job-title">{job['title']}</div>
              <div class="job-org">{job['org']}</div>
              <span class="job-reason">{job['reason']}</span>
            </div>""", unsafe_allow_html=True)
            if st.button(f"Select", key=f"btn_{job['id']}", use_container_width=True):
                st.session_state.selected = job["id"]
                st.rerun()

with right:
    job = JOBS[st.session_state.selected]
    c_pct = pct_color(job["pct"])

    st.markdown(f"""
    <div class="detail-card">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem">
        <div>
          <div class="detail-title">{job['title']}</div>
          <div class="detail-sub">{job['org']}</div>
          <div class="detail-sub">{job['comp']}</div>
        </div>
        <div style="text-align:center">
          <div style="font-size:36px;font-weight:700;color:{c_pct};line-height:1">{job['pct']}%</div>
          <div style="font-size:11px;color:#94A3B8">overall match</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Match breakdown**")
    for label, val in job["scores"].items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(val / 100, text=label)
        with col2:
            st.markdown(f"<div style='text-align:right;font-size:13px;font-weight:600;padding-top:4px'>{val}%</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="ai-reason">
      <strong>Why this fits you:</strong><br>{job['ai_why']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        st.button("View full details", type="primary", use_container_width=True)
    with col_btn2:
        st.button("Save to list", use_container_width=True)
    with col_btn3:
        st.button("Not interested", use_container_width=True)

st.markdown("<hr style='border:none;border-top:0.5px solid #E2E8F0;margin:1.5rem 0'>", unsafe_allow_html=True)

bv_col, kc_col = st.columns(2, gap="large")

with bv_col:
    st.markdown("""
    <div style="background:white;border:0.5px solid #E2E8F0;border-radius:12px;padding:1.1rem 1.25rem;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.9rem;">
        <div style="width:28px;height:28px;border-radius:8px;background:#EFF6FF;"></div>
        <span style="font-size:13px;font-weight:600;color:#1B2A4A;">Expected Impact</span>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#185FA5;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Better physician-job fit</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">Preference-based scoring helps reduce mismatches</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#185FA5;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Higher application conversion</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">More relevant recommendations can increase engagement</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#185FA5;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Less recruiter manual review</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">Shortlisting support can reduce time spent on initial screening</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with kc_col:
    st.markdown("""
    <div style="background:white;border:0.5px solid #E2E8F0;border-radius:12px;padding:1.1rem 1.25rem;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.9rem;">
        <div style="width:28px;height:28px;border-radius:8px;background:#FFF7ED;"></div>
        <span style="font-size:13px;font-weight:600;color:#1B2A4A;">Implementation Notes</span>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#D4610C;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Salesforce data sync</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">Requires reliable API connections and consistent job data</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#D4610C;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Privacy and compliance</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">Candidate data handling must follow internal policy and healthcare requirements</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:10px;">
          <div style="width:6px;height:6px;border-radius:50%;background:#D4610C;margin-top:6px;flex-shrink:0;"></div>
          <div>
            <div style="font-size:12.5px;font-weight:600;color:#1E293B;">Explainable recommendations</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">Users should understand why a role is ranked highly</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;font-size:11px;color:#94A3B8;padding:1rem 0">
  PracticeLink AI Matching - JHU IT Consulting Lab
</div>
""", unsafe_allow_html=True)

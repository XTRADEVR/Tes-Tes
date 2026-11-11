import streamlit as st

st.set_page_config(page_title="Social Hub — Premium", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")

APPS = [
    {"name": "Instagram", "category": "FOTO & VIDEO", "desc": "Bagikan momen, Stories, dan Reels.", "url": "https://www.instagram.com/", "mark": "◎", "tone": "ig"},
    {"name": "TikTok", "category": "VIDEO PENDEK", "desc": "Temukan video dan tren terbaru.", "url": "https://www.tiktok.com/", "mark": "♪", "tone": "tt"},
    {"name": "YouTube", "category": "VIDEO & LIVE", "desc": "Tonton, unggah, dan siarkan video.", "url": "https://www.youtube.com/", "mark": "▶", "tone": "yt"},
    {"name": "Facebook", "category": "KOMUNITAS", "desc": "Tetap terhubung dengan teman dan grup.", "url": "https://www.facebook.com/", "mark": "f", "tone": "fb"},
    {"name": "X", "category": "PERCAKAPAN", "desc": "Ikuti kabar dan percakapan secara real-time.", "url": "https://x.com/", "mark": "𝕏", "tone": "x"},
    {"name": "LinkedIn", "category": "PROFESIONAL", "desc": "Bangun koneksi dan kembangkan karier.", "url": "https://www.linkedin.com/", "mark": "in", "tone": "li"},
    {"name": "WhatsApp", "category": "PESAN", "desc": "Kirim pesan dan lakukan panggilan.", "url": "https://web.whatsapp.com/", "mark": "◔", "tone": "wa"},
    {"name": "Telegram", "category": "PESAN & CHANNEL", "desc": "Chat, ikuti channel, dan berbagi file.", "url": "https://web.telegram.org/", "mark": "➤", "tone": "tg"},
    {"name": "Pinterest", "category": "INSPIRASI", "desc": "Simpan ide dan temukan inspirasi baru.", "url": "https://www.pinterest.com/", "mark": "P", "tone": "pin"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#f5f4f8; --muted:#92909f; --panel:#14141b; --line:rgba(255,255,255,.085); }
.stApp { background: radial-gradient(ellipse at 15% -10%, rgba(118,77,255,.20), transparent 34%), radial-gradient(ellipse at 95% 12%, rgba(48,186,185,.10), transparent 26%), #0b0b10; color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1180px; padding-top:2.2rem; padding-bottom:3rem; }
header, footer {visibility:hidden;}
.brand {display:flex;align-items:center;gap:11px;color:#f5f4f8;font:800 14px Manrope,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.brand-mark {width:33px;height:33px;border-radius:11px;background:linear-gradient(145deg,#9b7aff,#6746df);display:grid;place-items:center;color:white;font-size:19px;box-shadow:0 7px 24px #7655ee55}
.topline {display:flex;justify-content:space-between;align-items:center;padding-bottom:25px;border-bottom:1px solid var(--line)}
.pill {border:1px solid #a18bff44;background:#8b70ff14;border-radius:30px;color:#c8bbff;padding:7px 12px;font-size:11px;letter-spacing:.1em;font-weight:700}
.hero {padding:53px 0 31px;max-width:730px}
.eyebrow {color:#ad98ff;font-size:11px;letter-spacing:.18em;font-weight:700;margin-bottom:14px}
h1 {font:800 clamp(36px,5vw,58px)/1.08 Manrope,sans-serif !important;letter-spacing:-.045em !important;color:#fff !important;margin:0 0 17px !important}
.sub {font-size:16px;color:#a6a4b1;line-height:1.7;max-width:620px}
.section-head {display:flex;justify-content:space-between;align-items:end;margin:24px 0 17px}
.section-head h3 {font:700 18px Manrope,sans-serif;color:#f4f2fa;margin:0}
.section-head span {font-size:12px;color:#858391}
.grid {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:15px}
.card {position:relative;display:block;text-decoration:none !important;color:inherit !important;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.018));border:1px solid var(--line);border-radius:19px;padding:19px 19px 17px;min-height:160px;transition:.22s ease;overflow:hidden}
.card:hover {transform:translateY(-4px);border-color:rgba(164,143,255,.42);background:linear-gradient(145deg,rgba(145,113,255,.11),rgba(255,255,255,.025));box-shadow:0 14px 40px #0005}
.cardtop {display:flex;justify-content:space-between;align-items:center;margin-bottom:17px}
.logo {width:42px;height:42px;border-radius:14px;display:grid;place-items:center;color:#fff;font:bold 21px Manrope,sans-serif;box-shadow:inset 0 1px 1px #ffffff33}
.logo.ig {background:linear-gradient(145deg,#ffc957,#f04477 52%,#7651da)} .logo.tt{background:#111;border:1px solid #333;text-shadow:2px 1px #ff356b,-2px -1px #44e5ea}
.logo.yt{background:#ff2638}.logo.fb{background:#1877f2;font-size:27px}.logo.x{background:#050505;border:1px solid #333}.logo.li{background:#0a66c2;font-size:19px}.logo.wa{background:#25c56a}.logo.tg{background:#30a9df}.logo.pin{background:#de2443}
.open {color:#8d8a99;font-size:16px}
.cat {font-size:9px;color:#9c98aa;font-weight:700;letter-spacing:.14em;margin-bottom:5px}
.title {font:700 17px Manrope,sans-serif;color:#f4f2f8;margin-bottom:5px}
.desc {font-size:12px;line-height:1.5;color:#9693a1}
.note {margin-top:24px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;color:#858391;font-size:12px;line-height:1.6}
.note b {color:#b6a7ff}
@media(max-width:760px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.hero{padding-top:38px}.sub{font-size:14px}}
@media(max-width:480px){.grid{grid-template-columns:1fr}.card{min-height:145px}.block-container{padding-left:1rem;padding-right:1rem}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="topline"><div class="brand"><div class="brand-mark">✦</div> SOCIAL <span style="color:#a28bff">HUB</span></div><div class="pill">✧ &nbsp; PREMIUM ACCESS</div></div>', unsafe_allow_html=True)
st.markdown('<div class="hero"><div class="eyebrow">RUANG DIGITAL ANDA</div><h1>Semua sosial media.<br>Dalam satu tempat.</h1><div class="sub">Akses platform favorit dengan cepat lewat satu halaman yang rapi, nyaman, dan siap menemani aktivitas digitalmu.</div></div>', unsafe_allow_html=True)
st.markdown('<div class="section-head"><h3>Jelajahi platform</h3><span>9 aplikasi pilihan</span></div>', unsafe_allow_html=True)

cards = []
for app in APPS:
    cards.append(f'''<a class="card" href="{app['url']}" target="_blank" rel="noopener noreferrer"><div class="cardtop"><div class="logo {app['tone']}">{app['mark']}</div><span class="open">↗</span></div><div class="cat">{app['category']}</div><div class="title">{app['name']}</div><div class="desc">{app['desc']}</div></a>''')
st.markdown('<div class="grid">' + ''.join(cards) + '</div>', unsafe_allow_html=True)
st.markdown('<div class="note"><b>Catatan:</b> Tombol akan membuka situs resmi platform di tab baru. Login, ketersediaan fitur, dan akses tetap mengikuti ketentuan masing-masing layanan.</div>', unsafe_allow_html=True)

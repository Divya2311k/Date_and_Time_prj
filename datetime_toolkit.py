import streamlit as st
from datetime import datetime, timedelta, date, time as dt_time
import time
import calendar
from zoneinfo import ZoneInfo

st.set_page_config(page_title="📅 Python Date & Time Toolkit", layout="wide")
st.title("📅 Python Date & Time Toolkit")

st.markdown("""
Explore Python's core date & time modules with live examples:

- 🧭 `datetime`
- 🕒 `time`
- 📆 `calendar`
- 🌍 `zoneinfo`
---
""")

# 1. ---------------- DATETIME MODULE --------------------
with st.expander("🧭 `datetime` Module"):
    st.subheader("Current Date & Time")
    now = datetime.now()
    st.write("**Now:**", now)
    st.write("**Formatted:**", now.strftime("%A, %d %B %Y %I:%M:%S %p"))

    st.subheader("Date Arithmetic")
    days = st.slider("Add/Subtract Days", -30, 30, 5)
    future = now + timedelta(days=days)
    st.write(f"{'Future' if days > 0 else 'Past'} Date:", future.date())

    st.subheader("Datetime Creation")
    y = st.number_input("Year", 1900, 2100, 2025)
    m = st.number_input("Month", 1, 12, 7)
    d = st.number_input("Day", 1, 31, 3)
    try:
        custom_date = datetime(year=int(y), month=int(m), day=int(d))
        st.success(f"Valid Date: {custom_date.strftime('%A, %d %B %Y')}")
    except:
        st.error("Invalid date!")

# 2. ---------------- TIME MODULE --------------------
with st.expander("🕒 `time` Module"):
    st.subheader("Time Module Functions")
    st.write("**Epoch Time (seconds since 1970):**", time.time())
    st.write("**Localtime (struct_time):**", time.localtime())
    st.write("**Formatted Time:**", time.strftime("%H:%M:%S", time.localtime()))

    st.subheader("Sleep Simulation")
    sleep_sec = st.slider("Sleep time (sec)", 0, 5, 2)
    if st.button("Run Sleep"):
        st.info(f"Sleeping for {sleep_sec} seconds...")
        time.sleep(sleep_sec)
        st.success("Done sleeping!")

# 3. ---------------- CALENDAR MODULE --------------------
with st.expander("📆 `calendar` Module"):
    st.subheader("Calendar View")
    year = st.slider("Select year", 2000, 2100, 2025)
    month = st.slider("Select month", 1, 12, 7)

    cal = calendar.TextCalendar()
    st.code(cal.formatmonth(year, month))

    st.subheader("Month Range")
    first_weekday, num_days = calendar.monthrange(year, month)
    st.write(f"**1st weekday**: {calendar.day_name[first_weekday]}")
    st.write(f"**Total days in month**: {num_days}")

    st.subheader("Leap Year Check")
    if calendar.isleap(year):
        st.success(f"{year} is a Leap Year ✅")
    else:
        st.warning(f"{year} is not a Leap Year ❌")

# 4. ---------------- ZONEINFO MODULE --------------------
with st.expander("🌍 `zoneinfo` Module"):
    st.subheader("Timezone Conversion")
    all_zones = ["UTC", "Asia/Kolkata", "America/New_York", "Europe/London", "Asia/Tokyo"]
    user_zone = st.selectbox("Select your timezone", all_zones, index=1)

    try:
        local_time = datetime.now(ZoneInfo(user_zone))
        st.write(f"**Current time in {user_zone}:**", local_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
    except Exception as e:
        st.error(f"Invalid timezone selected: {e}")

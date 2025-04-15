# -*- coding: utf-8 -*-
"""Streamlit 코드

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XwqxaNvy11oa2HAisVbpxfVmCoYtAvBD
"""

# 예시 Streamlit 코드
import streamlit as st
import pandas as pd

# 샘플 데이터
data = {
    'date': ['2025-04-01', '2025-04-02', '2025-04-03'],
    'campaign': ['Campaign A', 'Campaign B', 'Campaign C'],
    'impressions': [12000, 15000, 18000],
    'clicks': [300, 400, 500],
    'conversions': [30, 40, 50],
}

df = pd.DataFrame(data)

# Streamlit 앱 제목
st.title("광고 리포트 대시보드")

# 테이블 출력
st.write("광고 리포트")
st.dataframe(df)

# 광고 효과 분석 차트
st.write("광고 성과 차트")
st.bar_chart(df.set_index('date')['impressions'])

# 클릭률 및 전환율 계산
df['CTR'] = df['clicks'] / df['impressions'] * 100
df['conversion_rate'] = df['conversions'] / df['clicks'] * 100
st.write("클릭률 및 전환율")
st.dataframe(df[['date', 'CTR', 'conversion_rate']])
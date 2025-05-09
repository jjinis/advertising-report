# -*- coding: utf-8 -*-
"""streamlit code

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XwqxaNvy11oa2HAisVbpxfVmCoYtAvBD
"""

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

# 엑셀 파일로 저장
# Pandas의 `to_excel` 메서드를 사용하여 DataFrame을 엑셀로 변환
import io

# 엑셀 파일을 메모리 버퍼에 저장
excel_buffer = io.BytesIO()
df.to_excel(excel_buffer, index=False, sheet_name='광고 리포트')

# 메모리 버퍼의 포인터를 맨 처음으로 되돌리기
excel_buffer.seek(0)

# 다운로드 버튼을 생성하여 엑셀 파일을 다운로드할 수 있게 함
st.download_button(
    label="엑셀 파일로 다운로드",
    data=excel_buffer,
    file_name="광고_리포트.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
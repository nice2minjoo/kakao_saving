import streamlit as st
import pandas as pd

origin = 0 # 시작
week = 0 # 매주 입금
total = 0 # 총 필요 금액
member = []

st.set_page_config(page_title = "kakao saving")
st.title('카카오 26주 풍차돌리기')
st.write('이 앱은 카카오 26주 적금 풍차돌리기에 필요한 금액과 이자를 계산하기 위해 제작되었습니다.')

tab1, tab2 = st.tabs(["계산기","풍차돌리기란?"])

with tab1:
    with st.form("calculator"):
        str_money = st.selectbox("증액 금액 선택",["1,000원","2,000원","3,000원","5,000원","10,000원"])
        if str_money == "1,000원":
            money = 1000
        elif str_money == "2,000원":
            money = 2000
        elif str_money == "3,000원":
            money = 3000
        elif str_money == "5,000원":
            money = 5000
        elif str_money == "10,000원":
            money = 10000
            
        submit = st.form_submit_button("OK")
        
        if submit:
            with st.spinner("calculating..."):
                for i in range(1,27):
                    week += money
                    origin += week
                    member.append(origin) # max 26 pcs

                for i in range(0, len(member)):
                    total += member[i]

                beforeTax = int(total * 0.138363 / 100)
                afterTax = int(beforeTax * 0.846) # tax 15.4%
                
                df = pd.DataFrame(
                    {
                        "content" : ["총 필요 금액", "26주 후 매주 출금 금액", "세전 이자", "세후 이자"],
                        "result": [format(total,',d')+"원", format(member[len(member)-1], ',d')+"원", format(beforeTax, ',d')+"원", format(afterTax, ',d')+"원"]
                    }
                )
                st.dataframe(
                    df,
                    use_container_width = True,
                )
                # data_df = df.style.hide(axis=0)
                # st.write(data_df.to_html(), unsafe_allow_html=True)

with tab2:
    st.write('풍차돌리기 설명 - TBD')
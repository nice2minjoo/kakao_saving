import streamlit as st
import pandas as pd
from PIL import Image

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

                st.divider()
                st.subheader("주차 별 납입 금액")
                col1, col2 = st.columns([5, 2])
                df_data = pd.DataFrame(
                    {
                        "주차" : [f"{i}주차" for i in range(1, 27)],
                        "납입 금액" : member
                    }
                )

                col1.caption("차트")
                col1.bar_chart(member)

                col2.caption("테이블")
                col2.write(df_data)

with tab2:
    st.markdown('#### 풍차돌리기란?')
    st.markdown('카카오 26주 적금을 총 **26개**를 운용하는 것. 매주 같은 요일에 1개씩 개설 !!')
    st.markdown('27주차 이후부터 효과를 본다.')
    st.divider()
    st.markdown('##### 장점')
    st.markdown('- 26주를 완성했을 때 :blue[고금리 효과(연 7%)]를 볼 수 있다.')
    st.markdown('- 매주 하나씩 :blue[쌓아가는] 재미가 있다.')
    st.markdown('- 26개 완성 후 :blue[매주 이자]를 받는 재미가 있다.')
    st.markdown('- 26주 이후로는 :blue[추가로 들어가는] 돈이 없다.')
    st.divider()
    st.markdown('##### 단점')
    st.markdown('- :red[시간]과 :red[끈기]가 필요하다.')
    st.markdown('- 매주 챙겨야 하는 :red[번거로움]이 있다. (납입 실패 시 :red[우대금리 X])')
    st.markdown('- 한 번이라도 :red[자동이체 실패]하면, 통장 이율이 :red[3.5%]가 된다.')
    st.markdown('- 생각보다 :red[부담]된다. 뒤로 갈수록 :red[매주 큰 돈]이 빠져 나간다.')
    
    st.divider()
    image = Image.open("kakao_saving.jpg")
    st.image(image, caption='kakao saving')

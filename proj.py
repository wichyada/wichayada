from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt


st.title('Top searches')
left, right = st.columns(2)
left.markdown("By the user entering the name of the search")
left.markdown("By the user to fill in the information")

def load_Y2K_data():
    return pd.read_excel('Y2K.xlsx')


def save_model(model):
    joblib.dump(model, 'model.joblib')


def load_model():
    return joblib.load('model.joblib')


generateb = right.button('generate Y2K.xlsx')


def generate_Y2K_data():
    pass


if generateb:
    right.write('generating "Y2K.xlsx" ...')
    generate_Y2K_data()
    right.write(' ... done')

loadb = right.button('load Y2K.xlsx')
if loadb:
    right.write('loading "Y2K.xlsx ..."')
    df = pd.read_excel('Y2K.xlsx', index_col=0)
    right.write('... done')
    right.dataframe(df)
    fig, ax = plt.subplots()

trainb = right.button('trainb นิยมมาก')
if trainb:
    right.write('training model ...')
    df = pd.read_excel('Y2K.xlsx', index_col=0)
    model = LinearRegression()
    right.write('... done')
    right.dataframe(df)
    save_model(model)


def add_bg_from_url():
    pass


st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/originals/7c/4f/15/7c4f15c187f4ff24a137f039022ef9f1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)
add_bg_from_url()




st.title('รวมไอเดีย สไตล์การแต่งตัวแนว Y2K.แฟชั่นในตำนาน')
tab1, tab2, tab3, tab4, tab5, tab6, = st.tabs(["หน้าหลัก", "ประวัติ", "ทรงผมสไตล์แนว Y2K.", "การแต่งตัวสไตล์ Y2K.(ผญ./ผช.)","เครื่องประดับ", "สอนแต่งภาพสไตล์ Y2K.ในแอป Picsart"])

with tab1:
    st.header("หน้าหลัก")
    st.write("สาวๆ คนไหนกำลังอินกับกระแสแฟชั่นสไตล์ Y2K. กันบ้างเอ่ยยยย เปลี่ยนสไตล์การแต่งตัวและการแต่งหน้าให้เข้ากับธีม Y2K. กันแบบเต็มตัวเลยดีกว่า! วันนี้ วิว วิ่ว วิ้วฯ ได้รวบรวมไอเดีย สไตล์การแต่งตัวแนว Y2K. มาให้เพื่อนๆ ไปทำตามกันแล้วค่ะ")
    image = st.image("https://files.vogue.co.th/uploads/d_20220103194810.PNG",width=700)

with tab2:
    col1, col2 = st.columns(2)
    st.header("ประวัติ")
    st.write("ในช่วงนี้สไตล์การแต่งตัวที่กำลังมาแรงมากๆ คงจะหนีไม่พ้น เทรนด์การแต่งตัวแนว Y2K. ย้อนยุค ซึ่งได้กลับมาฮอตฮิตเป็นกระแสอีกครั้ง และสำหรับใครที่เป็นสายแฟชั่นต้องห้ามพลาดเทรนด์นี้เลยค่ะ แต่ก่อนที่เราจะพาไปดูไอเดียการแต่งตัวแนว Y2K. แฟชั่นในตำนานนี้ เราจะพาทุกคนไปทำความรู้จักกับการแต่งตัวแนว Y2K. ให้มากขึ้นกันค่ะ สไตล์การแต่งตัวแบบ Y2K. คือแฟชั่นในช่วงปลายปี 90s' จนถึงช่วงต้นของปี 2000s' ไม่ว่าจะเป็นเสื้อครอปท็อปเอวลอย เสื้อยืดพอดีตัวสกรีนลายกราฟิกใหญ่ๆ รวมไปถึงพวกกางเกงเอวต่ำทรงหลวมๆ หรือกระโปรงยีนส์สั้นกุด ซึ่งส่วนใหญ่โทนสีของเสื้อผ้าในยุคนั้น มักจะเน้นไปทางสีที่ค่อนข้างฉูดฉาด เน้นความสนุกสนาน และความคิดสร้างสรรค์ในการแต่งตัวอย่างมีเอกลักษณ์ และวันนี้เราก็มีไอเดีย สไตล์แต่งตัวแนว Y2K. แฟชั่นในตำนาน ที่กลับมาฮิตอีกครั้ง มาให้สาวๆ ไปลองแต่งตามกันได้เลยค่ะ")

with col1:
    if st.button(' Video1'):
        st.video("https://youtu.be/VXdILAKI7pY")
        with col1:
            st.video("https://youtu.be/MthPsQO2oGA")
with col2:
    if st.button(' Video2'):
        st.video("https://youtu.be/3twFo3ImRrQ")
        with col2:
            st.video("https://youtu.be/PMFCi-prVrI")

with tab3:
    st.header("ทรงผมสไตล์แนว Y2K.")
    image = st.image("https://img.wongnai.com/p/1920x0/2022/12/04/dd627045c6914f0580c6ef73a1f83d01.jpg")
    col1, col2, col3, col4, = st.columns(4)

with tab3:
    st.subheader("(ทรงผมเปียคู่ด้านหน้าเรียบๆ ง่ายๆ ดูคลาสสิก)")
    col1, col2, = st.columns(2)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/0ab76ac7eaa24cd0927d789339c2cf6a.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/d1b313128a2c45da9009247a59decfe6.jpg", width=350)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/d852f9c1d0894bf2ac24488570039702.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/ca135a017ca6478eae69400cd1959cc2.jpg", width=350)

with tab3:
    st.subheader("(ถักเปียแกละสองข้างทำง่ายแถมน่ารักมากก)")
    col1, col2, = st.columns(2)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/a5ca2b20659943bea4798090968eb4cf.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/b4561542c81642d2b7476c2968a6d384.jpg", width=350)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/e20362c2c59f4edda4b7b01c09deef76.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/d11d82df8fda4349aacb866ee1f1e677.jpg", width=350)

with tab3:
    st.subheader("(ถักผมเปียวงกลมโดนัทสองข้างแบบลูกคุณหนู)")
    col1, col2, = st.columns(2)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/66f644b4274b4b5d8e422cab58bc375c.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/a3a7f2050cf6468b8aabfdad134b02dd.jpg", width=350)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/ef30e4907c3943c181d69ccfd259d9b9.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/c033b1ff24e94d5d80b9c6f118518e6a.jpg", width=350)

with tab3:
    st.subheader("(ช่อผมเปียน่ารัก ๆ สไตล์สาว Y2K ที่แท้ทรู!!)")
    col1, col2, = st.columns(2)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/0523740d8da44c1eb6513d02396a5684.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/a215de127612487a9ceb77d7b7278510.jpg", width=350)
with col1:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/c7a1caffb01543c2aea2bcb125e30345.jpg", width=350)
with col2:
    image = st.image("https://img.wongnai.com/p/400x0/2022/12/04/3dc91827a7df4ae4a422c99cb60bad79.jpg", width=350)

with tab4:
    st.header("การแต่งตัวสไตล์ Y2K.(ผญ./ผช.)")
    st.subheader("(ผู้หญิง)")

    image = st.image("https://i.pinimg.com/564x/df/93/63/df9363608f135443ced5dd912a30e2ed.jpg")
    image = st.image("https://plusprinting.bookplus.co.th/wp-content/uploads/2022/11/Y2K-13.jpg")
    image = st.image("https://digitalmore.co/wp-content/uploads/2022/12/Y2K-18.jpg")
    image = st.image("https://plusprinting.bookplus.co.th/wp-content/uploads/2022/11/Y2K-010.jpg")
    image = st.image("https://plusprinting.bookplus.co.th/wp-content/uploads/2022/11/Y2K-05.jpg")
    image = st.image("https://plusprinting.bookplus.co.th/wp-content/uploads/2022/11/Y2K-12.jpg.webp")
    image = st.image("https://digitalmore.co/wp-content/uploads/2022/12/Y2K-14-e1669991629940.jpg")

with tab4:
    st.subheader("(ผู้ชาย)")

    image = st.image("https://www.reviewnews.info/wp-content/uploads/2022/10/%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%99%E0%B8%94%E0%B9%8C%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B8%B5%E0%B8%95-Y2K.jpg")
    image = st.image("https://files.gqthailand.com/uploads/Cover_Alyx3.jpg")
    image = st.image("https://files.gqthailand.com/uploads/1A04CA71-1127-4616-82C1-486574B363EF.jpeg")

with tab5:
    st.header("เครื่องประดับ")
    image = st.image("https://cheezelooker.com/file_managers/uploads/file_managers/source/2022%20DAILY%20CULTURE/DECEMBER/WEEK%203/10%20ACCESSORIES/fy2k.jpg")
    option = st.selectbox(
        'ค้นหาเครื่องประดับ',
        ('แหวน', 'กำไล','สร้อย','กระเป๋า','หมวก','รองเท้า'))

    st.write('You selected:', option)
    x = st.button('ตกลง')
if x:
    if option =='แหวน':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://sc04.alicdn.com/kf/Hdd852a34f31b44d9a9ec9a0925a377b4j.jpg", width=220)
            st.image("https://cf.shopee.co.th/file/79d51e8215859e51edad6b984fcc6bf4",width=220)
        with col2:
            st.image("https://ae03.alicdn.com/kf/Hacc0dae21bc94221b30b132bdbdb961eB.jpg",width=220)
            st.image("https://ae01.alicdn.com/kf/Hdee6e8b96bf94b5bab2734f0883f7dc3N/9-Y2K.jpg_Q90.jpg_.webp", width=220)
        with col3:
            st.image("https://ae01.alicdn.com/kf/S3a3c6566e0294228821e1fa6dbff5531M/Y2k-Vintage-Golden-Y2K.png_.webp",width=220)
            st.image("https://ae01.alicdn.com/kf/H288db0ed8c604f6d8f761480524fe8a1q/Sindlan-Kpop-Tai-Chi-Punk-Letter.jpg_Q90.jpg_.webp",width=220)
    if option =='กำไล':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://ae01.alicdn.com/kf/H97ec6b1c4f57464784edf18c01252637E/Hand-2021.jpg_.webp",width=220)
            st.image("https://cf.shopee.co.th/file/4f1ad00f65a372f0a4d32ba914fd4964",width=220)
        with col2:
            st.image("https://ae01.alicdn.com/kf/H0e3f84a8ffdc45698e5c10eaa894058di/Y2K-Smile-Face-Paint-Sweet-Bohemian.jpg_Q90.jpg_.webp",width=220)
            st.image("https://sc04.alicdn.com/kf/H7dc6dda687e04045a7c92303eb74e8a3i/243897285/H7dc6dda687e04045a7c92303eb74e8a3i.jpg",width=220)
        with col3:
            st.image("https://s.alicdn.com/@sc04/kf/H7fb646e135c941488c1d5b2abd2144b0k.jpg", width=220)
            st.image("https://ae01.alicdn.com/kf/S2b09ee503463480197abbf41281c71b0M/Y2K-Enamel-Moon-2022.jpg_Q90.jpg_.webp",width=220)
    if option =='สร้อย':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://ae01.alicdn.com/kf/S009edb355d494731bc1826139554b3b5i/Y2K-Rainbow-Heart-Goth-Charms-Vintage-90S-Choker.jpg_Q90.jpg_.webp",width=220)
            st.image("https://sc04.alicdn.com/kf/H71ed4cc97df74313a750cd76c6351aebR/248472338/H71ed4cc97df74313a750cd76c6351aebR.jpg",width=220)
        with col2:
            st.image("https://cf.shopee.co.th/file/489c7c7ec64e354b3ef15a9042acf2e7",width=220)
            st.image("https://lzd-img-global.slatic.net/g/p/0b5d33069e23c638ed616d9dd63717ae.jpg_720x720q80.jpg_.webp",width=220)
        with col3:
            st.image("https://lzd-img-global.slatic.net/g/p/c1b05f33310ca6bfca8615dd0ba9f084.jpg_2200x2200q80.jpg",width=220)
            st.image("https://cf.shopee.co.th/file/94e3007513ddb32db6b431c2874102cf",width=220)
    if option =='กระเป๋า':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://cf.shopee.co.th/file/sg-11134201-22100-2w8pspu9crivc1",width=220)
            st.image("https://lzd-img-global.slatic.net/g/p/6d6a8443baf3a69ccc61169f12b5b2cb.jpg_720x720q80.jpg_.webp",width=220)
        with col2:
            st.image("https://lzd-img-global.slatic.net/g/ff/kf/Se7893cda55724c9094603752eaba8141F.jpg_720x720q80.jpg_.webp",width=220)
            st.image("https://lzd-img-global.slatic.net/g/p/ddb372cc668ba913b7178db2aeaee39b.jpg_720x720q80.jpg_.webp",width=220)
        with col3:
            st.image("https://filebroker-cdn.lazada.co.th/kf/S84ff0541826a4997a8ec7a219cbd56f17.jpg",width=220)
            st.image("https://lzd-img-global.slatic.net/g/ff/kf/Se9fefbf3a9fc4550a60e3953762cea02R.jpg_200x200q80.jpg_.webp",width=220)
    if option =='หมวก':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://sc04.alicdn.com/kf/H29fe511e95b741e5b253c80a640b07c6m/243726071/H29fe511e95b741e5b253c80a640b07c6m.jpg",width=220)
            st.image("https://cf.shopee.co.th/file/sg-11134201-22100-uqlu00ghy3iv12_tn",width=220)
        with col2:
            st.image("https://cf.shopee.co.th/file/985746599e063e7cb3886a295025d97a",width=220)
            st.image("https://ae01.alicdn.com/kf/Hdd7e2e78a6664502aecbdc4d53d5ea0af.jpg?width=1080&height=1080&hash=2160",width=220)
        with col3:
            st.image("https://lzd-img-global.slatic.net/g/p/955bf0f2507510d0552a00ba961dc84d.jpg_200x200q80.jpg_.webp",width=220)
            st.image("https://my-live-02.slatic.net/p/1a0eade52e83ad3d5ccdcc7310d515d0.jpg",width=220)
    if option =='รองเท้า':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://cf.shopee.co.th/file/952b8d06dfeb6b8a700c7ac1fe657b85",width=220)
            st.image("https://cf.shopee.com.br/file/b839013e1305a36cf93062f995153030",width=220)
        with col2:
            st.image("https://cf.shopee.com.br/file/af61220386fb55260f40eb4e4d8d3b91_tn",width=220)
            st.image("https://cf.shopee.com.br/file/55b133a1cc1c425e4062cfa3a7674799",width=220)
        with col3:
            st.image("https://mywearshop.com/wp-content/uploads/2021/08/50226341-1.jpg",width=220)
            st.image("https://ae01.alicdn.com/kf/Sb5d19db15996416492f1f667f855422dq/Cotton-Calf-Socks-Lolita-Y2K-Bow-Pearl-Crystal-Knee-High-Socks-Thigh-High-Loose-Stockings-for.jpg",width=220)

with tab6:
    st.header("สอนแต่งภาพสไตล์ Y2K. ในแอป Picsart")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto,width=1600/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/cover_image/1%281%29_1.png")
    st.write("1.เลือกรูปที่เราต้องการจะแต่ง แล้วนำไปตัด(ตัดส่วนที่ไม่ต้องการออก) กดเครื่องมือตามในรูปที่วงเอาไว้ด้วยสีน้ำเงินแล้วจากนั้นก็ตัดโดยระบายสีแดงในส่วนที่ต้องการ หรือใครจะนำรูปไปตัดด้วย https://www.remove.bg/ ก็ได้เช่นกันตามที่สะดวกกันเลยเสร็จแล้วกดบันทึกเข้าอัลบั้ม")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto%2Cwidth=1600%2Cheight=900/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/5_1352.png")
    st.write("2.ในส่วนต่อมาเราจะสร้างพื้นหลังใหม่เป็นหน้าเปล่าแบบในรูป แล้วนำรูปที่เราตัดเอาไว้เสร็จแล้วลงในหน้าที่สร้างใหม่ แล้วย่อขยายรูปปรับขนาดตามต้องการ")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto%2Cwidth=1600%2Cheight=900/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/6_913.png")
    st.write("3.กดค้นหาสติกเกอร์คีย์เวิร์ด y2k จากนั้นเลือกหาลายที่ชอบและต้องการแล้วจัดองค์ประกอบมุมตามเหมาะสม โดยสติกเกอร์จะมีทั้งอันที่สามารถใช้ได้ฟรีและไม่ฟรีสังเกตจะรูปมงกุฎอยู่มุมล่างขวา")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto%2Cwidth=1600%2Cheight=900/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/7_685.png")
    st.write("4.การย้ายตำแหน่งสติกเกอร์ให้เรากดไปที่ไอคอนรูปสี่เหลี่ยมแล้วเลือก เลื่อนลง จะเป็นการจัดให้สติกเกอร์ลงไปอยู่ด้านหลัง และหากต้องการให้สติกเกอร์มีความโปร่งใสมากกว่านี้ ให้กดเลื่อนปรับค่าความทึบตรงแถบด้านล่างใต้รูป")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto%2Cwidth=1600%2Cheight=900/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/8_511.png")
    st.write("5.หากต้องการจะเปลี่ยนสีสติกเกอร์ให้เลือกหาไอคอนสีสันในแถบด้านล่าง แล้วเลื่อนปรับหาสีที่ถูกใจเลยจ้า หากต้องการจะแต่งหน้าหรือเสริมสวยเพิ่มให้ค้นหาสติกเกอร์ในคีย์เวิร์ด Make up ได้เลยชอบปากสีไหน ตาสีอะไร ขนตางอนแค่ไหน จัดได้หมดเลยเอาอยู่ทุกอัน แค่นี้เราก็สามารถแต่งรูปสวยๆได้ไม่ยากแค่ภายในไม่กี่นาทีแล้ว")
    image = st.image("https://img-prod.api-onscene.com/cdn-cgi/image/format=auto%2Cwidth=1600%2Cheight=900/https://sls-prod.api-onscene.com/partner_files/trueidintrend/223657/9_398.png")

# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# from PIL import Image as img

# st.set_page_config(page_title="VSP | RINL | DA Project", 
#                 #    page_icon="https://www.vizagsteel.com/photos/logonew.jpg", 
#                     page_icon="❤️",
#                    layout="wide", 
#                    initial_sidebar_state="auto", 
#                    menu_items=None)

# ########### Title Header################
# st.markdown("<h1 style='color:green; text-align:center;'>Visakapatnam Steel Plant</h1><br>",unsafe_allow_html=True)
# st.markdown("<h3 style='color:gold; text-align:center;'>LEVERAGING DATA   ANALYTICS TO OPTIMIZE MATERIAL CONSUMPTION" 
#          "IN A VIZAG STEEL PLANT</h3>",unsafe_allow_html=True)

# ################# Side Menu ################
# st.sidebar.title("Visakapatnam Steel Plant")
# st.sidebar.subheader("Rastriya Ispath Nigam Limited")

# uf=st.sidebar.file_uploader("Upload Your Custom CSV File")


# month=st.sidebar.radio("Select Month:",('July','August','September','Custom File'))
# # x1=""
# # y1=""
# # data=""
# if month=="July":
#     data=pd.read_csv("Data/DATA1.csv")
#     month="JULY"
#     # x1=data.Material_Type
#     # y1=data.MATERIAL
# if month=="August":
#     data=pd.read_csv("Data/DATA2.csv")
#     month="August"
#     # x1=data.Material_Type
#     # y1=data.MATERIAL
# if month=="September":
#     data=pd.read_csv("demo_data_set.csv")
#     month="September"
#     # x1=data.Country
#     # y1=data.Smokes
# if month=="Custom File":
#     if(uf) is not None:
#         cf=pd.read_csv(uf)
#         st.write(cf.columns)
#         # data=pd.read_csv(uf)
#         month="Custom File"
#         x1=cf.Country
#         y1=cf.Smokes
#     else:
#         x1=""
#         y1=""
#         st.write("File has No Data or Data May be Corrupted")



# # st.write(cf)

# # st.sidebar.write("Select to Compare with :red[Y]")
# # i=0
# # st.columns=[1,2]
# # for xcols in range(len(data.columns)):
# #     xcol=(data.columns[xcols])
# #     if st.sidebar.checkbox(data.columns[xcols],key=xcols):
# #         # st.write(xcol[xcol]) 
# #         x1=xcol
# # st.sidebar.write("Selct to Compare with X")
# # for ycols in range(len(data.columns)):
# #     ycol=(data.columns[ycols])
# #     if st.sidebar.checkbox(data.columns[ycols]):
# #         st.write(ycol[ycol]) 
# #         y1=ycol

# column_headers = data.columns.tolist()
# selected_column = st.sidebar.radio("Select a column", column_headers,key="xcol")
# st.write(data[selected_column])
# x1=(data[selected_column])
# column_headers = data.columns.tolist()
# selected_column = st.sidebar.radio("Select a column", column_headers,key="ycol")
# st.write(data[selected_column])
# y1=(data[selected_column])

# # done by
# st.sidebar.markdown("### Project Done by-")
# dp=img.open("21VV5A1268.jpg")
# st.sidebar.image(dp,width=150)
# st.sidebar.latex("Dannna Sai Ajith Kumar")
# st.sidebar.latex("Trainee-no:100019761")

# ########## Main Content ################

# if x1 is not None and y1 is not None:
#     st.header(" Showing Production Graph of: :blue[{}]".format(month) )
#     fig =go.Figure()
#     # fig.add_trace(go.Scatter(x = x1, y=y1,
#     #                                 mode = 'lines'))
#     fig.add_trace(go.Bar(x=x1, y=y1,
#                                 name='Smoked'))
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.markdown(" <h4 style='color:red; text-align:center;'>Upload your custom CSV file (or) Please Select any Month and any Two(2) Colums for Comparison  </h4><br>",unsafe_allow_html=True)





import streamlit as st
import pandas as pd
import plotly.graph_objects as go 


def pageinfo():
    st.set_page_config(page_title="VSP | RINL | DA Project", 
                    page_icon="https://www.vizagsteel.com/photos/logonew.jpg", 
                    # page_icon="❤️",
                    layout="wide", 
                    initial_sidebar_state="auto", 
                    menu_items=None)

def header():
    col1, col2=st.columns([1,5])
    with col1:
        logo=('https://www.vizagsteel.com/photos/logonew.jpg')
        st.image(logo,width=150)
    with col2:    
        st.markdown("<h1 style='color:green; text-align:center;'>Visakapatnam Steel Plant</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='color:silver; text-align:center;'>Rashtriya Ipsath Nigam Limited</h1><br>",unsafe_allow_html=True)
    st.markdown("#")
    st.markdown("<h3 style='color:gold; text-align:center;'>LEVERAGING DATA   ANALYTICS TO OPTIMIZE MATERIAL CONSUMPTION" 
            " IN A VIZAG STEEL PLANT</h3>",unsafe_allow_html=True)
def sidemenu():
    # sm1,sm2=st.sidebar.columns([1,3])
    # with sm1:
    logo=('https://www.vizagsteel.com/photos/logonew.jpg')
    st.sidebar.image(logo,width=30)
    # with sm2:
    st.sidebar.title(":green[Visakapatnam Steel Plant]")
    st.sidebar.subheader("Rastriya Ispat Nigam Limited")
    
    
    uf=st.sidebar.file_uploader("Upload Your Custom CSV File",type="csv")
    
    st.sidebar.markdown("")
    st.sidebar.write("# :green[Elements for Comparison:]")
    st.sidebar.write("#### Upload Your file above to Compare (or)")
        # if st.sidebar.radio("Select here to Choose your file",["name"]):

    month=st.sidebar.radio(":red[Choose Month]",('None','Custom File Comparison','July','August','September'))
    if month=="None":
        st.markdown("<h4 style='color:red; text-align:center;'>Upload your custom CSV file (or) Please Select any Month and any Two(2) Colums for Comparison  </h4><br>",unsafe_allow_html=True)
    if month=="Custom File Comparison":
        if uf is not None:
            nm="Custom File: "+uf.name
            st.sidebar.success(nm)
            cf=pd.read_csv(uf)
            columns(cf,uf.name)
        else:
            st.warning("Please upload your own CSV file at Side menu which you want to make  plot comaprison ")
            # uf=st.sidebar.file_uploader("Upload Your Custom CSV File",type="csv",label_visibility="hidden")

        
    
    if month=="July":
        data=pd.read_csv('Data/DATA1.csv')
        columns(data,month)
    if month=="August":
        data=pd.read_csv('Data/DATA2.csv')
        columns(data,month)
    if month=="September":
        data=pd.read_csv('Data/DATA3.csv')
        columns(data,month)

    # st.markdown("<img src='21VV5A1268.jpg' alt='Me' height='150' widht='150'>", unsafe_allow_html=True)
    st.sidebar.markdown(":blue[Project Done by-]")
    dp=("https://dannanasaiajithkumar.vercel.app/Images/SBProfile.jpg")
    st.sidebar.image(dp,width=200)
    st.sidebar.latex("Dannna Sai Ajith Kumar")
    st.sidebar.latex("Trainee-no:100019761")

def columns(data,month):
    # x1=(xcols(data))
    st.sidebar.markdown(":blue[Select any One value to Comapre with :green[Y]]")
    column_headers = data.columns.tolist()
    selected_column = st.sidebar.radio("Select a column", column_headers,key="xcol")
    x1=(data[selected_column])
    # y1=(ycols(data))    
    st.sidebar.markdown(":blue[Select any One value to Comapre with :green[{}]]".format(selected_column))
    column_headers = data.columns.tolist()
    selected_column = st.sidebar.radio("Select a column", column_headers,key="ycol")
    y1=(data[selected_column])
    month=month
    body(x1,y1,month)

def ploting(x1,y1,month):
    st.header(" Showing Comparison Plotting Graph of: :blue[{}]".format(month) )
    # st.header(" X-axis:blue[{}]".format(x1) )
    fig =go.Figure()
    fig.add_trace(go.Bar(x=x1,y=y1)) 
    # st.success(x1)
    # st.success(y1)
    st.plotly_chart(fig, use_container_width=True) 



def body(x1,y1,month):
    if x1 is not None and y1 is not None and month is not None:
        ploting(x1,y1,month)
        # st.markdown("<h1 style='color:cyan; text-align:center;'>By Dannana Sai Ajith Kumar <br> Trinee NO: 100019761  </h4><br>",unsafe_allow_html=True)
    else:
        st.markdown("<h4 style='color:red; text-align:center;'>Upload your custom CSV file (or) Please Select any Month and any Two(2) Colums for Comparison  </h4><br>",unsafe_allow_html=True)


def main():
    pageinfo()
    header()
    sidemenu()

main()
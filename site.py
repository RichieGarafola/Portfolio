import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="My Webpage", 
    page_icon=":tada:", 
    layout="wide")

# Create a function to access the data of the lottie annimation
def load_lottieurl(url):
    # use the request method to send a get to request URL
    r = requests.get(url)
    # if status is successful it will return 
    if r.status_code != 200: 
        return None
    # return the json data of the lottie animation
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_dl87KC.json")


######################
#Sidebar Menu
######################
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast", 
        default_index=0,
        # orientation="horizontal",
        
    )

######################
#Home
######################    
if selected == "Home":
    st.markdown(""" <style> .font {
    font-size:20px ;
    font-family: 'MERRIWEATHER';
    }
    </style> """, unsafe_allow_html=True)
        # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("./Images/profile-pic.png", width=230)

    with col2:
        st.title("Richie Garafola")
        st.write("Data Analyst, assisting enterprises by supporting data-driven decision-making. Passionate about finding ways to use Python to be more efficient and effective in business settings!")
        st.write("📫", "Richiegarafola@hotmail.com")
    col1,col2 = st.columns(2)
    with col1:
        st.title("[GitHub ](https://github.com/RichieGarafola)")
    with col2:
        st.title("[LinkedIn ](https://www.linkedin.com/in/richiegarafola/)")
    with st.container():
        st.write("---")
        col1,col2 = st.columns(2)
        with col1:
            st.header("About Me")
            st.write("##")
            st.markdown('<p class="font"> I am a Results-driven Analyst, recognized for bringing strategic perspective to projects and tool development. Team leader, able to inspire others to deliver solutions in a collaborative way. Highly productive with a passion for learning and applying new skills to improve project outcomes. Known for the ability to identify relevant issues and develop alternate paths to proceed. Strengths include: Achiever, Learner, Focus, Strategic, Futuristic.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> I am a resourceful Financial Analyst with 5+ years of hands-on experience in the financial trading arena. I recently completed a FinTech Bootcamp through Arizona State University to further my expertise in the field.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> I am known for leadership and technical aptitude in data analysis, financial modeling, and forecasting. I am capable of supporting budgeting and planning processes that include data validation, setup and maintenance of reporting tools, tracking, and auditing.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> I take a collaborative approach to problem solving within teams when defining needs, evaluating risks, and implementing compliant solutions. I appreciate sharing ideas and best practices with my teammates to deliver the best solutions.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> I am skilled in Python, with an emphasis in Pandas, Numpy, and Streamlit. I am an active learner, currently studying machine learning, algorithms, and blockchain.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font">I enjoy furthering my knowledge and experience in financial analytics. Current passions are time series analysis andextracting data insights through statistical techniques and quantitative methods that enhance decision-making and drive competitive growth.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> I am seeking a position where I can use my skills to add business value and contribute to the success of my team. Eager to connect with you to learn more about what I can do to provide data-centric solutions for your organization.</p>',unsafe_allow_html=True) 
            with col2:
                st_lottie(lottie_coding, height=500, key="coding")            
######################
# Projects
######################    
if selected == "Projects":
    st.title(f"You have selected {selected}")
    
        # NFA
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        st.markdown(""" <style> .font {
            font-size:20px ;
            font-family: 'MERRIWEATHER';
            }
            </style> """,
                        unsafe_allow_html=True)
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/NFAOverview.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> This is your one stop shop for all analysis as it relates to the Stock Markets. Whether you are intersted in general information on the company, fundamental analysis, technical analysis or perhaps you want to see what your asset looks like forecasted in the future, we have the tools you are looking for!</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> Some Libraries used:  streamlit, pandas, datetime, matplotlib, yfinance, pathlib, prophet, plotly, wordcloud, vadersentiment, regex, path, pandas-datareader, mplfinance, finta, nltk, snscrape, hvplot, sklearn, tensorflow </p>',unsafe_allow_html=True)
            
            
            st.subheader("[Deployed Dashboard ](https://richiegarafola-nfa-notfinancialadvice-home-395c34.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/NFA-NotFinancialAdvice)")


    # Expense Sheets        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/expenseSheet.gif")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Keep track of your monthly income and expenses without the need for Excel!                 In this platform I will lever the power of Python using the streamlit library to build an interactive web                 application. Store your monthly reports using the FREE NoSQL Database.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-expensesheet.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ExpenseSheet)")

    # Sales Analysis    
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/sales_analysis.gif")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> A company has been tracking their sales for the year of 2019. At the end of the fisical year the company decided to upgrade tech from using Excel to a more optimal SQL-centric database. The data contains hundreds of thousands of electronics store purchases broken down by `Order ID`, `Product`, `Quantity Ordered`, `Price Each`, `Order Date`, `Purchase Address`.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://salesdashboard.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Sales_Analysis)")

    # Excel Sales        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/excelSales.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Aggregate your Excel spreadsheets interactively! In this platform I will display the power of Python using the streamlit library to build an interactive web application. I will build a KPI that aggregates data tailored to the users interest and visually display the output </p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-kpi-sales.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/SalesAnalysisExcelKPI)")
            
    # EDA   
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/eda.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Exploratory Data Analysis refers to the critical process of performing initial investigations on data to discover patterns, spot anomalies, test hypothesis and to check assumptions with the help of summary statistics and graphical representations. In this platform I will display the power of Python using the streamlit library to build an EDA tool. I will build a KPI that performs complete customized data analysis based on the data provided by the user.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-eda.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/EDA)")
            
    # Housing Price Sentiment        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/housingPriceWordCloud.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Analyze the 15 and 30 year fixed mortgage rates from FRED economic database and look for correlations with Case Shiller housing prices. The fixed mortgage rates will act as indicators to help us understand the future outlook of the housing market. The economic sentiment will be gauged using NLP to see if there is a correlation with sentiment on twitter and our predictor. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Housing_Price_Sentiment_Advisor)")
            
    # RoboAdvisor        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/robot.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> An AWS chatbot using Lambda and Lex that will recommend an investment portfolio for a retirement plan. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/RoboAdvisor)")
            
    # Forex Travel Planner        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/forexTravelPlanner.jpg")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Travel planning tool that will allow the end user to select a set of countries they would like to travel to and the travel timeframe. The tool will analyze historical forex data and predict the country that will have the most favorable currency within the given timeframe for traveling. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Travel_Planner_Currency_Conversion)")
            
    # Machine Learning Data Analysis        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/MLDA.png")
        with text_column:
            st.subheader("")
            st.markdown('<p class="font"> Given a dataset comprised of features and sequences, describe the data set, come up with a predictive model. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/DataAnalysisUsingMachineLearning)")
            
            
            
            
######################
# Contact
######################    
if selected == "Contact":
    st.title(f"You have selected {selected}")    
    with st.container():
        st.write("---")
        st.header(":mailbox: Get In Touch With Me!")
        st.write("##")    
        contact_form = """
        <form action="https://formsubmit.co/8c1144f613c50b43e7ddf63b49e40672" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="your name" required>
            <input type="email" name="email" placeholder="your email" required>
            <textarea name="message" placeholder="Leave your comments"></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html = True)
        # Use local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("./style/style.css")




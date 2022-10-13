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
            st.subheader("Not Financial Advice - NFA")
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
            st.subheader("Expense Sheet")
            st.markdown('<p class="font"> Keep track of your monthly income and expenses without the need for Excel!                 In this platform I will lever the power of Python using the streamlit library to build an interactive web                 application. Store your monthly reports using the FREE NoSQL Database.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-expensesheet.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ExpenseSheet)")

# Sales Analysis    
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/sales_analysis.gif")
        with text_column:
            st.subheader("Sales Analysis")
            st.markdown('<p class="font"> A company has been tracking their sales for the year of 2019. At the end of the fisical year the company decided to upgrade tech from using Excel to a more optimal SQL-centric database. The data contains hundreds of thousands of electronics store purchases broken down by `Order ID`, `Product`, `Quantity Ordered`, `Price Each`, `Order Date`, `Purchase Address`.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://salesdashboard.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Sales_Analysis)")

# Excel Sales        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/ExcelSales.gif")
        with text_column:
            st.subheader("Interact with Excel Sales")
            st.markdown('<p class="font"> Aggregate your Excel spreadsheets interactively! In this platform I will display the power of Python using the streamlit library to build an interactive web application. I will build a KPI that aggregates data tailored to the users interest and visually display the output </p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-kpi-sales.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/SalesAnalysisExcelKPI)")
            
# EDA   
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/eda.png")
        with text_column:
            st.subheader("Exploratory Data Analysis Tool")
            st.markdown('<p class="font"> Exploratory Data Analysis refers to the critical process of performing initial investigations on data to discover patterns, spot anomalies, test hypothesis and to check assumptions with the help of summary statistics and graphical representations. In this platform I will display the power of Python using the streamlit library to build an EDA tool. I will build a KPI that performs complete customized data analysis based on the data provided by the user.</p>',unsafe_allow_html=True) 
            st.subheader("[Deployed Dashboard ](https://richiegarafola-eda.streamlitapp.com/)")
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/EDA)")
            
# Housing Price Sentiment        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/housingPriceWordCloud.png")
        with text_column:
            st.subheader("Housing Price Sentiment Advisor")
            st.markdown('<p class="font"> Analyze the 15 and 30 year fixed mortgage rates from FRED economic database and look for correlations with Case Shiller housing prices. The fixed mortgage rates will act as indicators to help us understand the future outlook of the housing market. The economic sentiment will be gauged using NLP to see if there is a correlation with sentiment on twitter and our predictor. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Housing_Price_Sentiment_Advisor)")
            
# RoboAdvisor        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/robot.png")
        with text_column:
            st.subheader("Robo Advisor")
            st.markdown('<p class="font"> An AWS chatbot using Lambda and Lex that will recommend an investment portfolio for a retirement plan. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/RoboAdvisor)")
            
# Forex Travel Planner        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/forexTravelPlanner.jpg")
        with text_column:
            st.subheader("Travel Planner based on Currency Conversion")
            st.markdown('<p class="font"> Travel planning tool that will allow the end user to select a set of countries they would like to travel to and the travel timeframe. The tool will analyze historical forex data and predict the country that will have the most favorable currency within the given timeframe for traveling. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Travel_Planner_Currency_Conversion)")
            
# Machine Learning Data Analysis        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/MLDA.png")
        with text_column:
            st.subheader("Exploratory Data Analysis using Machine Learning")
            st.markdown('<p class="font"> Given a dataset comprised of features and sequences, describe the data set, come up with a predictive model. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/DataAnalysisUsingMachineLearning)")
            
# unit 13, Clustering Crypto        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/clusteringCrypto.jpg")
        with text_column:
            st.subheader("Crypto Clustering")
            st.markdown('<p class="font"> Generate a report of what cryptocurrencies are available on the trading market and how they can be grouped using classification. Cluster cryptocurrencies and create plots to present results. Use unsupervivsed learning algorithm PCA to reduce data dimensions and clustering will be predicted with the K-Means algorithm, Project is deployed using Amazon SageMaker. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/blob/main/unit%2013%20AWS%20Crypto%20Clustering)")
            
# unit 14, LSTM Stock Predictor       
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/lstm.jpg")
        with text_column:
            st.subheader("LSTM Stock Predictor")
            st.markdown('<p class="font"> Due to the volatility of cryptocurrency speculation, investors will often try to incorporate sentiment from social media and news articles to help guide their trading strategies. One such indicator is the Crypto Fear and Greed Index (FNG) which attempts to use a variety of data sources to produce a daily FNG value for cryptocurrency. Build and evaluate deep learning models using both the FNG values and simple closing prices to determine if the FNG indicator provides a better signal for cryptocurrencies than the normal closing price data. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Unit%2014%20LSTM%20Stock%20Predictor)")
            
# unit 15, Machine Learning Trading Bot       
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/tradingBot.png")
        with text_column:
            st.subheader("Machine Learning Trading Bot")
            st.markdown('<p class="font"> Create an algorithmic trading bot that learns and adapts to new data and evolving markets.  Baseline Performance is established by generating trade signals using short and long window SMA values. The SVC classifier model from SKLearns support vector machine (SVM) is used to fit the training data and make predictions based on the testing data. Once this is established the parameters will be applied to a second machine learning model. Classifiers used: AdaBoost, DecisionTreeClassifier and LogisticRegression. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Unit%2015%20Machine%20Learning%20Trading%20Bot)")
            
# Unit 12, Crypto NLP        
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/cryptoNLP.png")
        with text_column:
            st.subheader("Natural Language Processing - Crypto")
            st.markdown('<p class="font"> There has been a lot of hype in the news lately about cryptocurrency, so you want to take stock, so to speak, of the latest news headlines regarding Bitcoin and Ethereum to get a better feel for the current public sentiment around each coin. Apply Natural language Processing (NLP) to understand the sentiment in the latest news articles featuring Bitcoin and Ethereum. Apply the fundamental NLP techniques to better understand the other factors involved with the coin prices such as common words and phrases and organizations and entities mentioned in the articles.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Tales%20from%20the%20Crypto)")
            
# Unit 11,Risky Business       
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/riskyBusiness.jpg")
        with text_column:
            st.subheader("Risky Business")
            st.markdown('<p class="font"> Mortgages, student and auto loans, and debt consolidation are just a few examples of credit and loans that people seek online. Peer-to-peer lending services let investors loan people money without using a bank. However, because investors always want to mitigate risk, lets predict credit risk with machine learning techniques. Build and evaluate several machine learning models to predict credit risk using data typical of lending services. Credit risk is an inherently imbalanced classification problem (the number of good loans is much larger than the number of at-risk loans), employ different techniques for training and evaluating models with imbalanced classes. The imbalanced-learn and Scikit-learn libraries will be used to build and evaluate models. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Risky%20Business)")
            
# unit 4, A Whale Off the Port(folio)     
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/portfolio-analysis.png")
        with text_column:
            st.subheader("Portfolio Analysis")
            st.markdown('<p class="font"> Create a tool that analyzes and visualizes the major metrics of portfolios using volatility, returns, risk, and Sharpe ratios. Determine which portfolio outperformed the others. Given the historical daily returns of several portfolios: some from the firms algorithmic portfolios, some that represent the portfolios of famous "whale" investors like Warren Buffett, and some from big hedge and mutual funds. Use this analysis to create a custom portfolio of stocks and compare its performance to that of the other portfolios, as well as the larger market (S&P 500 Index). </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Whale%20Analysis)")
            
# unit 6, Pythonic Monopoly     
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/panelDashboard.png")
        with text_column:
            st.subheader("Pythonic Monopoly")
            st.markdown('<p class="font"> Build a prototype dashboard using Panel to provide charts, maps, and interactive visualizations that help customers explore the data and determine if they want to invest in rental properties in San Francisco.  </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Pythonic%20Monopoly)")
            
# unit 10, Forecasting Net Prophet     
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/prophet.png")
        with text_column:
            st.subheader("Forecasting using Prophet")
            st.markdown('<p class="font"> Tasked with analyzing a companys financial and user data to help the company grow, find out if the ability to predict search traffic can translate into the ability to successfully trade the stock. Create a time series model using Prophet on Google Colab to analyze and forecast patterns in the hourly search data. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Forecasting%20Net%20Prophet)")
            
# API - Financial Planning     
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/financial-planner.png", width=300)
        with text_column:
            st.subheader("Financial Planner")
            st.markdown('<p class="font"> Create a tool for a credit union that helps their members enhance their financial health. Develop a prototype application to demo using APIs as part of the technical solution. The first financial analysis tool will be a personal finance planner that will allow users to visualize their savings composed by investments in shares and cryptocurrencies to assess if they have enough money as an emergency fund. The second tool will be a retirement planning tool that will use the Alpaca API to fetch historical closing prices for a retirement portfolio composed of stocks and bonds, then run Monte Carlo simulations to project the portfolio performance at 30 years. Use the Monte Carlo data to calculate the expected portfolio returns given a specific initial investment amount. </p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Financial%20Planning)")
            
# Travel Planner Currency Conversion 
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/travelPlannerCurrencyConversion.png")
        with text_column:
            st.subheader("Currency Conversion based on Travel Horizones")
            st.markdown('<p class="font"> Create a travel planning tool that will allow the user to select a set of countries they would like to travel to and a travel timeframe (3,6,12 months). The tool will analyze historical Forex data and predict the country that will have the most favorable currency within the given travel timeframe.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/Travel_Planner_Currency_Conversion)")
            
# Unit 18 Blockchain
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/blockchain.png")
        with text_column:
            st.subheader("Blockchain Ledger System")
            st.markdown('<p class="font"> Build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Blockchain)")
            
# Unit 21: Martian Token Crowdsale
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/kaseicoin.png")
        with text_column:
            st.subheader("Token Crowdsale")
            st.markdown('<p class="font"> After waiting for years and passing several tests, the Martian Aerospace Agency selected you to become part of the first human colony on Mars. As a prominent fintech professional, they chose you to lead a project developing a monetary system for the new Mars colony. </p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> Base this new system on blockchain technology and to define a new cryptocurrency named KaseiCoin. (Kasei means Mars in Japanese.) KaseiCoin will be a fungible token that’s ERC-20 compliant. Launch a crowdsale that will allow people who are moving to Mars to convert their earthling money to KaseiCoin.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/21_Advanced_Solidity)")
            
# Unit 20 Joint Savings Account
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/joinSavings.png")
        with text_column:
            st.subheader("Solidity Joint Savings")
            st.markdown('<p class="font"> A fintech startup is disrupting the finance industry with its own cross-border, Ethereum-compatible blockchain that connects financial institutions. Currently, the team is building smart contracts to automate many of the institutions financial processes and features, such as hosting joint savings accounts.</p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> To automate the creation of joint savings accounts, you’ll create a Solidity smart contract that accepts two user addresses. These addresses will be able to control a joint savings account. Your smart contract will use ether management functions to implement a financial institution’s requirements for providing the features of the joint savings account. These features will consist of the ability to deposit and withdraw funds from the account.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/Blockchain)")
            
# Unit 19 Cryptocurrency Wallet
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("./Images/cryptoWallet.png")
        with text_column:
            st.subheader("FinTech Finder")
            st.markdown('<p class="font"> Fintech Finder is an application that its customers can use to find fintech professionals from among a list of candidates, hire them, and pay them. Integrate the Ethereum blockchain network into the application in order to enable your customers to instantly pay the fintech professionals whom they hire with cryptocurrency.</p>',unsafe_allow_html=True) 
            st.subheader("[GitHub Repo ](https://github.com/RichieGarafola/ASU-FinTech-Python/tree/main/19%20-%20Blockchain%20Wallets)")
            
            
            
                 
            
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




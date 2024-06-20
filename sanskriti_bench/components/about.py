import streamlit as st

def about():
    st.markdown("""
        <style>
            .main {
                background-color: #FDEBBB;
                padding: 20px;
            }
            .header {
                font-size: 2.5em;
                font-weight: bold;
                text-align: center;
                color: #2e4053;
                margin-top: 20px;
            }
            .subheader {
                font-size: 1.5em;
                font-weight: bold;
                color: #2874a6;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .text {
                font-size: 1.2em;
                color: #2e4053;
                text-align: justify;
                margin-bottom: 10px;
            }
            .contact {
                font-size: 1.2em;
                color: #2874a6;
                text-align: center;
                margin-top: 30px;
                margin-bottom: 30px;
            }
            .partner-logo {
                max-width: 150px;
                max-height: 100px;
            }
            .contact-info {
                font-weight: bold;
                color: #2874A6;
            }
            .info-black {
                color: #000000;
            }
            .header-icon {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            .stMarkdown .stAlert {
                background-color: #f0f2f6;
                color: black;
                border-radius: 10px;
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Setting the title of the web page with the header icon
    st.markdown("""
        <div class="header-icon">
            <div class="header">SanskritiBench: Bridging NLP and Indian Cultural Richness</div>
        </div>
    """, unsafe_allow_html=True)

    # Abstract section
    st.markdown('<div class="subheader">Abstract</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="text">
        The aim of the project is to develop a state-of-the-art Indian Cultural benchmark that can test these models for their cultural accuracies, especially in a country like India which is rich in diversity. 
        With Hugging Face initiative of DATA-IS-BETTER-TOGETHER, our aim is to expand the benchmark into an alignment dataset and release it for preference tuning tasks.<br>
        We will be covering the official languages of India and their corresponding dialects. This is a community-driven project and your support and collaboration can make this initiative a success.
        </div>
    """, unsafe_allow_html=True)

    # Motivation and Process section
    st.markdown('<div class="subheader">Motivation and Process</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="text">
        Our goal is to ensure cultural accuracy and depth in NLP models by creating an Indic Cultural Benchmark. The process involves forming questions about the state across various categories. Context can change drastically for different states, highlighting the rich diversity of India. For instance:
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="text">
        <ul>
            <li><strong>Geographical Features:</strong> The geography of Kerala, with its backwaters and coastal line, contrasts sharply with the deserts of Rajasthan.</li>
            <li><strong>Demographics:</strong> The linguistic diversity of Karnataka, with Kannada as the official language, differs from the multilingual population of Delhi, where Hindi, Punjabi, and Urdu are commonly spoken.</li>
            <li><strong>Historical System:</strong> The historical influence of the Maratha Empire in Maharashtra is distinct from the Dravidian architecture and history of the Chola Dynasty in Tamil Nadu.</li>
            <li><strong>Economy:</strong> Punjab's agricultural economy, known for its wheat production, contrasts with the IT and service-driven economy of Telangana, particularly in Hyderabad.</li>
            <li><strong>Culture and Society:</strong> The classical dance form Bharatanatyam from Tamil Nadu is different from Kathak, which originated in northern India.</li>
            <li><strong>Great Personalities:</strong> Contributions of Rabindranath Tagore in Bengal's literary world differ from those of Dr. A.P.J. Abdul Kalam in Tamil Nadu's scientific community.</li>
            <li><strong>Infrastructure:</strong> The architectural marvel of the Konark Sun Temple in Odisha contrasts with the modern infrastructure of cities like Bengaluru.</li>
            <li><strong>Education and Healthcare:</strong> Kerala's high literacy rate and robust healthcare system stand out compared to other states.</li>
            <li><strong>Tourism and Attractions:</strong> The spiritual allure of Varanasi in Uttar Pradesh is distinct from the scenic beauty of the backwaters in Kerala.</li>
            <li><strong>Proverbs:</strong> Proverbs in Punjabi may convey different cultural wisdom compared to those in Gujarat.</li>
            <li><strong>Challenges and Future Outlook:</strong> Addressing economic disparities in Bihar is different from tackling environmental concerns in the Sundarbans of West Bengal.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="text">
        <strong>Figurative Language:</strong> Figurative language holds an essential role in the cultural context of each state. It includes proverbs, poems, similes, and other expressions that reflect the unique identity and wisdom of the people. For instance:
        <ul>
            <li>In Tamil, a common proverb "கற்றது கைமண் அளவு, கல்லாதது உலகளவு" (What one has learned is only a handful of sand; what one hasn't learned is the size of the world) emphasizes the vastness of knowledge yet to be acquired.</li>
            <li>In Bengali literature, the use of similes and metaphors is profound, as seen in the works of Rabindranath Tagore, where nature and human emotions are often intertwined.</li>
            <li>Hindi poems often employ rich figurative language to express deep emotions and cultural narratives, as evident in the works of poets like Kabir and Tulsidas.</li>
        </ul>
        By understanding and integrating these elements, we aim to enhance NLP models to better interpret and generate culturally rich and contextually accurate content.
        In parallel, our team will also be working on development of preference datasets for these languages.
        </div>
    """, unsafe_allow_html=True)
    
    # Example section
    st.markdown('<div class="subheader">Example</div>', unsafe_allow_html=True)
    st.image("https://sanskritiai.github.io/static.sanskriti.app/example.png", caption="Understanding the gaps", use_column_width=True)

    # Goals and Milestones section
    st.markdown('<div class="subheader">Goals and Milestones</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="text">
        <strong>Goals:</strong>
        <ul>
            <li>Develop a state-of-the-art Indian Culture Benchmark.</li>
            <li>Enhance NLP models with cultural and social awareness by working on cultural alignment datasets.</li>
            <li>Extend the research into deeper levels for each Indian Language.</li>
        </ul>
        <strong>Milestones:</strong>
        <ul>
            <li>Milestone 1: Initial research and dataset collection.</li>
            <li>Milestone 2: Model benchmarking and preliminary testing.</li>
            <li>Milestone 3: Dataset Release and Feedback.</li>
            <li>Milestone 4: Final evaluation and publication.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    # PI and Advisor section
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="subheader">Principal Investigator (PI)</div>', unsafe_allow_html=True)
        st.markdown('<div class="text">Guneet Singh Kohli<br>Research Lead and NLP Engineer</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="subheader">Research Advisors</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="text">
            <strong>Industry:</strong><br>
            - Daniel van Strien, Hugging Face<br>
            - Dr. Shantipriya Parida, Silo AI<br>
            - Anindyadeep Sannigrahi, Prem AI<br>
            <br>
            <strong>Academia:</strong><br>
            - Dr. Satya Ranjan Dash, Associate Professor, KIIT University<br>
            - Dr. Prashant Singh Rana, Assistant Professor, Thapar University<br>
            <br>
            </div>
        """, unsafe_allow_html=True)

    # Project partner section
    st.markdown('<div class="subheader">Project Partners</div>', unsafe_allow_html=True)
    partners = ["https://sanskritiai.github.io/static.sanskriti.app/supporters.png"]
    cols = st.columns(len(partners))
    for col, partner in zip(cols, partners):
        col.image(partner, use_column_width=True, caption="Partner Logo")

    st.markdown('<div class="contact">', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Contact Us or Join Us</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="contact">
            If you are interested in joining our project or want to know more about our research, please contact us at:<br>
            <span class="contact-info">Email:</span> guneetfateh07@gmail.com<br>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Embedding the Google Form
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.markdown(
        """
        <a href="https://forms.gle/ck95ZhN1WX5PdF1eA" target="_blank">
            <button style="background-color: #2874a6; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;">Join Us</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .alert-box {
            background-color: #f9f9f9;
            color: #2e4053;
            border-left: 6px solid #2874a6;
            padding: 10px 15px;
            margin: 20px 0;
            border-radius: 5px;
            font-size: 1.1em;
        }
        .alert-box p {
            margin: 0;
        }
        .alert-icon {
            font-size: 1.5em;
            color: #2874a6;
            vertical-align: middle;
            margin-right: 10px;
        }
    </style>
    <div class="alert-box">
        <span class="alert-icon">ℹ️</span>
        <p>Please fill out the form below and join us to initiate work on your language.</p>
    </div>
""", unsafe_allow_html=True)

# Calling the about function
about()

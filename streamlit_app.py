import streamlit as st
from PIL import Image
from forms.contact import contact_form

@st.dialog("Sponsor the Future of Fisheries / Partner with Us") # pop-up dialog
def show_contact_form():
    contact_form()

# Set up the page configuration
st.set_page_config(page_title="Post-Harvest Transparency Initiative", layout="centered")

# Header Section
st.title("Post-Harvest Transparency Initiative")
st.subheader("Monitoring Ocean Resources with Precision — Transforming Longline Fishing with AI Object Detection")
st.write("The technology to transform longline fisheries is here. Help us bring precision and transparency to the seafood industry.")

st.markdown("---")

# Hero Image Section
hero_image = Image.open('hero_image.jpg')  # Use your own hero image here
st.image(hero_image, caption="Transforming longline fisheries with AI-driven monitoring", use_column_width=True)

# Section 1: Why This Matters
st.header("Onshore Catch Monitoring: The Key to Effective Resource Management")
st.write(
    """
    Fishing practices are rapidly evolving, yet monitoring is lagging behind. Live onboard monitoring is often unfeasible for many vessels—due to lack of onboard conditions, restricted access, and remoteness of operations. However, all catches must come onshore to be monetized. Here lies the opportunity.
    \n\nWith **Post-Harvest Transparency**, we aim to accurately track every catch at the point of landing, providing unmatched precision in monitoring ocean resources, enforcing regulations, and offering transparency throughout the seafood supply chain.
    """
)
st.markdown(
    """
    **Problem**: Traditional catch identification relies on the eyes of experienced inspectors and manual weight scaling, which is prone to error and inefficiency.
    \n**Solution**: An AI-powered object detection model to identify species and estimate weight from images of the processed frozen catch at the point of landing.
    """
)

st.markdown("---")

# Section 2: The Vision
st.header("Transforming Longline Fishing Data with AI")
st.write(
    """
    Our AI-driven object detection module has a single mission: bring transparency to post-harvest data in longline fisheries, a critical step in protecting ocean resources and ensuring responsible fishing practices.
    
    - Consumers know the fish alive in the ocean and the packaged products in supermarkets, but what about in-between—processed catches being offloaded? These fish are head-off, tail-off, and gut-off, sometimes making identification almost impossible without expert human eyes.
    - We bring **efficiency and effectiveness** to this often-overlooked stage, with a **camera and smart detection** system that records everything automatically—species, weight, quantity.
    """
)

st.markdown("---")

# Section 3: Why NGOs and Industry Should Care
st.header("Impact on Resource Management and Sustainability")
st.write(
    """
    - **Real-Time Resource Accountability**: Accurate onshore monitoring that can plug critical gaps in current seafood traceability initiatives.
    - **Address Illegal, Unreported, and Unregulated (IUU) Fishing**: Easily enforce fishing quotas and prevent overfishing by tracking each offloaded catch.
    - **Empowering Conservation Bodies**: NGOs, conservation groups, and authorities can finally obtain **quantitative data** with precision, helping to manage resources effectively.
    """
)

st.markdown("##### **Note on Current Solutions**")
st.write(
    """
    - **Onboard monitoring systems**: Costly, unfeasible for many vessels, and access may be restricted.
    - **Manual monitoring**: Inconsistent, subjective, error-prone.
    
    Our solution provides **end-to-end transparency**, making it much more accessible and reliable than existing alternatives.
    """
)

st.markdown("---")

# Section 4: How It Works
st.header("How It Works")
st.subheader("Steps for the Project: The Roadmap")
st.write(
    """
    1. **Image Collection & Training Dataset Development**: Collect diverse images of frozen, processed catches at offloading sites.
        - **Current Stage & Challenge**: Gaining access to private facilities for data collection. We plan to provide **incentives for traders** to allow image collection—sponsorship from NGOs, corporations, or any interested parties would help greatly.
    
    2. **Identifying Distinguishing Characteristics**: Define specific features of processed fish to help train the AI model. Use expert insights to understand how each species can be identified even after processing.
    
    3. **Model Development**: Use **Convolutional Neural Networks (CNNs)** for feature extraction. Develop a regression model to estimate weight using multi-angle images.
    
    4. **Validation and Implementation**: Test the model on-site to ensure reliability. Calibrate with periodic scale measurements to enhance accuracy.
    """
)
st.markdown("##### **Overcoming Challenges**")
st.write(
    """
    - **Depth Cameras and Reference Scaling**: Enhance weight estimation by combining RGB images with depth data.
    - **Data Quality**: Using standardized imaging protocols to ensure the accuracy and consistency of the data.
    """
)

st.markdown("---")

# Section 5: Get Involved
st.header("Get Involved")
st.write(
    """
    The technology to transform longline fisheries is here—but We need support from all possible and passionate parties, such as NGOs, research bodies, corporations, and individuals committed to protecting marine resources.
    
    - **Investment Opportunities**: Directly fund the AI development, deployment, and image collection initiatives.
    - **Research & Collaboration**: Partner with us to bring research expertise into fisheries monitoring.
    - **NGO Sponsorship**: Help provide **incentives** for fisheries and traders, ensuring we can gather the data needed to build this model and transform transparency in seafood supply chains.
    """
)

if st.button(" 👉 Sponsor the Future of Fisheries / Partner with Us 👈 "):
        show_contact_form()


st.markdown("---")

# Section 6: FAQs
st.header("FAQs")

with st.expander("How is this project different from onboard monitoring systems?"):
    st.write("Most vessels lack the facilities to install monitoring systems onboard, and access to these vessels can often be limited. Our solution focuses on **onshore monitoring**—a critical juncture when all catches must be offloaded. Monitoring at the landing point offers an efficient way to ensure compliance without the need for onboard systems.")

with st.expander("Can AI reliably estimate the weight of frozen fish from images?"):
    st.write("Our AI module is aimed at accurately estimating weight using images from multiple angles and depth cameras, even for processed forms (head-off, tail-off). While AI is theoretically capable of achieving this, we are currently focused on data collection, after which we will move to model development and validation to ensure reliability.")

with st.expander("Why not just rely on traditional manual monitoring?"):
    st.write("Manual monitoring is prone to **inconsistencies** and is resource-intensive. AI-based monitoring is scalable, consistent, and capable of processing data much more efficiently.")

with st.expander("How do you deal with variability between species, especially when processed?"):
    st.write("We use a combination of **domain expertise** and advanced **computer vision techniques** to ensure that distinguishing features are adequately captured in the training dataset, allowing the model to differentiate between species accurately.")

st.markdown("---")

# Section 7: About Us
st.header("About Us")
st.write(
    """
    The **Post-Harvest Transparency Initiative** is currently backed by an experienced sponsor from the seafood industry—a professional with **10 years of experience** and a self-taught Python programmer passionate about merging **AI with sustainable practices** in fishing.
    """
)
if st.button("Learn More About Our Sponsor"):
    st.markdown("[Visit LinkedIn Profile](https://www.linkedin.com/in/william-rw-yeh/)")

# st.markdown("---")

# # Contact Us Section
# st.header("Contact Us")
# st.write("**Partner Inquiry**: [partner@postharvesttransparency.com](mailto:partner@postharvesttransparency.com)")
# st.write("**NGO Sponsorship**: [sponsor@postharvesttransparency.com](mailto:sponsor@postharvesttransparency.com)")
# st.write("**General Contact**: [info@postharvesttransparency.com](mailto:info@postharvesttransparency.com)")

# st.markdown("**Follow Us on LinkedIn**")
# st.button("LinkedIn")

st.markdown("---")
st.write("© 2024 Post-Harvest Transparency Initiative")
pip install --upgrade pip
import streamlit as st
import json
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Brand Catalyst - The Social Lab",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Manrope:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Manrope', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    h1 {
        font-family: 'Manrope', sans-serif;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
    }
    
    .tagline {
        font-family: 'Space Mono', monospace;
        color: #a78bfa;
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin-top: -20px;
        margin-bottom: 30px;
    }
    
    .platform-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
    }
    
    .platform-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(102, 126, 234, 0.5);
        transition: all 0.3s ease;
    }
    
    .caption-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        color: white;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 15px 30px;
        font-weight: 700;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
    }
    
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>select {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        color: white;
        padding: 10px;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    }
    
    label {
        color: #c4b5fd !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .success-banner {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        text-align: center;
        font-weight: 700;
    }
    
    .section-header {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 20px;
        border-left: 4px solid #667eea;
        padding-left: 15px;
    }
    
    .image-container {
        border-radius: 12px;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.1);
        margin: 10px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: rgba(255, 255, 255, 0.6);
        font-weight: 600;
        padding: 12px 24px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .feature-badge {
        display: inline-block;
        background: rgba(102, 126, 234, 0.2);
        color: #c4b5fd;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-size: 0.9rem;
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = None
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Header
st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h1>✨ Brand Catalyst - The Social Lab</h1>
    <p class='tagline'>CREATE SMART. MARKET FASTER. GROW BIGGER.</p>
</div>
""", unsafe_allow_html=True)

# Tabs for navigation
tab1, tab2 = st.tabs(["🎨 Create Campaign", "📱 Generated Content"])

with tab1:
    st.markdown("<div class='section-header'>Campaign Basics</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        username = st.text_input("👤 Username", placeholder="Your username", key="username")
        
        st.markdown("**🌐 Select Platform**")
        platform_col1, platform_col2 = st.columns(2)
        with platform_col1:
            instagram = st.button("📷 Instagram", use_container_width=True)
            twitter = st.button("🐦 Twitter", use_container_width=True)
        with platform_col2:
            linkedin = st.button("💼 LinkedIn", use_container_width=True)
            facebook = st.button("👥 Facebook", use_container_width=True)
        
        # Set platform based on button clicks
        if instagram:
            platform = "instagram"
        elif linkedin:
            platform = "linkedin"
        elif twitter:
            platform = "twitter"
        elif facebook:
            platform = "facebook"
        else:
            platform = st.selectbox("Or select from dropdown:", 
                                   ["instagram", "linkedin", "twitter", "facebook"])
        
        company = st.text_input("🏢 Company/Brand Name", placeholder="e.g., SUGAR", key="company")
        event = st.text_input("🎉 Campaign Event", placeholder="e.g., New Skincare Launch", key="event")
        title = st.text_input("📝 Campaign Title", placeholder="e.g., Glow That Speaks", key="title")
    
    with col2:
        product_description = st.text_area(
            "📋 Product Description", 
            placeholder="Describe your product in detail...",
            height=200,
            key="product_description"
        )
    
    st.markdown("<div class='section-header'>Creative Direction</div>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        target_audience = st.text_input(
            "🎯 Target Audience", 
            placeholder="e.g., Women aged 18-35, beauty enthusiasts",
            key="target_audience"
        )
        product_type = st.text_input(
            "💎 Product Type", 
            placeholder="e.g., Hydrating serum",
            key="product_type"
        )
        style = st.text_input(
            "🎨 Visual Style", 
            placeholder="e.g., modern beauty brand aesthetic",
            key="style"
        )
        color_palette = st.text_input(
            "🎨 Color Palette", 
            placeholder="e.g., soft peach, nude pink, warm beige",
            key="color_palette"
        )
    
    with col4:
        campaign_message = st.text_input(
            "💬 Campaign Message", 
            placeholder="e.g., Hydrate. Glow. Repeat.",
            key="campaign_message"
        )
        mood = st.text_input(
            "😊 Mood & Tone", 
            placeholder="e.g., confident, radiant, luxurious",
            key="mood"
        )
        cta = st.text_input(
            "📣 Call to Action", 
            placeholder="e.g., Shop Now",
            key="cta"
        )
        layout = st.text_area(
            "🖼️ Layout Description", 
            placeholder="Describe the desired visual layout...",
            height=100,
            key="layout"
        )
    
    st.markdown("<div class='section-header'>Product Features</div>", unsafe_allow_html=True)
    
    # Dynamic feature inputs
    num_features = st.number_input("Number of features", min_value=1, max_value=10, value=4)
    features = []
    
    feature_cols = st.columns(2)
    for i in range(num_features):
        with feature_cols[i % 2]:
            feature = st.text_input(
                f"Feature {i+1}", 
                placeholder=f"e.g., Deep Hydration Formula",
                key=f"feature_{i}"
            )
            if feature:
                features.append(feature)
    
    st.markdown("<div class='section-header'>Content Options</div>", unsafe_allow_html=True)
    
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("**📸 Content Type**")
        want_images = st.checkbox("Generate Images", value=True)
        want_captions = st.checkbox("Generate Captions", value=True)
    
    with col6:
        st.markdown("**📊 Quantity**")
        num_images = st.slider("Number of Images", min_value=1, max_value=10, value=3)
        num_captions = st.slider("Number of Captions", min_value=1, max_value=10, value=4)
    
    # Generate button
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("✨ Generate Content", use_container_width=True):
        # Collect all form data
        st.session_state.form_data = {
            "username": username,
            "platform": platform,
            "company": company,
            "event": event,
            "title": title,
            "product_description": product_description,
            "brand_name": company,
            "color": color_palette,
            "want_images": want_images,
            "want_captions": want_captions,
            "Target_audience": target_audience,
            "Product": product_type,
            "Style": style,
            "campaign_message": campaign_message,
            "features": features,
            "layout": layout,
            "mood": mood,
            "call_to_action": cta,
            "num_images": num_images,
            "num_captions": num_captions
        }
        
        # Show loading animation
        with st.spinner("🎨 Generating amazing content..."):
            time.sleep(2)  # Simulate API call
            
            # Mock generated content
            st.session_state.generated_content = {
                "captions": [
                    "✨ Discover the secret to radiant skin with our new hydrating serum. Your glow journey starts here. #HydrateGlowRepeat",
                    "Vitamin C meets deep hydration 💧 Our dermatologist-tested formula works for ALL skin types. Ready to glow?",
                    "Why choose between hydration and brightness? Get both with SUGAR's new skincare collection. Shop Now 🌟",
                    "Deep Hydration ✓ Vitamin C Boost ✓ Dermatologist Tested ✓ All Skin Types ✓ Your skin's new best friend is here."
                ],
                "images": [
                    {
                        "url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800&h=800&fit=crop",
                        "alt": "Product showcase"
                    },
                    {
                        "url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=800&h=800&fit=crop",
                        "alt": "Lifestyle shot"
                    },
                    {
                        "url": "https://images.unsplash.com/photo-1570554886111-e80fcca6a029?w=800&h=800&fit=crop",
                        "alt": "Close-up detail"
                    }
                ],
                "platform": platform,
                "brand_name": company,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        st.markdown("<div class='success-banner'>🎉 Content Generated Successfully!</div>", unsafe_allow_html=True)
        st.info("👉 Switch to the 'Generated Content' tab to view your results!")

with tab2:
    if st.session_state.generated_content:
        content = st.session_state.generated_content
        
        # Platform header
        platform_emojis = {
            "instagram": "📷",
            "linkedin": "💼",
            "twitter": "🐦",
            "facebook": "👥"
        }
        
        platform_colors = {
            "instagram": "#E1306C",
            "linkedin": "#0077B5",
            "twitter": "#1DA1F2",
            "facebook": "#4267B2"
        }
        
        emoji = platform_emojis.get(content['platform'], "📱")
        color = platform_colors.get(content['platform'], "#667eea")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 12px; margin-bottom: 30px;
                    border: 2px solid {color}44;'>
            <h2 style='color: white; margin: 0;'>{emoji} {content['platform'].capitalize()} Campaign</h2>
            <p style='color: #c4b5fd; margin: 10px 0 0 0; font-family: "Space Mono", monospace;'>
                {content['brand_name']} • Generated on {content['timestamp']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Export button
        col_export1, col_export2, col_export3 = st.columns([1, 1, 2])
        with col_export1:
            if st.button("📥 Download JSON", use_container_width=True):
                json_str = json.dumps(st.session_state.form_data, indent=2)
                st.download_button(
                    label="💾 Save Campaign Data",
                    data=json_str,
                    file_name=f"campaign_{content['platform']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        with col_export2:
            if st.button("📋 Copy All Captions", use_container_width=True):
                all_captions = "\n\n".join(content['captions'])
                st.code(all_captions, language=None)
        
        # Generated Images
        if st.session_state.form_data.get('want_images', True):
            st.markdown("<div class='section-header'>📸 Generated Images</div>", unsafe_allow_html=True)
            
            img_cols = st.columns(3)
            for idx, img in enumerate(content['images']):
                with img_cols[idx % 3]:
                    st.markdown(f"<div class='image-container'>", unsafe_allow_html=True)
                    st.image(img['url'], caption=img['alt'], use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.download_button(
                        label=f"⬇️ Download Image {idx + 1}",
                        data=img['url'],
                        file_name=f"image_{idx + 1}.jpg",
                        mime="image/jpeg",
                        key=f"download_img_{idx}"
                    )
        
        # Generated Captions
        if st.session_state.form_data.get('want_captions', True):
            st.markdown("<div class='section-header'>✍️ Generated Captions</div>", unsafe_allow_html=True)
            
            for idx, caption in enumerate(content['captions']):
                st.markdown(f"""
                <div class='caption-card'>
                    <p style='font-size: 1.05rem; line-height: 1.6; margin-bottom: 15px;'>{caption}</p>
                    <div style='display: flex; gap: 10px; align-items: center;'>
                        <span class='feature-badge'>Caption {idx + 1}</span>
                        <span style='color: rgba(255, 255, 255, 0.5); font-size: 0.9rem;'>
                            {len(caption)} characters
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"📋 Copy Caption {idx + 1}", key=f"copy_{idx}"):
                    st.code(caption, language=None)
        
        # Analytics/Metrics
        st.markdown("<div class='section-header'>📊 Content Metrics</div>", unsafe_allow_html=True)
        
        metric_cols = st.columns(4)
        with metric_cols[0]:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>{len(content['captions'])}</h3>
                <p style='color: white; margin: 5px 0 0 0;'>Captions</p>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_cols[1]:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>{len(content['images'])}</h3>
                <p style='color: white; margin: 5px 0 0 0;'>Images</p>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_cols[2]:
            avg_length = sum(len(c) for c in content['captions']) // len(content['captions'])
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>{avg_length}</h3>
                <p style='color: white; margin: 5px 0 0 0;'>Avg. Caption Length</p>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_cols[3]:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>{content['platform'].capitalize()}</h3>
                <p style='color: white; margin: 5px 0 0 0;'>Platform</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Product Features Display
        if st.session_state.form_data.get('features'):
            st.markdown("<div class='section-header'>⭐ Product Features</div>", unsafe_allow_html=True)
            features_html = "".join([f"<span class='feature-badge'>{f}</span>" for f in st.session_state.form_data['features']])
            st.markdown(f"<div style='padding: 20px;'>{features_html}</div>", unsafe_allow_html=True)
    
    else:
        st.markdown("""
        <div style='text-align: center; padding: 60px 20px; color: rgba(255, 255, 255, 0.6);'>
            <h2 style='color: rgba(255, 255, 255, 0.8);'>No Content Generated Yet</h2>
            <p style='font-size: 1.1rem; margin-top: 20px;'>
                Head over to the "Create Campaign" tab and generate your first social media content! ✨
            </p>
        </div>
        """, unsafe_allow_html=True)

# Sidebar with additional info
with st.sidebar:
    st.markdown("### 📚 About")
    st.markdown("""
    **Brand Catalyst - The Social Lab** uses advanced AI to generate professional social media content 
    tailored to your brand and campaign needs.
    """)
    
    st.markdown("### 🎯 Supported Platforms")
    st.markdown("""
    - 📷 Instagram
    - 💼 LinkedIn
    - 🐦 Twitter
    - 👥 Facebook
    """)
    
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Be specific in your product description
    - Define your target audience clearly
    - Use descriptive visual style keywords
    - Include 3-5 key product features
    """)
    
    st.markdown("### 👥 Team")
    st.markdown("""
    - Alex Jefferson
    - Lindsay Stephenson
    - Iyanu Kofoworade
    - Anudnya Khandekar
    - Aarya Joshi
    - Yogith Sai Meda
    """)
    
    st.markdown("---")
    st.markdown("*Georgia State University - CIS Department*")

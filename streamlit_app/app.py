import streamlit as st
from PIL import Image
import numpy as np
from pathlib import Path
import tensorflow as tf

st.set_page_config(
    page_title="Bone Age Estimator",
    page_icon="🦴",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stTitle {
        color: #58a6ff;
    }
    .stMarkdown, .stWrite, .stCaption {
        color: #c9d1d9;
    }
    .stInfo {
        background-color: #161b22;
        color: #c9d1d9;
    }
    .stError {
        background-color: #21262d;
        color: #f85149;
    }
    .stSuccess {
        background-color: #161b22;
    }
    .stSpinner {
        color: #58a6ff;
    }
    .prediction-box {
        background-color: #1a2e1a;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 15px auto;
        border: 2px solid #3d8b3d;
        width: 70%;
    }
    .category-box {
        background-color: #1f2d1f;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #3d8b3d;
        width: 50%;
        margin: 10px auto;
    }
    .instruction-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3d8b3d;
    }
    div[data-testid="stFileUploader"] {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
    }
    .stFileUploader label {
        color: #c9d1d9;
    }
    hr {
        border-color: #30363d;
    }
    div[data-testid="stImage"] {
        background-color: #161b22;
        padding: 10px;
        border-radius: 10px;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
    div[data-testid="stImage"] img {
        width: 80%;
        max-width: 80%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🦴 Estimation de l'age osseux")
st.markdown("### Projet Deep Learning - RSNA Bone Age")
st.divider()

MODEL_PATH = Path(__file__).parent.parent / 'models' / 'bone_age_model.keras'
IMAGE_SIZE = (224, 224)

@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modele: {e}")
        return None

def preprocess_image(image: Image.Image):
    """Preprocess image: resize, normalize to [0, 1], and add batch dimension"""
    img = image.resize(IMAGE_SIZE)
    img = np.array(img, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

st.markdown("### 📤 Importer une radiographie")
uploaded_file = st.file_uploader("Cliquer pour selectionner une image (PNG, JPG, JPEG)", 
                                   type=["png", "jpg", "jpeg"])

st.divider()

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    
    st.image(image, caption="Radiographie chargee", use_container_width=True)
    
    model = load_model()
    
    if model is not None:
        with st.spinner('Analyse en cours...'):
            processed = preprocess_image(image)
            prediction = model.predict(processed, verbose=0)[0][0]
            prediction = max(0, prediction)
        
        st.markdown(f"""
        <div class="prediction-box">
            <h2 style="color: #7dcea0;">🦴 Age osseux predit</h2>
            <h1 style="color: #7dcea0; font-size: 48px;">{int(prediction)} mois</h1>
            <p style="font-size: 20px; color: #a5d6a7;">Equivalent: <b>{prediction/12:.1f} ans</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        if prediction < 60:
            category = "Bebe / Jeune enfant"
        elif prediction < 120:
            category = "Enfant"
        elif prediction < 144:
            category = "Pre-adolescent"
        else:
            category = "Adolescent"
        
        st.markdown(f"""
        <div class="category-box">
            <span style="color: #a5d6a7;"><b>Categorie:</b> {category}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ Modele non trouve. Verifier le fichier 'bone_age_model.keras'.")
else:
    st.markdown("""
    <div class="instruction-box">
        <span style="color: #a5d6a7;"><b>💡 Comment importer une image:</b><br>
        1. Copier l'image de la radiographie<br>
        2. L'enregistrer sur votre ordinateur (clic droit > Enregistrer sous)<br>
        3. Cliquer sur 'Browse files' ci-dessus<br>
        4. Selectionner le fichier enregistre</span>
    </div>
    """, unsafe_allow_html=True)
    st.info("👆 Importer une radiographie de la main gauche pour debuter l'analyse.")
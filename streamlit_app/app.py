import streamlit as st
from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import tensorflow as tf

st.set_page_config(
    page_title="BoneAge AI",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #f5f8fc;
        --surface: #ffffff;
        --surface-alt: #f8fbff;
        --border: #dbe4f0;
        --text: #102033;
        --muted: #5f7086;
        --primary: #1f5fa8;
        --primary-dark: #173f6d;
        --accent: #18a6b9;
        --success: #0f7c66;
        --shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
        --shadow-soft: 0 10px 24px rgba(31, 95, 168, 0.08);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(24, 166, 185, 0.08), transparent 32%),
            radial-gradient(circle at top right, rgba(31, 95, 168, 0.08), transparent 28%),
            linear-gradient(180deg, #f7fafc 0%, #eef4fb 100%);
        color: var(--text);
        font-family: 'Source Sans 3', 'Segoe UI', system-ui, -apple-system, sans-serif;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2.5rem;
        max-width: 1180px;
    }

    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: var(--text);
    }

    h1, h2, h3 {
        letter-spacing: -0.02em;
    }

    .hero-card {
        position: relative;
        overflow: hidden;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(219, 228, 240, 0.9);
        border-radius: 24px;
        padding: 30px 32px;
        box-shadow: var(--shadow);
        backdrop-filter: blur(8px);
    }

    .hero-card::after {
        content: '';
        position: absolute;
        inset: auto -10% -55% auto;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(31, 95, 168, 0.10), transparent 68%);
        pointer-events: none;
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 12px;
        border-radius: 999px;
        background: #eef5fd;
        color: var(--primary-dark);
        font-size: 0.83rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-bottom: 14px;
    }

    .hero-title {
        font-size: clamp(2rem, 3vw, 3.2rem);
        line-height: 1.05;
        font-weight: 800;
        margin: 0 0 10px 0;
        color: #0b1b33;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: var(--muted);
        margin: 0;
        max-width: 760px;
    }

    .hero-row {
        display: grid;
        grid-template-columns: minmax(0, 1.2fr) minmax(280px, 0.8fr);
        gap: 20px;
        align-items: end;
    }

    .hero-card-right {
        position: relative;
        z-index: 1;
        display: grid;
        gap: 10px;
    }

    .mini-panel {
        background: linear-gradient(180deg, #f9fcff 0%, #eef6fd 100%);
        border: 1px solid #d8e6f3;
        border-radius: 18px;
        padding: 14px 16px;
        box-shadow: var(--shadow-soft);
    }

    .mini-panel-title {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        margin-bottom: 6px;
        font-weight: 700;
    }

    .mini-panel-value {
        font-size: 0.98rem;
        color: #13263c;
        font-weight: 700;
        line-height: 1.35;
    }

    .section-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 22px;
        box-shadow: var(--shadow);
    }

    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 16px;
    }

    .workflow-strip {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
        margin-top: 18px;
    }

    .workflow-step {
        background: #f9fcff;
        border: 1px solid #d9e6f2;
        border-radius: 18px;
        padding: 14px 16px;
    }

    .workflow-step-index {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: #eaf3fb;
        color: var(--primary-dark);
        font-weight: 800;
        margin-bottom: 10px;
    }

    .workflow-step-title {
        font-size: 0.96rem;
        font-weight: 700;
        margin-bottom: 4px;
        color: #10223f;
    }

    .workflow-step-copy {
        font-size: 0.88rem;
        color: var(--muted);
        line-height: 1.45;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0;
        color: #10223f;
    }

    .section-note {
        font-size: 0.92rem;
        color: var(--muted);
        margin: 4px 0 0 0;
    }

    .upload-card {
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.96) 0%, rgba(250, 253, 255, 0.98) 100%),
            linear-gradient(135deg, rgba(31, 95, 168, 0.04), rgba(24, 166, 185, 0.05));
        border: 1.5px dashed #bfd0e3;
        border-radius: 22px;
        padding: 26px;
    }

    div[data-testid="stFileUploader"] {
        background: transparent;
        border: none;
        padding: 0;
    }

    div[data-testid="stFileUploader"] section {
        border: 1px solid #cfdceb;
        border-radius: 20px;
        background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
        padding: 18px;
        box-shadow: var(--shadow-soft);
    }

    div[data-testid="stFileUploader"] button {
        background: var(--primary);
        color: white;
        border: none;
        border-radius: 12px;
    }

    div[data-testid="stFileUploader"] button:hover {
        background: var(--primary-dark);
        color: white;
    }

    .preview-frame {
        background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 20px;
        box-shadow: var(--shadow);
    }

    .preview-image-wrap {
        margin-top: 8px;
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid #dfe8f1;
        background: #f6fbff;
    }

    .meta-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
        margin-top: 16px;
    }

    .meta-item {
        background: var(--surface-alt);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 14px 16px;
    }

    .meta-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        margin-bottom: 4px;
        font-weight: 700;
    }

    .meta-value {
        font-size: 0.98rem;
        font-weight: 700;
        color: #12263f;
    }

    .cta-row {
        display: flex;
        gap: 12px;
        align-items: center;
        justify-content: flex-start;
        flex-wrap: wrap;
        margin-top: 16px;
    }

    div.stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, #255f93 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.8rem 1.2rem;
        font-weight: 700;
        min-height: 52px;
        box-shadow: 0 12px 24px rgba(31, 95, 168, 0.18);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #255f93 0%, var(--primary-dark) 100%);
        color: white;
    }

    .result-card {
        position: relative;
        overflow: hidden;
        background: linear-gradient(180deg, #ffffff 0%, #f8fcff 100%);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 24px;
        box-shadow: var(--shadow);
    }

    .result-card::before {
        content: '';
        position: absolute;
        inset: 0 auto 0 0;
        width: 6px;
        background: linear-gradient(180deg, var(--primary) 0%, var(--accent) 100%);
    }

    .result-label {
        font-size: 0.92rem;
        font-weight: 700;
        color: var(--primary-dark);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 8px;
    }

    .result-value {
        font-size: clamp(2.6rem, 5vw, 4.4rem);
        line-height: 1;
        font-weight: 800;
        color: #0b1b33;
        margin: 0;
    }

    .result-subvalue {
        font-size: 1.05rem;
        color: var(--muted);
        margin-top: 10px;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 14px;
        border-radius: 999px;
        background: #edf7fb;
        color: var(--primary-dark);
        font-weight: 700;
        font-size: 0.9rem;
        border: 1px solid #d6e7f5;
    }

    .hint-card {
        background: #f8fbfe;
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 18px 20px;
        color: var(--muted);
    }

    .helper-line {
        display: flex;
        align-items: center;
        gap: 10px;
        color: var(--muted);
        font-size: 0.95rem;
        margin-top: 10px;
    }

    .helper-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 5px rgba(24, 166, 185, 0.12);
        flex: none;
    }

    .footer-note {
        margin-top: 18px;
        text-align: center;
        color: var(--muted);
        font-size: 0.88rem;
    }

    .spacer-sm { height: 0.5rem; }

    @media (max-width: 768px) {
        .hero-card, .section-card, .preview-frame, .result-card {
            padding: 18px;
        }

        .meta-grid {
            grid-template-columns: 1fr;
        }

        .workflow-strip,
        .hero-row {
            grid-template-columns: 1fr;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero-card">
    <div class="hero-row">
        <div>
            <div class="eyebrow">AI-powered radiographic analysis</div>
            <h1 class="hero-title">BoneAge AI</h1>
            <p class="hero-subtitle">Deep Learning-Based Bone Age Estimation</p>
            <div class="helper-line"><span class="helper-dot"></span><span>Upload a hand X-ray image to estimate bone age using a deep learning model.</span></div>
        </div>
        <div class="hero-card-right">
            <div class="mini-panel">
                <div class="mini-panel-title">Workflow</div>
                <div class="mini-panel-value">Upload an image, run the analysis, review the estimate.</div>
            </div>
            <div class="mini-panel">
                <div class="mini-panel-title">Model</div>
                <div class="mini-panel-value">Trained bone age estimator loaded locally from .keras weights.</div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

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


def iter_layers(layer):
    yield layer
    if hasattr(layer, 'layers'):
        for sublayer in layer.layers:
            yield from iter_layers(sublayer)


def find_last_conv_layer_name(model):
    candidate_name = None
    for layer in iter_layers(model):
        if isinstance(layer, (tf.keras.layers.Conv2D, tf.keras.layers.DepthwiseConv2D, tf.keras.layers.SeparableConv2D)):
            candidate_name = layer.name
    return candidate_name


def find_layer_by_name(model, layer_name):
    for layer in iter_layers(model):
        if layer.name == layer_name:
            return layer
    return None


def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    last_conv_layer = find_layer_by_name(model, last_conv_layer_name)
    if last_conv_layer is None:
        raise ValueError(f'Layer not found: {last_conv_layer_name}')

    grad_model = tf.keras.Model(
        model.inputs,
        [last_conv_layer.output, model.output],
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = 0
        class_output = predictions[:, pred_index]

    grads = tape.gradient(class_output, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ tf.expand_dims(pooled_grads, axis=-1)
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0)
    max_value = tf.reduce_max(heatmap)
    if tf.equal(max_value, 0):
        return np.zeros(heatmap.shape, dtype=np.float32)
    heatmap /= max_value
    return heatmap.numpy()


def build_gradcam_overlay(image: Image.Image, heatmap: np.ndarray):
    base_image = image.resize(IMAGE_SIZE).convert('RGB')
    base_array = np.array(base_image, dtype=np.float32) / 255.0

    heatmap_resized = tf.image.resize(heatmap[..., np.newaxis], IMAGE_SIZE).numpy().squeeze()
    colored_heatmap = plt.get_cmap('jet')(heatmap_resized)[..., :3]
    overlay = np.clip((0.58 * base_array) + (0.42 * colored_heatmap), 0, 1)
    return (overlay * 255).astype(np.uint8), (colored_heatmap * 255).astype(np.uint8)

st.markdown(
    """
<div class="section-card">
    <div class="section-header">
        <div>
            <p class="section-title">Upload Hand X-Ray</p>
            <p class="section-note">PNG, JPG or JPEG</p>
        </div>
        <div class="status-pill">Medical imaging input</div>
    </div>
    <div class="upload-card">
        <div class="workflow-strip">
            <div class="workflow-step">
                <div class="workflow-step-index">1</div>
                <div class="workflow-step-title">Upload</div>
                <div class="workflow-step-copy">Select a radiography file from your device.</div>
            </div>
            <div class="workflow-step">
                <div class="workflow-step-index">2</div>
                <div class="workflow-step-title">Analyze</div>
                <div class="workflow-step-copy">Use the model to estimate bone age from the image.</div>
            </div>
            <div class="workflow-step">
                <div class="workflow-step-index">3</div>
                <div class="workflow-step-title">Review</div>
                <div class="workflow-step-copy">Read the result and simple clinical interpretation.</div>
            </div>
        </div>
        <div class="spacer-sm"></div>
""",
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Drop an X-ray image here or browse files",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed",
)

st.markdown("</div></div>", unsafe_allow_html=True)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image_format = (uploaded_file.name.split('.')[-1] or '').upper()
    image_width, image_height = image.size

    left_col, right_col = st.columns([1.15, 0.85], gap="large")

    with left_col:
        st.markdown(
            """
            <div class="preview-frame">
                <div class="section-header">
                    <div>
                        <p class="section-title">X-Ray Preview</p>
                        <p class="section-note">Review the uploaded radiograph before running the analysis.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="preview-image-wrap">', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-header">
                    <div>
                        <p class="section-title">Image Details</p>
                        <p class="section-note">Simple technical information about the uploaded file.</p>
                    </div>
                </div>
                <div class="meta-grid">
                    <div class="meta-item">
                        <div class="meta-label">Status</div>
                        <div class="meta-value">Image loaded</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Format</div>
                        <div class="meta-value">{image_format or 'UNKNOWN'}</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-label">Dimensions</div>
                        <div class="meta-value">{image_width} × {image_height}px</div>
                    </div>
                </div>
                <div class="spacer-sm"></div>
                <div class="hint-card">
                    Upload completed. Click the primary action below to run the model inference.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
    action_col, _ = st.columns([0.42, 0.58])
    with action_col:
        estimate_clicked = st.button("Estimate Bone Age", use_container_width=True)

    if estimate_clicked:
        model = load_model()

        if model is not None:
            processed = preprocess_image(image)
            with st.status("Analyzing X-Ray...", expanded=False):
                prediction = model.predict(processed, verbose=0)[0][0]
                prediction = max(0, prediction)

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Estimated Bone Age</div>
                    <div class="result-value">{int(round(prediction))} months</div>
                    <div class="result-subvalue">Bone age estimate generated by the trained model.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            last_conv_layer_name = find_last_conv_layer_name(model)
            if last_conv_layer_name is not None:
                st.markdown(
                    f"""
                    <div class="section-card" style="margin-top: 16px;">
                        <div class="section-header">
                            <div>
                                <p class="section-title">Grad-CAM Visualization</p>
                                <p class="section-note">Highlighting regions that contributed most to the estimate.</p>
                            </div>
                            <div class="status-pill">Last conv layer: {last_conv_layer_name}</div>
                        </div>
                    """,
                    unsafe_allow_html=True,
                )

                show_gradcam = st.button("Generate Grad-CAM", use_container_width=True)
                if show_gradcam:
                    heatmap = make_gradcam_heatmap(processed, model, last_conv_layer_name)
                    overlay_image, heatmap_image = build_gradcam_overlay(image, heatmap)

                    gradcam_left, gradcam_right = st.columns(2, gap="medium")
                    with gradcam_left:
                        st.image(overlay_image, caption="Grad-CAM overlay", use_container_width=True)
                    with gradcam_right:
                        st.image(heatmap_image, caption="Heatmap", use_container_width=True)

                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("Grad-CAM not available for this model architecture.")

            if prediction < 60:
                category = "Bebe / Jeune enfant"
            elif prediction < 120:
                category = "Enfant"
            elif prediction < 144:
                category = "Pre-adolescent"
            else:
                category = "Adolescent"

            st.markdown(
                f"""
                <div class="section-card" style="margin-top: 16px;">
                    <div class="section-header">
                        <div>
                            <p class="section-title">Clinical Interpretation</p>
                            <p class="section-note">A simple age category derived from the estimated bone age.</p>
                        </div>
                    </div>
                    <div class="status-pill">Category: {category}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error("Modele non trouve. Verifier le fichier 'bone_age_model.keras'.")
else:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-header">
                <div>
                    <p class="section-title">Getting Started</p>
                    <p class="section-note">Upload a hand X-ray to begin the analysis workflow.</p>
                </div>
            </div>
            <div class="hint-card">
                The interface is designed to keep the workflow simple: upload an image, preview it, then run the estimate.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="footer-note">Built for fast, clear, and private bone age review.</div>
    """,
    unsafe_allow_html=True,
)
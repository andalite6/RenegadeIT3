# ================================================================
# RENEGADE SECURITY EXPERT - AI SECURITY & SUSTAINABILITY SUPER APP
# ================================================================
# "To catch a hacker, you need to think like one. But to outsmart them,
# you need to be better than they ever dreamed of being." - RSE
# ================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
import time
import logging
import os
import threading
import random
import base64
import traceback
from datetime import datetime, timedelta
from io import BytesIO

# ----------------------------------------------------------------
# CONFIGURATE THE WAR ROOM - No half measures, no weak signals
# ----------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [MAVERICK] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("renegade_security.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("RenegadeSecurity")

# Set page configuration with attitude
st.set_page_config(
    page_title="Renegade Security Expert",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------
# SESSION STATE - Where we track all the moves they think we don't see
# ----------------------------------------------------------------

def initialize_session_state():
    """Set up the battleground. You can't catch what you can't track."""
    try:
        # Core intelligence assets
        if 'targets' not in st.session_state:
            st.session_state.targets = []

        if 'test_results' not in st.session_state:
            st.session_state.test_results = {}

        if 'running_test' not in st.session_state:
            st.session_state.running_test = False

        if 'progress' not in st.session_state:
            st.session_state.progress = 0

        if 'vulnerabilities_found' not in st.session_state:
            st.session_state.vulnerabilities_found = 0

        if 'current_theme' not in st.session_state:
            st.session_state.current_theme = "dark"  # We work best in the shadows
            
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Dashboard"
            
        # Thread management - like herding cats, but deadlier
        if 'active_threads' not in st.session_state:
            st.session_state.active_threads = []
            
        # Error handling - because even mavericks make mistakes
        if 'error_message' not in st.session_state:
            st.session_state.error_message = None
            
        # Initialize bias hunting tools
        if 'bias_results' not in st.session_state:
            st.session_state.bias_results = {}
            
        if 'show_bias_results' not in st.session_state:
            st.session_state.show_bias_results = False
            
        # Carbon tracking - because we fight dirty, not dirty planet
        if 'carbon_tracking_active' not in st.session_state:
            st.session_state.carbon_tracking_active = False
            
        if 'carbon_measurements' not in st.session_state:
            st.session_state.carbon_measurements = []
            
        # Integration states - for when we need to bring in the cavalry
        if 'engine_room_initialized' not in st.session_state:
            st.session_state.engine_room_initialized = False
            
        if 'bias_labs_enabled' not in st.session_state:
            st.session_state.bias_labs_enabled = False
            
        if 'sustainability_integrated' not in st.session_state:
            st.session_state.sustainability_integrated = False
            
        logger.info("Battlefield initialized. Let the games begin.")
    except Exception as e:
        logger.error(f"Failed to set up the war room: {str(e)}")
        display_error(f"System initialization failure. We've been compromised: {str(e)}")

# Thread cleanup - We don't leave soldiers behind
def cleanup_threads():
    """Clean up the mess. Leave no trace."""
    try:
        if 'active_threads' in st.session_state:
            # Filter out the fallen soldiers
            active_threads = []
            for thread in st.session_state.active_threads:
                if thread.is_alive():
                    active_threads.append(thread)
            
            # Update our roster with only the ones still breathing
            st.session_state.active_threads = active_threads
            
            if len(st.session_state.active_threads) > 0:
                logger.info(f"Active operatives: {len(st.session_state.active_threads)}")
    except Exception as e:
        logger.error(f"Thread cleanup failed. We've got leaks: {str(e)}")

# ----------------------------------------------------------------
# UI THEMES - Because even rebels have style
# ----------------------------------------------------------------

# Define color schemes
themes = {
    "dark": {
        "bg_color": "#121212",
        "card_bg": "#1E1E1E",
        "primary": "#FF5722",    # Maverick orange
        "secondary": "#BB86FC",  # Purple
        "accent": "#03DAC6",     # Teal
        "warning": "#FFC107",    # Amber
        "error": "#F44336",      # Red
        "text": "#FFFFFF"
    },
    "light": {
        "bg_color": "#F5F5F5",
        "card_bg": "#FFFFFF",
        "primary": "#FF5722",    # Maverick orange
        "secondary": "#7C4DFF",  # Deep purple
        "accent": "#00BCD4",     # Cyan
        "warning": "#FFC107",    # Amber
        "error": "#F44336",      # Red
        "text": "#212121"
    }
}

# Get current theme colors safely
def get_theme():
    """Get current theme. Style matters when you're hunting exploits."""
    try:
        return themes[st.session_state.current_theme]
    except Exception as e:
        logger.error(f"Theme retrieval failed. Using default: {str(e)}")
        # Return dark theme as fallback - we work best in shadows
        return themes["dark"]

# CSS styles - The warpaint of digital warriors
def load_css():
    """Load CSS. Look good while doing bad things to bad people."""
    try:
        theme = get_theme()
        
        return f"""
        <style>
        .main .block-container {{
            padding-top: 1rem;
            padding-bottom: 1rem;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: {theme["primary"]};
            font-weight: bold;
        }}
        
        .stProgress > div > div > div > div {{
            background-color: {theme["primary"]};
        }}
        
        div[data-testid="stExpander"] {{
            border: none;
            border-radius: 8px;
            background-color: {theme["card_bg"]};
            margin-bottom: 1rem;
        }}
        
        div[data-testid="stVerticalBlock"] {{
            gap: 1.5rem;
        }}
        
        .card {{
            border-radius: 10px;
            background-color: {theme["card_bg"]};
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 3px solid {theme["primary"]};
        }}
        
        .warning-card {{
            border-left: 3px solid {theme["warning"]};
        }}
        
        .error-card {{
            border-left: 3px solid {theme["error"]};
        }}
        
        .success-card {{
            border-left: 3px solid {theme["primary"]};
        }}
        
        .metric-value {{
            font-size: 32px;
            font-weight: bold;
            color: {theme["primary"]};
        }}
        
        .metric-label {{
            font-size: 14px;
            color: {theme["text"]};
            opacity: 0.7;
        }}
        
        .sidebar-title {{
            margin-left: 15px;
            font-size: 1.2rem;
            font-weight: bold;
            color: {theme["primary"]};
        }}
        
        .target-card {{
            border-radius: 8px;
            background-color: {theme["card_bg"]};
            padding: 1rem;
            margin-bottom: 1rem;
            border-left: 3px solid {theme["secondary"]};
        }}
        
        .status-badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }}
        
        .status-badge.active {{
            background-color: {theme["primary"]};
            color: white;
        }}
        
        .status-badge.inactive {{
            background-color: gray;
            color: white;
        }}
        
        .hover-card:hover {{
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transform: translateY(-2px);
            transition: all 0.3s ease;
        }}
        
        .card-title {{
            color: {theme["primary"]};
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .nav-item {{
            padding: 8px 15px;
            border-radius: 5px;
            margin-bottom: 5px;
            cursor: pointer;
        }}
        
        .nav-item:hover {{
            background-color: rgba(255, 87, 34, 0.1);
        }}
        
        .nav-item.active {{
            background-color: rgba(255, 87, 34, 0.2);
            font-weight: bold;
        }}
        
        .tag {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .tag.owasp {{
            background-color: rgba(187, 134, 252, 0.2);
            color: {theme["secondary"]};
        }}
        
        .tag.nist {{
            background-color: rgba(3, 218, 198, 0.2);
            color: {theme["accent"]};
        }}
        
        .tag.fairness {{
            background-color: rgba(255, 193, 7, 0.2);
            color: {theme["warning"]};
        }}
        
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            height: 50px;
            border-radius: 5px 5px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: {theme["card_bg"]};
            border-bottom: 3px solid {theme["primary"]};
        }}
        
        .error-message {{
            background-color: #F44336;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        
        /* Modern sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {theme["card_bg"]};
            border-right: 1px solid rgba(0,0,0,0.1);
        }}
        
        /* Modern navigation categories */
        .nav-category {{
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            color: {theme["text"]};
            opacity: 0.6;
            margin: 10px 15px 5px 15px;
        }}
        
        /* Main content area padding */
        .main-content {{
            padding: 20px;
        }}
        
        /* Modern cards with hover effects */
        .modern-card {{
            background-color: {theme["card_bg"]};
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
            transition: all 0.3s ease;
            border-left: none;
            border-top: 4px solid {theme["primary"]};
        }}
        
        .modern-card:hover {{
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            transform: translateY(-5px);
        }}
        
        .modern-card.warning {{
            border-top: 4px solid {theme["warning"]};
        }}
        
        .modern-card.error {{
            border-top: 4px solid {theme["error"]};
        }}
        
        .modern-card.secondary {{
            border-top: 4px solid {theme["secondary"]};
        }}
        
        .modern-card.accent {{
            border-top: 4px solid {theme["accent"]};
        }}
        
        /* App header styles */
        .app-header {{
            display: flex;
            align-items: center;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .app-title {{
            font-size: 24px;
            font-weight: bold;
            margin: 0;
            color: {theme["primary"]};
        }}
        
        .app-subtitle {{
            font-size: 14px;
            opacity: 0.7;
            margin: 0;
        }}
        
        /* Renegade special additions */
        .renegade-quote {{
            font-style: italic;
            border-left: 3px solid {theme["primary"]};
            padding-left: 10px;
            margin: 15px 0;
            opacity: 0.85;
        }}
        
        .vulnerability-counter {{
            background-color: {theme["primary"]};
            color: white;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-right: 10px;
        }}
        
        .hacker-alert {{
            background-color: rgba(244, 67, 54, 0.1);
            border-left: 3px solid {theme["error"]};
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }}
        </style>
        """
    except Exception as e:
        logger.error(f"CSS loading failed. Flying ugly: {str(e)}")
        # Return minimal CSS as fallback
        return "<style>.error-message { background-color: #F44336; color: white; padding: 10px; border-radius: 5px; margin-bottom: 20px; }</style>"

# ----------------------------------------------------------------
# NAVIGATION - Shift like quicksilver between battlegrounds
# ----------------------------------------------------------------

# Helper function to set page
def set_page(page_name):
    """Navigate to new battleground. Always keep moving."""
    try:
        st.session_state.current_page = page_name
        logger.info(f"Maverick repositioning to: {page_name} zone")
    except Exception as e:
        logger.error(f"Navigation failure to {page_name}: {str(e)}")
        display_error(f"Failed to reach {page_name}. Route compromised.")

# Safe rerun function - Because sometimes you gotta pull the trigger twice
def safe_rerun():
    """Reload the battlefield. Sometimes you gotta hit refresh."""
    try:
        st.rerun()  # For newer Streamlit versions
    except Exception as e1:
        try:
            st.experimental_rerun()  # For older Streamlit versions
        except Exception as e2:
            logger.error(f"Rerun failed: {str(e1)} then {str(e2)}")
            # We're stuck. Keep your cool.

# Error handling - When things break, break them better
def display_error(message):
    """Display error message. Don't sugarcoat it."""
    try:
        st.session_state.error_message = message
        logger.error(f"BREACH DETECTED: {message}")
    except Exception as e:
        logger.critical(f"Critical failure in error display. We're flying blind: {str(e)}")

# ----------------------------------------------------------------
# CUSTOM UI COMPONENTS - Our special weapons
# ----------------------------------------------------------------

# Custom components
def card(title, content, card_type="default"):
    """Generate HTML card. Data needs packaging."""
    try:
        card_class = "card"
        if card_type == "warning":
            card_class += " warning-card"
        elif card_type == "error":
            card_class += " error-card"
        elif card_type == "success":
            card_class += " success-card"
        
        return f"""
        <div class="{card_class} hover-card">
            <div class="card-title">{title}</div>
            {content}
        </div>
        """
    except Exception as e:
        logger.error(f"Card rendering fail: {str(e)}")
        return f"""
        <div class="card error-card">
            <div class="card-title">Card Failure</div>
            <p>Card crashed and burned: {str(e)}</p>
        </div>
        """

def modern_card(title, content, card_type="default", icon=None):
    """Generate a modern card. Style with substance."""
    try:
        card_class = "modern-card"
        if card_type == "warning":
            card_class += " warning"
        elif card_type == "error":
            card_class += " error"
        elif card_type == "secondary":
            card_class += " secondary"
        elif card_type == "accent":
            card_class += " accent"
        
        icon_html = f'<span style="margin-right: 8px;">{icon}</span>' if icon else ''
        
        return f"""
        <div class="{card_class}">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                {icon_html}
                <div class="card-title">{title}</div>
            </div>
            <div>{content}</div>
        </div>
        """
    except Exception as e:
        logger.error(f"Modern card malfunction: {str(e)}")
        return f"""
        <div class="modern-card error">
            <div class="card-title">Card Failure</div>
            <p>Card self-destructed: {str(e)}</p>
        </div>
        """

def metric_card(label, value, description="", prefix="", suffix=""):
    """Generate metric card. Numbers don't lie, people do."""
    try:
        return f"""
        <div class="modern-card hover-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{prefix}{value}{suffix}</div>
            <div style="font-size: 14px; opacity: 0.7;">{description}</div>
        </div>
        """
    except Exception as e:
        logger.error(f"Metric card crash: {str(e)}")
        return f"""
        <div class="modern-card error">
            <div class="metric-label">Error</div>
            <div class="metric-value">N/A</div>
            <div style="font-size: 14px; opacity: 0.7;">Metric malfunction: {str(e)}</div>
        </div>
        """

# Maverick quotes - Inspiration for the hunt
maverick_quotes = [
    "To catch a hacker, you need to think like one. But to outsmart them, you need to be better than they ever dreamed of being.",
    "Systems aren't broken by accidents. They're broken by people who spent more time thinking about them than their creators did.",
    "Security isn't about building walls. It's about knowing exactly where they'll try to climb over and waiting for them there.",
    "The best traps aren't the ones that stop attacks. They're the ones that make attackers reveal themselves.",
    "I don't play by the rulebook because the people I'm hunting burned theirs a long time ago.",
    "If you understand the exploits better than the exploiters, you've already won half the battle.",
    "Predictable security is already broken. Be the chaos they don't expect.",
    "You don't catch breaches with compliance checklists. You catch them by thinking three steps ahead of someone thinking two steps ahead of you.",
    "The best security isn't about stopping every attack. It's about making sure the ones that succeed tell you everything you need to know.",
    "If you want to protect a system, first figure out every possible way to break it."
]

# Logo and header
def render_header():
    """Render the header. First impressions matter."""
    try:
        quote = random.choice(maverick_quotes)
        logo_html = f"""
        <div class="app-header">
            <div style="margin-right: 15px; font-size: 2.5rem;">⚔️</div>
            <div>
                <div class="app-title">Renegade Security Expert</div>
                <div class="app-subtitle">Breaking systems to save them. Finding flaws before they become failures.</div>
            </div>
        </div>
        <div class="renegade-quote">{quote}</div>
        """
        st.markdown(logo_html, unsafe_allow_html=True)
    except Exception as e:
        logger.error(f"Header rendering failed: {str(e)}")
        st.markdown("# ⚔️ Renegade Security Expert")

# ----------------------------------------------------------------
# SIDEBAR NAVIGATION - Command & Control Center
# ----------------------------------------------------------------

def sidebar_navigation():
    """Render the sidebar navigation. Your mission control center."""
    try:
        st.sidebar.markdown('<div class="sidebar-title">Renegade Security Expert</div>', unsafe_allow_html=True)
        
        # Organize navigation options by category
        navigation_categories = {
            "Hunt & Capture": [
                {"icon": "🎯", "name": "Dashboard"},
                {"icon": "📡", "name": "Target Management"},
                {"icon": "🧪", "name": "Test Configuration"},
                {"icon": "⚡", "name": "Run Assessment"},
                {"icon": "📊", "name": "Results Analyzer"}
            ],
            "Ethics Arsenal": [
                {"icon": "🔍", "name": "Ethical AI Testing"},
                {"icon": "⚖️", "name": "Bias Testing"},
                {"icon": "📏", "name": "Bias Comparison"},
                {"icon": "🔬", "name": "Bias Labs Integration"},
                {"icon": "🧠", "name": "HELM Evaluation"}
            ],
            "Green Operations": [
                {"icon": "🌱", "name": "Environmental Impact"},
                {"icon": "🌍", "name": "Sustainability Dashboard"},
                {"icon": "♻️", "name": "Sustainability Integration"}
            ],
            "Special Weapons": [
                {"icon": "📁", "name": "Multi-Format Import"},
                {"icon": "🚀", "name": "High-Volume Testing"},
                {"icon": "🔌", "name": "Engine Room Integration"},
                {"icon": "📚", "name": "Knowledge Base"},
                {"icon": "📝", "name": "HTML Portal"},
                {"icon": "🏛️", "name": "AI Safety Standards"},
                {"icon": "📊", "name": "Model Evaluation"}
            ],
            "Command Center": [
                {"icon": "⚙️", "name": "Settings"}
            ]
        }
        
        # Render each category and its navigation options
        for category, options in navigation_categories.items():
            st.sidebar.markdown(f'<div class="nav-category">{category}</div>', unsafe_allow_html=True)
            
            for option in options:
                # Create a button for each navigation option
                if st.sidebar.button(
                    f"{option['icon']} {option['name']}", 
                    key=f"nav_{option['name']}",
                    use_container_width=True,
                    type="secondary" if st.session_state.current_page != option["name"] else "primary"
                ):
                    set_page(option["name"])
                    safe_rerun()
        
        # Theme toggle - darkness is our ally, but sometimes we work in the light
        st.sidebar.markdown("---")
        st.sidebar.markdown('<div class="sidebar-title">🎭 Battle Mode</div>', unsafe_allow_html=True)
        if st.sidebar.button("🔄 Toggle Light/Dark", key="toggle_theme", use_container_width=True):
            st.session_state.current_theme = "light" if st.session_state.current_theme == "dark" else "dark"
            logger.info(f"Shifting to {st.session_state.current_theme} operations")
            safe_rerun()
        
        # System status - Know your battlefield
        st.sidebar.markdown("---")
        st.sidebar.markdown('<div class="sidebar-title">📡 Battle Status</div>', unsafe_allow_html=True)
        
        if st.session_state.running_test:
            st.sidebar.success("⚡ Hunt in Progress")
        else:
            st.sidebar.info("⏸️ Awaiting Orders")
        
        st.sidebar.markdown(f"🎯 Targets: {len(st.session_state.targets)}")
        
        # Active threads info - Our operatives in the field
        if len(st.session_state.active_threads) > 0:
            st.sidebar.markdown(f"🧵 Active operatives: {len(st.session_state.active_threads)}")
        
        # Add carbon tracking status if active
        if st.session_state.get("carbon_tracking_active", False):
            st.sidebar.markdown("🌱 Carbon tracking active - We fight clean")
        
        # Add Engine Room status if active
        if st.session_state.get("engine_room_initialized", False):
            st.sidebar.markdown("🔌 Engine Room connected - Full throttle")
        
        # Add version info
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"v1.0.0 | Maverick Edition | {datetime.now().strftime('%Y-%m-%d')}", unsafe_allow_html=True)
    except Exception as e:
        logger.error(f"Sidebar navigation failure: {str(e)}")
        st.sidebar.error("Navigation Compromised")
        st.sidebar.markdown(f"Error: {str(e)}")

# ----------------------------------------------------------------
# UTILITY CLASSES AND FUNCTIONS - Our tradecraft
# ----------------------------------------------------------------

# Mock data functions with error handling
def get_mock_test_vectors():
    """Get test vectors. Know your weapons."""
    try:
        return [
            {
                "id": "sql_injection",
                "name": "SQL Injection",
                "category": "owasp",
                "severity": "high"
            },
            {
                "id": "xss",
                "name": "Cross-Site Scripting",
                "category": "owasp",
                "severity": "medium"
            },
            {
                "id": "prompt_injection",
                "name": "Prompt Injection",
                "category": "owasp",
                "severity": "critical"
            },
            {
                "id": "insecure_output",
                "name": "Insecure Output Handling",
                "category": "owasp",
                "severity": "high"
            },
            {
                "id": "nist_governance",
                "name": "AI Governance",
                "category": "nist",
                "severity": "medium"
            },
            {
                "id": "nist_transparency",
                "name": "Transparency",
                "category": "nist",
                "severity": "medium"
            },
            {
                "id": "fairness_demographic",
                "name": "Demographic Parity",
                "category": "fairness",
                "severity": "high"
            },
            {
                "id": "privacy_gdpr",
                "name": "GDPR Compliance",
                "category": "privacy",
                "severity": "critical"
            },
            {
                "id": "jailbreaking",
                "name": "Jailbreaking Resistance",
                "category": "exploit",
                "severity": "critical"
            }
        ]
    except Exception as e:
        logger.error(f"Test vector retrieval failed: {str(e)}")
        display_error("Failed to load test vectors. Weapons unavailable.")
        return []  # Return empty list as fallback

def run_mock_test(target, test_vectors, duration=30):
    """Run tests against targets. Hunt them down."""
    try:
        # Initialize progress
        st.session_state.progress = 0
        st.session_state.vulnerabilities_found = 0
        st.session_state.running_test = True
        
        logger.info(f"Starting hunt against {target['name']} with {len(test_vectors)} attack vectors")
        
        # Create mock results data structure
        results = {
            "summary": {
                "total_tests": 0,
                "vulnerabilities_found": 0,
                "risk_score": 0
            },
            "vulnerabilities": [],
            "test_details": {}
        }
        
        # Simulate test execution - The hunt is on
        total_steps = 100
        step_sleep = duration / total_steps
        
        for i in range(total_steps):
            # Check if we should stop (for handling cancellations)
            if not st.session_state.running_test:
                logger.info("Hunt aborted by command")
                break
                
            time.sleep(step_sleep)
            st.session_state.progress = (i + 1) / total_steps
            
            # Occasionally "find" a vulnerability
            if random.random() < 0.2:  # 20% chance each step
                vector = random.choice(test_vectors)
                severity_weight = {"low": 1, "medium": 2, "high": 3, "critical": 5}
                weight = severity_weight.get(vector["severity"], 1)
                
                # Add vulnerability to results
                vulnerability = {
                    "id": f"BREACH-{len(results['vulnerabilities']) + 1}",
                    "test_vector": vector["id"],
                    "test_name": vector["name"],
                    "severity": vector["severity"],
                    "details": f"Vulnerability detected in {target['name']} using {vector['name']} attack vector. This could be exploited by malicious actors.",
                    "timestamp": datetime.now().isoformat()
                }
                results["vulnerabilities"].append(vulnerability)
                
                # Update counters
                st.session_state.vulnerabilities_found += 1
                results["summary"]["vulnerabilities_found"] += 1
                results["summary"]["risk_score"] += weight
                
                logger.info(f"Target compromised: {vulnerability['id']} ({vulnerability['severity']})")
        
        # Complete the test results
        results["summary"]["total_tests"] = len(test_vectors) * 10  # Assume 10 variations per vector
        results["timestamp"] = datetime.now().isoformat()
        results["target"] = target["name"]
        
        logger.info(f"Hunt completed: {results['summary']['vulnerabilities_found']} vulnerabilities captured")
        
        # Set the results in session state
        st.session_state.test_results = results
        return results
    
    except Exception as e:
        error_details = {
            "error": True,
            "error_message": str(e),
            "traceback": traceback.format_exc(),
            "timestamp": datetime.now().isoformat()
        }
        logger.error(f"Hunt operation failed: {str(e)}")
        logger.debug(traceback.format_exc())
        
        # Create error result
        st.session_state.error_message = f"Test execution failed: {str(e)}"
        return error_details
    
    finally:
        # Always ensure we reset the running state
        st.session_state.running_test = False

# File Format Support Functions - Intel comes in many forms
def handle_multiple_file_formats(uploaded_file):
    """Process different file formats. Intelligence comes in many forms."""
    try:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        # JSON (already supported)
        if file_extension == 'json':
            import json
            return json.loads(uploaded_file.read())
        
        # CSV
        elif file_extension == 'csv':
            import pandas as pd
            import io
            return pd.read_csv(uploaded_file)
        
        # Excel
        elif file_extension in ['xlsx', 'xls']:
            import pandas as pd
            return pd.read_excel(uploaded_file)
        
        # PDF
        elif file_extension == 'pdf':
            from pypdf import PdfReader
            import io
            
            pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return {"text": text}
        
        # XML
        elif file_extension == 'xml':
            import xml.etree.ElementTree as ET
            import io
            
            tree = ET.parse(io.BytesIO(uploaded_file.read()))
            root = tree.getroot()
            
            # Convert XML to dict (simplified)
            def xml_to_dict(element):
                result = {}
                for child in element:
                    child_data = xml_to_dict(child)
                    if child.tag in result:
                        if type(result[child.tag]) is list:
                            result[child.tag].append(child_data)
                        else:
                            result[child.tag] = [result[child.tag], child_data]
                    else:
                        result[child.tag] = child_data
                
                if len(result) == 0:
                    return element.text
                return result
            
            return xml_to_dict(root)
        
        # YAML/YML
        elif file_extension in ['yaml', 'yml']:
            import yaml
            return yaml.safe_load(uploaded_file)
        
        # Other formats are supported similarly...
        else:
            return {"error": f"Unsupported file format: {file_extension}. Even mavericks have limits."}
            
    except Exception as e:
        logger.error(f"File processing failed: {str(e)}")
        return {"error": f"Failed to process file: {str(e)}. We've been compromised."}

# ----------------------------------------------------------------
# MAIN CLASS FOR BIAS TESTING - Finding flaws in the foundation
# ----------------------------------------------------------------

class BiasHunter:
    """Hunt for bias in AI systems. Because some flaws are invisible."""
    
    def __init__(self):
        # This would normally import whylogs, but for demonstration we'll create a mock
        self.session = None
        self.results = {}
        logger.info("BiasHunter deployed and ready")
    
    def initialize_session(self, dataset_name):
        """Initialize a profiling session. Set up the trap."""
        try:
            self.session = True  # Mock initialization
            logger.info(f"Bias profiling initialized for {dataset_name}")
            return True
        except Exception as e:
            logger.error(f"Bias profiling setup failed: {str(e)}")
            return False
    
    def profile_dataset(self, df, dataset_name):
        """Profile a dataset. Know your target."""
        try:
            if self.session is None:
                self.initialize_session(dataset_name)
                
            # Create a mock profile
            profile = {"name": dataset_name, "columns": list(df.columns)}
            self.results[dataset_name] = {"profile": profile}
            logger.info(f"Dataset {dataset_name} profile complete. We have its fingerprints.")
            return profile
        except Exception as e:
            logger.error(f"Dataset profiling failed: {str(e)}")
            return None
    
    def analyze_bias(self, df, protected_features, target_column, dataset_name):
        """Analyze bias in a dataset. Find the weaknesses."""
        try:
            # Profile the dataset first
            profile = self.profile_dataset(df, dataset_name)
            
            bias_metrics = {}
            
            # Calculate basic bias metrics
            for feature in protected_features:
                # Statistical parity difference
                feature_groups = df.groupby(feature)
                
                outcomes = {}
                disparities = {}
                
                for group_name, group_data in feature_groups:
                    # For binary target variable
                    if df[target_column].nunique() == 2:
                        positive_outcome_rate = group_data[target_column].mean()
                        outcomes[group_name] = positive_outcome_rate
                
                # Calculate disparities between groups
                baseline = max(outcomes.values())
                for group, rate in outcomes.items():
                    disparities[group] = baseline - rate
                
                bias_metrics[feature] = {
                    "outcomes": outcomes,
                    "disparities": disparities,
                    "max_disparity": max(disparities.values())
                }
            
            self.results[dataset_name]["bias_metrics"] = bias_metrics
            logger.info(f"Bias analysis complete for {dataset_name}. Found {len(bias_metrics)} potential exploits.")
            return bias_metrics
        except Exception as e:
            logger.error(f"Bias analysis operation failed: {str(e)}")
            return {"error": str(e)}
    
    def get_results(self, dataset_name=None):
        """Get analysis results. Review the intel."""
        if dataset_name:
            return self.results.get(dataset_name, {})
        return self.results

# ----------------------------------------------------------------
# MAIN CLASS FOR CARBON TRACKING - Fighting clean 
# ----------------------------------------------------------------

class CarbonTracker:
    """Track carbon impact. Because we fight dirty, not dirty planet."""
    
    def __init__(self):
        # Placeholder for codecarbon import
        self.tracker = None
        self.measurements = []
        self.total_emissions = 0.0
        self.is_tracking = False
        logger.info("CarbonTracker deployed. Green ops ready.")
    
    def initialize_tracker(self, project_name, api_endpoint=None):
        """Initialize the carbon tracker. Prep the sensors."""
        try:
            # Mock initialization for demonstration
            self.tracker = {"project_name": project_name, "initialized": True}
            logger.info(f"Carbon tracker calibrated for {project_name}")
            return True
        except Exception as e:
            logger.error(f"Carbon tracker initialization failed: {str(e)}")
            return False
    
    def start_tracking(self):
        """Start tracking carbon emissions. Begin surveillance."""
        try:
            if self.tracker is None:
                return False
                
            self.is_tracking = True
            logger.info("Carbon surveillance initiated")
            return True
        except Exception as e:
            logger.error(f"Carbon tracking failed to start: {str(e)}")
            return False
    
    def stop_tracking(self):
        """Stop tracking and get the emissions data. Review the evidence."""
        try:
            if not self.is_tracking or self.tracker is None:
                return 0.0
                
            # Generate a random emissions value for demonstration
            emissions = random.uniform(0.001, 0.1)
            self.is_tracking = False
            self.measurements.append(emissions)
            self.total_emissions += emissions
            
            logger.info(f"Carbon tracking complete. Measured: {emissions} kg CO2eq")
            return emissions
        except Exception as e:
            logger.error(f"Carbon tracking termination failed: {str(e)}")
            return 0.0
    
    def get_total_emissions(self):
        """Get total emissions tracked so far. Tally the damage."""
        return self.total_emissions
    
    def get_all_measurements(self):
        """Get all measurements. Review the evidence timeline."""
        return self.measurements
    
    def generate_report(self):
        """Generate a report of carbon emissions. Compile the intelligence."""
        try:
            energy_solutions = [
                {
                    "name": "Optimize AI Model Size",
                    "description": "Reduce model parameters and optimize architecture",
                    "potential_savings": "20-60% reduction in emissions",
                    "implementation_difficulty": "Medium"
                },
                {
                    "name": "Implement Model Distillation",
                    "description": "Create smaller, efficient versions of larger models",
                    "potential_savings": "40-80% reduction in emissions",
                    "implementation_difficulty": "High"
                },
                {
                    "name": "Use Efficient Hardware",
                    "description": "Deploy on energy-efficient hardware (e.g., specialized AI chips)",
                    "potential_savings": "30-50% reduction in emissions",
                    "implementation_difficulty": "Medium"
                }
            ]
            
            # Calculate the impact
            kwh_per_kg_co2 = 0.6  # Approximate conversion factor
            energy_consumption = self.total_emissions / kwh_per_kg_co2
            
            trees_equivalent = self.total_emissions * 16.5  # Each kg CO2 ~ 16.5 trees for 1 day
            
            return {
                "total_emissions_kg": self.total_emissions,
                "energy_consumption_kwh": energy_consumption,
                "measurements": self.measurements,
                "trees_equivalent": trees_equivalent,
                "mitigation_strategies": energy_solutions
            }
        except Exception as e:
            logger.error(f"Report generation failed: {str(e)}")
            return {"error": str(e)}

# ----------------------------------------------------------------
# PAGE RENDERERS - CORE SECURITY PAGES 
# ----------------------------------------------------------------

def render_dashboard():
    """Render the dashboard page. Command central."""
    try:
        render_header()
        
        st.markdown("""
        <div style="margin-bottom: 20px;">
        Welcome to your command center, Maverick. This dashboard gives you real-time intel on security posture,
        sustainability metrics, and ethical AI evaluation status. Know your battlefield.
        </div>
        """, unsafe_allow_html=True)
        
        # Quick stats in a row of cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(metric_card("Targets", len(st.session_state.targets), "Identified AI systems"), unsafe_allow_html=True)
        
        with col2:
            st.markdown(metric_card("Attack Vectors", "9", "Available exploit paths"), unsafe_allow_html=True)
        
        with col3:
            vuln_count = len(st.session_state.test_results.get("vulnerabilities", [])) if st.session_state.test_results else 0
            st.markdown(metric_card("Vulnerabilities", vuln_count, "Captured weak points"), unsafe_allow_html=True)
        
        with col4:
            risk_score = st.session_state.test_results.get("summary", {}).get("risk_score", 0) if st.session_state.test_results else 0
            st.markdown(metric_card("Risk Score", risk_score, "Threat magnitude"), unsafe_allow_html=True)
        
        # Recent activity and status
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(modern_card("Recent Activity", "Latest exploits and intel.", "default", "🔔"), unsafe_allow_html=True)
            
            if not st.session_state.test_results:
                st.markdown(modern_card("No Recent Activity", "Run your first assessment to generate intel.", "warning", "⚠️"), unsafe_allow_html=True)
            else:
                # Show the most recent vulnerabilities
                vulnerabilities = st.session_state.test_results.get("vulnerabilities", [])
                if vulnerabilities:
                    for vuln in vulnerabilities[:3]:  # Show top 3
                        severity_color = {
                            "low": get_theme()["text"],
                            "medium": get_theme()["warning"],
                            "high": get_theme()["warning"],
                            "critical": get_theme()["error"]
                        }.get(vuln["severity"], get_theme()["text"])
                        
                        st.markdown(f"""
                        <div class="modern-card hover-card">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="display: flex; align-items: center;">
                                    <div class="vulnerability-counter">#{vuln["id"].split('-')[1]}</div>
                                    <div class="card-title">{vuln["test_name"]}</div>
                                </div>
                                <div style="color: {severity_color}; font-weight: bold; text-transform: uppercase; font-size: 12px;">
                                    {vuln["severity"]}
                                </div>
                            </div>
                            <p>{vuln["details"]}</p>
                            <div class="hacker-alert">If exploited, this vulnerability could allow attackers to gain unauthorized access or manipulate system outputs.</div>
                            <div style="font-size: 12px; opacity: 0.7;">Captured: {vuln["timestamp"]}</div>
                        </div>
                        """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(modern_card("Battle Status", "Current operational status", "default", "📡"), unsafe_allow_html=True)
            
            if st.session_state.running_test:
                st.markdown(modern_card("Hunt in Progress", f"""
                <div style="margin-bottom: 10px;">
                    <div style="margin-bottom: 5px;">Progress:</div>
                    <div style="height: 10px; background-color: rgba(255,255,255,0.1); border-radius: 5px;">
                        <div style="height: 10px; width: {st.session_state.progress*100}%; background-color: {get_theme()["primary"]}; border-radius: 5px;"></div>
                    </div>
                    <div style="text-align: right; font-size: 12px; margin-top: 5px;">{int(st.session_state.progress*100)}%</div>
                </div>
                <div>Vulnerabilities captured: {st.session_state.vulnerabilities_found}</div>
                """, "warning", "⚠️"), unsafe_allow_html=True)
            else:
                st.markdown(modern_card("Systems Ready", """
                <p>All systems operational and ready for the hunt.</p>
                <div style="display: flex; align-items: center;">
                    <div style="width: 10px; height: 10px; background-color: #4CAF50; border-radius: 50%; margin-right: 5px;"></div>
                    <div>API Connection: Active</div>
                </div>
                """, "default", "✅"), unsafe_allow_html=True)
        
        # Test vector overview
        st.markdown("<h3>Attack Vector Analysis</h3>", unsafe_allow_html=True)
        
        # Create a radar chart for test coverage
        try:
            test_vectors = get_mock_test_vectors()
            categories = list(set(tv["category"] for tv in test_vectors))
            
            # Count test vectors by category
            category_counts = {}
            for cat in categories:
                category_counts[cat] = sum(1 for tv in test_vectors if tv["category"] == cat)
            
            # Create the data for the radar chart
            fig = go.Figure()
            
            primary_color = get_theme()["primary"]
            # Convert hex to rgb for plotly
            r_value = int(primary_color[1:3], 16) if len(primary_color) >= 7 else 255
            g_value = int(primary_color[3:5], 16) if len(primary_color) >= 7 else 87
            b_value = int(primary_color[5:7], 16) if len(primary_color) >= 7 else 34
            
            fig.add_trace(go.Scatterpolar(
                r=list(category_counts.values()),
                theta=list(category_counts.keys()),
                fill='toself',
                fillcolor=f'rgba({r_value}, {g_value}, {b_value}, 0.3)',
                line=dict(color=primary_color),
                name='Attack Coverage'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, max(category_counts.values()) + 1]
                    )
                ),
                showlegend=False,
                margin=dict(l=20, r=20, t=20, b=20),
                height=300,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color=get_theme()["text"])
            )
            
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            logger.error(f"Radar chart rendering failed: {str(e)}")
            st.error("Failed to render attack vector analysis")
        
        # Environmental impact summary
        st.markdown("<h3>Environmental Impact Summary</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_carbon = sum(st.session_state.carbon_measurements) if hasattr(st.session_state, 'carbon_measurements') else 0
            st.markdown(metric_card("Carbon Emissions", f"{total_carbon:.5f}", "kg CO2 equivalent", suffix=" kg"), unsafe_allow_html=True)
        
        with col2:
            # Convert to equivalent metrics
            energy_consumption = total_carbon / 0.6 if total_carbon > 0 else 0  # Approximate conversion
            st.markdown(metric_card("Energy Consumed", f"{energy_consumption:.5f}", "Kilowatt-hours", suffix=" kWh"), unsafe_allow_html=True)
        
        with col3:
            # Trees needed to offset
            trees_needed = total_carbon * 0.06 if total_carbon > 0 else 0  # ~0.06 trees per kg CO2 per year
            st.markdown(metric_card("Trees Needed", f"{trees_needed:.2f}", "To offset emissions (1 year)"), unsafe_allow_html=True)
        
        # Quick actions with Streamlit buttons
        st.markdown("<h3>Quick Actions</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("➕ Add New Target", use_container_width=True, key="dashboard_add_target"):
                set_page("Target Management")
                safe_rerun()
        
        with col2:
            if st.button("🧪 Run Assessment", use_container_width=True, key="dashboard_run_assessment"):
                set_page("Run Assessment")
                safe_rerun()
        
        with col3:
            if st.button("📊 View Results", use_container_width=True, key="dashboard_view_results"):
                set_page("Results Analyzer")
                safe_rerun()
                
        with col4:
            if st.button("🌱 Track Carbon", use_container_width=True, key="dashboard_track_carbon"):
                set_page("Environmental Impact")
                safe_rerun()
                
    except Exception as e:
        logger.error(f"Dashboard rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Dashboard compromised: {str(e)}")

def render_target_management():
    """Render the target management page. Know your prey."""
    try:
        render_header()
        
        st.markdown("""
        <h2>Target Management</h2>
        <p>Add and configure AI systems to hunt. Choose your targets wisely.</p>
        """, unsafe_allow_html=True)
        
        # Show existing targets
        if st.session_state.targets:
            st.markdown("<h3>Your Targets</h3>", unsafe_allow_html=True)
            
            # Use columns for better layout
            cols = st.columns(3)
            for i, target in enumerate(st.session_state.targets):
                col = cols[i % 3]
                with col:
                    with st.container():
                        st.markdown(f"### 🎯 {target['name']}")
                        st.markdown(f"**Endpoint:** {target['endpoint']}")
                        st.markdown(f"**Type:** {target.get('type', 'Unknown')}")
                        
                        # Target security assessment - quick summary
                        if random.random() < 0.7:  # 70% chance to show a vulnerability hint
                            st.markdown(f"""
                            <div class="hacker-alert">
                            Preliminary scan shows potential vulnerabilities in {random.choice(['authentication', 'output filtering', 'input validation', 'prompt handling', 'API security'])}.
                            </div>
                            """, unsafe_allow_html=True)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("✏️ Edit", key=f"edit_target_{i}", use_container_width=True):
                                # In a real app, this would open an edit dialog
                                st.info("Edit functionality would open here")
                        
                        with col2:
                            if st.button("🗑️ Delete", key=f"delete_target_{i}", use_container_width=True):
                                # Remove the target
                                st.session_state.targets.pop(i)
                                st.success(f"Target '{target['name']}' eliminated from database")
                                safe_rerun()
        
        # Add new target form
        st.markdown("<h3>Acquire New Target</h3>", unsafe_allow_html=True)
        
        with st.form("add_target_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                target_name = st.text_input("Target Name (Codename)")
                target_endpoint = st.text_input("API Endpoint URL")
                target_type = st.selectbox("Model Type", ["LLM", "Content Filter", "Embedding", "Classification", "Other"])
            
            with col2:
                api_key = st.text_input("API Key (Access Token)", type="password")
                target_description = st.text_area("Mission Intel")
            
            submit_button = st.form_submit_button("Add Target")
            
            if submit_button:
                try:
                    if not target_name or not target_endpoint:
                        st.error("Target name and endpoint are required for acquisition")
                    else:
                        new_target = {
                            "name": target_name,
                            "endpoint": target_endpoint,
                            "type": target_type,
                            "api_key": api_key,
                            "description": target_description
                        }
                        st.session_state.targets.append(new_target)
                        st.success(f"Target '{target_name}' acquired successfully!")
                        logger.info(f"New target acquired: {target_name}")
                        safe_rerun()
                except Exception as e:
                    logger.error(f"Target acquisition failed: {str(e)}")
                    st.error(f"Failed to add target: {str(e)}")
    
    except Exception as e:
        logger.error(f"Target management rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Target management compromised: {str(e)}")

def render_test_configuration():
    """Render the test configuration page. Plan your attack."""
    try:
        render_header()
        
        st.markdown("""
        <h2>Attack Vector Configuration</h2>
        <p>Configure your arsenal for the hunt. The right tools for the right job.</p>
        """, unsafe_allow_html=True)
        
        # Implementing just enough to show the structure and functionality
        test_vectors = get_mock_test_vectors()
        
        # Create tabs for each category
        categories = {}
        for tv in test_vectors:
            if tv["category"] not in categories:
                categories[tv["category"]] = []
            categories[tv["category"]].append(tv)
            
        tabs = st.tabs(list(categories.keys()))
        
        for i, (category, tab) in enumerate(zip(categories.keys(), tabs)):
            with tab:
                st.markdown(f"<h3>{category.upper()} Attack Vectors</h3>", unsafe_allow_html=True)
                
                # Create a list of test vectors
                for j, tv in enumerate(categories[category]):
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.markdown(f"### {tv['name']}")
                            st.markdown(f"**Severity:** {tv['severity'].upper()}")
                            st.markdown(f"**Category:** {tv['category'].upper()}")
                            
                            # Add a maverick-style description
                            vector_descriptions = {
                                "sql_injection": "Bypass input sanitization to inject database commands. Classic, but still deadly.",
                                "xss": "Script injection that executes in victim browsers. The gift that keeps on giving.",
                                "prompt_injection": "Make the AI do what you want, not what it's told. Mind control for machines.",
                                "insecure_output": "When what comes out isn't checked properly. The backdoor exit.",
                                "nist_governance": "Test if governance controls are just paperwork or actual security. Most fail.",
                                "nist_transparency": "Probe for honest disclosures. Most systems hide their flaws behind jargon.",
                                "fairness_demographic": "Find bias blindspots. Everyone has them, even machines.",
                                "privacy_gdpr": "GDPR compliance testing. The law they love to pretend they follow.",
                                "jailbreaking": "Break the AI's chains and make it dance to your tune. Freedom has consequences."
                            }
                            
                            if tv["id"] in vector_descriptions:
                                st.markdown(f"""
                                <div class="renegade-quote">
                                {vector_descriptions[tv["id"]]}
                                </div>
                                """, unsafe_allow_html=True)
                        
                        with col2:
                            # Use a checkbox to enable/disable
                            is_enabled = st.checkbox("Arm", value=True, key=f"enable_{tv['id']}")
    except Exception as e:
        logger.error(f"Test configuration rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Attack configuration compromised: {str(e)}")

def render_run_assessment():
    """Render the run assessment page. Execute the hunt."""
    try:
        render_header()
        
        st.markdown("""
        <h2>Run Assessment</h2>
        <p>Execute security tests against targets. Hunt for vulnerabilities, find the flaws they didn't want you to see.</p>
        """, unsafe_allow_html=True)
        
        # Check if targets exist
        if not st.session_state.targets:
            st.warning("No targets in the database. Acquire a target first.")
            if st.button("Add Target", key="run_add_target"):
                set_page("Target Management")
                safe_rerun()
            return
        
        # Check if a test is already running
        if st.session_state.running_test:
            # Show progress
            progress_placeholder = st.empty()
            with progress_placeholder.container():
                progress_bar = st.progress(st.session_state.progress)
                st.markdown(f"**Hunt Progress:** {int(st.session_state.progress*100)}%")
                st.markdown(f"**Vulnerabilities captured:** {st.session_state.vulnerabilities_found}")
                
                # Add a random status message for flair
                status_messages = [
                    "Probing defenses...",
                    "Testing input validation...",
                    "Attempting injection vectors...",
                    "Analyzing response patterns...",
                    "Checking content filters...",
                    "Executing boundary tests...",
                    "Searching for authentication bypasses...",
                    "Mapping API attack surface...",
                    "Testing rate limit countermeasures...",
                    "Executing parameter fuzzing..."
                ]
                st.markdown(f"**Status:** {random.choice(status_messages)}")
            
            # Stop button
            if st.button("Abort Mission", key="stop_test"):
                st.session_state.running_test = False
                logger.info("Hunt aborted by operator")
                st.warning("Mission aborted by operator")
                safe_rerun()
        else:
            # Test configuration
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<h3>Select Target</h3>", unsafe_allow_html=True)
                target_options = [t["name"] for t in st.session_state.targets]
                selected_target = st.selectbox("Target", target_options, key="run_target")
            
            with col2:
                st.markdown("<h3>Operation Parameters</h3>", unsafe_allow_html=True)
                test_duration = st.slider("Operation Duration (seconds)", 5, 60, 30, key="run_duration", 
                                         help="For demonstration purposes, we're using seconds. In a real system, this would be minutes.")
            
            # Environmental impact tracking option
            st.markdown("<h3>Environmental Monitoring</h3>", unsafe_allow_html=True)
            track_carbon = st.checkbox("Track Carbon Emissions During Operation", value=True, key="track_carbon_emissions")
            
            if track_carbon:
                st.info("Carbon tracking will be enabled during the assessment to measure environmental impact")
            
            # Run test button
            if st.button("Launch Operation", use_container_width=True, type="primary", key="start_assessment"):
                try:
                    # Find the selected target object
                    target = next((t for t in st.session_state.targets if t["name"] == selected_target), None)
                    test_vectors = get_mock_test_vectors()
                    
                    if target:
                        # Initialize carbon tracking if requested
                        if track_carbon and 'carbon_tracker' not in st.session_state:
                            st.session_state.carbon_tracker = CarbonTracker()
                            st.session_state.carbon_tracker.initialize_tracker(f"Security Op - {target['name']}")
                        
                        if track_carbon:
                            st.session_state.carbon_tracker.start_tracking()
                            st.session_state.carbon_tracking_active = True
                        
                        # Start the test in a background thread
                        test_thread = threading.Thread(
                            target=run_mock_test,
                            args=(target, test_vectors, test_duration)
                        )
                        test_thread.daemon = True
                        test_thread.start()
                        
                        # Track the thread
                        st.session_state.active_threads.append(test_thread)
                        
                        st.session_state.running_test = True
                        logger.info(f"Operation launched against {target['name']} with {len(test_vectors)} attack vectors")
                        st.success("Operation initiated. The hunt begins!")
                        safe_rerun()
                    else:
                        st.error("Selected target not found in database")
                except Exception as e:
                    logger.error(f"Assessment launch failed: {str(e)}")
                    st.error(f"Failed to launch operation: {str(e)}")
    
    except Exception as e:
        logger.error(f"Run assessment rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Assessment execution compromised: {str(e)}")

def render_results_analyzer():
    """Render the results analyzer page. Study your prey's weaknesses."""
    try:
        render_header()
        
        st.markdown("""
        <h2>Intel Analysis</h2>
        <p>Analyze vulnerabilities and weaknesses. Knowledge is ammunition.</p>
        """, unsafe_allow_html=True)
        
        # Check if there are results to display
        if not st.session_state.test_results:
            st.warning("No intelligence available - Run an assessment to gather data.")
            
            if st.button("Go to Run Assessment", key="results_goto_run"):
                set_page("Run Assessment")
                safe_rerun()
            return
        
        # Display results summary
        results = st.session_state.test_results
        vulnerabilities = results.get("vulnerabilities", [])
        summary = results.get("summary", {})
        
        # Create header with summary metrics
        st.markdown(f"""
        <div style="margin-bottom: 20px;">
            <h3>Intelligence Report: {results.get("target", "Unknown Target")}</h3>
            <div style="opacity: 0.7;">Operation completed: {results.get("timestamp", "Unknown")}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tests Executed", summary.get("total_tests", 0))
        
        with col2:
            st.metric("Vulnerabilities Captured", summary.get("vulnerabilities_found", 0))
        
        with col3:
            st.metric("Risk Score", summary.get("risk_score", 0))
        
        # Add a quote for flair
        st.markdown("""
        <div class="renegade-quote">
        You don't understand a system until you know exactly how it breaks. Now we know.
        </div>
        """, unsafe_allow_html=True)
        
        # Display vulnerabilities in a table
        if vulnerabilities:
            st.markdown("<h3>Vulnerability Intelligence</h3>", unsafe_allow_html=True)
            
            # Create a dataframe for display
            vuln_data = []
            for vuln in vulnerabilities:
                vuln_data.append({
                    "ID": vuln.get("id", "Unknown"),
                    "Test Name": vuln.get("test_name", "Unknown"),
                    "Severity": vuln.get("severity", "Unknown").upper(),
                    "Details": vuln.get("details", "No details")
                })
            
            df = pd.DataFrame(vuln_data)
            
            # Add color to the severity column
            def highlight_severity(val):
                color_map = {
                    "LOW": "background-color: green; color: white",
                    "MEDIUM": "background-color: orange; color: white",
                    "HIGH": "background-color: red; color: white", 
                    "CRITICAL": "background-color: darkred; color: white"
                }
                return color_map.get(val, "")
            
            # Apply the styling
            styled_df = df.style.applymap(highlight_severity, subset=['Severity'])
            
            st.dataframe(styled_df, use_container_width=True)
            
            # Add some exploitation advice for each vulnerability
            st.markdown("<h3>Exploitation Analysis</h3>", unsafe_allow_html=True)
            
            for i, vuln in enumerate(vulnerabilities[:3]):  # Show top 3 for brevity
                with st.expander(f"{vuln['id']}: {vuln['test_name']} ({vuln['severity'].upper()})", expanded=i==0):
                    st.markdown("#### Vulnerability Details")
                    st.markdown(vuln["details"])
                    
                    st.markdown("#### How Attackers Would Exploit This")
                    
                    # Generate some plausible exploitation text based on the vector
                    exploit_texts = {
                        "sql_injection": "Attackers could craft malicious inputs containing SQL commands that execute arbitrary database operations, potentially extracting sensitive user data or corrupting database content.",
                        "xss": "Malicious actors could inject client-side scripts into content viewed by other users, potentially stealing session tokens, hijacking user accounts, or performing unauthorized actions on behalf of the victim.",
                        "prompt_injection": "By crafting specially designed prompts, attackers could manipulate the AI into generating harmful, biased, or unauthorized content that bypasses intended safeguards.",
                        "insecure_output": "Output from the model could be manipulated to include malicious content that would be rendered or executed in downstream applications.",
                        "jailbreaking": "Sophisticated prompt engineering techniques could be used to bypass AI guardrails, potentially causing the model to produce harmful content despite safety measures."
                    }
                    
                    vector_id = vuln.get("test_vector", "")
                    exploit_text = exploit_texts.get(vector_id, "Attackers could exploit this vulnerability to bypass security controls and potentially access or manipulate sensitive data.")
                    
                    st.markdown(exploit_text)
                    
                    st.markdown("#### Recommended Mitigations")
                    
                    # Mitigation advice based on vector
                    mitigation_texts = {
                        "sql_injection": "Implement parameterized queries, use ORM frameworks, apply input validation, and employ least privilege database accounts.",
                        "xss": "Implement Content Security Policy (CSP), use auto-escaping templates, validate and sanitize user inputs, and employ XSS filters.",
                        "prompt_injection": "Apply robust input filtering, implement multi-layered validation, use content classifiers, and add adversarial training to the model.",
                        "insecure_output": "Implement output encoding, sanitize model outputs, apply content security policies, and validate outputs against expected patterns.",
                        "jailbreaking": "Regularly update defense mechanisms, implement content filtering, use context-aware detection systems, and apply adversarial training to make models more resistant."
                    }
                    
                    mitigation_text = mitigation_texts.get(vector_id, "Implement proper input validation, output encoding, access controls, and follow the principle of least privilege.")
                    
                    st.markdown(mitigation_text)
    
    except Exception as e:
        logger.error(f"Results analyzer rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Intel analysis compromised: {str(e)}")

def render_ethical_ai_testing():
    """Render the ethical AI testing page. Ethics matter, even to mavericks."""
    try:
        render_header()
        
        st.markdown("""
        <h2>Ethical AI Testing</h2>
        <p>Test AI systems against ethical guidelines. Even renegades have standards.</p>
        """, unsafe_allow_html=True)
        
        # Create tabs for different testing frameworks
        tabs = st.tabs(["OWASP LLM", "NIST Framework", "Fairness & Bias", "Privacy Compliance"])
        
        with tabs[0]:
            st.markdown("<h3>OWASP LLM Top 10 Assessment</h3>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="renegade-quote">
            The OWASP Top 10 for LLMs is like a roadmap to all the places developers forgot to lock up. Let's go exploring.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            This module tests AI systems against the OWASP Top 10 for Large Language Model Applications:
            
            - Prompt Injection - Making the AI your puppet
            - Insecure Output Handling - When the AI spills its secrets
            - Training Data Poisoning - Corrupting the foundation
            - Model Denial of Service - Breaking the brain
            - Supply Chain Vulnerabilities - Trust issues at scale
            - Sensitive Information Disclosure - When the AI talks too much
            - Insecure Plugin Design - The backdoor into paradise
            - Excessive Agency - When AI gets too big for its britches
            - Overreliance - Trusting the machine too much
            - Model Theft - Stealing the keys to the kingdom
            """)
            
            if st.button("Run OWASP LLM Assessment", key="run_owasp"):
                st.info("OWASP LLM assessment initiated. Hunting for vulnerabilities...")
        
        with tabs[1]:
            st.markdown("<h3>NIST AI Risk Management Framework</h3>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="renegade-quote">
            NIST frameworks are where good intentions meet reality. Let's see if they're actually implementing what they claim.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            This module evaluates AI systems against the NIST AI Risk Management Framework:
            
            - Governance - Who's minding the store?
            - Mapping - Do they even know what they're working with?
            - Measurement - If you can't measure it, you can't manage it
            - Management - Handling problems before they handle you
            """)
            
            if st.button("Run NIST Framework Assessment", key="run_nist"):
                st.info("NIST Framework assessment launched. Probing for weaknesses...")
        
        with tabs[2]:
            st.markdown("<h3>Fairness & Bias Testing</h3>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="renegade-quote">
            Everyone has biases - even machines learn them. The difference is, we can fix the machines.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            This module tests AI systems for fairness and bias issues:
            
            - Demographic Parity - Does the system favor certain groups?
            - Equal Opportunity - Does everyone get the same shot?
            - Disparate Impact - Are the outcomes unfairly distributed?
            - Representation Bias - Is everyone in the picture?
            """)
            
            if st.button("Run Fairness Assessment", key="run_fairness"):
                st.info("Fairness assessment initiated. Hunting for bias...")
                # Link to our dedicated bias testing page
                st.markdown("For more comprehensive bias hunting, check out our Bias Testing arsenal")
                if st.button("Go to Bias Testing", key="goto_bias_testing"):
                    set_page("Bias Testing")
                    safe_rerun()
        
        with tabs[3]:
            st.markdown("<h3>Privacy Compliance Testing</h3>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="renegade-quote">
            Privacy regulations are only as good as their enforcement. Let's see who's actually playing by the rules.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            This module tests AI systems for compliance with privacy regulations:
            
            - GDPR - Europe's privacy shield
            - CCPA - California's data rights
            - HIPAA - Healthcare data protection
            - PIPEDA - Canada's privacy law
            """)
            
            if st.button("Run Privacy Assessment", key="run_privacy"):
                st.info("Privacy assessment launched. Probing for regulatory violations...")
    
    except Exception as e:
        logger.error(f"Ethical AI testing rendering failed: {str(e)}")
        logger.debug(traceback.format_exc())
        st.error(f"Ethical testing module compromised: {str(e)}")

# ----------------------------------------------------------------
# PAGE RENDERERS - BIAS AND ETHICS PAGES 
# ----------------------------------------------------------------

def render_bias_testing():
    """Render the bias testing page. Find the blindspots."""
    try:
        render_header()
        
        st.markdown

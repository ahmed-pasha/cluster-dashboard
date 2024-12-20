import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to draw a modern gauge with text below the needle
def draw_modern_gauge(value, max_value, title, unit, color='orange', gradient=False):
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})

    # Normalize the value to degrees
    normalized_value = (value / max_value) * 180

    # Background arc
    theta = np.linspace(0, np.pi, 100)
    ax.plot(theta, [1] * len(theta), color='gray', linewidth=20, zorder=1, alpha=0.4)

    # Active arc
    active_theta = np.linspace(0, np.radians(normalized_value), 50)
    ax.plot(active_theta, [1] * len(active_theta), color=color, linewidth=20, zorder=2)

    # Gradient effect for active arc
    if gradient:
        colors = plt.cm.plasma(np.linspace(0, 1, len(active_theta)))
        for i in range(len(active_theta) - 1):
            ax.plot(
                active_theta[i:i+2],
                [1, 1],
                color=colors[i],
                linewidth=20,
                zorder=3,
            )

    # Draw ticks and labels
    for tick_value in range(0, max_value + 1, max_value // 10):
        tick_angle = np.radians((tick_value / max_value) * 180)
        ax.text(
            tick_angle,
            1.15,
            f"{tick_value}",
            fontsize=10,
            color='white',
            horizontalalignment='center',
            verticalalignment='center',
        )

    # Needle
    ax.arrow(
        0, 0,
        np.radians(normalized_value),
        0.9,  # Length of the needle
        width=0.02,
        head_width=0.05,
        head_length=0.1,
        color='red',
        zorder=4
    )

    # Centered Title and Value (Below the Needle)
    ax.text(
        0, -0.4,  # Position text slightly below the center
        f"{value} {unit}\n{title}",
        fontsize=16,
        ha='center',
        color=color,
        fontweight='bold',
        linespacing=1.2,
        zorder=5,
    )

    # Hide polar grid and ticks
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)

    # Set the facecolor
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")
    return fig

# Streamlit app
st.title("Modern Car Dashboard ")

# Layout
col1, col2, col3 = st.columns(3)

# Speedometer
with col1:
    speed = st.slider("Speed (km/h)", 0, 220, 80)
    fig1 = draw_modern_gauge(speed, 220, "Speed", "km/h", color='limegreen', gradient=True)
    st.pyplot(fig1)

# RPM Gauge
with col2:
    rpm = st.slider("RPM", 0, 8000, 3000)
    fig2 = draw_modern_gauge(rpm, 8000, "RPM", "RPM", color='red', gradient=True)
    st.pyplot(fig2)

# Temperature Gauge
with col3:
    temp = st.slider("Temperature (°C)", 0, 120, 70)
    fig3 = draw_modern_gauge(temp, 120, "Temp", "°C", color='blue', gradient=True)
    st.pyplot(fig3)

# Fuel Level
fuel = st.slider("Fuel Level (%)", 0, 100, 50)
fig4 = draw_modern_gauge(fuel, 100, "Fuel", "%", color='orange', gradient=True)
st.pyplot(fig4)

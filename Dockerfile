FROM manimcommunity/manim:v0.20.1

USER root

# Install Chinese fonts and additional dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-noto-cjk \
    fonts-noto-cjk-extra \
    texlive-lang-chinese \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml README.md /app/
COPY src/ /app/src/
WORKDIR /app

RUN pip install --no-cache-dir -e .

# Create output directory
RUN mkdir -p /app/animation_output

ENV OUTPUT_DIR=/app/animation_output
ENV LANG=zh_CN.UTF-8

EXPOSE 7860

# Default: start web interface
CMD ["python", "-m", "math_animation_mcp", "--web", "--port", "7860"]

FROM python:3.11

RUN pip install torch==1.7.1 torchvision==0.8.2 clip-by-openai
RUN pip install git+https://github.com/openai/CLIP.git
RUN pip3 install flask flask_cors pillow numpy matplotlib requests psycopg2

RUN mkdir /home/ImagesSinNeXAPI


WORKDIR /home/ImagesSinNeXAPI

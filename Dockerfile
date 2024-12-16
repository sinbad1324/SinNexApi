FROM python:3.11

RUN  pip install --upgrade pip
RUN pip install git+https://github.com/openai/CLIP.git
RUN pip3 install flask flask_cors pillow numpy matplotlib requests cryptography
RUN mkdir /home/ImagesSinNeXAPI


WORKDIR /home/ImagesSinNeXAPI

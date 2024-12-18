FROM python:3.11

RUN  pip install --upgrade pip
RUN pip install git+https://github.com/openai/CLIP.git
RUN pip install flask flask_cors matplotlib requests cryptography
RUN mkdir /home/ImagesSinNeXAPI
WORKDIR /home/ImagesSinNeXAPI

CMD [ "python", "main.py"]

FROM python:3.10

RUN  pip install --upgrade pip
RUN pip install git+https://github.com/openai/CLIP.git
RUN pip install flask flask_cors matplotlib requests cryptography
RUN mkdir /home/ImagesSinNeXAPI
RUN chmod 777 /home/ImagesSinNeXAPI
COPY . .
WORKDIR /home/ImagesSinNeXAPI

CMD [ "python3", "-m" , "flask" , "run" , "--host=0.0.0.0"]

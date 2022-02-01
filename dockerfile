FROM nvcr.io/nvidia/pytorch:21.06-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
      apt-get -y install sudo


RUN :\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :
    
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER docker
CMD /bin/bash




RUN pip install --upgrade torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 torchtext==0.11.0 \
    -f https://download.pytorch.org/whl/cu113/torch_stable.html
RUN pip install torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric \
    -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
RUN curl -sSL https://install.python-poetry.org | python3 - 
RUN echo "export PATH=$HOME/.local/bin:$PATH" >> $HOME/.bashrc

SHELL ["/bin/bash", "--login", "-c"]

WORKDIR /home/docker

COPY ./ /home/docker/

RUN pip install -r requirements.txt

# RUN :\
#     && poetry config virtualenvs.create false \
#     && poetry install \
#     && :

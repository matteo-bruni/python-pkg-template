ARG BASE_IMAGE
ARG BASE_IMAGE_TAG


FROM ${BASE_IMAGE}:${BASE_IMAGE_TAG} 

ARG USER
ARG UID
ARG GID

RUN apt-get update && apt-get install -y sudo openssh-client git ffmpeg mediainfo less nano bat && \
    addgroup --gid "${GID}" "${USER}" && \
    adduser --disabled-password --shell /usr/bin/bash --uid "${UID}" --gid "${GID}" --gecos "${USER}" "${USER}" && \
    usermod -aG sudo "${USER}" && \
    sh -c 'echo "${USER} ALL=(ALL:ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/${USER}' && \
    python3 -m pip install -U pip ipython build virtualenv

FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
  curl \
  git \
  bash \
  sudo \
  python3 \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash codespace && echo "codespace:codespace" | chpasswd && adduser codespace sudo

USER codespace
WORKDIR /workspace

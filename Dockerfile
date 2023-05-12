# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}
ARG INSTALL_NODE_VERSION=${INSTALL_NODE_VERSION:-NODE_VERSION_NOT_SET}

FROM node:${INSTALL_NODE_VERSION}-buster-slim AS node
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS builder

WORKDIR /app

COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/lib/ /usr/lib/
# See https://github.com/moby/moby/issues/37965
RUN true
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY requirements requirements
RUN pip install --no-cache -r requirements/prod.txt

COPY package.json ./
RUN npm install

COPY webpack.config.js autoapp.py ./
COPY onlyonecode onlyonecode
COPY assets assets
COPY .env.example .env
RUN npm run-script build

# ================================= PRODUCTION =================================
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster as production

WORKDIR /app

RUN useradd -m onlyonecode
RUN chown -R onlyonecode:onlyonecode /app
USER onlyonecode
ENV PATH="/home/onlyonecode/.local/bin:${PATH}"

COPY --from=builder --chown=onlyonecode:onlyonecode /app/onlyonecode/static /app/onlyonecode/static
COPY requirements requirements
RUN pip install --no-cache --user -r requirements/prod.txt

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisord_programs /etc/supervisor/conf.d

COPY . .

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "shell_scripts/supervisord_entrypoint.sh"]
CMD ["-c", "/etc/supervisor/supervisord.conf"]


# ================================= DEVELOPMENT ================================
FROM builder AS development
RUN pip install --no-cache -r requirements/dev.txt
EXPOSE 2992
EXPOSE 5000
CMD [ "npm", "start" ]

FROM alpine:3.11 as builder

# hadolint ignore=DL3018
RUN set -eux \
 && apk add --no-cache \
 bash gcc \
 python3 python3-dev

WORKDIR /src

COPY . /src/
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN set -eux \
 && python3 setup.py install \
 && salt-lint --version \
 && find /usr/lib/ -name '__pycache__' -print0 | xargs -0 -n1 rm -rf \
 && find /usr/lib/ -name '*.pyc' -print0 | xargs -0 -n1 rm -rf


FROM alpine:3.11 as production
LABEL maintainer="info@warpnet.nl" \
      repo="https://github.com/warpnet/salt-lint"
# hadolint ignore=DL3018
RUN set -eux \
 && apk add --no-cache bash git python3
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN set -eux \
 && find /usr/lib/ -name '__pycache__' -print0 | xargs -0 -n1 rm -rf \
 && find /usr/lib/ -name '*.pyc' -print0 | xargs -0 -n1 rm -rf \
 && addgroup -S -g 800 linter \
 && adduser -S -u 800 -S -H -D -G linter linter
COPY --from=builder /usr/lib/python3.8/site-packages/ /usr/lib/python3.8/site-packages/
COPY --from=builder /usr/bin/salt-lint /usr/bin/salt-lint
WORKDIR /data
USER linter
ENTRYPOINT ["salt-lint"]

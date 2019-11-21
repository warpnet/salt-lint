FROM python:3.7-alpine
LABEL maintainer="info@warpnet.nl"

# Install required alpine packages
# hadolint ignore=DL3018,DL3019
RUN apk add --no-cache gcc g++ build-base libzmq musl-dev zeromq-dev

# Install the salt-lint package
RUN pip install --no-cache salt-lint==v0.2.0

# Remove development utilities
RUN apk del --no-cache gcc g++ build-base libzmq musl-dev zeromq-dev \
 && rm -rf /var/cache/apk/*

RUN addgroup -S -g 800 linter \
 && adduser -S -u 800 -S -H -D -G linter linter

# Run as linter user
USER linter

CMD ["/usr/local/bin/salt-lint"]
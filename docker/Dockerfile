FROM python:3.7-alpine
LABEL maintainer="info@warpnet.nl"

# Install the salt-lint package
# hadolint ignore=DL3013
RUN pip install --no-cache salt-lint

# Create the linter user
RUN addgroup -S -g 800 linter \
 && adduser -S -u 800 -S -H -D -G linter linter

# Run as linter user
USER linter

CMD ["/usr/local/bin/salt-lint"]

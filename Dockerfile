FROM debian:buster-slim

WORKDIR /app
COPY . /app
	
RUN \
    echo "==> Install common stuff missing from the slim base image..."   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
        gnupg   \
        dirmngr \
        wget    \
        ca-certificates               && \
        rm -rf /var/lib/apt/lists/*   && \
    \
    \
    echo "==> Add Google repo for Chrome..."   && \
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  && \
    \
    \
    echo "==> Install prerequisite stuff..."   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
		dpkg google-chrome-stable_current_amd64.deb && \
        xvfb                     \
        libfontconfig            \
        libfreetype6             \
        xfonts-scalable          \
        fonts-liberation         \
        fonts-noto-cjk           \
    \
    \
    echo "==> Install ChromeDriver..."   && \
    wget -qO- $CHROME_DRIVER_TARBALL | zcat > /usr/local/bin/chromedriver  && \
    chown root:root /usr/local/bin/chromedriver  && \
    chmod 0755 /usr/local/bin/chromedriver       && \
             

RUN apt-get update && apt-get install -y \
    python3-pip 

RUN pip3 install -r requirements.txt


CMD ["behave", "--tags=@flag_off_decline", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]

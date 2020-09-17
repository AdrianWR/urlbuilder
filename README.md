# AIvsCOVID19  URL Builder

## Motivation
This repository contains a simple setup to create a URL Builder instance to act in the context of Data Mining workflow in the AIvsCOVID19 project. The URL Builder is a special type of data mining Python script; it iterates through search pages from a scientific article website, gathering all the links which could have valuable data to extract in a further process. At each iteration, the URL Builder will send the links extracted to a Google BigQuery table, given the right permissions to write data.

### Installation

Before proceeding, it's not advised to run this scraper on your local machine, as some websites may block yor IP address upon a number of requests on a particular domain. When data mining, be assured to follow very stricit ethical guidelines before running your process, to not clog up domain servers from scientific websites. Be polite while mining.  

#### With Docker
The most common way to run this URL Builder script is to run it on a Docker container, as the dependencies will be updated to the latest working Python packages. To download the repository and build the Docker image, you can run the following command:

    git clone https://github.com/AdrianWR/urlbuilder.git
    docker build -t IMAGE_NAME urlbuilder

### Getting Started
